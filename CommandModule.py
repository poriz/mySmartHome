import GPIOCommand as Gcmd

onlamp = Gcmd.LampOn
offlamp = Gcmd.LampOff
takePicture = TakePicture
open1 = DoorOpen
close1 = DoorClose

class Command:
    def __init__(self,str):
        self.str = str
    
    def chooseCommand(self):
        if self.str == "turn on the lamp":
            onlamp()
        elif self.str == "turn off the lamp":
            offlamp()
        elif self.str == "take a picture":
            takePicture()
        elif self.str == "open the door":
            open1
        elif self.str == "close the door":
            close1
        else:
            
        