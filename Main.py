from cmath import sin
from cmath import cos
import math
from pip._vendor.distlib.compat import raw_input

def compute_decline(user_input):
    userinput = user_input.split()
    p = int(userinput[0])
    a = int(userinput[1])
    b = int(userinput[2])
    c = int(userinput[3])
    d = int(userinput[4])
    n = int(userinput[5])
    timeline = []
    for num in range(1,n):
        timeline.append(compute_price(p, a, b, c, d, num))
    max_decline = 0
    for i in range(0,n-1):
        for j in range(i+1,n-1):
            if timeline[i] > timeline[j]:
                diff = timeline[i] - timeline [j]
                if diff > max_decline:
                    max_decline = diff
    
    print (math.ceil((max_decline)*1000000)/1000000)
    
def compute_price(p, a, b, c, d, k):
    return math.ceil(((p*(sin(a*k+b)+cos(c*k+d)+2)).real)*10000000)/10000000
    
#user_input=[100, 432, 406, 867, 60, 1000]
user_input = raw_input('Enter the sequence separated by spaces: ')
print(compute_decline(user_input))