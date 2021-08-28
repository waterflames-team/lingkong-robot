import json
def weater_id_conf():


    conf_z = open("config.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg["weater"]["id"]

    return conf_jg

def weater_key_conf():


    conf_z = open("config.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg["weater"]["key"]

    return conf_jg

def begin_conf():


    conf_z = open("config.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg["begin"]["name"]

    return conf_jg

def snowboy_conf():


    conf_z = open("config.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg["snowboy"]["file"]

    return conf_jg

def city_conf():


    conf_z = open("config.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg["city"]["name"]

    return conf_jg

def tuling_id_conf():


    conf_z = open("config.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg["tuling"]["id"]

    return conf_jg

def tuling_key1_conf():


    conf_z = open("config.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg["tuling"]["key1"]

    return conf_jg

def tuling_key2_conf():


    conf_z = open("config.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg["tuling"]["key2"]

    return conf_jg

def tuling_key3_conf():


    conf_z = open("config.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg["tuling"]["key3"]

    return conf_jg

def tuling_key4_conf():


    conf_z = open("config.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg["tuling"]["key4"]

    return conf_jg

def tuling_key5_conf():


    conf_z = open("config.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg["tuling"]["key5"]

    return conf_jg

def snowboy_fk_conf():


    conf_z = open("config.json",'r')
    conf_s = conf_z.read()
    conf_z.close()

    conf_j = str(conf_s)

    conf_jg = json.loads(conf_j)
    conf_jg = conf_jg["snowboy_fk"]["modle"]

    return conf_jg
