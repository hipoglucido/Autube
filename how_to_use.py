from autube import *

dw=Downloader()

#Directory where the songs will be downloaded

#output_dir='/home/hipoglucido/Music'
#output_dir='/media/ntfs/Dropbox/MUSIIIC'
output_dir='C:\\Users\\gcvic\\Dropbox\\MUSIIIC'

#Download a youtube playlist
#playlist_url='https://www.youtube.com/watch?v=qyE9vFGKogs&list=PL9mZ9LN8BNsziV_PrOKbcMMQ80n-ByJ9W'
#dw.downloadPlayList(to_mp3=True,output_dir='/media/ntfs/Dropbox/MUSIIIC',playlist_url=playlist_url,allowParallelism=True)


#Download a local custom playlist
#urls_path='default_songs_urls.txt'
#urls_path='/media/ntfs/Dropbox/notas/music.txt'
urls_path='C:\\Users\\gcvic\\Dropbox\\notas\\music.txt'
dw.downloadLocalPlaylist(urls_path=urls_path,
						output_dir=output_dir,
						to_mp3=True,
						allowParallelism=0)

