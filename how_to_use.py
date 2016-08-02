from autube import *

dw=Downloader()

#Directory where the songs will be downloaded
output_dir='/home/hipoglucido/Music'

#Download a youtube playlist
playlist_url='https://www.youtube.com/watch?v=BrBpewHG-wI&list=PLmDTvnzs8qB22Sjh1E2MJq2VCxuit-JNn'
dw.downloadPlayList(to_mp3=True,output_dir=output_dir,playlist_url=playlist_url,allowParallelism=True)


#Download a local custom playlist
urls_path='default_songs_urls.txt'
dw.downloadLocalPlaylist(urls_path=urls_path,output_dir=output_dir,to_mp3=True,allowParallelism=True)

