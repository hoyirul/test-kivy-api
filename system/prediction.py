import requests
from base_url import base_url

def probabilitas_kelas(self):
    store = requests.get(base_url + 'dataset/probabilitas_kelas').json()

    list_data = {
        'naik': store['naik'],
        'tetap': store['tetap'],
        'turun': store['turun']
    }

    return list_data