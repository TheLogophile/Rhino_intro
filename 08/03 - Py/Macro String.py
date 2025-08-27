# Marcro string generator

f = open('macro.txt',"w")
import math

len_both_sides = 100
actual_len = len_both_sides * 2
array_number = 100
segment = actual_len / array_number
def distance(x,y):
    return math.sqrt((x**2) + (y**2))
for i in range(array_number+1):
    y = -len_both_sides + (segment*i)
    for j in range(array_number+1):
        x = -len_both_sides + (segment*j)
        z = (math.sin(distance(x/5,y/5)))*distance(x,y)/2
        f.write(f"polygon {x},{y},{z} n 4 {segment/3} enter \nsellast rotate 0,0,0 {distance(x,y)/5} \n")






