
class Player:   
   def __init__(self, name_,active_,symbol_,func_):
        self.Name = name_
        self.IsActive=active_
        self.Symbol=symbol_
        self.fun = func_
    

   def StepPlayer(self):
        self.fun(self)

class CommonCore:
    arraysetka=[]
    arraysteps=[]
    players=[]

    def __init__(self,setka_=3): 
        self.setka=setka_   

    def askwin(self,win_combinations):   
        for i in range(len(win_combinations)-1):
            if win_combinations[i]!=win_combinations[i+1]:
                return False
        return True
 
    def is_integer(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False 
    
    def GetActivePlayer(self):
        for i in range (len(self.players)):
            if self.players[i].IsActive:
                self.players[i].IsActive=False
                if i==len(self.players)-1 :             
                  self.players[0].IsActive=True
                else:
                  self.players[i+1].IsActive=True
                return self.players[i]

    def AddPlayer(self,Pl):
        self.players=Pl

class OneCore(CommonCore):


    def Step(self,activeplayer_):
        #ActivePlayer=self.GetActivePlayer()
        
        x=input('следующий ход игрока '+activeplayer_.Name + ' ['+ activeplayer_.Symbol +'], выберите номер: ')

        if x.upper()=='R' :
            if  len(self.arraysteps)!=0:
                stepp=self.arraysteps[len(self.arraysteps)-1]# последний ход
                self.arraysetka[stepp-1]=stepp
                self.arraysteps.pop(len(self.arraysteps)-1)
        if self.is_integer(x) :
            x=int(x)
            try:
                if not(x<=self.setka**2 and x>0 ):
                    raise BaseException("введи допустимое значение")
                if not(x in self.arraysetka):
                    raise BaseException("поле занято")
                self.arraysetka[x-1]=activeplayer_.Symbol
                self.arraysteps.append(x)
            except BaseException as ve:
              print(ve)
              self.Step(activeplayer_)    
        

    def ResearchOfSize(self,current_element,maxlensymbol_):    
        dlina=len(str(current_element))
        return maxlensymbol_-dlina


    def vuvod_stroka(self,k): 
        stroka='|'
        maxlensymbol=len(str(self.setka**2))
        for i in range(k,k+self.setka):
            stroka+=str(self.arraysetka[i])
            stroka+=' '*self.ResearchOfSize(self.arraysetka[i],maxlensymbol)
            stroka+='|'
        return stroka

    def ToConsoleArray(self):    
        t=0
        for i in range(self.setka):
            stroka=self.vuvod_stroka(t)
            print(stroka)
            t+=self.setka

    def win(self):
        k=0
        mass=[]

        # проверка по строкам
        for i in range(self.setka):
            for s in range(k,k+self.setka):
                mass.append(self.arraysetka[s])
            if self.askwin(mass):
                return True
            else:
                k+=self.setka

        mass.clear()
            # проверка по столбцам
        for i in range(self.setka):  
            mass.clear()
            for s in range(i,i+self.setka*(self.setka-1)+1,self.setka):
                mass.append(self.arraysetka[s])
            if self.askwin(mass):
                return True

        mass.clear()
         # проверка по диагоналям
        for i in range(0,self.setka**2,self.setka+1):
            mass.append(self.arraysetka[i])
        if self.askwin(mass):
                return True

        mass.clear()
        for i in range(self.setka-1,self.setka**2-self.setka+1,self.setka-1):
            mass.append(self.arraysetka[i])
        if self.askwin(mass):
                return True
        
        return False

 
    

    def initArr(self):
       for i in range(1,self.setka**2+1):
        self.arraysetka.append(i)
