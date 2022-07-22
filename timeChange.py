import sys
import time

if __name__ == '__main__':
    id = time.CLOCK_REALTIME
    timeStamp = float(sys.argv[1])
    time.clock_settime(id, timeStamp)
