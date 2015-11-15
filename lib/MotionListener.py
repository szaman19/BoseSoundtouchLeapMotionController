import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from SoundInterface import SoundInterface
        
class MotionListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"
        #self.leapControl = SoundInterface()
        #self.leapControl.playSong()

    def on_connect(self, controller):
        print "Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"
        
    def commandSwipe(self,directionTuple):
        command = ""
        x = directionTuple[0]
        z = directionTuple[2]
        if abs(x) > abs(z):
            if (x > 0):
                command = "next"
            else:
                command = "last"
        else:
            if (z > 0):
                command = "volumeUp"
            else:
                command = "volumeDown"
        return command
    
    def on_frame(self, controller):
        frame = controller.frame()
        nextCommand = ""
        start_time_frame = frame.timestamp
        
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"

            normal = hand.palm_normal
            direction = hand.direction


            #for finger in hand.fingers.extended():

                #print "    %s finger, id: %d, length: %fmm, width: %fmm" % (
                   # self.finger_names[finger.type],
                   # finger.id,
                   # finger.length,
                   # finger.width)
            
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                circle = CircleGesture(gesture)
                if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                    clockwiseness = "clockwise"
                    
                else:
                    clockwiseness = "counterclockwise"
                    self.leapControl.restartCurrent()
                    
                    print frame.timestamp
            #print clockwiseness
                
              
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                nextCommand = self.commandSwipe(swipe.direction)
                print nextCommand
                #if nextCommand == "volumeDown":
                   # self.leapControl.downVolume()
               # elif nextCommand == "volumeUp":
                   # self.leapControl.upVolume()
               # elif nextCommand == "next":
                    #self.leapControl.nextSong()
              #  elif nextCommand == "last":
                    #self.leapControl.prevSong()
                
                #self.leapControl.nextSong()
                #print " Key Tap id: %s,state: %s, position: %s, direction: %s" % (
                  #     self.state_names[gesture.state],
                   #    swipe.position, swipe.direction)
                #if self.state_names[gesture.state]=="STATE_START":
                   # while self.state_names[gesture.state] != "STATE_END":
                    #    print "swipe in prgoress"
                #for hand in frame.hands:
                   # if len(hand.fingers.extended())==2:
                        #print "Two finger swipe"
                  #  elif len(hand.fingers.extended())==3:
                    #    #print "Three finger swipe"
                    
            
            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                keytap = KeyTapGesture(gesture)
                #self.leapControl.togglePlay()
                print "  Key Tap id: %d, %s, position: %s, direction: %s" % (
                        gesture.id, self.state_names[gesture.state],
                        keytap.position, keytap.direction )
                

    
    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def main():
    # Create a sample listener and controller
    listener = MotionListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
