import socket
import time

serverIP = "10.0.1.2"

dst_ip = "10.0.1.2"


print(dst_ip)

port = 12346



#Write your code here:
#1. Add code to send HTTP GET / PUT / DELETE request. The request should also include KEY.
#2. Add the code to parse the response you get from the server.
while True:
    s = socket.socket()
    s.connect((dst_ip, port))
    print("Which request do you want to send\n")
    print("1)PUT\n2)GET\n3)EXIT")
    inp = str(input("Enter your number: "))
    print(inp)

    if inp == '1':
        print("Now you have entered PUT, Enter the values of key, value, assignment, and HTTP version: ")
        key = str(input("key is: "))
        val = str(input("val is: "))
        assignment = str(input("assignment (e.g., assignment2): "))
        http_version = str(input("HTTP version (e.g., HTTP/1.1): "))
        req = "PUT /"+assignment+"/"+key+"/"+val+" "+http_version
        begin = time.time()
        s.send((req + '\r\n\r\n').encode())

    elif inp == '2':
        print("Now you have entered GET, Enter the values of key, assignment, and HTTP version: ")
        key = str(input("key is: "))
        assignment = str(input("assignment (e.g., assignment2): "))
        http_version = str(input("HTTP version (e.g., HTTP/1.1): "))
        req = "GET /"+assignment+"?request="+key+" "+http_version
        begin = time.time()
        s.send((req + '\r\n\r\n').encode())

    elif(inp=='3'):
      print("Exiting..............")
      break
      s.close()

    else:
      print("ERROR!!!\nInvalid requet method")
      continue
      s.send('Hello server'.encode())


    print ('Client received: '+s.recv(1024).decode())
    end = time.time()

    print("Total time for the request is : ")
    print((end-begin)*1000)

    s.close()