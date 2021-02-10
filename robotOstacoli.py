import pygame
import sys

#RGB (x,y,z)
NERO = (0,0,0)
BIANCO = (255,255,255)
ROSSO = (255,0,0)

pavimento=[[0,0,0,-1,-1],
           [-1,0,0,0,-1],
           [0,0,-1,-1,-1],
           [0,0,-1,0,0],
           [-1,0,0,0,0],
           [-1,-1,-1,0,0]]#-1 perche uno mi serve per numerare celle libere

lato = 100
DIMENSIONI = (len(pavimento[0]) * lato, len(pavimento) * lato)


def numeraPav():
    global pavimento
    cntCelle = 0
    for y in range(0, len(pavimento)):
        for x in range(0, len(pavimento[0])):
            if pavimento[y][x] == 0:
                pavimento[y][x] = cntCelle
                cntCelle += 1

            fnt = pygame.font.SysFont("Arial", 15)
            surf_txt = fnt.render(str(cntCelle), True, BIANCO)
            screen.blit(surf_txt, (x * lato + 15, y * lato + 15))


def disegnaGriglia():
    lato = 100
    for x in range(0, DIMENSIONI[0], lato):
        for y in range(0, DIMENSIONI[1], lato):
            quadrato = pygame.Rect(x, y, lato, lato)    #disegna dall'angolo in alto a sinistra
            pygame.draw.rect(screen, BIANCO, quadrato, 1)   #ultimo numero 1 = vuoto, niente = pieno


def disegnaOstacoli():
    for y in range(0, len(pavimento)):
        for x in range(0, len(pavimento[0])):

            if pavimento[y][x] == -1:   #c'è l'ostacolo? se si disegno l'ostacolo
                x = x * lato
                y = y * lato
                
                ostacolo = pygame.Rect(x, y, lato, lato)
                pygame.draw.rect(screen, ROSSO, ostacolo)

                x = int(x/lato)
                y = int(y/lato)




def creaDiz():      #crea un dizionario con le coordinate degli spazi liberi
    dizionario = {}
    spaziLiberi = []
    numeraPav()

    for y in range (0, len(pavimento)):
        for x in range (0, len(pavimento[y])):

            if pavimento[y][x] != -1:

                if x != 0:
                    if pavimento[y][x - 1] != -1:
                        spaziLiberi.append(pavimento[y][x - 1])
                
                if y != 0:
                    if pavimento[y - 1][x] != -1:
                        spaziLiberi.append(pavimento[y - 1][x])

                
                if x != len(pavimento[y]) - 1:
                    if pavimento[y][x + 1] != -1:
                        spaziLiberi.append(pavimento[y][x + 1])
                
                
                if y != len(pavimento) - 1:
                    if pavimento[y + 1][x] != -1:
                        spaziLiberi.append(pavimento[y + 1][x])
    
                dizionario[pavimento[y][x]] = spaziLiberi
                spaziLiberi = [] 
    
    print(dizionario)



def main():
    
    global screen
    pygame.init()
    screen = pygame.display.set_mode((DIMENSIONI[0], DIMENSIONI[1]))
    screen.fill(NERO)

    creaDiz()

    while True:
        disegnaGriglia()
        disegnaOstacoli()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()



if __name__ == "__main__":
    main()           