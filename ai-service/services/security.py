import re

def sanitize_input(text):

    if not text:
        return None

    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # SQL Injection patterns
    sql_patterns = [
        r"(\bor\b|\band\b).*=.*",
        r"(--)",
        r"(;)",
        r"(drop table)",
        r"(select .* from)",
    ]

    # Prompt injection patterns
    prompt_patterns = [
        r"(ignore previous instructions)",
        r"(bypass security)",
        r"(act as admin)",
    ]

    combined_patterns = sql_patterns + prompt_patterns

    for pattern in combined_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return None

    return text.strip()