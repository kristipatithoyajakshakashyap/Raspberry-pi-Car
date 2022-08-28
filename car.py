import cv2
import pygame
import numpy as np
from MotorModule import Motor
from gpiozero import Buzzer
from time import sleep 
from distance import distance 
motor = Motor(2,3,4,17,27,22)
buzzer = Buzzer(23)

pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
surface = pygame.display.set_mode([1280,720])
cap = cv2.VideoCapture(0)

fps = cap.get(cv2.CAP_PROP_FPS)
print("fps:", fps)
cap.set(cv2.CAP_PROP_FPS, 60)

while True:
    dist = distance(20,21)
    
    surface.fill([0,0,0])

    success, frame = cap.read()
    if not success:
        break
    frame = np.fliplr(frame)
    frame = np.rot90(frame)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    surf = pygame.surfarray.make_surface(frame)

       
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                motor.move(0.9,0,0.1)
            if event.key == pygame.K_s:
                motor.move(-0.9,0,0.1)
            if event.key == pygame.K_a:
                motor.move(0.85,0.9,0.1)
            if event.key == pygame.K_d:
                motor.move(-0.85,-0.9,0.1)
            if event.key == pygame.K_h:
                buzzer.on()
                sleep(0.1)
                buzzer.off()
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_a or event.key == pygame.K_d:
                 motor.stop(0.1)
            
    surface.blit(surf, (0,0))
    pygame.display.flip()
    print ("Measured Distance = %.1f cm" % dist)
    sleep(0.0001)
