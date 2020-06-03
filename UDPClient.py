from socket import *

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()

#https://stackoverflow.com/questions/2582036/an-existing-connection-was-forcibly-closed-by-the-remote-host?rq=1
#https://stackoverflow.com/questions/46223078/c-sharp-httpclient-an-existing-connection-was-forcibly-closed-by-the-remote-host?noredirect=1&lq=1