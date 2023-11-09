import socket

dst_ip = '10.0.1.2'

srv_ip = '10.0.1.3'

dport = 12346

sport = 12345

s = socket.socket()
s.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))
s.listen(5)
print ("socket is listening")

cache = {}

while True:
  c, addr = s.accept()
  print ('Got connection from', addr )
  recvmsg = c.recv(1024).decode()

  r = str(recvmsg).split()

  if(r[0]=="PUT"):
    a = socket.socket()
    a.connect((srv_ip,sport))
    a.send(recvmsg.encode())
    opt = a.recv(1024).decode()
    c.send(opt.encode())
    r4 = str(opt).split(":")
    if(len(r4)==1):
      continue
    r1 = str(r[1]).split("/")
    if r1[2] in cache:
      cache[r1[2]] = r1[3]
    a.close()

  elif(r[0]=="GET"):
    r2 = str(r[1]).split("=")
    print(r2[1])
    print(cache)
    if (r2[1] in cache):
  	  c.send(("The value at this key is " +str(cache[r2[1]])).encode())

    else:
      #print("I am not in cache ;)")
      a = socket.socket()
      a.connect((srv_ip,sport))
      a.send(recvmsg.encode())
      opt = a.recv(1024).decode()
      c.send(opt.encode())
      r3 = str(opt).split(":")
      if(len(r3)==1):
        continue
      print(r3[1])
      cache[r2[1]] = r3[1]#output
      a.close()

  c.close
      