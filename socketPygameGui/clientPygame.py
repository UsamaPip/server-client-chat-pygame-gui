###      CLIENTGAME, BY usamaPip
### THIS program will be a socket client program
### that use socket module to recv/send data to server program
### and use pygame module to display responses send by server program.
#
###     IN MY THINKING 
### There are two weak point 
### (1) Uses console to input data.
### (2) Pygame gui takes too time initialize.

###      SCRIPT STARTS  ###
import socket, pygame, sys

### SOCKET variable
clntHost = socket.gethostname()
clntPort = 30001
buffSize = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((clntHost, clntPort))
sockName = str(sock.getsockname())
### SOCKET END

### PYGAME variable
pygame.init()
widthHight = [240, 480]
surface = pygame.display.set_mode((widthHight[1], widthHight[0]))
pygame.display.set_caption('pygame client')
fontObj = pygame.font.Font('font/Inkfree.ttf', 30)
fps = pygame.time.Clock()
fps.tick(60)
### PYGAME END

while True:
   
   for event in pygame.event.get():
      if event.type == 'QUIT':
         pygame.quit()
         sys.exit(1)
   
   
   respMsg = input('>>>')
   sock.send(bytes(respMsg, 'utf-8'))
   msg = sock.recv(buffSize)
   surface.fill((180, 180, 180))
   sockDis = fontObj.render(sockName, 0, (255, 255, 255))
   surface.blit(sockDis, (20, 20))
   textObj = fontObj.render(msg, 0, (255, 255, 255))
   surface.blit(textObj, (widthHight[1]/2, widthHight[0]/2))
   pygame.display.update()
