#!/usr/bin/python3
"""
1-hbtn_header.py
Fetches the status from https://alu-intranet.hbtn.io/status using urllib.
Displays the response header value of X-Request-Id.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # Get the URL from command-line arguments

    try:
        # Send a request to the URL
        with urllib.request.urlopen(url) as response:
            # Retrieve the value of the X-Request-Id header
            x_request_id = response.getheader('X-Request-Id')

            # Display the value
            print(x_request_id)
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
