import tornado.ioloop
import tornado.web
import threading
import asyncio
import json

gethistory_s_r = None
jineng_s_r = None
readlog_s_r = None
readlog_s_r = None


'''
http://localhost:8888/
'''

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class MainHandler(BaseHandler):
    
    def get(self):
        global history
        history = None
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('index.html')

class DsHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('ds.html')

class LogHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('log.html', log=readlog_s_r)

class StudyHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('study.html')


class DhHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('dh.html',history=gethistory_s_r.getHistory())

class HistoryHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
        else:
            res = {'code': 0, 'message': 'ok', 'history': json.dumps(gethistory_s_r.getHistory())}
        self.write(json.dumps(res))
        self.finish()

class GetLogHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
        else:
            res = {'code': 0, 'message': 'ok', 'log': readlog_s_r}
        self.write(json.dumps(res))
        self.finish()

class ChatHandler(BaseHandler):
    def post(self):
        if not self.current_user:
            res = {'code': 1, 'message': 'illegal visit'}
            print('chl1..........')
        else:
            global jineng_s_r
            query = self.get_argument('query', '')
            sc_s = str(query)
            if sc_s !='':
                jineng_s_r.jineng(sc_s)
                print('chl3..........')
            res = {'code': 0, 'message': 'ok'}
        self.write(json.dumps(res))
        self.finish()

class ListHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        self.render('list.html')

class LoginHandler(BaseHandler):
    def get(self):

        if self.current_user:
            self.redirect('/')
            return
        '''
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name"><br/>'
                   'Password: <input type="password" name="password">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')
        '''
        self.render('login.html')


    def post(self):

        if '12345' == self.get_argument('password', default=''):#可自行修改
            self.set_secure_cookie("user", self.get_argument("name"))
            self.redirect("/")
        else:
            self.write('用户名或密码错误，请尝试重新输入')
            pass


class ds():
    def get(self):
        self.render('ds.html')
        

settings = {
    "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    "template_path": "server/template",
    "static_path": "server/static"
}
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        (r"/ds", DsHandler),
        (r"/log", LogHandler),
        (r"/study", StudyHandler),
        (r"/dh", DhHandler),
        (r"/list", ListHandler),
        (r"/history",HistoryHandler),
        (r"/chat",ChatHandler),
        (r"/getlog",GetLogHandler)
    ], **settings)

app = make_app()

def start_server():
    asyncio.set_event_loop(asyncio.new_event_loop())
    app.listen(8888)#可自行修改
    tornado.ioloop.IOLoop.current().start()

def run(jineng_r,gethistory_r,readlog_r):
    global jineng_s_r
    global gethistory_s_r
    global readlog_s_r
    jineng_s_r = jineng_r
    gethistory_s_r = gethistory_r
    readlog_s_r = readlog_r
    threading.Thread(target=start_server).start()

def hread(readlog_r):
    global readlog_s_r
    readlog_s_r = readlog_r