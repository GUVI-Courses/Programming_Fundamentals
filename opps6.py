from abc import ABC,abstractmethod

# creating a abstract class
class Mobile(ABC):

    @abstractmethod
    def camera(self):
        pass
    

    @abstractmethod
    def musicplayer(self):
        pass

    @abstractmethod
    def whatsapp(self):
        pass

    def contact(self):
        pass


# implementing a abstract class into PHone
class Phone(Mobile):
    def camera(self):
        print("On the camera")

    def musicplayer(self):
        print("play the music")

    def whatsapp(self):
        print("on the whatsapp")

obj1=Phone()
obj1.camera()
obj1.musicplayer()
obj1.whatsapp()