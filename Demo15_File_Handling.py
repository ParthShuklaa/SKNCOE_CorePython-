#Step1: Creating connection



def Read ():
    Myfile = open("Myfile.txt",'r')

    #Reading Data using Same connection
    MyData = Myfile.readline()
    FinalData = Myfile.readlines()
    print(MyData)
    for line in FinalData:
        print(line)
    Myfile.close()

def Write():
    MyCon = open("Myfile.txt",'a')
    Msg = input("Enter your message")
    MyCon.writelines(Msg)
    MyCon.close()

def Create ():
    MyFile = open("Myprofile.txt",'w+')
    MyFile.write("Created file at run time ...!!!!")
    MyFile.close()

    MyFile1 = open("Myprofile.txt",'r')
    msg = MyFile1.readlines()
    print(msg)
    MyFile1.close()
"""Read()
Write()
Read()"""
Create()