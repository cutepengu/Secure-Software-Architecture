import re

username = input("Enter your username: ")
def sanitize_input(user_input):
    sanitized = re.sub(r'<script.*?>.*?</script>', '', user_input, flags=re.IGNORECASE | re.DOTALL)
    sanitized = sanitized.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return sanitized

# Example usage
raw_input = '<script>alert("Hacked!")</script><b>Hello</b>'
clean_input = sanitize_input(raw_input)
print("Sanitized input:", clean_input)
