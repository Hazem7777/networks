from socket import *

msg = "\r\n I love computer networks!"

endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = 'localhost'
mailPort = 80
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, mailPort))
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':

 print("220 reply not recieved")


# Send HELO command and print server response.
helloCommand = 'HELLO Alice\r\n'
clientSocket.send(helloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
 print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
clientSocket.send('Mail FROM: <alice@crepes.edu>\r\n')
recv1 = clientSocket.recv(1024)
print (recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
clientSocket.send('RCPT TO: <sullivanmax@my.easternct.edu> \r\n')
recv1 = clientSocket.recv(1024)
print (recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
# Fill in end
# Send DATA command and print server response.
# Fill in start
clientSocket.send('DATA\r\n')
recv1 = clientSocket.recv(1024)
print (recv1)
if recv1[:3] != '354':
    print('250 reply not received from server.')
 
# Fill in end
# Send message data.
# Fill in start
clientSocket.send('\r\n')
clientSocket.send("amr")



# Fill in end
# Message ends with a single period.
# Fill in start
clientSocket.send('.\r\n')
recv1=clientSocket.recv(1024)
print (recv1)
if recv1[:3]!='250':
 print('250 reply not received from server.')


# Fill in end
# Send QUIT command and get server response.
# Fill in start
clientSocket.send('QUIT\r\n')
clientSocket.close()
# Fill in end