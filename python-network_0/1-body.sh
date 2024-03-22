#!/bin/bash
body=$(curl -s -w "%{http_code}" -o temp_body "$1")
[ "$(tail -n1 <<<"$body")" -eq 200 ] && cat temp_body; rm temp_body
