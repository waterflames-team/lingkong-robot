import subprocess
import threading
import os



global play

def hh(src):
    foo, ext = os.path.splitext(src)
    
global stop


def run(src):
    cmd = ['play', src]
    global proc
    proc = subprocess.Popen(cmd)


def stop():
    try:
        outs, errs = proc.communicate(timeout=1)
    except subprocess.TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()    


def play(src):
    hh(src)
    run(src)

