import turtle
import math
import time
import random

class Rtest:
    t = turtle.Pen()
    t.speed(0)
    turtle.bgcolor("black") 
    t.pencolor("red")
    #Ergebnis
    start = 0
    sprung = 0
    treffer = 0
    fehler = 0
    durchschnitt = 0
    def paintKreisBogen(self, radius):   
        self.t.up() # nicht malen
        self.t.setpos(0,0)
        self.t.pencolor("green")
        self.t.dot(5) # mittelpunkt
        self.t.setpos(0,-radius)
        self.t.down() #wieder malen
    
        #berechnen vom umfang und alpha für eine Bogenlänge von 3
        #bogenlaenge=3
        #umfang= 2*radius*math.pi
        #grad = 360/umfang*bogenlaenge

        
        self.t.circle(radius,360) # kompletter kreis 
        
        self.t.up() # nicht malen
    
    def kreise(self,radius):
        self.t.up()
        self.t.setpos(0,radius)
        self.t.down()
        self.t.circle(10)
        xpos = 0
        ypos = radius-10
        for i in range(0, 360, 10):
            self.punkt(i,radius,False)

    def punkt(self,grad,radius,gefuellt):
        umfang = 2*radius*math.pi
        teilumfang = umfang / 360 * grad
      #  print(f"Teil:{teilumfang}")
        seite1 = radius*math.sin(teilumfang/radius)
        seite2 = radius*math.cos(teilumfang/radius)
        seite3 = radius
       # print(f"a:{seite1},b:{seite2},c:{seite3}")
        xpos = seite1
        ypos = seite2
        self.t.up()
        
        if gefuellt:
            self.t.setpos(xpos,ypos+10)
            self.t.down()
            self.t.dot(20)
        else:
            self.t.pencolor("black")
            self.t.setpos(xpos,ypos+10)
            self.t.down()
            self.t.dot(20)
            self.t.up()
            self.t.setpos(xpos,ypos)
            self.t.down()
            self.t.pencolor("red")
            self.t.circle(10)

    def runtest(self,radius):
        turtle.onkey(self.getroffen, 'w')
        turtle.listen()
        for i in range(0, 360, 10):
            number = random.randint(0,11)
            if number != 10:
                self.punkt(i,radius,True)
                time.sleep(0.5)
                self.punkt(i,radius,False)
            else:
                #Sprung
                self.sprung = self.sprung + 1
                self.start = time.time_ns()

    def getroffen(self):
        #Tasteninput
        end = time.time_ns()
        zeit = (end - self.start) / 1000 / 1000
        if zeit <= 3000:
            self.treffer = self.treffer + 1
            self.durchschnitt = self.durchschnitt + zeit
            self.start = 0
        else:
            self.fehler = self.fehler + 1
            print(f"fehler:{self.fehler}")

    def ergebnis(self):
        print(f"Ergebnis:{self.sprung},{self.treffer},{self.fehler}")
        print(f"Durchschnitt:{self.durchschnitt / self.treffer}")
def main():
    rt = Rtest()
    #rt.paintKreisBogen(400)
    rt.kreise(400)
    rt.runtest(400)
    rt.ergebnis()
    input("Press key to exit")


if __name__ == "__main__":
    main()


