import time
import timeit

def sigma():
    first=1
    last = [
    15972490,
    80247910,
    92031257,
    75940266,
    97986012,
    87599664,
    75231321,
    11138524,
    68870499,
    11872796,
    79132533,
    40649382,
    63886074,
    53146293,
    36914087,
    62770938,
    ] 
    for x in last:
        sum((x-i)*i for i in range(first, x+1))


