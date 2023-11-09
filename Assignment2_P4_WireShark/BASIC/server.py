import socket

# WRITE CODE HERE:
# 1. Create KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).

# dst_ip = str(input("Enter Server IP: "))
dst_ip = "10.0.1.2"

s = socket.socket()
print("Socket successfully created")

dport = 12346

s.bind((dst_ip, dport))
print("socket binded to %s" % (dport))

s.listen(5)
print("socket is listening")
data = {}

# Write your code here
# 1. Uncomment c.send
# 2. Parse the received HTTP request
# 3. Do the necessary operation depending upon whether it is GET, PUT, or DELETE
# 4. Send response
# 5. Handle errors related to HTTP version and input name

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    recvmsg = c.recv(1024).decode()
    r = recvmsg.split()
    if len(r) == 0:
        continue
    print('Server received ' + r[0])

    if r[0] == "PUT":
        msg = str(r[1]).split("/")
        if len(msg) != 4 :
            c.send("HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid PUT request format\r\n\r\n".encode())
        elif(msg[1] != "assignment2" and r[2] != "HTTP/1.1"):
            c.send("HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid path name\nInvalid HTTP version\r\n\r\n".encode()) 
        elif msg[1] != "assignment2":
            c.send("HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid path name\r\n\r\n".encode())
        elif r[2] != "HTTP/1.1":
            c.send("HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid HTTP version\r\n\r\n".encode())
            continue

        else:
            if msg[2] in data:
                data[msg[2]] = msg[3]
                c.send(("HTTP/1.1 200 OK\nUpdated the value of " + msg[2] + " to " + data[msg[2]] + '\r\n\r\n').encode())
            else:
                data[msg[2]] = msg[3]
                print(data[msg[2]])
                c.send(("HTTP/1.1 200 OK\nInserted the value " + data[msg[2]] + " into " + msg[2] + '\r\n\r\n').encode())

    elif r[0] == "GET":
        msg = str(r[1]).split("=")
        print(msg[0])
        if len(msg) != 2:
            c.send("HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid GET request format\r\n\r\n".encode())
        elif(msg[0] != "/assignment2?request" and r[2] != "HTTP/1.1"):
            c.send("HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid path name\nInvalid HTTP version\r\n\r\n".encode()) 
        elif msg[0] != "/assignment2?request":
            print(msg[1])
            c.send("HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid path name\r\n\r\n".encode())
        elif r[2] != "HTTP/1.1":
            c.send("HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid HTTP version\r\n\r\n".encode())
            continue

        else:
            print(msg[1])
            if msg[1] in data:
                c.send(("HTTP/1.1 200 OK\nValue asked is " + data[msg[1]] + '\r\n\r\n').encode())
            else:
                c.send('HTTP/1.1 404 Not Found\nERROR!!!!\nGiven Key is not present in the table \r\n\r\n'.encode())

    elif r[0] == "DELETE":
        msg = str(r[1]).split("/")
        if len(msg) != 3:
            c.send("HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid DELETE request format\r\n\r\n".encode())
        elif(msg[1] != "assignment2" and r[2] != "HTTP/1.1"):
            c.send("HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid path name\nInvalid HTTP version\r\n\r\n".encode()) 
        elif msg[1] != "assignment2":
            c.send("HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid path name\r\n\r\n".encode())
        elif r[2] != "HTTP/1.1":
            c.send("HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid HTTP version\r\n\r\n".encode())
            continue

        else:
            if msg[2] in data:
                data.pop(msg[2])
                c.send("HTTP/1.1 200 OK\nValue in " + msg[2] + " has been deleted" + '\r\n\r\n')
            else:
                c.send('HTTP/1.1 404 Not Found\nERROR!!!!\nGiven Key is not present in the table \r\n\r\n'.encode())
    else:
        c.send('HTTP/1.1 400 Bad Request\nERROR!!!!\nInvalid request method\r\n\r\n'.encode())

    c.close()
    # break
