import socket
import datetime
host = socket.gethostname()
port = 12345
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("192.168.43.41",port))
s.listen(1)
sock,addr = s.accept()
print('Connection built')
info = sock.recv(1024).decode()
while info != 'exit':
  print('jreal:'+info)
  t=datetime.datetime.ctime(datetime.datetime.now())
  send_mes =input("server:")
  send_mess=send_mes+"  "+t
  sock.send(send_mess.encode())
  if send_mes =='exit':
    break
  info = sock.recv(1024).decode()
sock.close()
s.close()
