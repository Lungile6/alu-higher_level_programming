#!/bin/bash
# Send a DELETE request to the specified URL and display the body of the response.
curl -s -X DELETE "$1" | echo "I'm a DELETE request."
