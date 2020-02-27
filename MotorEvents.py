class MotorEvents:

    def __init__(self):
        self.moving = False
    
    def up_event(self, trigger):
        if not self.moving:
            self.moving = True
            print('Drive forward')
    def down_event(self, trigger):
        if not self.moving:
            self.moving = True
            print('Drive backward')
    def left_event(self, trigger):
        if not self.moving:
            self.moving = True
            print('Drive left')
    def right_event(self, trigger):
        if not self.moving:
            self.moving = True
            print('Drive right')
    def stop_event(self, trigger):
        if self.moving:
            self.moving = False
            print('Stop')
