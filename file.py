# #read
# rfile=open("test.txt","r")
# line=rfile.readline()
# while len(line)>0:
#     print(line)
#     line=rfile.readline().strip()
# rfile.close()



# rfile=open("test.txt","r")
# for line in rfile:
#     print(line.strip())
# rfile.close()


# #write
# wfile=open("test.txt","w")
# for count in range(3):
#     strStudent=input("name=")
#     wfile.write(strStudent+"\n")
# wfile.close()



class Student:
    def __init__(self,name:str,gender:str,age:int)->None:
        self.name=name
        self.gender=gender
        self.age=age

    def __str__(self)->str:
        return f"{self.name},{self.gender},{self.age}"
    


def read_file(file_name:str)->list[Student]:
    f=open(file_name,"r")
    students=[None]*7
    index=0
    for line in f:
        record_data=line.strip().split(",")
        student_record=Student(record_data[0],record_data[1],int(record_data[2]))
        students[index]=student_record
        index+=1
        if index >=len(students):
            print("Array is full")
            break
    f.close()
    return students



def write_file(file_name:str):
    f=open(file_name,"w")
    for count in range(10):
        strName=input("name=")
        strGender=input("gender=")
        strAge=input("age=")
        f.write(strName+",")
        f.write(strGender+",")
        f.write(strAge+"\n")
    f.close()



if __name__=="__main__":
    write_file("StudentsInfo.txt")
    stus=read_file("StudentsInfo.txt")
    for stu in stus:
        print(stu)