# random-bits
## SpeedTestClient
This is a python script that uses selenium to extract network speed data from open-source speedtest https://librespeed.org/. 

TODO:

1. Create a commandline tool from the script, that works in background and raises an alert when the data is extracted. 

2. Currently, the server is not selected. Use the  ip2location to find the IP and then select the nearest server.

## url_shortner
This python script creates a rest api server that records the url and provide a shortned version of the url. 

TODO:

1. Reduce the size of url: find a way to reduce the length of url. Current size is although fixed but is still large.

2. Create a basic UI, and try to deploy it using MongoDB Atlas and GithubPages hosted on www.adhyay2000.github.io

## 2048
A basic python implementation of 2048 with GUI made using PyQt5.
Visit these link to know the rules https://rosettacode.org/wiki/2048. Objective is to get higest possible score. 

## Songs-downloader
A basic Youtube-Dl client that syncs the youtube-playlist songs with local copy, and downloads newly added songs from the playlist. 

Follow installation guide on 
https://github.com/ytdl-org/youtube-dl/blob/master/README.md#installation.

`ln -s song_dl.sh song_dl`

`sudo mv song_dl /etc/cron.daily`

This is preferred over setting up a cron job as the latter doesn't account for cases when the system is not available at the time of sync. However, using cron.daily ensures no such cases are missed.

Ref: https://serverfault.com/questions/52335/job-scheduling-using-crontab-what-will-happen-when-computer-is-shutdown-during