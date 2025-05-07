# All supported API key regex patterns
ALL_API_KEY_PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "AWS Secret Key": r"(?i)aws_secret_access_key[^\n]*['\"]([A-Za-z0-9/+=]{40})['\"]",
    "Google API Key": r"AIza[0-9A-Za-z\-_]{35}",
    "Slack Token": r"xox[baprs]-([0-9a-zA-Z]{10,48})",
    "GitHub Token": r"gh[pousr]_[A-Za-z0-9_]{36,255}",
    "Stripe Secret Key": r"sk_live_[0-9a-zA-Z]{24}",
    "OpenAI API Key": r"sk-[a-zA-Z0-9]{48}",
    "JWT Token": r"eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}",
    "Generic Phrase": r"(?i)(api|secret|token|key)[^\n]*['\"]([A-Za-z0-9\-_=]{16,})['\"]"
}