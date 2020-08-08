#Info
Version='2.0'
Author=['Redroadsl']

Capition='NJTools v'+Version
#Import
##import numba
import pygame
from pygame.locals import *
import threading
import os
import sys
import ctypes
#Init
threading.ThreadError()
class S(object):
    RUN=True
    WTYPE='FULL'
    X=ctypes.windll.user32.GetSystemMetrics(0)
    Y=ctypes.windll.user32.GetSystemMetrics(1)

os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d" % (0,0)#设置窗口坐标
#获取屏幕大小
pygame.init()#初始化
pygame.display.set_caption(Capition)#窗口标题
screen=pygame.display.set_mode((S.X,S.Y),0,32)#设置窗口大小
#screen=pygame.display.set_mode((S.X,S.Y),FULLSCREEN,32)
#screen=pygame.display.set_mode((S.X,S.Y),DOUBLEBUF,32),HWSURFACE
pygame.event.set_grab(True)#定向输入
Font=pygame.font.SysFont("宋体",50,False,False,None)
Font_big=pygame.font.SysFont("宋体",300,False,False,None)
capition=Capition


#WindowPaint
def main():
    if S.RUN:
        global screen
        screen.fill((102,204,255))
            #|__|
        pygame.draw.lines(screen,(255,255,255),False,[(50,50),(S.X-50,50)],4)
        pygame.draw.lines(screen,(255,255,255),False,[(50,50),(50,S.Y-50)],4)
        pygame.draw.lines(screen,(255,255,255),False,[(S.X-50,S.Y-50),(S.X-50,50)],4)
        pygame.draw.lines(screen,(255,255,255),False,[(S.X-50,S.Y-50),(50,S.Y-50)],4)
        # [-] [l=l] [x]
        pygame.draw.rect(screen,(0,255,0),((S.X-150,0),(50,50)),0)
        pygame.draw.rect(screen,(0,0,255),((S.X-100,0),(50,50)),0)
        pygame.draw.rect(screen,(255,0,0),((S.X-50,0),(50,50)),0)
        #"X"
        pygame.draw.line(screen,(0,0,0),(S.X-40,10),(S.X-10,40),4)
        pygame.draw.line(screen,(0,0,0),(S.X-40,40),(S.X-10,10),4)
        #CAPITION
        screen.blit(Font.render(capition,1,(0,0,0)),(0,0))
        #"|=|"
        pygame.draw.rect(screen,(0,0,0),((S.X-90,10),(30,30)),4)
        #"[-]"
        pygame.draw.lines(screen,(0,0,0),1,[(S.X-140,25),(S.X-110,25)],4)
        pygame.display.flip()
        pygame.display.update()
#Function: IsClick
def cliL(x,y,x2,y2):
    while S.RUN:
        for event in pygame.event.get():
            if event.type==MOUSEBUTTONDOWN or event.type==MOUSEBUTTONUP:
                xx,yy=event.pos[0],event.pos[1]
                if xx > x and xx < x2 and yy > y and yy < y2:
                    return True


#Functions
def qui():
    '''QuitEvent>Thread'''
    global capition
    global screen
    while S.RUN:
        for event in pygame.event.get():
            x=S.X
            if event.type == QUIT or cliL(x-50,0,x,50):
                screen.blit(Font_big.render('Exit',1,(255,0,0)),(50,50))
                pygame.display.update()
                S.RUN=False
                pygame.quit()
                #sys.exit()
                exit()
                os.system("taskkill /f /im python")
##            if event.type == KEYDOWN and event.key == K_ESCAPE:
##                screen.blit(Font_big.render('Exit',1,(255,0,0)),(50,50))
##                pygame.display.update()
##                S.RUN=False
##                pygame.quit()
##                sys.exit()
##                os.system("taskkill /f /im python")   
#Thread: QuitEvent
qtEvent_=threading.Thread(target=qui)
qtEvent_.setName('QuitEvent')
qtEvent_.start()
#if xx > x and xx < x2 and yy > y and yy < y2:
def WType():
    global screen
    typee=pygame.event.get(MOUSEBUTTONDOWN)
    x,y=pygame.mouse.get_pos()
    if x>(S.X-100) and y>0 and x<(S.X-50) and y<50 and S.WTYPE=='FULL' and typee:
        print('FULL -> WIN')
        os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d" % (S.X//3,S.Y//3)
        screen=pygame.display.set_mode((S.X//2,S.Y//2),NOFRAME,32)
        pygame.event.set_grab(False)#定向输入
        S.X=S.X//2
        S.Y=S.Y//2
        S.WTYPE='WIN'
        main()
        pygame.time.delay(100)
    if x>(S.X-100) and y>0 and x<(S.X-50) and y<50 and S.WTYPE=='WIN' and typee:
        os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d" % (0,0)
        S.X=ctypes.windll.user32.GetSystemMetrics(0)
        S.Y=ctypes.windll.user32.GetSystemMetrics(1)
        screen=pygame.display.set_mode((S.X,S.Y),0,32)
        pygame.event.set_grab(True)#定向输入
        S.WTYPE='FULL'
        main()
        pygame.time.delay(100)


#Mousepaint
def mouse():
    global screen
    #pygame.event.get()
    if pygame.mouse.get_pressed()==(1,0,0) and S.RUN:
        x,y=pygame.mouse.get_pos()
        pygame.draw.rect(screen,(0,0,0),((x,y),(10,10)),0)
        pygame.display.flip()
        pygame.display.update()
##mouse_=threading.Thread(target=mouse)
##mouse_.setName('MouseImg')
##mouse_.start()

##WT_=threading.Thread(target=WType)
##WT_.setName('TypeContrler')
##WT_.start()
main()
#MainLoop
while S.RUN:
    WType()
    mouse()
    pygame.display.flip()
    pygame.display.update()
    pygame.event.pump()
    #qui()

