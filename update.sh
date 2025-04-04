#!/bin/bash
curl -o /root/rawboard.json --location 'https://api.sportradar.us/golf/trial/pga/v3/en/2025/tournaments/2cba1945-dc1c-4131-92f4-cfdac8c45060/leaderboard.json?api_key=1RGi6YGiXgDcJoXN0kWxx3HMSqJLSKFKZitbDK3Q'
python3 mungedata.py
cd /root/golfdraft
git pull
git commit -a -m "update leaderboard"
git push
date
