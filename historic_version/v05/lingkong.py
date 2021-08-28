import snowboydecoder
from subprocess import call
import re
import sys
import subprocess
import threading
import urllib.request
import signal
import os
import requests
import json
import base64
import time
import random
import uuid
import logging
from logging import handlers

import lk.player
import lk.config
import shan
from server import server

modle = lk.config.snowboy_fk_conf()
'''
1方案是：唤醒后说ding，然后录完音说dong
2方案是：唤醒后说在呢或干嘛，录完音啥都不说
默认为方案1
'''

py = int(sys.version_info.major)
print(py)
if py == 3:
    pass
else:
    print("请使用python3运行")
    sys.exit(0)

interrupted = False
player = None
global history
history = None
jineng_s = None
readlog_s = None
logger = None
logger_go = 1
global config
config = None



#沙雕取log----------------------------------------------------------------------------------

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)


#沙雕取log----------------------------------------------------------------------------------

read_log_s = None


global log_log
log_log = Logger('all.log',level='debug')

log_log.logger.debug('''

---------------------------------------
        灵空-一个中文语音对话机器人 
        版本号：0.5.9.200321
        by ffxw0720                
        欢迎使用!!!                              
---------------------------------------

''')

f = open("all.log",'r')#1
read_log_s = f.read() 
f.close()
readlog_s = read_log_s

#机器人主体分界线-------------------------------------------------------------------------------------



#web对话
class History():

    def __init__(self):
        self.history = []

    def getHistory(self):
        return self.history

    def appendHistory(self, type, text):
        if type in (0,1) and text != '':
            self.history.append({'type': type, 'text': text, 'uuid': str(uuid.uuid1())})

#web对话

history = History()

def audioRecorderCallback(fname):#snowboy to asr

    f = open("all.log",'r')#1
    read_log_s = f.read() 
    f.close()
    readlog_s = read_log_s

    

    f = open("fname.txt",'w+')
    f.write(fname)
    f.close()

    f = open("fname.txt",'r')
    yuansheng = f.read()
    
    if modle==2:
        pass
        next
    else:
        lk.player.play('music/dong.wav')
    
    #asr
    IS_PY3 = sys.version_info.major == 3


    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    timer = time.perf_counter


    API_KEY = 'kVcnfD9iW2XVZSMaLMrtLYIz'
    SECRET_KEY = 'O9o1O213UgG5LFn0bDGNtoRN3VWl2du6'



    

    def asr(file):
	    global AUDIO_FILE
	    global FORMAT
	    AUDIO_FILE = file
	    FORMAT = AUDIO_FILE[-3:]
    	#文件后缀只支持pcm/wav/amr格式
    	
    asr(fname)# 需要识别的文件	

    CUID = '123456PYTHON'
    # 采样率
    RATE = 16000  # 固定值

    # 普通版

    DEV_PID = 1536  # 1537 表示识别普通话，使用输入法模型。1536表示识别普通话，使用搜索模型。根据文档填写PID，选择语言及识别模型
    ASR_URL = 'http://vop.baidu.com/server_api'
    SCOPE = 'audio_voice_assistant_get'  # 有此scope表示有asr能力，没有请在网页里勾选，非常旧的应用可能没有



    class DemoError(Exception):
        pass


    """  TOKEN start """

    TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'


    def fetch_token():
	
        params = {'grant_type': 'client_credentials',
                  'client_id': API_KEY,
                  'client_secret': SECRET_KEY}
        post_data = urlencode(params)
        if (IS_PY3):
            post_data = post_data.encode( 'utf-8')
        req = Request(TOKEN_URL, post_data)
        try:
            f = urlopen(req)
            result_str = f.read()
        except URLError as err:
            #print('token http response http code : ' + str(err.code))
            result_str = err.read()
        if (IS_PY3):
            result_str =  result_str.decode()

        #print(result_str)
        result = json.loads(result_str)
        #print(result)
        if ('access_token' in result.keys() and 'scope' in result.keys()):
            #print(SCOPE)
            if SCOPE and (not SCOPE in result['scope'].split(' ')):  # SCOPE = False 忽略检查
                raise DemoError('scope is not correct')
            #print('SUCCESS WITH TOKEN: %s  EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
            return result['access_token']
        else:
            raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')

    """  TOKEN end """

    if __name__ == '__main__':
        token = fetch_token()
    
        speech_data = []
        global AUDIO_FILE
        with open(AUDIO_FILE, 'rb') as speech_file:
            speech_data = speech_file.read()

        length = len(speech_data)
        if length == 0:
            raise DemoError('file %s length read 0 bytes' % AUDIO_FILE)
        speech = base64.b64encode(speech_data)
        if (IS_PY3):
            speech = str(speech, 'utf-8')
        global FORMAT
        params = {'dev_pid': DEV_PID,
                 #"lm_id" : LM_ID,    #测试自训练平台开启此项
                  'format': FORMAT,
                  'rate': RATE,
                  'token': token,
                  'cuid': CUID,
                  'channel': 1,
                  'speech': speech,
                  'len': length
                  }
        post_data = json.dumps(params, sort_keys=False)
    
        req = Request(ASR_URL, post_data.encode('utf-8'))
        req.add_header('Content-Type', 'application/json')
        try:
            begin = timer()
            f = urlopen(req)
            result_str = f.read()
            #print ("Request time cost %f" % (timer() - begin))
        except URLError as err:
            #print('asr http response http code : ' + str(err.code))
            result_str = eer.read()


        if (IS_PY3):
            #global cg
            #cg = result_str['result'][0]
            #cg = result_str.json['result']
            result_str = str(result_str, 'utf-8')
       #print(result_str)
        with open("result.txt","w") as of:
            of.write(result_str)
      

    log_log.logger.debug('-------------')  

    cg = json.loads(result_str)
    
  
    cg = cg['result'][0]
    log_log.logger.debug(cg)

    log_log.logger.debug('-------------')

    jineng.jineng(0,cg)#调用技能

    f = open("fname.txt",'r')#删除动作
    yuansheng = f.read()
    f.close()
    shan.dele(yuansheng)
    shan.dele("fname.txt")

    #asr

    f = open("all.log",'r')#2
    read_log_s = f.read()   
    f.close()
    readlog_s = read_log_s

    #--------------------------------------------------------asr 和 tts 的分界线---------------------------------------
