# importlar
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager # mapmanager sınıfını diğer dosyadan aldık
from hero import Hero # Hero sınıfını al

class Game(ShowBase):
   def __init__(self):
       ShowBase.__init__(self)
       self.land = Mapmanager() #mapmanager sınıfını çağır
       x,y = self.land.loadLand("land.txt") # harita yükle (land2 ve land3 de var)
       base.camLens.setFov(90) # bakış açısı
       self.hero = Hero() # ana karakter oluştur

game = Game() #oyunu yükle
game.run() # oyunu çalıştır