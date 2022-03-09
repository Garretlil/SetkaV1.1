import Core

setka=4

MainSetka=Core.OneArr(setka)

plaeyr1=Core.Player("Tom",True,"X",MainSetka.Step,MainSetka.setka)
plaeyr2=Core.Player("Jane",False,"Y",MainSetka.Step,MainSetka.setka)

MainSetka.AddPlayer(plaeyr1)
MainSetka.AddPlayer(plaeyr2)

MainSetka.initArr(setka)
MainSetka.ToConsoleArray(setka)

while True:
     MainSetka.GetActivePlayer().StepPlayer()
     MainSetka.ToConsoleArray(setka)    
     if MainSetka.win(setka):
        print('Win!')
        break
