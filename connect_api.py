# path server = /programming/python/kivy/server-api
import json
from urllib import response
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
import numpy as np
# from sklearn.svm import SVR

class Main(MDApp):

    def build(self):
        bld = Builder.load_file("styles/connect_api.kv")
        return bld

    def get_data(self):
        # prob kelas
        prob = self.probabilitas_kelas()

        # permintaan
        permintaan_naik = self.sort_permintaan('naik')
        permintaan_tetap = self.sort_permintaan('tetap')
        permintaan_turun = self.sort_permintaan('turun')

        # ketersediaan
        ketersediaan_naik = self.sort_ketersediaan('naik')
        ketersediaan_tetap = self.sort_ketersediaan('tetap')
        ketersediaan_turun = self.sort_ketersediaan('turun')

        # Harga
        harga_naik = self.sort_harga('naik')
        harga_tetap = self.sort_harga('tetap')
        harga_turun = self.sort_harga('turun')

        # sample data
        x_permintaan = 8920
        x_ketersediaan = 3769
        x_harga = 19000
        x_berita = ''

        # prob permintaan [x = naik, y = tetap, z = turun]
        x_prob_permintaan = 1/np.sqrt(2*3.14*permintaan_naik['stdev']) * np.exp(-(pow(x_permintaan-permintaan_naik['mean'], 2))/(pow(permintaan_naik['stdev'], 2)))
        y_prob_permintaan = 1/np.sqrt(2*3.14*permintaan_tetap['stdev']) * np.exp(-(pow(x_permintaan-permintaan_tetap['mean'], 2))/(pow(permintaan_tetap['stdev'], 2)))
        z_prob_permintaan = 1/np.sqrt(2*3.14*permintaan_turun['stdev']) * np.exp(-(pow(x_permintaan-permintaan_turun['mean'], 2))/(pow(permintaan_turun['stdev'], 2)))
        
        print('PROBABILITAS PERMINTAAN')
        print(x_prob_permintaan)
        print(y_prob_permintaan)
        print(z_prob_permintaan)

        # prob ketersediaan [x = naik, y = tetap, z = turun]
        x_prob_ketersediaan = 1/np.sqrt(2*3.14*ketersediaan_naik['stdev']) * np.exp(-(pow(x_ketersediaan-ketersediaan_naik['mean'], 2))/(pow(ketersediaan_naik['stdev'], 2)))
        y_prob_ketersediaan = 1/np.sqrt(2*3.14*ketersediaan_tetap['stdev']) * np.exp(-(pow(x_ketersediaan-ketersediaan_tetap['mean'], 2))/(pow(ketersediaan_tetap['stdev'], 2)))
        z_prob_ketersediaan = 1/np.sqrt(2*3.14*ketersediaan_turun['stdev']) * np.exp(-(pow(x_ketersediaan-ketersediaan_turun['mean'], 2))/(pow(ketersediaan_turun['stdev'], 2)))
        
        print('\nPROBABILITAS KETERSEDIAAN')
        print(x_prob_ketersediaan)
        print(y_prob_ketersediaan)
        print(z_prob_ketersediaan)

        # prob harga [x = naik, y = tetap, z = turun]
        x_prob_harga = 1/np.sqrt(2*3.14*harga_naik['stdev']) * np.exp(-(pow(x_harga-harga_naik['mean'], 2))/(pow(harga_naik['stdev'], 2)))
        y_prob_harga = 1/np.sqrt(2*3.14*harga_tetap['stdev']) * np.exp(-(pow(x_harga-harga_tetap['mean'], 2))/(pow(harga_tetap['stdev'], 2)))
        z_prob_harga = 1/np.sqrt(2*3.14*harga_turun['stdev']) * np.exp(-(pow(x_harga-harga_turun['mean'], 2))/(pow(harga_turun['stdev'], 2)))
        
        print('\nPROBABILITAS HARAG')
        print(x_prob_harga)
        print(y_prob_harga)
        print(z_prob_harga)

        # hasil klasifikasi [x = naik, y = tetap, z = turun]
        x_klasifikasi = x_prob_permintaan*x_prob_ketersediaan*x_prob_harga*prob['naik']
        y_klasifikasi = y_prob_permintaan*y_prob_ketersediaan*y_prob_harga*prob['tetap']
        z_klasifikasi = z_prob_permintaan*z_prob_ketersediaan*z_prob_harga*prob['turun']

        print('\nHASIL KLASIFIKASI')
        print('{0:.12f}'.format(x_klasifikasi))
        print('{0:.12f}'.format(y_klasifikasi))
        print('{0:.12f}'.format(z_klasifikasi))

        hasil_klasifikasi = 0

        if x_klasifikasi > y_klasifikasi and x_klasifikasi > z_klasifikasi:
            x_berita = 'naik'
            hasil_klasifikasi = x_klasifikasi
        if y_klasifikasi > x_klasifikasi and y_klasifikasi > z_klasifikasi:
            x_berita = 'tetap'
            hasil_klasifikasi = y_klasifikasi
        if z_klasifikasi > x_klasifikasi and z_klasifikasi > y_klasifikasi:
            x_berita = 'turun'
            hasil_klasifikasi = z_klasifikasi
        
        print('\nMAKA HASILNYA')
        print('BERITA : ' + x_berita)
        print('ANGKA  : ' + '{0:.12f}'.format(hasil_klasifikasi))
        print('\nSAMPLE DATA')
        print('Permintaan (KG)   : ', x_permintaan, ' atau ', (x_permintaan/1000), ' ton')
        print('Ketersediaan (KG) : ', x_ketersediaan, ' atau ', (x_ketersediaan/1000), ' ton')

        return x_berita

    def probabilitas_kelas(self):
        store = requests.get('http://localhost:8000/api/dataset/probabilitas_kelas').json()

        list_data = {
            'naik': store['naik'],
            'tetap': store['tetap'],
            'turun': store['turun']
        }

        return list_data

    def get_all(self):
        response = requests.get('http://localhost:8000/api/dataset').json()
        
        # print(data)
        # return list_data
        # print(list_data)
    
    def sort_permintaan(self, params):
        store = requests.get('http://localhost:8000/api/dataset/sort_permintaan/' + params).json()

        list_data = {
            'total': store['total'],
            'count': store['count'],
            'total_pangkat_2': store['total_pangkat_2'],
            'count_pangkat_2': store['count_pangkat_2'],
            'mean': store['mean'],
            'stdev': store['stdev'],
            'berita': store['berita'],
        }

        return list_data
    
    def sort_ketersediaan(self, params):
        store = requests.get('http://localhost:8000/api/dataset/sort_ketersediaan/' + params).json()

        list_data = {
            'total': store['total'],
            'count': store['count'],
            'total_pangkat_2': store['total_pangkat_2'],
            'count_pangkat_2': store['count_pangkat_2'],
            'mean': store['mean'],
            'stdev': store['stdev'],
            'berita': store['berita'],
        }

        return list_data
    
    def sort_harga(self, params):
        store = requests.get('http://localhost:8000/api/dataset/sort_harga/' + params).json()

        list_data = {
            'total': store['total'],
            'count': store['count'],
            'total_pangkat_2': store['total_pangkat_2'],
            'count_pangkat_2': store['count_pangkat_2'],
            'mean': store['mean'],
            'stdev': store['stdev'],
            'berita': store['berita'],
        }

        return list_data

if __name__ == '__main__':
    Main().run()