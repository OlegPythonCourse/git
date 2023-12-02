import sys
import time

timer = int(sys.argv[-1])
for seconds in range(timer):
    print(time.ctime())
    time.sleep(1)
    timer = -1
    if timer == 0:
        break
