import os

def dele(fpath):
    if os.path.exists(fpath):
        os.remove(fpath) 
    #检测+删除