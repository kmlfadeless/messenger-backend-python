import tornado.ioloop
import tornado.web
import tornado.autoreload
import tornado.websocket
import os
from v1.handlers.AuthHandler import *


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('static/index.html')


class Application(tornado.web.Application):
    def __init__(self, db=None):
        # if db == None:
        #     db = Session()
        self.webSocketsPool = []
        handlers = [
            (r'/v1', MainHandler),
            (r'/v1/auth/register/?', AuthHandlerRegister),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static/'})
        ]

        # если понадобится cookie_secret(для подписания cookie),
        # login_url(декоратор для перенаправления на страницу авторизации не зарегистрированного пользователя
        settings = dict()
        # websocket_ping_interval=1 (для включения пинга) для отключение неактивных клиентов
        tornado.web.Application.__init__(self, handlers, **settings, websocket_ping_interval=10,
                                         websocket_ping_timeout=5 * 60)

        # self.db = db


if __name__ == '__main__':
    application = Application()
    application.listen(3000)
    tornado.autoreload.start()
    for dir, _, files in os.walk('static'):
        [tornado.autoreload.watch(dir + '/' + f) for f in files if not f.startswith('.')]

    tornado.ioloop.IOLoop.instance().start()
