# Autube
Download youtube songs fast and easy. It works as high-level interface of the pafy package: https://github.com/mps-youtube/pafy
# Downloading local lists of songs
- 1 Create a local `.txt` file with the url songs, i.e:

`https://www.youtube.com/watch?v=lqHoAEJBuss`

`https://www.youtube.com/watch?v=1jfoScCnjRY`

`https://www.youtube.com/watch?v=I0zDdr9FOyM`

- 2 Download them with the `downloadLocalPlaylist(urls_path,...)` method

# Downloading online existent lists of songs
- 1 Get the url of a youtube playlist, i.e:

`https://www.youtube.com/watch?v=BrBpewHG-wI&list=PLmDTvnzs8qB22Sjh1E2MJq2VCxuit-JNn`

- 2 Download them with the `downloadPlayList(playlist_url)` method

# Features
- Convert downloaded songs to `.mp3` using `ffmpeg` and `pydub`
- Parallel downloads and convertions (the author encourages a responsible use of this functionality)
- Python 3 support only
