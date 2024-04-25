#!/bin/bash
# Displays all HTTP methods the server will accept using curl
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d ' ' -f 2-
