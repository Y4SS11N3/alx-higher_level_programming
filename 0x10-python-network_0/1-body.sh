#!/bin/bash
# Displays the body of the response with a 200 status code using curl

curl -sL -w "%{http_code}\n" "$1" -o /dev/null | grep "200" > /dev/null && curl -sL "$1"
