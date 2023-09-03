#!/bin/bash
# takes url send request and display size of body
curl -sI $1  | grep 'Content-Length' | awk '{print $2}'