global yuansheng


def tts(tts_text):    
    #tts
    IS_PY3 = sys.version_info.major == 3
    if IS_PY3:
        from urllib.request import urlopen
        from urllib.request import Request
        from urllib.error import URLError
        from urllib.parse import urlencode
        from urllib.parse import quote_plus
    else:
        log_log.logger.debug('请使用python3运行')

    API_KEY = '4E1BG9lTnlSeIf1NQFlrSq6h'
    SECRET_KEY = '544ca4657ba8002e3dea3ac2f5fdd241'



    TEXT = tts_text#要识别的文字
    


    # 发音人选择, 基础音库：0为度小美，1为度小宇，3为度逍遥，4为度丫丫，
    # 精品音库：5为度小娇，103为度米朵，106为度博文，110为度小童，111为度小萌，默认为度小美 
    PER = 3
    # 语速，取值0-15，默认为5中语速
    SPD = 5
    # 音调，取值0-15，默认为5中语调
    PIT = 5
    # 音量，取值0-9，默认为5中音量
    VOL = 5
    # 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
    AUE = 3

    FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
    FORMAT = FORMATS[AUE]

    CUID = "123456PYTHON"

    TTS_URL = 'http://tsn.baidu.com/text2audio'


    class DemoError(Exception):
        pass


    """  TOKEN start """

    TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
    SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选


    def fetch_token():
        #print("fetch token begin")
        params = {'grant_type': 'client_credentials',
                  'client_id': API_KEY,
                  'client_secret': SECRET_KEY}
        post_data = urlencode(params)
        if (IS_PY3):
            post_data = post_data.encode('utf-8')
        req = Request(TOKEN_URL, post_data)
        try:
            f = urlopen(req, timeout=5)
            result_str = f.read()
        except URLError as err:
            #print('token http response http code : ' + str(err.code))
            result_str = err.read()
        if (IS_PY3):
            result_str = result_str.decode()

        #print(result_str)
        result = json.loads(result_str)
        #print(result)
        if ('access_token' in result.keys() and 'scope' in result.keys()):
            if not SCOPE in result['scope'].split(' '):
                raise DemoError('scope is not correct')
            #print('SUCCESS WITH TOKEN: %s ; EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
            return result['access_token']
        else:
            raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')


    """  TOKEN end """

    if __name__ == '__main__':
        token = fetch_token()
        tex = quote_plus(TEXT)  # 此处TEXT需要两次urlencode
        #print(tex)
        params = {'tok': token, 'tex': tex, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL, 'aue': AUE, 'cuid': CUID,
                  'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数

        data = urlencode(params)
        #print('test on Web Browser' + TTS_URL + '?' + data)

        req = Request(TTS_URL, data.encode('utf-8'))
        has_error = False
        try:
            f = urlopen(req)
            result_str = f.read()

            headers = dict((name.lower(), value) for name, value in f.headers.items())

            has_error = ('content-type' not in headers.keys() or headers['content-type'].find('audio/') < 0)
        except  URLError as err:
            #print('asr http response http code : ' + str(err.code))
            result_str = err.read()
            has_error = True

        save_file = "error.txt" if has_error else 'result.' + FORMAT
        with open(save_file, 'wb') as of:
            of.write(result_str)

        if has_error:
            if (IS_PY3):
                result_str = str(result_str, 'utf-8')
            #print("tts api  error:" + result_str)

        #print("result saved as :" + save_file)
        fname = save_file
    #tts
    global player
    lk.player.play('result.mp3')
    time.sleep(1)
    shan.dele("result.mp3")
    log_log.logger.debug('已成功返回答复')
    log_log.logger.debug(tts_text)
    
    
    shan.dele("result.txt")
    
    
    history.appendHistory(1, tts_text)

    f = open("all.log",'r')#4
    read_log_s = f.read() 
    f.close()       
    readlog_s = read_log_s
    server.hread(readlog_s)

    log_log.logger.debug('按Ctrl +4 退出程序')

    pass
    

class jineng():

    def jineng(rl,j_hua):
    
        global jn_hua
        jn_hua = j_hua
        history.appendHistory(0, jn_hua)
    

        class yuliao():

            def can():
                if '你会' in jn_hua:
                    tts("我会的东西可多了，有闲聊、问问题、讲笑话等。想知道更多的就去灵空的github看看吧！")
        
            def father():
                if "你爸爸" in jn_hua or "你的爸爸" in jn_hua:
                    tts("我爸比是非凡小王！")

        def xsh():
            if "学我说" in jn_hua:
                sxh_hua_z = None
                sxh_hua_z = re.sub(r'学我说', ' ', jn_hua)
                tts(sxh_hua_z)

        class xiaohua():
            if '笑话' in jn_hua:

                xh_f = open("xh.json",'r')
                xh_ji = xh_f.read()
                xh_f.close()

                xh_ji = str(xh_ji)

                xh_jg = json.loads(xh_ji)
                xh_jg = xh_jg["result"][str(random.randint(1, 40))]["text"]

                tts(xh_jg)


        class weather():

            if "天气" in jn_hua:

                global LOCATION
                global API
                global UNIT
                global LANGUAGE
                global KEY
                global UID



                KEY = lk.config.weater_id_conf()  
                UID = lk.config.weater_key_conf()  

                LOCATION = lk.config.city_conf()  
                API = 'https://api.seniverse.com/v3/weather/now.json'  
                UNIT = 'c'  # 单位
                LANGUAGE = 'zh-Hans'  # 查询结果的返回语言
                
                def run_wea():
                    if __name__ == '__main__':
                        location = LOCATION

                        result = requests.get(API, params={
                            'key': KEY,
                            'location': location,
                            'language': LANGUAGE,
                            'unit': UNIT
                        }, timeout=1)
                        wea_test = result.text

                        result = wea_test
                        reu = str(result)
                        re = json.loads(reu)
                        text_one=re['results'][0]['location']['name']
                        text_two=re['results'][0]['now']['text']
                        text_three=re['results'][0]['now']['temperature']
                        tts(text_one+","+text_two+",温度"+text_three+"摄氏度")

        class daiban():

            if '待办' in jn_hua or '代办' in jn_hua:

                if '待办' in jn_hua:
                    jn_hua = re.sub(r'待办', '代办', jn_hua)
                elif '代办' in jn_hua:
                    pass
            
                if '进入' in jn_hua:
                    jn_hua = re.sub(r'进入', '记录', jn_hua)

                class daiban(object):

                    def rukou(self,qidong):

                        def daiban(what):
                            db_lj = str(what)
                            log = open(('daiban_log/'+db_lj) , mode='a', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
                            log.write (what + '\n')
                            log.close
                            global th
                            th = what

                        if "添加" in qidong:
                            global jn_hua
                            if '待办' in jn_hua:
                                jn_hua = re.sub(r'待办', '代办', jn_hua)

                            if '进入' in jn_hua:
                                jn_hua = re.sub(r'进入', '添加', jn_hua)
                                
                            thing = re.sub(r'添加代办', ' ', jn_hua)
                            daiban(thing)
                            tts('完事')

                        if "删除" in qidong:
                            if '待办' in jn_hua:
                                jn_hua = re.sub(r'待办', '代办', jn_hua)
                            db_hua = re.sub(r'删除代办', ' ', jn_hua)
                            shan.dele('daiban_log/'+db_hua)
                            tts('完事')



                        elif "查看" in qidong:
                            tts('对不起，这个功能还未推出')
                    

                a=daiban()
                a.rukou(jn_hua)

        def tuling(t_hua):
        
            #感谢图灵提供服务！！！

            url = 'http://openapi.tuling123.com/openapi/api/v2'
            city = lk.config.city_conf()
            apid = lk.config.tuling_id_conf()

            sj = random.randint(1, 5)
            if sj == 1:
                apikey = lk.config.tuling_key1_conf()
                log_log.logger.debug("tuling_key1选择成功")
                pass
            if sj == 2:
                apikey = lk.config.tuling_key2_conf()
                log_log.logger.debug("tuling_key2选择成功")
                pass
            if sj == 3:
                apikey = lk.config.tuling_key3_conf()
                log_log.logger.debug("tuling_key3选择成功")
                pass
            if sj == 4:
                apikey = lk.config.tuling_key4_conf()
                log_log.logger.debug("tuling_key4选择成功")
                pass
            if sj == 5:
                apikey = lk.config.tuling_key5_conf()
                log_log.logger.debug("tuling_key5选择成功")
                pass
        


            a = t_hua
            log_log.logger.debug('已接入图灵')
            log_log.logger.debug(a)
            req={
                "reqType":0,
                "perception": {
                    "inputText": {
                        "text": a
                    },
                    "inputImage": {
                        "url": "imageUrl"
                    },
                    "selfInfo": {
                        "location": {
                            "city": city,
                        }
                    }
                },
                "userInfo": {
                    "apiKey": apikey,
                    "userId": apid 
                }
            }
            req=json.dumps(req).encode('utf8')
            post=requests.post(url,data=req,headers={'content-type': 'application/json'})
            r=post.text
            r=r.encode('utf8')
            r=json.loads(r)
            text=r['results'][0]['values']['text']
            tts(text)

        #定义结束，开始执行技能----------------------------------------------------------------------------
        if "你会" in jn_hua:
            yuliao.can()
            next
            pass
        elif "笑话" in jn_hua:
            xiaohua()
            next
            pass
        elif "你爸爸" in jn_hua or "你的爸爸" in jn_hua:
            yuliao.father()
            next
            pass
        elif '待办' in jn_hua or '代办' in jn_hua:
            daiban()
            next
            pass
        elif "学我说" in jn_hua:
            xsh()
            next
            pass
        elif "天气" in jn_hua:
            weather.run_wea()
            next
            pass
        else:
            tuling(jn_hua)
            next
            pass

        f = open("all.log",'r')#3
        read_log_s = f.read()   
        f.close()
        readlog_s = read_log_s

        

        
    
jineng_s =jineng()


    #机器人主体分界线-------------------------------------------------------------------------------------    
    #snowboy分界线--------------------------------------------------------------------------------------



def detectedCallback():
    lk.player.stop()
    if modle==2:
        
        h_sj = random.randint(1, 2)
        if h_sj==1:
            lk.player.play('music/h1.mp3')
        if h_sj==2:
            lk.player.play('music/h2.mp3')
    else:
        lk.player.play('music/ding.wav')



def signal_handler(signal, frame):
    global interrupted
    interrupted = True
    
    
    
def interrupt_callback():
    global interrupted
    return interrupted
    
    
'''
if len(sys.argv) == 1:
    print("错误：确认你打开snowboy的代码是否有错误")
    sys.exit(-1)
'''
    
server.run(jineng_s,history,readlog_s)

#model = sys.argv[1]
model = lk.config.snowboy_conf()
signal.signal(signal.SIGINT, signal_handler)
detector = snowboydecoder.HotwordDetector(model, sensitivity=0.7)
beg_name = lk.config.begin_conf()
tts(beg_name+"你好啊，欢迎使用灵空机器人，快说出唤醒词来唤醒我吧，啾咪")



detector.start(detected_callback=detectedCallback,
               audio_recorder_callback=audioRecorderCallback,
               interrupt_check=interrupt_callback,
               sleep_time=0.01)              
detector.terminate()

#snowboy分界线--------------------------------------------------------------------------------------