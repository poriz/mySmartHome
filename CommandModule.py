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
            self.Gcmd.TakePicture()
        elif self.str == "open the door":
            self.Gcmd.DoorOpen()
        elif self.str == "close the door":
            self.Gcmd.DoorClose()
        elif self.str == "clear":
            self.Gcmd.clear()
        else:
            return 0
        