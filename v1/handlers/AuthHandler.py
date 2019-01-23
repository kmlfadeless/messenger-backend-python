import tornado.web


class AuthHandlerRegister(tornado.web.RequestHandler):
    def get(self):
        self.write({'message': 'hello world'})


