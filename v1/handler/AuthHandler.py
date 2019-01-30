import tornado.web
import v1.model.user as user


class AuthHandlerRegister(tornado.web.RequestHandler):
    def get(self):
        self.write({'message': 'hello world'})

    def post(self):
        email = self.get_argument('email')
        password = self.get_argument('password')
        name = self.get_argument('name')
        new_user = user.User()
        new_user.email = email
        new_user.password = password
        new_user.name = name
        new_user.save()
        self.write({'status': 'success'})
