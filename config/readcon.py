print("readcon OK")

import json

def ReadCon():
    config_file = open("config/config.json","r",encoding = "utf-8")
    config_json = config_file.read()
    config_file.close()
    config = json.loads(config_json)
    return config

ReadFile = ReadCon()

def ReadNow(one,two):
    One = one
    Two = two
    Out = ReadFile[one][two]
    return Out

def ReadAPI(where,one):
    One = one
    Where = where
    Out = json.loads(Where)
    Out = Out['sysTime2']
    return Out