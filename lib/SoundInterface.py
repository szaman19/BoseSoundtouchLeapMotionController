import requests
import socket
import xml.etree.ElementTree as ET

IP_ADDRESS = "http://172.20.10.6:8090/"
KEY_PRESS = "<key state=\"press\" sender=\"Gabbo\">"
KEY_RELEASE = "<key state=\"release\" sender=\"Gabbo\">"
KEY_END_TAG = "</key>"

class SoundInterface:
    def __init__(self):
        self.curVolume = 20
        self.power = False
        self.play = True

    def upVolume(self, val=1):
        newVol = "<volume>"+str(self.curVolume+(5*val))+"</volume>"
        com = requests.post(IP_ADDRESS+'volume', newVol)
        self.curVolume += 10
    
    def setVolume(self, newVol):
        newVol = "<volume>"+str(newVol)+"</volume>"
        com = requests.post(IP_ADDRESS+'volume', newVol)

    def downVolume(self,val=1):
        newVol = "<volume>"+str(self.curVolume-(5*val))+"</volume>"
        com = requests.post(IP_ADDRESS+'volume', newVol)
        self.curVolume -=10
        
    def nextSong(self):
        commandOne = requests.post(IP_ADDRESS+'key',KEY_PRESS+"NEXT_TRACK"+KEY_END_TAG)
        commandTwo = requests.post(IP_ADDRESS+'key',KEY_RELEASE+"NEXT_TRACK"+KEY_END_TAG)

    def prevSong(self):
        commandPrevOne = requests.post(IP_ADDRESS+'key',KEY_PRESS+"PREV_TRACK"+KEY_END_TAG)
        commandPrevTwo = requests.post(IP_ADDRESS+'key',KEY_RELEASE+"PREV_TRACK"+KEY_END_TAG)

    def restartCurrent(self):
        self.nextSong()
        self.prevSong()

    def playSong(self):
        commandOne = requests.post(IP_ADDRESS+'key',KEY_PRESS+"PLAY"+KEY_END_TAG)
        commandTwo = requests.post(IP_ADDRESS+'key',KEY_RELEASE+"PLAY"+KEY_END_TAG)
        self.play = True

    def pauseSong(self):
        commandOne = requests.post(IP_ADDRESS+'key',KEY_PRESS+"PAUSE"+KEY_END_TAG)
        commandTwo = requests.post(IP_ADDRESS+'key',KEY_RELEASE+"PAUSE"+KEY_END_TAG)
        self.play = False

    def togglePlay(self):
        if self.play:
            self.pauseSong()
        else:
            self.playSong()

    def stopSong(self):
        commandOne = requests.post(IP_ADDRESS+'key',KEY_PRESS+"STOP"+KEY_END_TAG)
        commandTwo = requests.post(IP_ADDRESS+'key',KEY_RELEASE+"STOP"+KEY_END_TAG)
        self.play = False

    def togglePower(self):
        commandOne = requests.post(IP_ADDRESS+'key',KEY_PRESS+"POWER"+KEY_END_TAG)
        commandTwo = requests.post(IP_ADDRESS+'key',KEY_PRESSS+"POWER"+KEY_END_TAG)
        if self.power:
            self.power = False
        else:
            self.power = True
    
    def listSources(self):
        commandOne = requests.get(IP_ADDRESS+'sources')
        return commandOne.text
