import Leap, sys, thread, time, math
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from SoundInterface import SoundInterface
        
class MotionListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    operation_names = ['volumeUp','volumeDown','togglePlay','togglePower','restartCurrent']

    def on_init(self, controller):
        print "Initialized"
        self.leapControl = SoundInterface()
        self.leapControl.togglePower()
        self.leapControl.playSong()

    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);

    def on_disconnect(self, controller):
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"
        
    def commandSwipe(self,directionTuple):
        command = ""
        x = directionTuple[0]
##        z = directionTuple[2]
##        if abs(x) > abs(z):
        if x > 0:
            command = "next"
        else:
            command = "last"
##        else:
##            if z > 0:
##                command = "volumeUp"
##            else:
##                command = "volumeDown"
        return command
    
    def listToDictInit(self, list_keys):
        dic = {}
        for each in list_keys:
            dic[each] = 0
        return dic
    
    def getCommand(self,dic):
        maximumInt = 0
        maximum = ""
        for eachKey in dic:
            if dic[eachKey] > maximumInt:
                maximum = eachKey
        return maximum

    def on_frame(self, controller):
        frame = controller.frame()
        start_time_frame = frame.timestamp        
        nextCommand = self.listToDictInit(self.operation_names)
        counter = 0
        currentPreset = 1
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            normal = hand.palm_normal
            direction = hand.direction

            if hand.grab_strength > .95:
                self.leapControl.pauseSong()
            elif not self.leapControl.play and hand.grab_strength < .2:
                self.leapControl.playSong()
            #elif hand.fingers.extended()[0]==hand.fingers.finger_type(hand.Finger.TYPE_INDEX):
            #    self.leapControl.choosePreset(1)


#            fingers = frame.fingers.extended()
#            currTime = frame.timestamp
#            cont = True
#            while (len(fingers)==2 and cont):
#                if float(currTime) -float(frame.timestamp) > 300:
#                    cont = False
#                    print "mission accomplished"
                   

                #print(len(finger))

                #print "    %s finger, id: %d, length: %fmm, width: %fmm" % (
                   # self.finger_names[finger.type],
                   # finger.id,
                   # finger.length,
                   # finger.width)
                   
        inputs = []    
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)
                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                    clockwiseness = "clockwise"
                    print "Volume up"
##                    if circle.state != Leap.Gesture.STATE_START:
##                        previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
##                        swept_circle =  int(circle.progress - previous_update.progress)
##                        print(swept_circle)
##                        self.leapControl.upVolume(swept_circle)
                    #if circle.progress > 0:
                        #
                    self.leapControl.upVolume()
                    #if len(inputs)>3 and inputs[-1] == inputs[-2]:
                   #    self.leapControl.upVolume()
                    #    inputs.pop()
                        #inputs.pop()
                   # else:
                    #    inputs.append("vu")
                    
                else:
                    self.leapControl.downVolume()
                   # clockwiseness = "counterclockwise"
                    
                    #if len(inputs)>1 and inputs[-1] == inputs[-2]:
                      #  print "Volume down"
                     #   self.leapControl.downVolume()
                      #  inputs.pop()
                        #inputs.pop()
                   # else:
                       # inputs.append("vd")
                       

                    #nextCommand['restartCurrent'] +=1
                    
                    #print frame.timestamp
            #print clockwiseness
                
              
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                nextCommand = self.commandSwipe(swipe.direction)
                print nextCommand
##                if nextCommand == "volumeDown":
##                    if len(inputs)>3 and inputs[-1] == inputs[-2]:
##                        self.leapControl.nextSong()
##                        inputs.pop()
##                        inputs.pop()
##                    else:
##                        inputs.append("p")
####                    nextCommand['volumeDown']  +=1
##                elif nextCommand == "volumeUp":
##                    if len(inputs)>3 and inputs[-1] == inputs[-2]:
##                        print "Prev Song"
##                        self.leapControl.prevSong()
##                        inputs.pop()
##                        inputs.pop()
##                    else:
##                        inputs.append("n")
                    
##                    nextCommand['volumeUp'] += 1
                if nextCommand == "next":
                    print inputs
                    if len(inputs)>1 and inputs[-1] == inputs[-2]:
                        print "Next Song"
                        self.leapControl.nextSong()
                        inputs.pop()
                        #inputs.pop()
                    else:
                        inputs.append("n")
##                    nextCommand['nextSong'] += 1
                elif nextCommand == "last":
                    print inputs
                    if len(inputs)>3 and inputs[-1] == inputs[-2]:
                        self.leapControl.prevSong()
                        inputs.pop()
                        #inputs.pop()
                    else:
                        inputs.append("p")
##                    nextCommand['prevSong'] += 1

                
                #self.leapControl.nextSong()
                #print " Key Tap id: %s,state: %s, position: %s, direction: %s" % (
                  #     self.state_names[gesture.state],
                   #    swipe.position, swipe.direction)
                #if self.state_names[gesture.state]=="STATE_START":
                   # while self.state_names[gesture.state] != "STATE_END":
                    #    print "swipe in prgoress"
                for hand in frame.hands:
                    if len(hand.fingers.extended())==2:
                        print "Two finger swipe"
                        if currentPreset < 6:
                            self.leapControl.choosePreset(currentPreset+1)
                    elif len(hand.fingers.extended())==3:
                        print "Three finger swipe"
                        if currentPreset > 1:
                            self.leapControl.choosePreset(currentPreset-1)
                    
            
            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                keytap = KeyTapGesture(gesture)
                self.leapControl.togglePlay()
                #nextCommand['togglePlay'] +=1
                #print "  Key Tap id: %d, %s, position: %s, direction: %s" % (
                #        gesture.id, self.state_names[gesture.state],
                #        keytap.position, keytap.direction )
        #if counter >5:
           # print self.getCommand(nextCommand)
           # nextCommand = self.listToDictInit(self.operation_names)
           # counter = 0
        #else:
           # counter +=1
                
def main():
    # Create a listener and controller
    listener = MotionListener()
    controller = Leap.Controller()
    controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
    controller.config.set("background_app_mode",2)
    controller.config.save()
    

    # Have the listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
