# -*- coding: utf-8 -*- 
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def prepare(self):
        if not self.request.uri.startswith(self.get_login_url()) and self.current_user is  None:
            self.redirect(self.get_login_url())

    def get_current_user(self):
        user_cookie = self.get_cookie("anju_user")
        if user_cookie:
            return user_cookie
        return None

    def admin(self):
	return ['adminaas']

    def get_template_namespace(self):
        namespace = {}
        namespace = super(BaseHandler,self).get_template_namespace()
        uimethods={
            "admiisssn": self.admin
        }
        namespace.update(uimethods)
        return namespace
