#!/bin/bash
# Send a GET request to the specified URL with a custom header and display the body of the reponse.
curl -s -H "X-HorbetonSchool_User-Id: 98" "$1"
