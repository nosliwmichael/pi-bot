# pi-bot-controls

This project aims to provide a simple way to interact with DC motors connected to a RaspberryPi using Python.
The first step is to define a simple class to abstract our interaction with the motors.

### MotorEvents:
  **Methods**
  1. up_event: Used to drive the motors forward.
  2. down_event: Used to drive the motors backward.
  3. left_event: Used to drive the left motor backward and the right motor forward.
  4. right_event: Used to drive the right motor backward and the left motor forward.
  5. stop_event: Used to stop the motors from spinning.

  **Properties**
  1. moving: This class also contains a "moving" property to see if the motors are already in motion. This is useful when dealing with key inputs because a key down event will get triggered many times while the key is being held down. Using the "moving" property, I can prevent the repeatedly spamming the motor driver with inputs.
 
### KeyboardListener:
  **Methods**
  1. on_press: Calls the keyMap to retrieve the correct event for the key that has been pressed. Then sends the key/event combo to the run_event method.
  2. on_release: Same as on_press except it occurs when the key is let go.
  3. run_event: If an event is provided, it executes the event.
  4. start: Starts listening to keyboard inputs.
  5. close: Stops the keyboard listener.
 
  **Properties**
  1. keyMap: The listener will call the keyMap to find and execute events for the key that is pressed.

### KeyMap
  **Methods**
  1. keyPressEvent: This method will loop through all of the keys we've mapped in our JSON file and try to get the event for the key that we've pressed. It returns the event to the caller.
  2. keyReleaseEvent: Same as keyPressEvent except it occurs when the key is let go.
  3. getEvent: This method checks if the key pressed matches the key from the JSON key map. If yes, it attempts to return an event for the key.

  **Properties**
  1. keyMap: The source of this object is not important. I'm loading it from a JSON file. It should contain an array called "keys" which contains objects that have 3 properties: name (name of key), pressed (event to call when key is pressed), released (event to call when key is released).
  2. events: This should be an object that contains methods that correspond to your pressed/released JSON events. For example: The UP arrow key is mapped to the "up_event". The events object in my case would be MotorEvents which has a method called "up_event". Hence, the "up_event" method will be called when I press the UP arrow key.
