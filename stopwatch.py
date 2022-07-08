from cryptography.fernet import Fernet
import pygame
import time
code = b"""
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Stopwatch")
pygame.font.init()
font = pygame.font.SysFont("Corbel",40)
pressed_start = False
pressed_stop = True
start_rect = pygame.Rect(200, 300, 80, 35)
reset_rect = pygame.Rect(300,300,85,35)
stop_rect = pygame.Rect(200, 300, 75, 40)
quit_rect = pygame.Rect(250,350,70,40)
min = 1//10
sec = min//60
millisec = sec//100
while True:
    mouse = pygame.mouse.get_pos()
    color = screen.get_at(mouse)
    screen.fill((191,239,255))
    if reset_rect.collidepoint(mouse):
        pygame.draw.rect(screen,(200,200,200),reset_rect)
    if quit_rect.collidepoint(mouse):
        pygame.draw.rect(screen,(200,200,200),quit_rect)
    text1 = font.render(f"{min} : {sec} : {millisec}", True, (0, 0, 0))
    screen.blit(text1, (200, 250))
    text2 = font.render("StopWatch",True,(0,0,0))
    if not pressed_start:
        if start_rect.collidepoint(mouse):
            pygame.draw.rect(screen, (200, 200, 200), start_rect)
        text3 = font.render("Start",True,(0,0,0))
        screen.blit(text3, (200, 300))
    if not pressed_stop:
        if stop_rect.collidepoint(mouse):
            pygame.draw.rect(screen,(198,198,198),stop_rect)
        text5 = font.render("Stop",True,(0,0,0))
        screen.blit(text5,(200,300))
    text4 = font.render("Reset",True,(0,0,0))
    text6 = font.render("Quit",True,(0,0,0))
    screen.blit(text2,(200,200))
    screen.blit(text4,(300,300))
    screen.blit(text6,(250,350))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(mouse) and color[:3] == (200,200,200):
                pressed_start = True
                pressed_stop = False
            if stop_rect.collidepoint(mouse) and color[:3] == (198,198,198):
                pressed_stop = True
                pressed_start = False
            if reset_rect.collidepoint(mouse):
                min = 1 // 10
                sec = min // 60
                millisec = sec // 100
            if quit_rect.collidepoint(mouse):
                pygame.quit()
    if millisec >= 100:
        sec += 1
        millisec = 0
    if sec > 60:
        min += 1
        sec = 0
    if pressed_start and not pressed_stop:
        millisec += 1
    time.sleep(0.01)
    pygame.display.update()"""
key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_msg = encryption_type.encrypt(code)
decrypted_message = encryption_type.decrypt(encrypted_msg)
exec(decrypted_message)
