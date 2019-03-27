class Dimensions:                           #classe para um retângulo de dimensões X e Y
    def __init__(self,x,y):
        self.x = x                          #tamanho X do retângulo
        self.y = y                          #tamanho Y do retângulo
        self.X = [0,0,x,x,0]                #coordenadas X dos vértices do retângulo
        self.Y = [0,y,y,0,0]                #coordenadas Y dos vértices do retângulo
    def __str__(self):
        return ("Area: " + str(self.x*self.y) + "m²\n"
                  + "Size: " + str(self.x) + "x" + str(self.y) + "\n")
        
class Mower:                                #classe para um cortador
    def __init__(self,size):
        self.size = Dimensions(size,size)   #tamanho (quadrado)
        self.speed = 1                      #velocidade linear em m/s
        self.turn_time = 5                  #tempo para girar 90 graus em segundos
        self.tax = 2/3                      #taxa de repasse do corte

class Field():                              #classe para o campo
    def __init__(self,x,y):
        self.size = Dimensions(x,y)         #tamanho do campo
    def __str__(self):
        return "Field:\n" + str(self.size)
                  
class Way:                                  #classe para o caminho a ser percorrido
    def __init__(self,lm,field):
        self.lm = lm                        #caminho recebe um objeto da classe Mower
        self.field = field                  #caminho recebe um objeto da classe Field
        self.count = 0                      #contador de repetições inicializado
        self.a = [lm.size.x/2]              #coordenadas iniciais do caminho em X
        self.b = [lm.size.y/2]              #coordenadas iniciais do caminho em Y
        self.setWay()                       #chamada da fuçõo para definir as próximas coordenadas do caminho
        
        self.dist = (field.size.y-lm.size.y)*(self.count+1)                 #cálculo da distância do caminho
        self.time = self.dist/lm.speed + ((self.count-1)*2*lm.turn_time)    #cálculo do tempo que o cortador demorará para percorrer o caminho inteiro
        
    def setWay(self):                                       #função para definir as coordenadas do caminho
        z = 1                                               #variável que define o sentido do movimento do cortador no campo
        while (self.a[-1]+lm.size.x*lm.tax)<field.size.x:   #verifica se cortador não chegou ao fim do campo
            #vertical move (soma em Y)
            self.a.append(self.a[-1])                               #mantém coordenada X
            self.b.append(self.b[-1]+(field.size.y-lm.size.y)*z)    #altera coordenada Y
            z = z *(-1)                                             #inverte o sendito do movimento para o próximo movimento vertical
            
            #horizontal move (soma em X)
            if (self.a[-1]+2*lm.size.x*lm.tax)<field.size.x:    #verifica se cortador não chegou ao fim do campo
                self.a.append(self.a[-1]+lm.size.x*lm.tax)      #altera coordenada X
                self.b.append(self.b[-1])                       #mantém coordenada Y
            else:   #caso tenha chegadoao fim finalizar com as últimas coordenadas
                self.a.append(field.size.x-lm.size.x/2)
                self.b.append(self.b[-1])
                self.a.append(self.a[-1])
                self.b.append(self.b[-1]+(field.size.y-lm.size.y)*z)
                self.count+=1
                
            self.count+=1   #contador de movimentos
    
    def plotWay(self):      #função para plotar o gráfico
        import matplotlib.pyplot as plt
        plt.rcParams['figure.figsize'] = (7,7)
        plt.plot(self.lm.size.X,self.lm.size.Y,"black")
        plt.plot(self.field.size.X,self.field.size.Y,"green")
        plt.plot(self.a,self.b,"gray")
        plt.axis('square')
        plt.grid()
        plt.show()
    
    def __str__(self):
        string = ("Way: \n"
                  + "Repetitions: " + str(self.count) + "\n"
                  + "Distance: " + str(self.dist) + "m\n"
                  + "Time: ")
        if self.time<60:
            string+= str(self.time) +" sec\n"
        elif way.time >= 60 and self.time/60<60:
            string+= str(self.time/60) + "min\n"
        else:
            string+= str(self.time/3600) + "h\n"
        
        return string
        

lm = Mower(0.128)             #cria objeto da classe Mower

#cria valores aleatórios para o tamanho do campo
import random
y = random.randint(3,5)
x = random.randint(2,y)
field = Field(x,y)          #cria objeto da classe Field com dimensões randômicas

way = Way(lm,field)         #cria o caminho do cortador no campo

#mostra a informação na tela
way.plotWay()
print(field)
print(way)