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
        if self.mode: # aynı şey: self.mode == 1
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

    def forward(self): # ileri
        # bakış açısını al
        angle = (self.hero.getH()) % 360
        # o açıya doğru git
        self.move_to(angle)

    def back(self): # geri
        # bakış açısını al
        # 180 ekleyerek arkaya döndür
        angle = (self.hero.getH()+180) % 360
        # hesaplanmış açıya doğru git
        self.move_to(angle)

    def right(self): # sağ
        # açı + 90 ile tam sağa açı hesapla
        angle = (self.hero.getH()+90) % 360
        # oraya doğru hareket et
        self.move_to(angle)

    def left(self): # sol
        # açı + 270 ile sola açı hesapla
        angle = (self.hero.getH()+270) % 360
        # oraya doğru hareket et
        self.move_to(angle)

    def accept_events(self):
        # metodlar ile basılacak tuşlar arası bağ

        # --- DÖN ---
        # sol dön
        base.accept(key_turn_left, self.turn_left)
        # tuşa basılı tutulunca yada tekrar tekrar basılınca
        base.accept(key_turn_left + "-repeat", self.turn_left)
        # sağ dön
        base.accept(key_turn_right, self.turn_right)
        # tekrar tekrar basılınca
        base.accept(key_turn_right + "-repeat", self.turn_right)

        # --- HAREKET ---
        # ileri git
        base.accept(key_forward, self.forward)
        base.accept(key_forward + "-repeat", self.forward)
        # geri git
        base.accept(key_back, self.back)
        base.accept(key_back + "-repeat", self.back)
        # sağa git (dönme değil)
        base.accept(key_right, self.right)
        base.accept(key_right + "-repeat", self.right)
        # sola git
        base.accept(key_left, self.left)
        base.accept(key_left + "-repeat", self.left)

        # --- KAMERA MODU DEĞİŞTİR ---
        base.accept(key_switch_camera, self.changeView)
