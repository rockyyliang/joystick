'''
class used to read in g29 inputs

axis index
0: wheel
1: clutch
2: gas
3: brake

button index
4: right paddle
5: left paddle
'''
import pygame

class JSManager():
    def __init__(self):
        pygame.init()
        #pygame.joystick.init()
        try:
            self.js = pygame.joystick.Joystick(0)
        except:
            print('could not find joystick')
            exit()
        self.js.init()
        self.axes = self.js.get_numaxes()
        self.buttons = self.js.get_numbuttons()

    def update_axes(self):
        '''get joystick values'''
        #pygame.event.get is needed to update axis values
        pygame.event.get()
        axes_values = []
        #self.js.init()
        for a in range(self.axes):
            axis = self.js.get_axis(a)
            axes_values.append(axis)
        return axes_values

    def update_buttons(self):
        '''get button presses'''
        pygame.event.get()
        button_presses = []
        for b in range(self.buttons):
            button = self.js.get_button(b)
            button_presses.append(button)
        return button_presses

if __name__=="__main__":
    '''testing code'''
    js = JSManager()
    while True:
        vals = js.update_axes()
        buts = js.update_buttons()
        print(*vals)
        print(*buts)
        print()
