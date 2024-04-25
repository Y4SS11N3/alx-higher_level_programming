#!/bin/bash
# Displays the size of the body of the response in bytes using curl
curl -s -o /dev/null -w "%{size_download}\n" "$1"
