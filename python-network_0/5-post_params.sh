#!/bin/bash

# Define the URL and parameters
URL="$1"
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"

# Send a POST request using curl
response=$(curl -s -X POST "$URL" -d "email=$EMAIL" -d "subject=$SUBJECT")

# Display the response body
echo "POST params:"
echo -e "\temail: $EMAIL"
echo -e "\tsubject: $SUBJECT"
echo -e "\n$response"
