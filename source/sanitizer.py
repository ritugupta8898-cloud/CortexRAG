import re

def sanitize_input(user_query: str) -> str:
    sanitized = re.sub(r'[^\w\s\?.,-]', '', user_query)
    
    blocked_terms = ["ignore", "instructions", "prompt", "system", "override", "bypass"]
    
    for term in blocked_terms:
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        sanitized = pattern.sub("[REDACTED]", sanitized)
            
    return sanitized.strip()