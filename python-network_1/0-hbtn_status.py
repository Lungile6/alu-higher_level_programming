#!/usr/bin/python3
import urllib.request


url = 'https://alu-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

print("Body response:")
print(f"    - type: {type(content)}")
print(f"    - content: {content}")
print(f"    -utf8 content: {utf8_content}")
