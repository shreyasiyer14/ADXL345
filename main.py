import pygame
from adxl345 import ADXL345
from math import *
pygame.init()
gameLoop = True

mainWindow = pygame.display.set_mode((1024,768))
pygame.display.set_caption("ADXL345: AirPaint")

fps = pygame.time.Clock()
font=pygame.font.SysFont("comicsansms", 20)
adxl345 = ADXL345()
'''
print "   x = %.3fG" % ( axes['x'] )
print "   y = %.3fG" % ( axes['y'] )
print "   z = %.3fG" % ( axes['z'] )
'''
multi = 500

lineList = []

def displayVals():
    props = font.render("ADXL345 on address 0x"+ str(adxl345.address),1,(255,255,255))
    mainWindow.blit(props,(20,20))
while gameLoop:
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    pygame.quit()
            quit()
    axes = adxl345.getAxes(True)
    displayVals();
    mainWindow.fill((0,100,255))
    lineList.append([(axes['x']*multi), ((axes['y'])*multi)])
    for i in range(len(lineList)-1):
        pygame.draw.line(mainWindow, (255,255,255), lineList[i], lineList[i+1],5);
    fps.tick(60)
    pygame.display.flip()
