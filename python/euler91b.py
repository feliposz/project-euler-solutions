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

from time import time

LIMIT = 50

inicio = time()

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
                lados[0] = x1*x1 + y1*y1
                lados[1] = x2*x2 + y2*y2
                lados[2] = (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)
                lados.sort() # ordena pelo tamanho dos lados, o maior é o candidato à hipotenusa
                catetoA2 = lados[0] # catetoA ^ 2
                catetoB2 = lados[1] # catetoB ^ 2
                hipotenusa2 = lados[2] # hipotenusa ^ 2
                if catetoA2 + catetoB2 == hipotenusa2: # catetoA ^ 2 + catetoB ^ 2 == hipotenusa ^ 2 ?
                    if (x1 == x2 and y1 <= y2) or (x1 < x2):
                        coord = (x1, y1, x2, y2)
                    else:
                        coord = (x2, y2, x1, y1)
                    triangulos[coord] = 1

print("Triangulos:", len(triangulos))
print("Tempo:", time() - inicio)
