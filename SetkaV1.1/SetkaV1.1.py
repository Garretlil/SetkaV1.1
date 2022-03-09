import Core
plaeyr1=Core.Player("Tom",True,"X")
plaeyr2=Core.Player("Jane",False,"Y")
plaeyr3=Core.Player("Kate",False,"Z")

setka=4

 

MainSetka=Core.OneArr([plaeyr1,plaeyr2,plaeyr3])

MainSetka.initArr(setka)
MainSetka.ToConsoleArray(setka)

while True:
     MainSetka.Step(setka)
     MainSetka.ToConsoleArray(setka)    
     if MainSetka.win(setka):
        print('Win!')
        break
