import time
import keyboard


def desennha_grafico(funcao):
    x = 0
    y = 0
    wall = []
    while(True):

        if funcao == 'a':
            y = x**2
        elif funcao == 'b':
            y = x**3
        elif funcao == 'c':
            y = x
        
        for i in range(-12,12):
            for j in range(-15,15):
                if i == int(y*(-1)) and j == int(x):
                    wall.append('*')
                elif i == 0 :
                    wall.append('-')
                elif j == 0:
                    wall.append(i*-1)
                else:
                    wall.append(' ')
            print(str(wall).strip('[]').replace(',', '').replace("'", ''))
            wall1 = wall
            wall.clear()
        x+=1   

        #Imprime as variaveis abaixo do grafico
        print("y = ",y)
        print("x = ",x)

        #Ajusta para melhor aparecer na tela
        if y > 12 and x>0:
            x=-10
        time.sleep(0.3)
        print('\033c') #Limpa a tela
        if keyboard.is_pressed('space'):
            break
 
while(True):
    funcao = input("Escolha a funçao a ser desenhada: a)quadratica b)cubica c)linear: \n")
    desennha_grafico(funcao)

