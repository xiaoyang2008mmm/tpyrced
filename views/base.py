# -*- coding: utf-8 -*- 
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        if not self.request.uri.startswith(self.get_login_url()) and self.current_user is  None:
            self.redirect(self.get_login_url())

    @property
    def db(self):
       return self.application.db
    def get_current_user(self):
       return self.get_secure_cookie("user")

    def admin(self):
	return ['admin']

    def get_template_namespace(self):
        namespace = {}
        namespace = super(BaseHandler,self).get_template_namespace()
        uimethods={
            "admin": self.admin
        }
        namespace.update(uimethods)
        return namespace
