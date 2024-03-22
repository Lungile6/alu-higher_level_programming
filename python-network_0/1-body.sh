#!/bin/bash
# Send a Get to the spesified URL and display the body of the response.
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
