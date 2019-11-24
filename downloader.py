from pytube import YouTube
import urllib.request
import urllib.parse
import sys
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow ,QFileDialog
from PyQt5.uic import loadUi


class youtubeDownloader(QMainWindow):
    def __init__(self):
        super(youtubeDownloader, self).__init__()
        loadUi('youtubedownloader.ui', self)
        try:
            self.yt = YouTube(self.linkURL.text())
            self.getTitle(self.yt.title)
        except Exception as e:
            print('handled a small error, no big deal.')
        else:
            self.videoTitle.setText('Put a valid link')       
        
        self.browseButton.clicked.connect(self.selectDir)
        self.downloadButton.clicked.connect(self.download)


    def getTitle(self,title):
    	if title== None:
    		self.videoTitle.setText('Put a valid link')

    	else:
    		self.videoTitle.setText(title)

    def selectDir(self):
    	self.downloadLocation.setText(QFileDialog.getExistingDirectory(self,'Select Directory'))


    def download(self):
    	try:
    		self.stream = self.yt.streams.first()
    		self.fileSize=self.stream.size()
    		self.stream.download(self.downloadLocation.text())
    	except Exception as e:
    		print('Still Error')
    	else:
    		self.videoTitle.setText('Put a valid link')
    		self.progressBar.setValue(0)
    		
    	 	
    	print('shit iz working')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = youtubeDownloader()
    window.setWindowTitle('Samaeen Downloader')
    window.show()
    sys.exit(app.exec_())