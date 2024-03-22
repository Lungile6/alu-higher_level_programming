#!/bin/bash
# Send a GET request to the specified URL and display the body of the response.
status=$(curl -s -o response_body -w "%{http_code}" "$1") [ "$status" -eq 200 ] && cat response_body; rm -f response_body
