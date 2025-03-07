# ---KONTROL TUŞLARI---
# -----Kamera Kontrolleri-----
key_switch_camera = "c" # kamera, karaktere bağlı mı
key_switch_mode = "z" # engellerin içinden geçebilir mi
# -----Hareket Kontrolleri-----
key_forward = "w" # ileri
key_back = "s" # geri
key_left = "a" # sol
key_right = "d" # sağ
key_up = "e" # yukarı
key_down = "q" #aşağı
# -----Dönüş Kontrolleri-----
key_turn_left = "n" # sola dön
key_turn_right = "m" # sağa dön

# --------------------

# ---HERO SINIFI---
class Hero():

    def __init__(self, pos, land):
        self.land = land
        self.mode = True # True: Spectator, False: Normal
        self.hero = loader.loadModel("smiley")
        self.hero.setColor((1, 0.5, 1)) # 0-1 arası renk
        self.hero.setScale(0.3) # 0-1 arası boyut
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(
            -pos[0],
            -pos[1],
            -pos[2]-3
        )
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()
    
    def turn_left(self): # heading + 5
        self.hero.setH((self.hero.getH()+5)%360)

    def turn_right(self):
        self.hero.setH((self.hero.getH()-5)%360)

    def look_at(self):
        # kahramanın pozisyon bilgilerini al:
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())

        # hero nereye bakıyor:
        dx, dy = self.check_dir(angle)
        # baktığı yönde ilerlerse:
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from

    def just_move(self, angle):
        # baktığı yöne git:
        pos = self.look_at(angle)
        self.hero.setPos()

    def move_to(self, angle):
        if self.mode:
            self.just_move(angle)

    def check_dir(self, angle):
        if angle => 0 and angle <= 20:
            return (0,-1)
        elif angle <= 65:
           return (1, -1)
       elif angle <= 110:
           return (1, 0)
       elif angle <= 155:
           return (1, 1)
       elif angle <= 200:
           return (0, 1)
       elif angle <= 245:
           return (-1, 1)
       elif angle <= 290:
           return (-1, 0)
       elif angle <= 335:
           return (-1, -1)
       else:
           return (0, -1)

    def forward(self):
        pass

    def back(self):
        pass

    def right(self):
        pass

    def left(self):
        pass

    def accept_events(self):
        pass
