from pydub import AudioSegment
import pafy
import numpy as np
import os
import sys
from unidecode import unidecode
from os import listdir
import re
import urllib.request
import urllib.error
import sys
import time
from time import sleep
from os.path import isfile, join

class Counter():
    def __init__(self):
        self.n=None
        self.until=None
        self.prc=None
    def getReady(self,until):
        self.n=0
        self.until=until
    def count(self):
        self.n+=1
        self.prc="{0:.2f}".format(100*self.n/self.until)




class Downloader():
    def __init__(self):
       self.counter=Counter()
       self.output_dir=''
    def downloadSong(self,url,to_mp3):
        self.counter.count()
        print("____________________________________________ [",self.counter.prc,"%]\n",url)
        video = pafy.new(url)
        audio = video.getbestaudio()
        for c in ['.','\"','|','/',' ']: #Replace also spaces for avoiding OS problems
            title=audio.title.replace(c,'_')
        title=unidecode(title)
        output_file=os.path.join(self.output_dir,title+'.'+audio.extension)
        desired_format='mp3'
        print("Going for... '",title,"'")
        if not os.path.exists(output_file) and not os.path.exists('.'.join(output_file.split('.')[:-1])+'.'+desired_format):
            print("Downloading...")
            audio.download(filepath=output_file,quiet=True,remux_audio=True)
        else:
            print("...is in local")
        if to_mp3:
            self.convert_file(input_file=output_file,desired_format=desired_format)

    def downloadSongs(self,to_mp3,urls):
        print("____________________________________________")
        print("Songs will be downloaded to ",self.output_dir)
        self.counter.getReady(until=len(urls))
        for url in urls:
            self.downloadSong(url,to_mp3)
        print("Downloaded songs are in ",self.output_dir)

    def convert_file(self,input_file,desired_format,extra_audio=0,delete_old=True):
        aux=input_file.split(os.sep)[-1]
        aux2=aux.split('.')
        name=aux2[0]
        #original_extension=aux2[1]
        output_file=os.path.join(self.output_dir,name+'.'+desired_format)
        print("Converting '",input_file,"' to ", desired_format)
        if os.path.exists(output_file):
            print("...already converted")
            return
        song = AudioSegment.from_file(input_file)
        song=song+extra_audio
        song.export(output_file, format=desired_format)
        if delete_old:
            os.remove(input_file)

    def downloadLocalPlaylist(self,urls_path=None,output_dir='',to_mp3=True):
        print("Reading url songs from ",urls_path)
        self.output_dir=output_dir
        if not urls_path:
            urls_path=join(os.path.dirname(os.path.abspath(__file__)),'default_songs_urls.txt')
        urls = [line.rstrip('\n') for line in open(urls_path)]
        self.downloadSongs(urls=urls,to_mp3=to_mp3)

    def downloadPlayList(self,playlist_url,output_dir='',to_mp3=True):
        self.output_dir=output_dir
        urls=self.getPLayListSongsUrls(playlist_url)
        self.downloadSongs(urls=urls,to_mp3=to_mp3)

    def getPLayListSongsUrls(self,playlist_url):
        '''
        Based on youParse.py project:
        http://pantuts.com/2013/02/16/youparse-extract-urls-from-youtube/
        '''
        print("Getting songs from playlist ",playlist_url)
        sTUBE = ''
        cPL = ''
        final_url = []
        if 'list=' in playlist_url:
            eq = playlist_url.rfind('=') + 1
            cPL = playlist_url[eq:]
        else:
            raise Exception('Incorrect Playlist ',playlist_url)
        try:
            yTUBE = urllib.request.urlopen(playlist_url).read()
            sTUBE = str(yTUBE)
        except urllib.error.URLError as e:
            print(e.reason)
        tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
        mat = re.findall(tmp_mat, sTUBE)
        if mat:
            for PL in mat:
                yPL = str(PL)
                if '&' in yPL:
                    yPL_amp = yPL.index('&')
                final_url.append('http://www.youtube.com/' + yPL[:yPL_amp])
            urls = list(set(final_url))
        return urls




d=Downloader()


d.downloadPlayList(to_mp3=True,output_dir='/media/ntfs/',playlist_url='https://www.youtube.com/watch?v=BrBpewHG-wI&list=PLmDTvnzs8qB22Sjh1E2MJq2VCxuit-JNn')







