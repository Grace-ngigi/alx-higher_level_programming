#!/bin/bash
# make a request to get a response message
curl -sX PUT -Ld "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
