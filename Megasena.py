# -*- coding: utf-8 -*-
import random

w = open("logmega.txt", "w")


lista = random.sample(range(1,60), 6)
lista.sort()


w.write (str(lista)+ "\n")

	

	
