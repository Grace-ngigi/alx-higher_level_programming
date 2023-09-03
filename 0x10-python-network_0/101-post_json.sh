#!/bin/bash
# send JSON post req and display the body of the response
curl -sX POST $1 -H "Content-Type: application/json" --data @"$2"
