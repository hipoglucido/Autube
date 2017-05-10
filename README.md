# Autube
Download youtube songs fast and easy. It works as high-level interface of the pafy package: https://github.com/mps-youtube/pafy

## Requirements
- python 3
- youtube-dl
- pafy
- unicodedecode
- pydub
- ffmpeg

## Downloading local lists of songs
- 1 Create a local `.txt` file with the url songs, i.e:

https://www.youtube.com/watch?v=lqHoAEJBuss

https://www.youtube.com/watch?v=1jfoScCnjRY

https://www.youtube.com/watch?v=I0zDdr9FOyM

- 2 Download them with the `downloadLocalPlaylist(urls_path,...)` method

## Downloading online existent playlists
- 1 Get the url of a youtube playlist, i.e:

`https://www.youtube.com/watch?v=BrBpewHG-wI&list=PLmDTvnzs8qB22Sjh1E2MJq2VCxuit-JNn`

- 2 Download them with the `downloadPlayList(playlist_url,...)` method

## Features
- Download individual songs in single/batch mode
- Download playlists
- Convert downloaded songs to `.mp3`
- Parallel downloads and conversions (the author encourages a responsible use of this functionality)

## Youtube songs to phone fast and ez:
The way I use this is very confortable and fast:
- I have a `music.txt` file in a place where I have fast access to.
- Whenever I find a nice song I just look it up in youtube and paste add its link to the `music.txt` file (you can put various, one below the other).
- I have the `autube.bat` file content with just the execution of the python file `how_to_use.py` (so it has to point to wherever it resides).
- The file `how_to_use.py` should be configured in such way that it will download the songs of the file `music.txt`. By default it has the configuration for my system and folder structure, just change it to yours.
- Then I add the repository folder (or wherever `autube.bat` resides) to the PATH in the environment variables, so that you can easily execute it from the command line without having to navigate folders. Once `autube.bat` is executed, the program will start downloading the songs of `music.txt` to the specified folder.
- In my case, this specified folder is my Dropbox folder, so the songs are automatically uploaded to the cloud.
- In my phone I have installed the app [Dropsync](https://play.google.com/store/apps/details?id=com.ttxapps.dropsync&hl=es), so once the files are in the cloud, I run the app from my phone and the songs will be downloaded to my phone (to a folder that you decide when you configure Dropsync).
- The idea is that you have in your phone a Music app that reads music files from that same folder

## Kown issues
youtube-dl sometimes complain. When this happens just reinstall it. If it still doesn't work uninstall pafy as well, then reinstall youtube-dl and then install pafy again.