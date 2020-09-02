#!/usr/bin/env python
#from gpiozero import Motor

class MotorEvents:

    def __init__(self, pins):
        print('GPIO Pins Used: ', pins)
        #self.motor_left = Motor(pins.back_left, pins.front_left)
        #self.motor_right = Motor(pins.back_right, pins.front_right)
        self.moving = False
    
    def up_event(self, trigger):
        if not self.moving:
            self.moving = True
            #self.motor_left.forward()
            #self.motor_right.forward()
            print('Drive forward')
    def down_event(self, trigger):
        if not self.moving:
            self.moving = True
            #self.motor_left.backward()
            #self.motor_right.backward()
            print('Drive backward')
    def left_event(self, trigger):
        if not self.moving:
            self.moving = True
            #self.motor_left.backward()
            #self.motor_right.forward()
            print('Drive left')
    def right_event(self, trigger):
        if not self.moving:
            self.moving = True
            #self.motor_left.forward()
            #self.motor_right.backward()
            print('Drive right')
    def stop_event(self, trigger):
        if self.moving:
            self.moving = False
            #self.motor_left.stop()
            #self.motor_right.stop()
            print('Stop')
    def close_event(self, trigger):
        self.stop_event(trigger)
        #self.motor_left.close()
        #self.motor_right.close()
        print('Resources released.')
        return 'close'
