#!/bin/bash
echo "chai@1234" | sudo systemctl disable tor.service
return_code=$?
echo $return_code
if [ $return_code -eq 0 ]; then
    echo "success"
elif [ $return_code -eq 1 ]; then
    echo "TOR service not found"
fi
