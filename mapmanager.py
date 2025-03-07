class Mapmanager(): # harita ile ilgilenen sınıf
    
   def __init__(self):
       self.model = 'block.egg' # blok modelini al
       self.texture = 'block.png' # blok resmini al
       self.colors = [
           (0.2, 0.2, 0.35, 1),
           (0.2, 0.5, 0.2, 1),
           (0.7, 0.2, 0.2, 1),
           (0.5, 0.3, 0.0, 1)
       ] # renk listemiz (4 renk seçeneği mevcut)
       self.startNew()
       # yeni blok eklemek için örnek kod:
       # self.addBlock((0,10,0))

   def startNew(self):
       self.land = render.attachNewNode("Land")
       # tüm harita blokları bu node'a bağlı

   def getColor(self, z): # renk listemizden seçim yapılırken kullanılır
       if z < len(self.colors): # seçilen renk numarası, listemizin içinde mevcut mu
           return self.colors[z] # varsa rengi ver
       else:
           return self.colors[len(self.colors) - 1] # yoksa son rengi ver

   def addBlock(self, position): # haritaya blok eklemek için metod
       self.block = loader.loadModel(self.model)
       self.block.setTexture(loader.loadTexture(self.texture))
       self.block.setPos(position) # pozisyonu metod girişinden alır
       self.color = self.getColor(int(position[2])) # rengi pozisyona göre otomatik verir
       # pozisyon: x, y, z
       # 2. eleman z olur bu da yüksekliktir
       # yani blok rengi yüksekliğe göre ayarlanır
       self.block.setColor(self.color)
       self.block.reparentTo(self.land) # Land node'una bağla

   def clear(self):
       # haritayı sıfırla
       self.land.removeNode() # land node'unu ve bağlı tüm blokları sil
       self.startNew() # yeni başlat


   def loadLand(self, filename):
       # text dosyasından harita oluşturur
       self.clear() # eskisini sil
       with open(filename) as file: # dosyayı aç
           y = 0
           for line in file:
               x = 0
               line = line.split(' ')
               for z in line:
                   for z0 in range(int(z)+1):
                       block = self.addBlock((x, y, z0))
                   x += 1
               y += 1
