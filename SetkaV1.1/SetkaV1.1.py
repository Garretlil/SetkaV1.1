import Core

setka=4

MainSetka=Core.OneArr(setka)

plaeyr1=Core.Player("Tom",True,"X",MainSetka.Step)
plaeyr2=Core.Player("Jane",False,"Y",MainSetka.Step)

MainSetka.AddPlayer(plaeyr1)
MainSetka.AddPlayer(plaeyr2)

MainSetka.initArr()
MainSetka.ToConsoleArray()

while True:
     MainSetka.GetActivePlayer().StepPlayer()
     MainSetka.ToConsoleArray()    
     if MainSetka.win():
        print('Win!')
        break
