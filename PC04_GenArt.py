#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:53:10 2021

@author: jacquie silvern and lyndan wall
"""

import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(200)
        some_turtle.right(90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    
    code = turtle.Turtle()
    code.shape("turtle")
    code.color("DarkOrchid")
    code.speed(10)
    code.pensize(4)
    for i in range (1,37):
        draw_square(code)
        code.right(10)
    
draw_art()

turtle.up()
turtle.pencolor("LightBlue")
turtle.down()

def draw_rectangle(go_turtle):
    for i in range(1,5):
       go_turtle.forward(90)
       go_turtle.right(45)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    
    fun = turtle.Turtle()
    fun.shape("turtle")
    fun.color("LightBlue")
    fun.speed(10)
    fun.pensize(1)
    for i in range (1,25):
        draw_square(fun)
        fun.right(15)

draw_art()

turtle.up()
turtle.down()

def draw_pentagon(happy_turtle):
    for i in range(1,9):
      happy_turtle.forward(60)
      happy_turtle.right(60)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    
    yay = turtle.Turtle()
    yay.shape("turtle")
    yay.color("LightGreen")
    yay.speed(10)
    yay.pensize(2)
    for i in range (1,15):
        draw_square(yay)
        yay.right(15)

draw_art()
