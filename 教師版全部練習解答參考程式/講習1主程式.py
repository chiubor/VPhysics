﻿from visual import *
g=9.8               #重力加速度 9.8 m/s^2
size = 0.25         #球半徑 0.25 m
height = 15.0       #球初始高度 15 m

scene = display(width=800, height=800, center = (0,height/2,0), background=(0.5,0.5,0)) #設定畫面
floor = box(length=30, height=0.01, width=10, color=color.blue)                         #畫地板
ball = sphere(radius = size, color=color.red)                                           #畫球

ball.pos = vector( 0, height, 0)        #球初始位置
ball.v = vector(0, 0 , 0)               #球初速

dt = 0.001                              #時間間隔 0.001 秒
while ball.pos.y >= size:               #模擬直到球落地 即 y=球半徑
    rate(1000)                          #每一秒跑 1000 次

    ball.pos += ball.v*dt
    ball.v.y += - g*dt
