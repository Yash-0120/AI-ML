# with open("03-EXCEPTION-HANDLING/info.txt","w") as text:
#     text.write("Name: Yash Varpe")
try:
    file=open("03-EXCEPTION-HANDLING/info.txt","r")
    print( file.read())
    file.close()
except FileNotFoundError:
    print("file not found!!!")    

