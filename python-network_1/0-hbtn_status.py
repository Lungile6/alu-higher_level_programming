#!/usr/bin/python3
import urllib.request


# Define the target URL
url = 'https://alu-intranet.hbtn.io/status'

# Open the URL and retrieve the response
with urllib.request.urlopen(url) as response:
    # Read the content of the response (in bytes)
    content = response.read()

    # Decode the content to UTF-8 to get a human-readable string
    utf8_content = content.decode('utf-8')

# Display the response details
print("Body response:")
print(f"    - type: {type(content)}")
print(f"    - content: {content}")
print(f"    -utf8 content: {utf8_content}")
