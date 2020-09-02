#!/usr/bin/env python
from gpiozero import Motor

class MotorEvents:

    def __init__(self, left_pins, right_pins):
        print(left_pins)
        print(right_pins)
        #self.motor_left = Motor(left_pins[0], left_pins[1])
        #self.motor_right = Motor(right_pins[0], right_pins[1])
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
