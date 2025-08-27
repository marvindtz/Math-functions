import time
import traceback
import inspect

Tuerme = ['T1','T2','T3']
#Nur für Start/Stop wahl
init = True
ScheibeEins = False
Scheiben = 5
#TurmVoll = [3,2,1]
Turmscheiben = [[5,4,3,2,1],[0,0,0,0,0],[0,0,0,0,0]]
#Turmscheiben = [[4,3,2,1],[0,0,0,0],[0,0,0,0]]
#Turmscheiben = [[3,2,1],[0,0,0],[0,0,0]]
Start = 0
Ziel = 2


# Start = input(f'Startturm({Tuerme}):')
# Verteilung = Tuerme.index(Start)
# Turmscheiben[Verteilung] = TurmVoll
# Tuerme.remove(Start)

# Ziel = input(f'Zielturm({Tuerme}):')

Schritte = 0
# print(Tuerme)


def printTurm():
    scheibe = False
    for level in reversed(range(0,Scheiben+1)):
        if level == 0:
            for t in range(0,3):
                print(f"=====      ", end="")
            print()
            continue
        
        for t in range(0,3):
            s = Turmscheiben[t][level-1]
            if  s != 0:
                print(f"{(3-s)*" "}{s*"-"}        ", end="")
            else:
                print(f"  |        ", end="")
        print()

printTurm()  

def TurmMitKleinsteScheibe():
    for t in Turmscheiben:
        if 1 in t:
            print(f"######### Turm m. kl. Scheibe: {Turmscheiben.index(t)}")
            return Turmscheiben.index(t)
        

# def TurmMitGroesterScheibe():
#     _, ts0 = getObersteScheibe(0)
#     _, ts1 = getObersteScheibe(1)
#     _, ts2 = getObersteScheibe(2)
    
#     if not ts0:
#         ts0 = -1
#     if not ts1:
#         ts1=-1
#     if not ts2: 
#         ts2=-1
#     if ts0 > ts1 and ts0 > ts2:
#         return 0
#     if ts1 > ts2 and ts1 > ts0:
#         return 1
#     return 2    


def getObersteScheibe(turmIdx):
    TurmToPop = Turmscheiben[turmIdx]
    for lvl in reversed(range(0,Scheiben)):
        if TurmToPop[lvl] == 0:
            continue
        Scheibe = TurmToPop[lvl]
        #TurmToPop[lvl] = 0
        print(f"getScheibe: T:{turmIdx} S:{Scheibe}")
        return (lvl, Scheibe)
    print('leerer Turm')
    return (-1, None)
    
def cntScheiben(turmIdx):
    anzahl = 0
    TurmToPop = Turmscheiben[turmIdx]
    for lvl in reversed(range(0,Scheiben)):
        if TurmToPop[lvl] == 0:
            continue
        anzahl = anzahl + 1
    print(f"Anzahl Scheiben: {anzahl}")
    return anzahl

def WaehleTurm(turmIdx,AktiveScheibe):
    zielturm = turmIdx
    while True:
        if AktiveScheibe == Scheiben and turmIdx == Ziel:
                # größte scheibe immer auf zielturm lassen
                return True
        
        zielturm = (zielturm + 1 ) % 3
        if zielturm == turmIdx:
            print(f"####################### NIX GEFUNDEN --- Next LEVEL ################### {AktiveScheibe}")
            LeereTurm()
            print("Leere Turm")
            return False

        elif cntScheiben(zielturm) == 0:
            moveScheibe(turmIdx,zielturm)
            return False
        else:
            _, zielscheibe = getObersteScheibe(zielturm)
            print(f"A:{AktiveScheibe} Z:{zielscheibe}")
            if zielscheibe and AktiveScheibe < zielscheibe:
                moveScheibe(turmIdx,zielturm)
                return False
            
            


def moveScheibe(turmIdx,zielTurmIdx):
    global Schritte
    Schritte = Schritte + 1
    index, QuellScheibe = getObersteScheibe(turmIdx)
    ZielIndex, ZielScheibe = getObersteScheibe(zielTurmIdx)
    
    print(f'Movefrom {turmIdx}, {index} to {zielTurmIdx}, {ZielIndex + 1}')
    if turmIdx == zielTurmIdx:
        print(f"ERROR from_to is the same {turmIdx}")
        raise Exception(f"ERROR from_to is the same {turmIdx}")
    
    if ZielScheibe and QuellScheibe > ZielScheibe:
        print(f"ERROR from is larger than too {QuellScheibe} {ZielScheibe}")
        raise Exception(f"ERROR from is larger than too {QuellScheibe} {ZielScheibe}")

    # löse alte scheibe
    Turmscheiben[turmIdx][index] = 0
    # setze neue 
    Turmscheiben[zielTurmIdx][ZielIndex + 1] = QuellScheibe
    


def LeereTurm():
    global init
    startturm = TurmMitKleinsteScheibe()
    while cntScheiben(startturm) != 0:
        level = len(inspect.stack(0))-1
        print(f"{level}-------------------- STARTTURM:{startturm}")
        index, AktiveScheibe = getObersteScheibe(startturm)
        cnt = cntScheiben(startturm)
        if init and Scheiben % 2 != 0:
            moveScheibe(startturm,Ziel)
            init = False
        else:
            TurmLeer = WaehleTurm(startturm, AktiveScheibe)
            if TurmLeer or cntScheiben(startturm) > cnt:
                break

        print(f"{level}----------------------------")
        printTurm()
        time.sleep(2)

try:
    while cntScheiben(Ziel) != Scheiben:   
        LeereTurm()
    print(" !!!!!!!!!!!!!!!!! GEWONNNNNEEEEENNN !!!!!!!!!!!!!!!")
    print(f"Schritte: {Schritte}")
except Exception as e:
    print(e)
    traceback.print_exc(e)