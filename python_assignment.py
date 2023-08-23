
class Flight :
    def __init__(self,flightid,initial,dest,price):
        self.flightid = flightid
        self.initial=initial
        self.dest=dest
        self.price=price
  
flights = [
    Flight('AI161E90', 'BLR', 'BOM',  5600),
    Flight('BR161F91', 'BOM', 'BBI',  6750),
    Flight('AI161F99', 'BBI', 'BLR',  8210),
    Flight('VS171E20', 'JLR', 'BBI',  5500),
    Flight('AS171G30', 'HYD', 'JLR',  4400),
    Flight('AI131F49', 'HYD', 'BOM',  3499)
]        

def search(flights , mode ,searchvar):
    ret=[]
    for f in flights:
        if mode ==1 and f.flightid==searchvar:
            ret.append(f)
        elif  mode ==2 and f.initial==searchvar:
             ret.append(f)
        elif mode==3 and f.dest==searchvar:
             ret.append(f) 
                   
    return ret  
print('''modes:
      1. flightid
      2.flight origin
      3.flight destination''')       
mode=int(input("Enter the mode of your search: "))
searchvar=input("Enter the searching value:  ")
resultlist=search(flights,mode,searchvar)
for f in resultlist:
    print(F"Flight information == \n flight id : {f.flightid}  flight origin: {f.initial}   flight destination: {f.dest}  , flight price: {f.price}")


