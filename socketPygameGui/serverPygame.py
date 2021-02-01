###         SOCKETGAME, BY usamaPip
### THIS program will be a socket server Program 
### that use socket module to send/recv data to client program
### and use pygame module to display responses send by the 
### client program.
#
###     IN MY THINKING 
### There are two weak point 
### (1) Uses console to input data.
### (2) Pygame gui takes too time initialize.

###     SCRIPT STARTS   ###
import socket, pygame, sys

### SOCKET variable
srvHost = ''
srvPort = 30001
buffSize = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((srvHost, srvPort))
sock.listen(1)
Conn, Addr = sock.accept()
connName = str(Conn.getpeername())
### SOCKET END

### PYGAME variable
pygame.init()
widthHight = [240, 480]
surface = pygame.display.set_mode((widthHight[1], widthHight[0]))
pygame.display.set_caption('pygame server')
fontObj = pygame.font.Font('font/Inkfree.ttf', 30)
fps = pygame.time.Clock()
fps.tick(60)
### PYGAME END

while True:
    for event in pygame.event.get():
        if event.type == 'QUIT':
            pygame.quit()
            sys.exit(1)

    
    clntMsg = Conn.recv(buffSize)
    surface.fill((180, 180, 180))
    connDis = fontObj.render(connName, 0, (255, 255, 255))
    surface.blit(connDis, (20, 20))
    textObj = fontObj.render(clntMsg, 0, (255, 255, 255))
    surface.blit(textObj, (widthHight[1]/2, widthHight[0]/2))
    pygame.display.update()
    msg = input('>>>')
    Conn.send(bytes(msg, 'utf-8'))
