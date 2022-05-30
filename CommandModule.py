import GPIOCommand

class Command:
    def __init__(self,str):
        self.str = str
        self.Gcmd = GPIOCommand.movement()
        
    def chooseCommand(self,str):
        if self.str == "turn on the lamp":
            self.Gcmd.LampOn()
            
        elif self.str == "turn off the lamp":
            self.Gcmd.LampOff()
            
        elif self.str == "take a picture":
            Gcmd.takePicture()
        elif self.str == "open the door":
            Gcmd.open1
        elif self.str == "close the door":
            Gcmd.close1
        else:
            return 0
        