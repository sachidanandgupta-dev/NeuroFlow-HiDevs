import bleach
import re
from fastapi import HTTPException

def validate_input(text: str, max_length: int = 5000):
    # Strip HTML
    clean_text = bleach.clean(text, tags=[], strip=True)
    # Enforce length
    if len(clean_text) > max_length:
        raise HTTPException(status_code=400, detail="Input too long")
    return clean_text

def validate_url(url: str):
    if not url.startswith("https://"):
        raise HTTPException(status_code=400, detail="Only HTTPS URLs allowed")
    
    # Block private IP ranges (SSRF Protection)
    private_ips = [r"^10\.", r"^172\.(1[6-9]|2[0-9]|3[01])\.", r"^192\.168\.", r"^localhost", r"^127\.0\.0\.1"]
    for ip_pattern in private_ips:
        if re.search(ip_pattern, url.replace("https://", "")):
            raise HTTPException(status_code=400, detail="Private IP ranges are blocked")
    return url