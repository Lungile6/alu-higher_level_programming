#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]   # Get the URL from command-line arguments
    email = sys.argv[2]   # Get the email from command-line arguments

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).emcode('utf-8')

    try:
        # Send a POST request to the URL
        with urllib.request.urlopen(url, data) as response:
            # Read the content of the response (in bytes)
            content = response.read()

            # Decode the content to UTF-8 to get a human-readable string
            utf8_content = content.decode('utf-8')

            # Display the response body
            print(utf8_content)
    except urllib.error.URLerror as e:
        print(f"Error: {e.reason")
