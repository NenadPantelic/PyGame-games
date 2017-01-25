

import random, pygame, sys
from pygame.locals import *


vlogo = 16
prozorw = 720
prozorh =  540
dimpolje = 20
assert prozorw % dimpolje == 0
assert prozorh % dimpolje == 0

poljew = int(prozorw / dimpolje)
poljeh = int (prozorh / dimpolje)

crna = (0, 0, 0)
plava1 = (0 , 0, 255)
zuta = (255, 255, 0)
bela = (255, 255, 255)
siva = (40, 40, 40)
tplava1 = (0, 0, 205)
bojapoz = crna

gore = 'gore'
dole = 'dole'
levo = 'levo'
desno = 'desno'

glava = 0

def main():
    global sat, displej, fontslova

    pygame.init()
    sat = pygame.time.Clock()
    displej = pygame.display.set_mode((prozorw, prozorh))
    fontslova = pygame.font.Font('freesansbold.ttf',18)
    pygame.display.set_caption('Piton by Nenad Pantelic')

    ekranizuj()
    while 1:
        pokreni()
        GameOverporaz()

def pokreni():
    xpoz = random.randint(15, poljew - 10)
    ypoz = random.randint(15, poljeh - 10)
    pitonpoz = [{'x':xpoz, 'y':ypoz},{'x':xpoz -1, 'y':ypoz},
                {'x':xpoz - 2, 'y':ypoz}]

    smer = desno
    jabuka = slucajnapoz()

    while 1:
        for potez in pygame.event.get():
            if potez.type == QUIT:
                kraj()
            elif potez.type == KEYDOWN:
                
                if (potez.key == K_RIGHT or potez.key == K_d) and smer != levo:
                    smer = desno
                elif (potez.key == K_UP or potez.key == K_w) and smer != dole:
                    smer = gore
                elif (potez.key == K_DOWN or potez.key == K_s) and smer != gore:
                    smer = dole
                elif (potez.key == K_LEFT or potez.key == K_a) and smer != desno:
                    smer = levo
                elif potez.key == K_ESCAPE:
                    kraj()


        if pitonpoz[glava]['x'] == -1 or pitonpoz[glava]['x'] == poljew or pitonpoz [glava]['y'] == -1 or pitonpoz[glava]['y'] == poljeh:
            return
        for pitontelo in pitonpoz[1:]:
            if pitontelo['x'] == pitonpoz[glava]['x'] and pitontelo['y'] == pitonpoz [glava]['y']:
                return
        if pitonpoz[glava]['x'] == jabuka ['x'] and pitonpoz[glava]['y'] == jabuka ['y']:
            jabuka = slucajnapoz()
        else:
            del pitonpoz[-1]

        if smer == gore:
            novaglava = {'x':pitonpoz[glava]['x'],'y':pitonpoz[glava]['y']-1}
        elif smer == dole:
            novaglava = {'x':pitonpoz[glava]['x'],'y':pitonpoz[glava]['y']+1}
        elif smer == levo:
            novaglava = {'x':pitonpoz[glava]['x']-1,'y':pitonpoz[glava]['y']}
        elif smer == desno:
            novaglava = {'x':pitonpoz[glava]['x']+1,'y':pitonpoz[glava]['y']}

        pitonpoz.insert(0, novaglava)
        displej.fill(bojapoz)
        mreza()
        nacrtajpitona(pitonpoz)
        nacrtajjabuku(jabuka)
        rezultat(len(pitonpoz) - 3)
        pygame.display.update()
        sat.tick(vlogo)

def poruka():
    porukapoc = fontslova.render('Pritisni neki taster za igru.', True ,siva)
    porukaprav = porukapoc.get_rect()
    porukaprav.topleft = (prozorw -400, prozorh - 30)
    displej.blit(porukapoc, porukaprav)

def priprema():
    if len(pygame.event.get(QUIT)) > 0:
        kraj()
    tasterpot = pygame.event.get(KEYUP)
    if len(tasterpot) == 0:
        return None
    if tasterpot[0].key == K_ESCAPE:
        kraj()
    return tasterpot[0].key

def ekranizuj():
    nazivf = pygame.font.Font('freesansbold.ttf',100)
    naziv1 = nazivf.render('Piton!',True,bela,tplava1)
    naziv2 = nazivf.render('Pajton!',True,plava1)

    rotiraj1 = 0
    rotiraj2 = 0
    while True:
        displej.fill(bojapoz)
        rotacija1 = pygame.transform.rotate(naziv1, rotiraj1)
        rotacijaprav = rotacija1.get_rect()
        rotacijaprav.center = (prozorw/ 2, prozorh /2)
        displej.blit(rotacija1, rotacijaprav)
        poruka()

        if priprema():
            pygame.event.get()
            return
        pygame.display.update()
        sat.tick(vlogo)
        rotiraj1 += 3
        rotiraj2 += 7

def kraj():

    pygame.quit()
    sys.exit()

def slucajnapoz():
    return {'x':random.randint(0,poljew-1), 'y':random.randint(0,poljeh -1)}

def GameOverporaz():
    
        
    porazfont = pygame.font.Font('freesansbold.ttf', 150)
    g = porazfont.render('Game' ,True,bela)
    o = porazfont.render('Over', True, bela)
    gp = g.get_rect()
    op = o.get_rect()
    gp.midtop = (prozorw/2,10)
    op.midtop = (prozorw /2,gp.height + 10   +25)
    displej.blit(g,gp)
    displej.blit(o,op)
    poruka()
    pygame.display.update()
    pygame.time.wait(500)
    priprema()

    while 1:
        if priprema():
            pygame.event.get()
            return
def rezultat(skor):
    skors = fontslova.render('Skor: %s' %(skor), True, bela)
    skorprav = skors.get_rect()
    skorprav.topleft =(prozorw -120,10)
    displej.blit(skors,skorprav)

def nacrtajpitona(pitonpoz):
    for poz in pitonpoz:
        x = poz['x'] *dimpolje
        y = poz['y'] * dimpolje
        pitonprav = pygame.Rect(x,y,dimpolje,dimpolje)
        pygame.draw.rect(displej,tplava1,pitonprav)
        pitonin = pygame.Rect(x+4,y+4,dimpolje - 8, dimpolje - 8)
        pygame.draw.rect(displej,plava1,pitonin)

def nacrtajjabuku(poz):
    x = poz['x'] * dimpolje
    y = poz['y'] * dimpolje
    jabukaprav = pygame.Rect(x, y,dimpolje, dimpolje)
    pygame.draw.rect(displej,zuta,jabukaprav)

def mreza():
    for x in  range(0,prozorw,dimpolje):
        pygame.draw.line(displej,siva,(x,0),(x,prozorh))
    for y in range(0,prozorh, dimpolje):
        pygame.draw.line(displej,siva,(0,y),(prozorw,y))

if __name__ =='__main__':
    main()    
    
                
                    
    
    
    
