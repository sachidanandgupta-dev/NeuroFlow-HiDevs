import re

SECRET_PATTERNS = {
    "aws_access_key": r"AKIA[0-9A-Z]{16}",
    "generic_api_key": r"['\"]?(?:api|secret|token|key|password)['\"]?\s*[:=]\s*['\"]?([A-Za-z0-9+/]{20,})['\"]?",
    "pem_header": r"-----BEGIN [A-Z ]+ PRIVATE KEY-----",
    "jwt_token": r"[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+"
}

def redact_secrets(text: str):
    redacted_text = text
    for name, pattern in SECRET_PATTERNS.items():
        redacted_text = re.sub(pattern, "[REDACTED]", redacted_text)
    return redacted_text