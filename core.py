import pygame as pg;import numpy as n;import math as m;from typing import*
W,H=800,600;FPS=60;G=.1
C={'S':(135,206,235),'G':(139,69,19),'R':(255,0,0),'B':(0,255,0)}
class T:
 def __init__(s,x,y,c,n='P',a=0):s.x=x;s.y=y;s.c=c;s.n=n;s.w=30;s.h=20;s.a=45;s.p=50;s.l=100;s.w={'B':10};s.i=0;s.v=[]
 def u(s,t):s.v=[(v['x']+v['dx'],v['y']+v['dy'],v['c'],v['l']-1)for v in s.v if v['l']>1];return s.l>0
 def d(s,r,o):
  x,y=int(s.x+o[0]),int(s.y+o[1])
  for v in s.v:pg.draw.circle(r,v[2],(int(v[0]+o[0]),int(v[1]+o[1])),2)
  pg.draw.rect(r,s.c,(x-s.w//2,y-s.h//2,s.w,s.h))
  pg.draw.line(r,s.c,(x,y),(x+m.cos(m.radians(s.a))*20,y-m.sin(m.radians(s.a))*20),3)
  pg.draw.rect(r,C['R'],(x-20,y-s.h-10,40,5))
  if s.l>0:pg.draw.rect(r,C['B'],(x-20,y-s.h-10,int(40*s.l/100),5))