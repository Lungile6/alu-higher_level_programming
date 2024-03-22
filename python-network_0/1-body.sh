#!/bin/bash
# Send a GET request to the specified URL and display the body of the response.
curl -s "$1" -o response_body -w '%{http_code}' | grep -q '^200$' && cat response_body; rm -f response_body
