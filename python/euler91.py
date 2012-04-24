"""Problem 91
18 March 2005

The points P (x1, y1) and Q (x2, y2) are plotted at integer
co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.

There are exactly fourteen triangles containing a right angle that can
be formed when each co-ordinate lies between 0 and 2 inclusive; that
is, 0 <= x1, y1, x2, y2 <= 2.

Given that 0  x1, y1, x2, y2  50, how many right triangles can be
formed?
"""

from math import sqrt
from tkinter import *
from random import randint

LIMIT = 50

triangulos = {}
for x1 in range(0, LIMIT+1):
    for y1 in range(0, LIMIT+1):
        if x1 == 0 and y1 == 0:
            continue
        for x2 in range(0, LIMIT+1):
            for y2 in range(0, LIMIT+1):
                if (x2 == 0 and y2 == 0) or (x1 == x2 and y1 == y2):
                    continue    
                lados = [0, 0, 0]
                lados[0] = sqrt(x1*x1 + y1*y1)
                lados[1] = sqrt(x2*x2 + y2*y2)
                lados[2] = sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))
                cand_hipotenusa = max(lados)
                lados.remove(cand_hipotenusa) # ?
                cand_catetoA = lados[0]
                cand_catetoO = lados[1]
                if abs(cand_catetoA**2 + cand_catetoO**2 - cand_hipotenusa**2) < 0.0000001:
                    if (x1 == x2 and y1 <= y2) or (x1 < x2):
                        coord = (x1, y1, x2, y2)
                    else:
                        coord = (x2, y2, x1, y1)
                    triangulos[coord] = 1

print(len(triangulos))

#print(sorted(triangulos.keys()))

##SIZE = 500
##BORDER = 20
##SCALE = (SIZE - BORDER*2) // LIMIT
##
##master = Tk()
##w = Canvas(master, width=SIZE, height=SIZE)
##w.pack()
##border = 1
##for coord in triangulos.keys():
##    x1, y1, x2, y2 = map(lambda n: BORDER + n * SCALE, coord)
##    color = "#%02x%02x%02x" % (randint(0, 255), randint(0, 255), randint(0, 255))
##    w.create_line(BORDER, BORDER, x1, y1, fill=color, width=border)
##    w.create_line(BORDER, BORDER, x2, y2, fill=color, width=border)
##    w.create_line(x1, y1, x2, y2, fill=color, width=border)
##
##mainloop()



"""
triangulos com os catetos na origem:
  largura * altura

triangulos com cateto A e hipotenusa na origem:
  largura * altura

triangulos com cateto B e hipotenusa na origem:
  largura * altura

7500 + 50

triangulos com hipotenusa na horizontal:
  largura // 2 se <= altura senão = altura

triangulos com hipotenusa na horizontal:
  altura // 2 se <= largura senão = largura

outros triangulos?
  se x1 = 0 ou x2 = 0 ou y1 = 0 ou y2 = 0
    -> já estão nas regras definidas anteriormente
  se x1 == x2 ou y1 == y2
    -> já está nas regras definidas ou não é um triângulo retângulo

lados = [0, 0, 0]
lados[0] = sqrt(x1*x1 + y1*y1)
lados[1] = sqrt(x2*x2 + y2*y2)
lados[2] = sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

cand_hipotenusa = max(lados)
lados.remove(cand_hipotenusa) # ?

cand_catetoA = lados[0]
cand_catetoO = lados[1]

se cand_catetoA^2 + cand_catetoO^2 = cand_hipotenusa^2 entao
  é triangulo retangulo

"""
