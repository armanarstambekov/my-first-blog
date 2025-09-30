'''
import pygame

pygame.init()
dis = pygame.display.set_mode((1000,800))
r = pygame.Rect(10, 90, 100, 100)

dis_over=False
while not dis_over:
    for event in pygame.event.get():
        pygame.draw.rect(dis, (205, 50, 5), r, 5,10)
        pygame.draw.polygon(dis, (205, 50, 5), [(100, 100), (900, 90), (60, 60)])
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
quit()
'''
#----------------------------------------------------------------------------------------
'''
import pygame
import sys
pygame.init()
width, height = 1000, 800
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption("")
WHITE = (255, 255, 255)
RED = (205, 50, 5)
BROWN = (150, 75, 0)
BLUE = (0, 191, 255)
running = True
while running:
    dis.fill(WHITE)
    house_rect = pygame.Rect(400, 400, 200, 200)
    pygame.draw.rect(dis, BROWN, house_rect)
    roof_points = [(400, 400), (600, 400), (500, 300)]
    pygame.draw.polygon(dis, RED, roof_points)
    door_rect = pygame.Rect(475, 500, 50, 100)
    pygame.draw.rect(dis, BLUE, door_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
'''
#----------------------------------------------------------------------------------------
'''
import pygame
pygame.init()
dis = pygame.display.set_mode((500,500))
r = pygame.Rect(10, 90, 100, 100)
dis_over = False
while not dis_over:
    for event in pygame.event.get():
        dis.fill((255, 255, 255))
        pygame.draw.rect(dis, (205, 50, 5), r)
        pygame.draw.polygon(dis, (150, 0, 0), [(10, 90), (110, 90), (60, 40)])
        pygame.draw.rect(dis, (0, 191, 255), (45, 120, 30, 30))
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
quit()
'''
#----------------------------------------------------------------------------------------
'''
import pygame
pygame.init()
dis = pygame.display.set_mode((500,500))
r = pygame.Rect(10, 90, 100, 100)
dis_over = False
while not dis_over:
    for event in pygame.event.get():
        dis.fill((255, 255, 255))
        pygame.draw.rect(dis, (205, 50, 5), r)
        pygame.draw.polygon(dis, (150, 0, 0), [(10, 90), (110, 90), (60, 40)])
        pygame.draw.rect(dis, (0, 191, 255), (45, 120, 30, 30))
        pygame.draw.circle(dis, (255, 224, 189), (300, 150), 50)
        pygame.draw.circle(dis, (0, 0, 0), (285, 140), 5)
        pygame.draw.circle(dis, (0, 0, 0), (315, 140), 5)
        pygame.draw.arc(dis, (0, 0, 0), (280, 150, 40, 20), 3.14, 2*3.14, 2)
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
quit()
'''
#----------------------------------------------------------------------------------------
'''
import pygame
pygame.init()
dis = pygame.display.set_mode((1000, 800))
r = pygame.Rect(10, 90, 100, 100)
dis_over = False
while not dis_over:
    for event in pygame.event.get():
        pygame.draw.rect(dis, (205, 50, 5), r, 5, 10)
        pygame.draw.polygon(dis, (205, 50, 5), [(100, 100), (900, 90), (60, 60)])
        dis.fill((34, 139, 34))
        pygame.draw.rect(dis, (50, 50, 50), (400, 0, 200, 800))  
        pygame.draw.line(dis, (255, 255, 0), (500, 0), (500, 800), 5)  
        pygame.draw.rect(dis, (178, 34, 34), (100, 100, 150, 100)) 
        pygame.draw.rect(dis, (70, 130, 180), (700, 200, 180, 120)) 
        pygame.draw.rect(dis, (160, 82, 45), (200, 500, 120, 90))  
        pygame.draw.ellipse(dis, (0, 191, 255), (700, 500, 200, 120))
        for x, y in [(300, 300), (320, 330), (280, 360), (750, 100), (780, 130)]:
            pygame.draw.rect(dis, (139, 69, 19), (x - 5, y + 20, 10, 20))  
            pygame.draw.circle(dis, (34, 139, 34), (x, y), 20)  
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
quit()
'''
#----------------------------------------------------------------------------------------