#!/usr/bin/python3
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from command-line arguments

    try:
        # Send a request to the URL
        with urllib.request.urlopen(url) as response:
            # Read the content of the response (in bytes)
            content = response.read()

            # Decode the content to UTF-8 to get a human-readable string
            utf8_content = content.decode('utf-8')

            # Display the response body
            print(utf8_content)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
