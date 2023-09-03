#!/bin/bash
# display only the status code of the response
curl -sIo /dev/null -w "%{response_code}" $1
