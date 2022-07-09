# path server = /programming/python/kivy/server-api
import kivy
from kivy.app import App
from kivy.uix.button import Button
import requests
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.screen import Screen
from kivy.uix.popup import Popup
from kivymd.toast import toast

class Main(MDApp):

    def build(self):
        bld = Builder.load_file("styles/test_api.kv")
        return bld

    def get_count(self):
        row = requests.get('http://localhost:8000/api/count').json()
        
        return row['count']

    def post_data(self):
        dataJson = {
            'city': self.root.ids.cityInput.text
        }
        store = requests.post('http://localhost:8000/api/city', json=dataJson)

        if store.status_code == 200:
            # popup = Popup(title='Popup', content=Label(text='Berhasil'),
            #   auto_dismiss=True)
            # popup.open()
            toast('Berhasil')
        else:
            toast('gagal, status code : 400')
    
    def put_data(self):
        dataJson = {
            'city': self.root.ids.cityInput.text
        }

        id = self.root.ids.cityID.text
        
        store = requests.put('http://localhost:8000/api/city/'+ id, json=dataJson)

        if store.status_code == 200:
            # popup = Popup(title='Popup', content=Label(text='Berhasil'),
            #   auto_dismiss=True)
            # popup.open()
            toast('Berhasil')
        else:
            toast('gagal, status code : 400')
    
    def destroy_data(self):
        id = self.root.ids.cityID.text
        store = requests.delete('http://localhost:8000/api/city/' + id)

        if store.status_code == 200:
            # popup = Popup(title='Popup', content=Label(text='Berhasil'),
            #   auto_dismiss=True)
            # popup.open()
            toast('Berhasil')
        else:
            toast('gagal, status code : 400')

    def load_data(self):
        store = requests.get('http://localhost:8000/api/city').json()

        list_data = []
        count = 0
        for item in store:
            # list_data.append({'id': item['id'], 'title': item['title']})
            count += item['id']
        return str(count)
    
    def data_set(self, count):
        return str(count)

if __name__ == '__main__':
    Main().run()