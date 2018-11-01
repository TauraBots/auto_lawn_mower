class Dimensions:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.X = [0,0,x,x,0]
        self.Y = [0,y,y,0,0]
    def __str__(self):
        return ("Area: " + str(self.x*self.y) + "m²\n"
                  + "Size: " + str(self.x) + "x" + str(self.y) + "\n")
        
class Mower:   
    def __init__(self,size):
        self.size = Dimensions(size,size)
        self.speed = 0.5
        self.turn_time = 3
        self.tax = 2/3

class Field():
    def __init__(self,x,y):
        self.size = Dimensions(x,y)
    def __str__(self):
        return "Field:\n" + str(self.size)
                  
class Way:
    def __init__(self,lm,field):
        self.lm = lm
        self.field = field
        self.count = 0
        self.a = [lm.size.x/2]
        self.b = [lm.size.y/2]
        self.setWay()
        
        self.dist = (field.size.y-lm.size.y)*(self.count+1)
        self.time = self.dist/lm.speed + ((self.count-1)*2*lm.turn_time)
        
    def setWay(self):    
        z = 1
        while (self.a[-1]+lm.size.x*lm.tax)<field.size.x:
            #vertical move
            self.a.append(self.a[-1])
            self.b.append(self.b[-1]+(field.size.y-lm.size.y)*z)
            z = z *(-1)
            
            #horizontal move
            if (self.a[-1]+2*lm.size.x*lm.tax)<field.size.x:
                self.a.append(self.a[-1]+lm.size.x*lm.tax)
                self.b.append(self.b[-1])
            else:
                self.a.append(field.size.x-lm.size.x/2)
                self.b.append(self.b[-1])
                self.a.append(self.a[-1])
                self.b.append(self.b[-1]+(field.size.y-lm.size.y)*z)
                self.count+=1
                
            self.count+=1
    
    def plotWay(self):
        import matplotlib.pyplot as plt
        plt.rcParams['figure.figsize'] = (7,7)
        plt.plot(self.lm.size.X,self.lm.size.Y,"black")
        plt.plot(self.field.size.X,self.field.size.Y,"green")
        plt.plot(self.a,self.b,"gray")
        plt.axis('square')
        #plt.grid()
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
        

lm = Mower(0.5)

import random
y = random.randint(1,50)
x = random.randint(1,y)
field = Field(x,y)

way = Way(lm,field)

way.plotWay()
print(field)
print(way)