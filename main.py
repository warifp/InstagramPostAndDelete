#! @@Author : WAHYU ARIF PURNOMO
#! @@Create : 18 Januari 2019
#! @@Modify : 19 Januari 2019
#! Gambar dari reddit.
#! Gunakan VPN karena DNS situs reddit sudah di blokir dari negara Indonesia.

import os
import json
import requests
import progressbar
from PIL import Image
from lxml import html
from time import sleep
from ImageDeleter import delete_png
from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI(input("Username: "), input("Password: "))
while True:
    if (InstagramAPI.login()):
        break
    else:
        for x in range(300):
            os.system('cls')
            print(300-x)
            sleep(1)
global useable
useable = []
os.system('pause')

def get_image():
    print("Memulai mendapatkan gambar ..")
    json_raw = requests.get('https://www.reddit.com/r/me_irl/new/.json', headers = {'User-agent': 'Image_Testing_V3'}).json()
    json_data = json_raw['data']
    json_children = json_data['children']
    for x in range(len(json_children)):
        json_current = json_children[x]
        json_current_data = json_current['data']
        json_current_url = json_current_data['url']
        if "https://i.redd.it/" not in json_current_url:
            pass
        else:
            if json_current_url not in useable:
                useable.append(json_current_url)
                download()
            else:
                pass

def download():
    print("Memulai download ..")
    global filename
    new_filename = ""
    filename = useable[-1]
    filename = filename.replace("https://i.redd.it/", "")
    print(filename)
    f = open(filename, 'wb')
    f.write(requests.get(useable[-1]).content)
    f.close()
    if (filename[-3] + filename[-2] + filename[-1]) != 'jpg':
        im = Image.open(filename)
        for x in range(len(filename)-3):
            new_filename = new_filename + filename[x]
        im = im.convert("RGB")
        im.save("edit" + new_filename + 'jpg')
        new_filename = "edit" + new_filename + "jpg"
        print(new_filename)
    else:
        new_filename = filename
    upload(new_filename)

def delete_image(bad_file):
    print("Memulai menghapus gambar ..")
    if (bad_file[0] + bad_file[1] + bad_file[2] + bad_file[3]) == "edit":
        png_bad_file = ''
        for x in range(len(bad_file)-3):
            png_bad_file = png_bad_file + bad_file[x]
        png_bad_file = png_bad_file + "png"
        try:
            os.remove(png_bad_file)
        except Exception as e:
            pass
    os.remove(bad_file)
    delete_png()
    print("Selesai.")
    wait()

def upload(file):
    print("Memulai upload ..")
    caption = ""
    InstagramAPI.uploadPhoto(file, caption=caption)
    delete_image(file)

def wait():
    for i in progressbar.progressbar(range(1800)):
        sleep(1)

while True:
    get_image()
    print("Gambar sukses di upload.")
    sleep(5)
    os.system('pause')
