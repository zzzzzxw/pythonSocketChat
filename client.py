import socket 
import datetime 
s= socket.socket() 
host = socket.gethostname() 
port = 12345 
s.connect(("192.168.43.41",port)) 
print('Linked') 
info = '' 
while info != 'exit':   
  print('Server:'+info)   
  now='  '+datetime.datetime.ctime(datetime.datetime.now())   
  send_mes=input('Lijie:')   
  send_mes2=send_mes+str(now)   
  s.send(send_mes2.encode())   
  if send_mes =='exit':     
    break   
info = s.recv(1024).decode() 
s.close() 
