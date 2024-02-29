#!/bin/bash
echo "chai@1234" | sudo -S apt -y install deborphan
sudo deborphan
yes | sudo apt --autoremove purge $(deborphan)
