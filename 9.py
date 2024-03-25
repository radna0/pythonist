import re

# Matching phone numbers
pattern = r'\d{3}-\d{3}-\d{4}'
text = "Call me at 123-456-7890"
match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())

# Replacing text
new_text = re.sub(pattern, "XXX-XXX-XXXX", text)
print("Updated text:", new_text)
