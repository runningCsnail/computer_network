#UDPClient.py

1. Import the socket package, then declare the server-name and port, caution that do not use `str` as port instead of `integer`.
2. Now create client socket, `socket (int af, int type, int protocol)` The af parameter specifies the protocol's address family, which determines what type of socket will be created. `AF_INET` uses IPV4
The type parameter is the protocol's communication type, and can be either `SOCK_STREAM` or `SOCK_DGRAM`. To create a TCP connection-oriented socket, use `SOCK_STREAM`. When creating a connectionless UDP socket, use SOCK_DGRAM


3. Convert strings to bytes in order to sent bytes to sockets. Use method `encode()`, or `encode('UTF-8')` in some editors. `sendto(self, data, address)` attaches a destination address `(serverName, serverPort)` to the message and send a result packet to the process's socket.
4. The `recvfrom()` method Python's socket class, reads a number of bytes sent from an UDP socket. Like `sendto()` , the `recvfrom()` method as well is to be called on a UDP socket. Unlike `sendto()`, the method `recvfrom()` does not take an IP address and port as a parameter.
5.print and close.
6. Problems reference

https://stackoverflow.com/questions/2582036/an-existing-connection-was-forcibly-closed-by-the-remote-host?rq=1

https://stackoverflow.com/questions/46223078/c-sharp-httpclient-an-existing-connection-was-forcibly-closed-by-the-remote-host?noredirect=1&lq=1

Run UDPServer.py before UDPClient.py please.



#UDPServer.py

After declaring server port and creating socket, `bind()` method bind the server  to socket.

`while` loop receives and packets from client infinitely.








