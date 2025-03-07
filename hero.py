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
    
    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def look_at(self):
        pass

    def just_move(self, angle):
        pass

    def move_to(self, angle):
        pass