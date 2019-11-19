# joystick
interface with g29 steering wheel

### Install
Import the JSManager class into your code

### Use
The update_axes and update_buttons methods return a list of axis values and list of booleans representing button presses.  

axis index  
0: wheel  
1: clutch  
2: gas  
3: brake  

button index  
4: right paddle  
5: left paddle  

### Requirements
* pygame
