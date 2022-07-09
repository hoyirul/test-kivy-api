# https://jsonplaceholder.typicode.com/posts
import kivy
from kivy.network.urlrequest import UrlRequest
from kivy.app import App
# from kivy.properties import ObjectProperty
from kivy.uix.label import Label

class Main(App):
    def build(self):
        req = UrlRequest('https://jsonplaceholder.typicode.com/posts', self.got_json)
        return req
    
    def got_json(self, req):
        for key, value in req.resp_headers.items():
            print('{}: {}'.format(key, value))

if __name__ == '__main__':
    Main().run()