import pygame
import sys
import copy as c
import random


dificultat = 0

while dificultat == 0:
    try:
        dificultat = int(input("Selecciona dificultat (1: fàcil, 2: mitjana, 3: difícil): "))
    except ValueError:
        print("Ingressa un valor vàlid")
    
    except IndexError:
                print("Ingressa uns índex vàlid")

radi = dificultat+2

if dificultat == 1:
    size = 8
    mines = 10

elif dificultat == 2:
    size = 15
    mines = 40

elif dificultat == 3:
    size = 20
    mines = 95
   
else:
    size = 5
    mines = 7
    radi = 2.5
    dificultat = 0

if dificultat > 2:
    difmida = 2
else:
    difmida = dificultat

ANCHO = 300 + 100*difmida*2
ALTO = ANCHO


FILAS = size
COLUMNAS = size
TAMANO_CASILLA = ANCHO // COLUMNAS

# Colores
BLANCO = "#8ecc39"
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
VERMELL = (255,0,0)
VERD = (0,255,0)
BLAU = (0,0,255)

pygame.font.init()

# *******************************************************

ruta = "PATH"

# *******************************************************

font = pygame.font.Font(ruta, 30)





def imprimeix(tablero,pantalla):
    
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if Llista[fila][columna] == 0:
                pygame.draw.rect(Llista, GRIS, (columna * TAMANO_CASILLA, fila * TAMANO_CASILLA, TAMANO_CASILLA, TAMANO_CASILLA), 1)
            else:
                pygame.draw.rect(Llista, NEGRO, (columna * TAMANO_CASILLA, fila * TAMANO_CASILLA, TAMANO_CASILLA, TAMANO_CASILLA), 1)
            

def Matriu(lst):
    llista = c.deepcopy(lst)
    for i in range(len(llista)):
        for j in range(len(llista)):
            
            if llista[i][j] == 0:
                llista[i][j] = " "

            if llista[i][j] == -1:
                llista[i][j] = "\u16B9"

    return llista



def guanyafinal(lst,Partida):
    contador = 0
    guanya = False
    llista = c.deepcopy(lst)
    for i in range(len(llista)):
        for j in range(len(llista)):
            if llista[i][j] == ' ' and Partida[i][j] != -1:
                
                contador += 1
                guanya = False

    if contador == 0:        
        guanya = True

    return guanya

def setup(lst):
    llista = c.deepcopy(lst)

    posicions = [(-1,-1), (-1,0), (-1,1),
                 (0, -1),         (0, 1),
                 (1, -1), (1, 0), (1, 1)]
  
    for i in range(len(llista)):
        valor = 0

        for j in range(len(llista)):
            valor = 0

            if llista[i][j] != -1:
                
                for direccio in posicions:
                    
                    fila_costat = direccio[0] + i
                    columna_costat = direccio[1] + j
                    
                    if 0 <= fila_costat < size and 0 <= columna_costat < size:

                        if llista[fila_costat][columna_costat] == -1:

                            valor += 1
                
                llista[i][j] = valor

    return llista

def set_mines(input_fila,input_columna,lst,mines,radi):
    
    lst_local = c.deepcopy(lst)

    for i in range(mines):
        repetit = False
        #rep = 0
        while repetit != True:
            fila = random.randint(0,size-1)
            columna = random.randint(0,size-1)

            distancia = ((columna - input_columna)**2 + (fila - input_fila)**2)**0.5
            
            if lst_local[fila][columna] == 0:
                
                if distancia > radi: 
                    lst_local[fila][columna] = -1    
                    repetit = True
    
    return lst_local

def buides(i,j,lst,visitat,cert):

    
    contador = 0
    zeros = 0
    llista = lst

    posicions = [(-1,-1), (-1,0), (-1,1),
                 (0, -1),         (0, 1),
                 (1, -1), (1, 0), (1, 1)]
    
    if llista[i][j] == 0 and (i,j) not in visitat:
        
        visitat.add((i,j))

        for direccio in posicions:

            fila_costat = direccio[0] + i
            columna_costat = direccio[1] + j
            
            if 0 <= fila_costat < size and 0 <= columna_costat < size:
                
                if (fila_costat,columna_costat) not in visitat:

                    if llista[fila_costat][columna_costat] == 0:
                       
                        Llista[i][j] = ' '
                        buides(fila_costat,columna_costat,llista,visitat,False)
                        
                    elif cert == False:
                       
                        Llista[fila_costat][columna_costat] = llista[fila_costat][columna_costat]
                        buides(fila_costat,columna_costat,llista,visitat,True)
                
                else: Llista[i][j] = ' '
   
    return Llista


def inicializar_tablero():
    return [[' ' for _ in range(COLUMNAS)] for _ in range(FILAS)]


