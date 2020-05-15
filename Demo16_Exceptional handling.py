name = input("Enter your name ")
try:
    MyFile = open("Myprofile1.txt", 'w+')
    MyFile.write(name)
    MyFile.close()
    print(name)

except  FileNotFoundError:
    print("Your file is not created")

except:
    print("You can't display value without defining it ")

finally:
    print("thank you for using my Application")

