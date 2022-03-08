
class Player:
   def __init__(self, name_,active_,symbol_):
        self.Name = name_
        self.IsActive=active_
        self.Symbol=symbol_


class CommonArr:
    arraysetka=[]
    arraysteps=[]
    players=[]

    def askwin(self,win_combinations):   
        for i in range(len(win_combinations)-1):
            if win_combinations[i]!=win_combinations[i+1]:
                return False
        return True
 

class OneArr(CommonArr):

    def __init__(self,players_): 
           self.players=players_

    def is_integer(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False 
    
    def GetActivePlayer(self):
        actPlayer=self.players[0]
        for i in range (len(self.players)):
            pl_=self.players[i]
            if pl_.IsActive==True:
                pl_.IsActive=False
                if i==len(self.players)-1 :             
                  self.players[0].IsActive=True
                else:
                  self.players[i+1].IsActive=True
                return pl_
        
  

    def Step(self,n):
        ActivePlayer=self.GetActivePlayer()
        
        x=input('следующий ход игрока '+ActivePlayer.Name + ' ['+ ActivePlayer.Symbol +'], выберите номер: ')

        if x.upper()=='R' :
            if  len(self.arraysteps)!=0:
                stepp=self.arraysteps[len(self.arraysteps)-1]# последний ход
                self.arraysetka[stepp-1]=stepp
                self.arraysteps.pop(len(self.arraysteps)-1)
        if self.is_integer(x) :
            x=int(x)
            try:
                if not(x<=n**2 and x>0 ):
                    raise BaseException("введи допустимое значение")
                if not(x in self.arraysetka):
                    raise BaseException("поле занято")
                self.arraysetka[x-1]=ActivePlayer.Symbol
                self.arraysteps.append(x)
            except BaseException as ve:
              print(ve)
              self.Step(n)    
        

    def ResearchOfSize(self,current_element,maxlensymbol_):    
        dlina=len(str(current_element))
        return maxlensymbol_-dlina


    def vuvod_stroka(self,setka_,k): 
        stroka='|'
        maxlensymbol=len(str(setka_**2))
        for i in range(k,k+setka_):
            stroka+=str(self.arraysetka[i])
            stroka+=' '*self.ResearchOfSize(self.arraysetka[i],maxlensymbol)
            stroka+='|'
        return stroka

    def ToConsoleArray(self,setka_):    
        t=0
        for i in range(setka_):
            stroka=self.vuvod_stroka(setka_,t)
            print(stroka)
            t+=setka_
    def win(self,n):
        k=0
        mass=[]
        # проверка по строкам
        for i in range(n):
            for s in range(k,k+n):
                mass.append(self.arraysetka[s])
            if self.askwin(mass):
                return True
            else:
                k+=n

        mass.clear()
            # проверка по столбцам
        for i in range(n):  
            mass.clear()
            for s in range(i,i+n*(n-1)+1,n):
                mass.append(self.arraysetka[s])
            if self.askwin(mass):
                return True

        mass.clear()
         # проверка по диагоналям
        for i in range(0,n**2,n+1):
            mass.append(self.arraysetka[i])
        if self.askwin(mass):
                return True

        mass.clear()
        for i in range(n-1,n**2-n+1,n-1):
            mass.append(self.arraysetka[i])
        if self.askwin(mass):
                return True
        
        return False

 
    

    def initArr(self,setka):
       for i in range(1,setka**2+1):
        self.arraysetka.append(i)
