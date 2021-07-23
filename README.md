-----------------------------------------------
Rangado Downloader
-----------------------------------------------

An automatic downloader script whcih downloads every .mp3 file from the Rangadó podcast which was uploaded to https://patria.rtvs.sk/clanky/rangado-derby. The Rangado podcast
last aired on 19.07.2021

-----------------------------------------------

How it works

-----------------------------------------------

- The script will scan through the dates of uploads and creates a folder for every seperate datetimes
- The .mp3 files will be stored on the date of upload folder
- The downloaded files will be renamed to satisfy the Windows rules for file names.
- An ID will be stored in a text file for every "article" so the downloader wont download the same files again.
