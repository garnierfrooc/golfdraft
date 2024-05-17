#!/bin/bash
curl -o /root/rawboard.json --location 'https://api.sportradar.us/golf/trial/pga/v3/en/2021/tournaments/790dc350-9dd7-4cbd-bd71-ee1e065d323d/leaderboard.json?api_key=LFqiquVQAd6RSldTRygPiacQK8Ub2BOu3WTXYMvZ'
python3 mungedata.py
cd /root/golfdraft
git pull
git commit -a -m "update leaderboard"
git push
date
