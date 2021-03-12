import requests
import os
TOKEN = ''

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        response = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources/upload',
                                params={'path': f'{os.path.basename(file_path)}'},
                                headers={'Authorization': f'OAuth {TOKEN}'})
        print(response.status_code)
        href = response.json()['href']
        with open(file_path) as f:
            requests.put(href, files={'file': f})

if __name__ == '__main__':
  uploader = YaUploader(TOKEN)
  result = uploader.upload(r'c:\my_folder\file.txt')


