import pygame as pg;import numpy as n;import math as m;from typing import*

W,H=800,600;FPS=60;G=.1
C={'S':(135,206,235),'G':(139,69,19),'R':(255,0,0),'B':(0,255,0)}

class T:
    def __init__(s,x,y,c,n='P',a=0):
        s.x=x;s.y=y;s.c=c;s.n=n;s.w=30;s.h=20
        s.a=45;s.p=50;s.l=100;s.w={'B':10};s.i=0;s.v=[]
        s.ai=a;s.f=0;s.t=[]
    
    def u(s,t):
        s.v=[(v['x']+v['dx'],v['y']+v['dy'],v['c'],v['l']-1)
             for v in s.v if v['l']>1]
        s.f=max(0,s.f-1)
        return s.l>0
    
    def d(s,r,o):
        x,y=int(s.x+o[0]),int(s.y+o[1])
        for v in s.v:
            pg.draw.circle(r,v[2],(int(v[0]+o[0]),int(v[1]+o[1])),2)
        c=tuple(min(255,c+100)for c in s.c)if s.f>0 else s.c
        pg.draw.rect(r,c,(x-s.w//2,y-s.h//2,s.w,s.h))
        e_x=x+m.cos(m.radians(s.a))*20
        e_y=y-m.sin(m.radians(s.a))*20
        pg.draw.line(r,c,(x,y),(e_x,e_y),3)
        pg.draw.rect(r,C['R'],(x-20,y-s.h-10,40,5))
        if s.l>0:
            w=int(40*s.l/100)
            pg.draw.rect(r,C['B'],(x-20,y-s.h-10,w,5))

class P:
    def __init__(s,x,y,a,p,c):
        s.x=x;s.y=y;s.vx=m.cos(m.radians(a))*p*.1
        s.vy=-m.sin(m.radians(a))*p*.1;s.c=c;s.t=[]
    
    def u(s,t):
        s.vy+=G;s.x+=s.vx;s.y+=s.vy
        s.t+=[(int(s.x),int(s.y))]
        if len(s.t)>20:s.t.pop(0)
        return s.y<t.h(s.x)and 0<=s.x<=W and s.y<=H
    
    def d(s,r,o):
        if len(s.t)>1:
            pg.draw.lines(r,s.c,0,
                [(x+o[0],y+o[1])for x,y in s.t],2)
        pg.draw.circle(r,s.c,
            (int(s.x+o[0]),int(s.y+o[1])),3)