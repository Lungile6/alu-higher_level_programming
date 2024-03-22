#!/bin/bash
# Send a GET request to the specified URL with a custom header and display the body of the reponse.
curl -s -L -w "%{http_code}\n" -H "X-HolbertonSchool-User-Id: 98" "$1"
