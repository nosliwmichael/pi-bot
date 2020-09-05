#!python3
from gpiozero import Motor

class MotorEvents:

    def __init__(self, pins):
        print('GPIO Pins Used: ', pins)
        self.motor_left = Motor(pins['left_forward'], pins['left_backward'])
        self.motor_right = Motor(pins['right_forward'], pins['right_backward'])
        self.moving = False
    
    def up_event(self):
        if not self.moving:
            self.moving = True
            self.motor_left.forward()
            self.motor_right.forward()
            return 'Drive forward'
    def down_event(self):
        if not self.moving:
            self.moving = True
            self.motor_left.backward()
            self.motor_right.backward()
            return 'Drive backward'
    def left_event(self):
        if not self.moving:
            self.moving = True
            self.motor_left.backward()
            self.motor_right.forward()
            return 'Drive left'
    def right_event(self):
        if not self.moving:
            self.moving = True
            self.motor_left.forward()
            self.motor_right.backward()
            return 'Drive right'
    def stop_event(self):
        if self.moving:
            self.moving = False
            self.motor_left.stop()
            self.motor_right.stop()
            return 'Stop'
    def close_event(self):
        self.stop_event()
        self.motor_left.close()
        self.motor_right.close()
        print('Resources released.')
        return 'close'
