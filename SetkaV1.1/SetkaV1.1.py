import Core
plaeyr1=Core.Player("Tom",False,"X")
plaeyr2=Core.Player("Jane",True,"Y")


setka=3
 

MainSetka=Core.OneArr([plaeyr1,plaeyr2])

MainSetka.initArr(setka)
MainSetka.ToConsoleArray(setka)

while True:
     MainSetka.Step(setka)
     MainSetka.ToConsoleArray(setka)    
     if MainSetka.win(setka):
        print('Win!')
        break