def dibujar_tablero(pantalla):
    k = 0
    for fila,row in enumerate(Llista):
        if size %2 == 0: k += 1
        for columna,num in enumerate(row):

            color = "#e5c29f" if k%2 !=0 else "#d7b899"
            coloret = (0,0,0)

            if Llista[fila][columna] == 1:
                coloret = "#2a8fe1"
            elif Llista[fila][columna] == 2:
                coloret = "#388e3c"
            elif Llista[fila][columna] == 3:
                coloret = "#d32f2f"
            elif Llista[fila][columna] == 4:
                coloret = "#7b1fa2"
            elif Llista[fila][columna] == 5:
                coloret = "#ffcd1a"
            elif Llista[fila][columna] == "#":
                coloret = "#d32f2f"

            elif Llista[fila][columna] == '?':
                coloret = "#d32f2f"
            
            
            elif Llista[fila][columna] != 0:
                pass

            elif k % 2 != 0:

                pygame.draw.rect(pantalla, "#a7d948", (columna * TAMANO_CASILLA, fila * TAMANO_CASILLA, TAMANO_CASILLA, TAMANO_CASILLA))


            if Llista[fila][columna] == 0:
                pass
            elif Llista[fila][columna] == '?' or Llista[fila][columna] == '#':

                color = "#a7d948" if k%2 !=0 else "#8ecc39"

                pygame.draw.rect(pantalla, color, (columna * TAMANO_CASILLA, fila * TAMANO_CASILLA, TAMANO_CASILLA, TAMANO_CASILLA))
                text = font.render(str(num), True, coloret)
                text_rect = text.get_rect(center=(columna * TAMANO_CASILLA + TAMANO_CASILLA // 2, fila * TAMANO_CASILLA + TAMANO_CASILLA // 2))
                pantalla.blit(text, text_rect)
                #pygame.draw.rect(pantalla, color, (columna * TAMANO_CASILLA, fila * TAMANO_CASILLA, TAMANO_CASILLA, TAMANO_CASILLA),1)
            else:
                pygame.draw.rect(pantalla, color, (columna * TAMANO_CASILLA, fila * TAMANO_CASILLA, TAMANO_CASILLA, TAMANO_CASILLA))
                text = font.render(str(num), True, coloret)
                text_rect = text.get_rect(center=(columna * TAMANO_CASILLA + TAMANO_CASILLA // 2, fila * TAMANO_CASILLA + TAMANO_CASILLA // 2))
                pantalla.blit(text, text_rect)

            k += 1


def guanya(Partida,Pantalla,fila,columna):
    #print(Pantalla)
    if Partida[fila-1][columna-1] == -1 and Pantalla[fila-1][columna-1] != '?':
                    Pantalla[fila-1][columna-1] = "#"
                    
                    print("BOOOOM!")
                    print("Has perdut bobi")
                    
                    return True
                        
                    
    elif guanyafinal(Pantalla,Partida) == True:
                    
                    
                    print("WINWIN!")
                    print("Has guanyat siu")
                    return True
    else: return False
 


Llista = [[0] * COLUMNAS for q in range(COLUMNAS)]

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Pescamines')

    tablero = inicializar_tablero()
    
    first = True
    trenca = False
    while trenca != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

         
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                fila = y // TAMANO_CASILLA +1
                columna = x // TAMANO_CASILLA +1

                if event.button == 1:

                    if first == True:
                        Llista_mines = set_mines(fila-1,columna-1,Llista,mines,radi)
                        Partida = setup(Llista_mines)

                        fila1 = fila-1
                        columna1 = columna-1
                        
                        Pantalla = Matriu(buides(fila-1,columna-1,Partida,set(),False))

                        first = False

                    else:
                        
                        if Partida[fila-1][columna-1] != 0:

                            if Pantalla[fila-1][columna-1] == '?':
                                pass
                            
                            else:
                                Pantalla = buides(fila1,columna1,Partida,set(),False)
                                Pantalla[fila-1][columna-1] = Partida[fila-1][columna-1]
                        
                        else: 
                            if Pantalla[fila-1][columna-1] == '?':
                                pass
                            else: 
                                Pantalla = buides(fila-1,columna-1,Partida,set(),False)
                        
                    if guanya(Partida,Pantalla,fila,columna) == True:
                        
                        pantalla.fill(BLANCO)
                        dibujar_tablero(pantalla)
                        pygame.display.flip()
                        pygame.time.delay(3000)
                        trenca = True
                        


                elif event.button == 3:
                 
                    if first:
                        pass

                    else:
                        Pantalla = buides(fila1,columna1,Partida,set(),False)
                        if Pantalla[fila-1][columna-1] == 0:
                        
                            Pantalla[fila-1][columna-1] = '?'
                        
                        elif Pantalla[fila-1][columna-1] == '?':
                            Pantalla[fila-1][columna-1] = 0
                    
                    
        pantalla.fill(BLANCO)
        dibujar_tablero(pantalla)
        pygame.display.flip()

if __name__ == "__main__":
    main()

