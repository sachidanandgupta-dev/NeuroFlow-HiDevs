from dataclasses import dataclass
from uuid import UUID
from typing import Optional, List, Dict, Any
import re

@dataclass
class Citation:
    reference: str      # e.g., "[Source 1]"
    chunk_id: UUID
    document_name: str
    page_number: Optional[int] = None
    content_preview: str = "" # first 100 chars

def resolve_citations(text: str, retrieved_chunks: List[Dict[str, Any]]) -> List[Any]:
    found_refs = re.findall(r"\[Source (\d+)\]", text)
    resolved = []
    
    for ref_num in set(found_refs):
        idx = int(ref_num) - 1
        if 0 <= idx < len(retrieved_chunks):
            chunk = retrieved_chunks[idx]
            resolved.append(Citation(
                reference=f"[Source {ref_num}]",
                chunk_id=chunk['id'],
                document_name=chunk['metadata'].get('filename', 'Unknown'),
                page_number=chunk['metadata'].get('page'),
                content_preview=chunk['content'][:100]
            ))
        else:
            # Hallucination detected
            resolved.append({"invalid_citation": True, "reference": f"[Source {ref_num}]"})
            
    return resolved