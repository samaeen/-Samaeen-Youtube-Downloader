from pytube import YouTube
import urllib.request
import urllib.parse
import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow ,QFileDialog
from PyQt5.uic import loadUi
global ytLink

class youtubeDownloader(QMainWindow):
    def __init__(self):
        super(youtubeDownloader, self).__init__()
        loadUi('youtubedownloader.ui', self)
        self.linkURL.textChanged.connect(self.updateWindow)
        self.count=1
	
            
        self.browseButton.clicked.connect(self.selectDir)
        self.downloadButton.clicked.connect(self.download)

    def updateWindow(self):
    	
    	#self.videoQuality.addItem([self.stream.resolution for self.stream in self.yt.streams.filter(progressive=True).all()])
    	try:
    		self.yt = YouTube(self.linkURL.text())
    		if self.yt.title==None:
    			print('no title available')
    			self.videoTitle.setText('Put a valid link')			
    		else:
    			self.videoTitle.setText(self.yt.title)
    			print('title loaded')
    		
    	except Exception as e:
        	self.videoTitle.setText('Put a valid link')
        	self.progressBar.setValue(0)
        	print('Something Messy')

    def selectDir(self):
    	self.downloadLocation.setText(QFileDialog.getExistingDirectory(self,'Select Directory'))

    def progressCheck(stream = None, chunk = None, file_handle = None, remaining = None,time =None):
    	print(str(filesize)+'2')
    	percent = (100*(int(str(filesize)))-remaining)/int(str(filesize))
    	print(percent)


    def download(self):
    	self.yt = YouTube(self.linkURL.text(),on_progress_callback=self.progressCheck)
    	self.stream = self.yt.streams.filter(progressive = True, file_extension = "mp4").first()
    	global filesize
    	filesize=self.stream.filesize
    	print(type(filesize))
    	self.stream.download(self.downloadLocation.text())
    	try:
    		
    		
    		
    		#self.length=self.yt.player_config_args['player_response']['videoDetails']['lengthSeconds']
    		
    		print('downloading')
    	except Exception as e:
    		self.videoTitle.setText('No valid link available')
    		print('yoooo')
    	else:
    		self.videoTitle.setText('Put a valid link')	 	
    	print('shit iz working')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = youtubeDownloader()
    window.setWindowTitle('Samaeen Downloader')
    window.show()
    sys.exit(app.exec_())