import requests
import socket

import xml.etree.ElementTree as ET

class SoundInterface:

	def upVolume(curVolume):
		newVol = curVolume + 10
		return "<volume>"+str(newVol)+"</volume>"

	def downVolume(curVolume):
		newVol = curVolume - 5
		return "<volume>"+str(newVol)+"</volume>"
	def nextSong():
		commandOne = requests.post('http://172.20.10.6:8090/key',"<key state=\"press\" sender=\"Gabbo\">NEXT_TRACK</key>")
		commandTwo = requests.post('http://172.20.10.6:8090/key',"<key state=\"release\" sender=\"Gabbo\">NEXT_TRACK</key>")

		#"<key state=\"release\" sender=\"Gabbo\">NEXT_TRACK</key>"
	def playSong():
		commandOne = requests.post('http://172.20.10.6:8090/key',"<key state=\"press\" sender=\"Gabbo\">PLAY</key>")
		commandTwo = requests.post('http://172.20.10.6:8090/key',"<key state=\"release\" sender=\"Gabbo\">PLAY</key>")

	def pauseSong():
		commandOne = requests.post('http://172.20.10.6:8090/key',"<key state=\"press\" sender=\"Gabbo\">PAUSE</key>")
		commandTwo = requests.post('http://172.20.10.6:8090/key',"<key state=\"release\" sender=\"Gabbo\">PAUSE</key>")

	def stopSong():
		commandOne = requests.post('http://172.20.10.6:8090/key',"<key state=\"press\" sender=\"Gabbo\">STOP</key>")
		commandTwo = requests.post('http://172.20.10.6:8090/key',"<key state=\"release\" sender=\"Gabbo\">STOP</key>")

	def turnOff():
		commandOne = requests.post('http://172.20.10.6:8090/key',"<key state=\"press\" sender=\"Gabbo\">POWER</key>")
		commandTwo = requests.post('http://172.20.10.6:8090/key',"<key state=\"release\" sender=\"Gabbo\">POWER</key>")
	
	def listSources():
		commandOne = requests.get('http://172.20.10.6:8090/sources')#,"<key state=\"press\" sender=\"Gabbo\">POWER</key>")
		return commandOne.text 


# #def main():
# 	#ip = socket.gethostbyname(socket.gethostname())
# 	#print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

# 	h2 = requests.get('http://172.20.10.6:8090/trackInfo')
# 	print h2.text
# 	print "\n \n"
# 	root = ET.fromstring(h2.text)
# 	for child in root:
# 		print child.tag, child.attrib
# 	#h3 = requests.post('http://172.20.10.6:8090/volume', setVolume(0))
# 	#print h3.text
	
# 	curVolume = 10
# 	x = raw_input("What command ?")
# 	while x:
# 		if x == "up":

# 			h3 = requests.post('http://172.20.10.6:8090/volume', upVolume(curVolume))
# 			print h3.text
# 			curVolume += 10
# 		elif x == "down":
# 			h3 = requests.post('http://172.20.10.6:8090/volume', downVolume(curVolume))
# 			print h3.text
# 			curVolume -= 10
# 		elif x == "next":
# 			#h3 = requests.post('http://172.20.10.6:8090/volume', setVolume(curVolume))
# 			#print h3.text
# 			nextSong()
# 		elif x == "play":
# 			playSong()
# 		elif x == "pause":
# 			pauseSong()
# 		elif x == "off":
# 			turnOff()
# 		elif x == "stopSong":
# 			stopSong()
# 		elif x =="source":
# 			print(listSources())
# 		else:
# 			print "incorrect input"
# 			x = raw_input("What command? ")



# 		x = raw_input("What command? ")
# main()


		


##print h2.text