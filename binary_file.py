import pickle

# #Sequentially access
# #write
# cars=[...]
# f=open("Car.txt","wb")
# for i in range(100):
#     pickle.dump(cars[i],f)            #文件在后
# f.close()

# #read
# f=open("Car.txt","rb")
# out=[]
# while True:
#     try:
#         car=pickle.load(f)
#         out.append(car)
#     except EOFError:
#         break
# f.close()


# #Randomly access
# #write
# f=open("CarRandom.txt","wb")
# for car in cars:
#     address=myhash(car.VehicleID)
#     f.seek(address)
#     pickle.dump(car,f)
# f.close()

# #read
# VehicleID=input()
# f=open("CarRandom.txt","rb")
# address=myhash(VehicleID)
# f.seek(address)
# car=pickle.load(f)
# f.close()
# print(car)



""" define a car record in python"""

class CarRecord:
    def __init__(self,v,r,d,e,p):
        self.VehicleID=v
        self.Registration=r
        self.DateOfRegistration=d
        self.EngineSize=e
        self.PurchasePrice=p

    def __str__(self):
        return f"{self.VehicleID} , {self.Registration}, {self.DateOfRegistration},{self.EngineSize},{self.PurchasePrice}"

carInfo=[["1","11111","1/1/1",1000,1000.00],["56","2222","2/2/2",2000,2000.00],["3","3456d","01/09/1998",344,45.68]]
#input information for these 100 cars

cars = [CarRecord("1","11111","1/1/1",1000,1000.00),CarRecord("56","2222","2/2/2",2000,2000.00),CarRecord("3","3456d","01/09/1998",2345,45.68)]

def myhash(id:str)->int:
    # code to be implemented
    #sum each char's ascii code and mod 97-->0...96   index*256
    sum=0
    for ch in id:
        sum=sum+ord(ch)
    re = sum %97 *256
    return re




""" 2. randomly access a binary file to write"""
#store these records to binary file randomly named as CarFileRandom.DAT
import pickle
# code to be implemented
f=open("CarFileRandom.DAT","wb")
for car in cars:
    address=myhash(car.VehicleID)
    f.seek(address)
    pickle.dump(car,f)
f.close()

""" 3. randomly access a binary file to find a record according the given VehicleID 
        print the car info """
VehicleID = input("Please input the VehicleID you want to search in file : ")
# code to be implemented
try:
    f=open("CarFileRandom.DAT","rb")
    address=myhash(VehicleID)
    f.seek(address)
    car=pickle.load(f)
    f.close()
    print(car)
except FileNotFoundError:
    print("Could not find the file 'CarFileRandom.DAT'")
