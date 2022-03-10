import Core

MainSetka=Core.OneArr(4)

MainSetka.AddPlayer([Core.Player("Tom",True,"X",MainSetka.Step),Core.Player("Jane",False,"Y",MainSetka.Step)])

MainSetka.initArr()
MainSetka.ToConsoleArray()

while True:
     MainSetka.GetActivePlayer().StepPlayer()
     MainSetka.ToConsoleArray()    
     if MainSetka.win():
        print('Win!')
        break
