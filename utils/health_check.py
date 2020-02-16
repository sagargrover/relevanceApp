import json
import os
import time


def bringIntoLB():
    f = open('intoLB', 'a')
    f.write("Brought into LB at {}".format(int(time.time()*1000)))
    f.close()
    return {
        "body":"OK",
        "status": 200
    }

def bringOutOfLB():
    if os.path.exists('intoLB'):
        os.remove('intoLB')
    return {
        "body": "OK",
        "status": 200
    }

def poll():
    if os.path.exists('intoLB'):
        return True
    else:
        return False