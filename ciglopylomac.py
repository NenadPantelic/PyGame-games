import pygame
import time

dimekran=960,720
ciglaw = 60
ciglah = 15
platfw = 100
platfh = 12
loptad = 16
loptar = loptad / 2
xmaxplatf= dimekran[0] - platfw
xmaxlopta = dimekran[0] - loptad
ymaxlopta = dimekran[1] - loptad
platfy = dimekran [1] - platfh - 10


loptaplatf = 0
igra = 1
pobeda = 2
poraz = 3
novinivo = 4

crna = ( 0, 0, 0)
bela = (255, 255, 255)
bojaplatf = (65, 105, 225)
bojacigla=(255,215,0)
bojalopta=(0,255,0)



class Ciglolomac:
	
        def __init__(sebe):
                pygame.init()
		
                sebe.ekran = pygame.display.set_mode(dimekran)
                pygame.display.set_caption("Ciglopylomac by Nenad Pantelic")
		
                sebe.sat = pygame.time.Clock()
		
                if pygame.font:
                        sebe.font = pygame.font.Font(None, 30)
                else:
                        self.font = None
		
	
			
                sebe.initigra(1, 0, 3)

        def initigra(sebe, nivo, skor, zivot):
                sebe.nivo = nivo
                sebe.zivot = zivot
                sebe.skor = skor
                sebe.stanje= loptaplatf
	
                sebe.platf = pygame.Rect(480, platfy, platfw, platfh)
                sebe.lopta = pygame.Rect(480, platfy - loptad, loptad ,loptad)
	
                sebe.loptav = [5, -5]
	
                if sebe.nivo == 1:
                        sebe.stvoricigle1()
                if sebe.nivo == 2:
                        sebe.stvoricigle2()
                if sebe.nivo == 3:
                        sebe.stvoricigle3()
                if sebe.nivo == 4:
                        sebe.stvoricigle4()
                if sebe.nivo == 5:
                        sebe.stvoricigle5()
                if sebe.nivo == 6:
                        sebe.stvoricigle6()
                if sebe.nivo == 7:
                        sebe.stvoricigle7()
                if sebe.nivo == 8:
                        sebe.stvoricigle8()
                if sebe.nivo == 9:
                        sebe.stvoricigle9()
                if sebe.nivo == 10:
                        sebe.stvoricigle10()
                if sebe.nivo == 11:
                        sebe.stvoricigle11()
                if sebe.nivo == 12:
                        sebe.stvoricigle12()
                if sebe.nivo == 13:
                        sebe.stvoricigle13()
                if sebe.nivo == 14:
                        sebe.stvoricigle14()
                if sebe.nivo == 15:
                        sebe.stvoricigle15()
                if sebe.nivo == 16:
                        sebe.stvoricigle16()
                if sebe.nivo == 17:
                        sebe.stvoricigle17()
                if sebe.nivo == 18:
                        sebe.stvoricigle18()
                if sebe.nivo == 19:
                        sebe.stvoricigle19()
                if sebe.nivo == 20:
                        sebe.stvoricigle20()

                if sebe.nivo in range(1,6):
                        sebe.loptav=[5,-5]
                if sebe.nivo in range(6,11):
                        sebe.loptav=[-6,6]
                if sebe.nivo in range(12,16):
                        sebe.loptav=[7,-7]
                if sebe.nivo in range(16,18):
                        sebe.loptav=[9,-9]
                if sebe.nivo in (11,18,19,20):
                        sebe.loptav=[10,-10]
                        
        def stvoricigle1(sebe):
            ypoz = 45
            sebe.cigle=[]
            for i in range(11):
                xpoz = 45
                for j in range(12):
                    sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=ciglaw + 12
                ypoz += ciglah + 8

        def stvoricigle2(sebe):
            ypoz = 45
            sebe.cigle=[]
            for i in range(11):
                xpoz = 45
                for j in range(12):
                    if (j % 2 ==0):
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                        xpoz+= (ciglaw + 25) * 2
                ypoz += ciglah + 8
	    
		
        def stvoricigle3(sebe):
            ypoz = 45
            sebe.cigle=[]
            for i in range(15):
                xpoz = 45
                if i % 2 == 1:
                    for j in range(12):
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                        xpoz+=ciglaw + 12
                    ypoz += (ciglah + 6) * 2

        def stvoricigle4(sebe):
            ypoz = 45
            sebe.cigle=[]
            for i in range(15):
                xpoz = 45
                if i % 2 == 1:
                    for j in range(16):
                        if j%2 == 1:
                            sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                        xpoz+=(ciglaw + 10) * 2
                    ypoz += (ciglah + 6) * 2

        def stvoricigle5(sebe):
            ypoz = 45
            sebe.cigle=[]
            for i in range(14):
                xpoz = 45
                if i % 2 == 1:
                    for j in range(13):
                        if j%2 == 1:
                            sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                        xpoz+=(ciglaw + 12) 
                    ypoz += ciglah + 33

        def stvoricigle6(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(16):
                xpoz = 35
                for j in range(12):
                    if j!= i and i+j!=11:
                        sebe.cigle.append(pygame.Rect(xpoz+8,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 12) 
                ypoz += ciglah + 7

        def stvoricigle7(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(16):
                xpoz = 35
                for j in range(12):
                    if (j+i)%2==0:
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 12) 
                ypoz += ciglah + 7
                
        def stvoricigle8(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(14,0,-1):
                xpoz = 35
                for j in range(12):
                    if j==i:
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 12) 
                ypoz += ciglah + 7
            for i in range(14,0,-1):
                xpoz = 35
                for j in range(12):
                    if j==i:
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 12) 
                ypoz += ciglah + 7
                
        def stvoricigle9(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(16):
                xpoz = 35
                for j in range(12):
                    if j**2==i or  i+2==j or j+2==i  :
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 12) 
                ypoz += ciglah + 7

        def stvoricigle10(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(11):
                xpoz = 35
                for j in range(12):
                    if i!=5 and j not in (2,5,6,9):
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 12) 
                ypoz += ciglah + 7


        def stvoricigle11(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(11):
                xpoz = 35
                for j in range(12):
                    if (i+j)%5==0 and (j-i)%5==0 :
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 12) 
                ypoz += ciglah + 7

        def stvoricigle12(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(11):
                xpoz = 35
                for j in range(12):
                    if i*3==j or j*2==i  or j+i==5 or j-i==4:
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 12) 
                ypoz += ciglah + 7

        def stvoricigle13(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(13):
                xpoz = 35
                for j in range(13):
                    if  i in (0,12) or j in (0,12) :
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 10) 
                ypoz += ciglah + 5

        def stvoricigle14(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(11):
                xpoz = 45
                for j in range(11):
                    if (i+j)==5 or (i-j)==5 or (i+j)==-5 or (i-j)==-5 or (i==5 and j==5) or(i+j)%15==0 and(i!=0 and j!=0):  
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 10) 
                ypoz += ciglah + 10

        def stvoricigle15(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(13):
                xpoz = 35
                for j in range(13):
                    if i in (0,12) or j in(0,2,4,6,8,10,12) :  
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 10) 
                ypoz += ciglah + 10

        def stvoricigle16(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(11):
                xpoz = 45
                for j in range(11):
                    if (i==0 and j==0) or j in(1,3,5,7,9) or (j==4 and i in (0,10)) or (j==8 and i in(0,10)):   
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 10) 
                ypoz += ciglah + 10

        def stvoricigle17(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(11):
                xpoz = 45
                for j in range(11):
                    if j==5 or i==10 or (i==9 and j in range(1,10)) or (i==8 and j in range(2,9)) or (i==7 and j in range(3,8)) or (i==6 and j in range (4,7)) or (i==5 and j in range (5,6)) or (i==4 and j in range(4,7)) or (i==3 and j in range (3,8))or (i==2 and j in range(2,9)) or (i==1 and j in range(1,10)) or (i==0 and j in range(0,11)):   
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 10) 
                ypoz += ciglah + 10

        def stvoricigle18(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(11):
                xpoz = 45
                for j in range(11):
                    if (i+j==3) or (i-j==4 and j <4)  or (i==8 and j<4) or (j==5 and i<9) or (j==7 and i<9) or (j==7 and i ==10):                   
                        sebe.cigle.append(pygame.Rect(xpoz+120,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 10) 
                ypoz += ciglah + 10


        def stvoricigle19(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(11):
                xpoz = 45
                for j in range(11):
                    if (i+j)==5 or (i-j)==5 or (i+j)==-5 or (i-j)==-5 or (i==3 and j in (4,6)) or(i+j)%15==0 and(i!=0 and j!=0) or ((i-j)==3 and j>2 and i!=10) or (i==7 and j==6) or (i==6 and j==7)   :  
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 10) 
                ypoz += ciglah + 10


        def stvoricigle20(sebe):
            ypoz = 35
            sebe.cigle=[]
            for i in range(13):
                xpoz = 45
                for j in range(13):
                    if j in (0,4,7,9) or (i in (0,5,12) and j<3) or (i==1 and j==5) or (i==2 and j==6) or (j==10 and i in(0,12)) or (j==12 and i in range(2,11)) or (j==11 and i in(1,11))   :  
                        sebe.cigle.append(pygame.Rect(xpoz,ypoz,ciglaw,ciglah))
                    xpoz+=(ciglaw + 10) 
                ypoz += ciglah + 10
		
    
	
			
        def nacrtajcigle(sebe):
            for cigla in sebe.cigle:
                pygame.draw.rect(sebe.ekran, bojacigla, cigla)
		
		
        def komande(sebe):
                tasteri = pygame.key.get_pressed()
	
                if tasteri[pygame.K_LEFT]:
                	sebe.platf.left -= 10
                	if sebe.platf.left < 0:
                		sebe.platf.left = 0
			
                if tasteri[pygame.K_RIGHT]:
                	sebe.platf.left += 10
                	if sebe.platf.left > xmaxplatf:
                		sebe.platf.left = xmaxplatf
			
                if tasteri[pygame.K_SPACE] and sebe.stanje == loptaplatf:
                	sebe.loptav = sebe.loptav
                	sebe.stanje = igra
			
                elif tasteri[pygame.K_RETURN] and sebe.stanje == pobeda:
                        sebe.nivo += 1
                        if sebe.nivo % 4==0:
                            sebe.zivot += 1
                        sebe.initigra(sebe.nivo, sebe.skor, sebe.zivot)
			
                elif tasteri[pygame.K_RETURN] and sebe.stanje == poraz:
                	sebe.initigra(1,0,3)
		
        def kretanje (sebe):
                sebe.lopta.left += sebe.loptav[0]
                sebe.lopta.top += sebe.loptav[1]
	
                if sebe.lopta.left <= 0:
                	sebe.lopta.left = 0
                	sebe.loptav[0] = -sebe.loptav[0]
                elif sebe.lopta.left >= xmaxlopta:
                	sebe.lopta.left = xmaxlopta
                	sebe.loptav[0] = -sebe.loptav[0]
		
                if sebe.lopta.top < 0:
                	sebe.lopta.top = 0
                	sebe.loptav[1] = -sebe.loptav[1]
		
        def sudari(sebe):
                for cigla in sebe.cigle:
                        if sebe.lopta.colliderect (cigla):
                                sebe.skor += 3
                                sebe.loptav[1] = -sebe.loptav[1]
                                sebe.cigle.remove(cigla)
                                pygame.mixer.Sound('dry.mp3')
                                break
		
                if len(sebe.cigle) == 0:
                        sebe.stanje = pobeda
    		
                if sebe.lopta.colliderect (sebe.platf):
                        sebe.lopta.top = platfy - loptad
                        sebe.loptav[1] = -sebe.loptav[1]
                        pygame.mixer.Sound('dry.mp3')
		
                elif sebe.lopta.top > sebe.platf.top:
                        sebe.zivot -= 1
                        pygame.mixer.Sound('ray.mp3')
                        if sebe.zivot > 0:
                        	sebe.stanje = loptaplatf
                        else:
                        	sebe.stanje = poraz
				
        def statusi(sebe):
        	if sebe.font:
        		fontpoz = sebe.font.render("NIVO: " + str(sebe.nivo ) + " SKOR: " + str(sebe.skor) + " ZIVOTI: " + str(sebe.zivot), False, crna)
        		sebe.ekran.blit(fontpoz, (205, 5))
		
		
        def poruka(sebe, poruka):
        	if sebe.font:
        		vel = sebe.font.size(poruka)
        		fontpoz = sebe.font.render(poruka, False, crna)
        		m = (dimekran[0] - vel[0])
        		n = (dimekran[1] - vel[1]) / 1
        		sebe.ekran.blit(fontpoz, (m, n))
		
		
        def pokreni(sebe):
        	while 1:
        		for event in pygame.event.get():
        			if event.type == pygame.QUIT:
        				sys.exit
				
        		sebe.sat.tick(50)
        		sebe.ekran.fill(bela)
        		sebe.komande()
		
        		if sebe.stanje == igra:
        			sebe.kretanje()
        			sebe.sudari()
        		elif sebe.stanje == loptaplatf:
        			sebe.lopta.left = sebe.platf.left + sebe.platf.width / 2
        			sebe.lopta.top = sebe.platf.top - sebe.lopta.height
        			sebe.poruka("PRITISNI SPEJS ZA START.")
        		elif sebe.stanje == poraz:
        			sebe.poruka("GAME OVER. PRITISNI ENTER ZA NOVU IGRU.")
        		elif sebe.stanje == pobeda:
        			sebe.poruka("POBEDA! PRITISNI ENTER ZA NOVI NIVO")
        		elif sebe.stanje == pobeda and sebe.nivo == 20:
        			sebe.poruka("BRAVO! KOMPLETIRALI STE IGRU!")
        		
			
		
			
        		pygame.draw.rect(sebe.ekran,bojaplatf, sebe.platf)
		
			
        		pygame.draw.circle(sebe.ekran, bojalopta, (sebe.lopta.left + loptar, sebe.lopta.top + loptar), loptar)
		
			
        		sebe.nacrtajcigle()
		
        		sebe.statusi()
        	
        		pygame.display.flip()
			
			
		
if __name__ == "__main__":
        Ciglolomac().pokreni()
