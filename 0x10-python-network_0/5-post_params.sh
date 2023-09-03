#!/bin/bash
# send post req with a body
curl -s -X POST -d "email: test@gmail.com" -d "subject: I will always be here for PLD" $1
