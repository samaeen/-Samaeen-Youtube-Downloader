
import pytube
import urllib.request
import urllib.parse
import sys
from PyQt4 import QtGui,QtCore
#video_link = 'https://www.youtube.com/watch?v=Oh2Dkkswy30'
#yt = pytube.YouTube(video_link)
#fn = yt.video_id
#videos = yt.streams.all()
#for vids in videos:
#	print(vids)

class Window(QtGui.QDialog):
	def __init__(self,parent=None):
		super(Window, self).__init__(parent)
		
		self.setGeometry(100,100,950,400)							#window size-first two are co ordinates of where it is starting,second two are size)
		self.setWindowTitle("Samaeen YouTube downloader")

		self.enterURL = QtGui.QLineEdit('Enter the URL')


		self.typeChoice = QtGui.QComboBox()
		self.typeChoice.addItem("Video")
		self.typeChoice.addItem("Audio")


		self.default_path='C:/Users/Shoummo/Downloads'
		self.downloadLocation = QtGui.QLineEdit(self.default_path)
		self.downloadLocation.setReadOnly(True)
		
		self.browseButton = QtGui.QPushButton('Browse')

		self.downloadButton=QtGui.QPushButton('Download')
		
		vbox=QtGui.QVBoxLayout()
		
		hbox = QtGui.QHBoxLayout()
		hbox.addWidget(self.enterURL)
		hbox.addWidget(self.typeChoice)
		
		hbox1=QtGui.QHBoxLayout()
		hbox1.addWidget(self.downloadLocation)
		hbox1.addWidget(self.browseButton)

		hbox2=QtGui.QHBoxLayout()
		hbox2.addWidget(self.downloadButton)


		vbox.addLayout(hbox)
		vbox.addLayout(hbox1)
		vbox.addLayout(hbox2)
		self.setLayout(vbox)

		self.browseButton.clicked.connect(self.selectDir)
		self.downloadButton.clicked.connect(self.download)

	def selectDir(self):
		labelSavePath.setText(QtGui.QFileDialog.getExistingDirectory(self,'Select Directory'))


	def download(self):
		url=self.enterURL.text()
		#to be added==add an exception to URL handling
		typeChoice = str(self.typeChoice.currentText())
		yt = pytube.YouTube(url)
		if typeChoice=='Video':
			videos=yt.streams.filter(mime_type="video/mp4").first().download('C:/Users/Shoummo/Downloads')
			
		if typeChoice=='Audio':
			audio=yt.streams.filter(only_audio=True).all()
		#videos=yt.streams.filter('only_'+typeChoice=True).all()
		#https://www.youtube.com/watch?v=8jPQjjsBbIc
		#https://www.youtube.com/watch?v=zOWJqNPeifU
		#print(a)
		#print(videos)
		print(typeChoice)
		

def run():
	app=QtGui.QApplication(sys.argv)
	GUI=Window()
	GUI.show()
	sys.exit(app.exec_())

run()