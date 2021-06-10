
from typing import List
import pygame
from pygame import event

class MyClass():
    def __init__(self, val):
        self.val = val
        self.val2 = 'mart'

    def test(self):
        pass


mylist: List[MyClass] = [] 
mylist.append(MyClass(1))
mylist.append(MyClass(2))
for curitem in mylist:
    print(curitem.val)
 
pygame.init()
for event in pygame.event.get():
    if event.EventType == 0:
        pass

