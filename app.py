import os
from bottle import route, run, static_file, request, error

@route("/")
def index():
    return "<!DOCTYPE html><html><head><meta charset='UTF-8'><title>RIKKA ER CRACK QUEEN</title><link rel='SHORTCUT ICON' href='rikka.ico' type='image/x-icon' /><link rel='ICON' href='rikka.ico' type='image/ico' /><style type='text/css'>html{background-color:#ff69b4;font-family: 'Oswald', sans-serif;font-size: 48px;text-align: center;}.bye{height: 500px;width: 790px;}</style></head><body><h1>OMG RIKKA ER QUEEN SEM REYKIR CRACK COCAIN XD</h1><img src='/static/crackew.jpg'><h2>SHE IS VERY GOOD WITH CARS</h2><img class='bye' src='/static/bye.jpg'></body></html>"

@route("/static/<filename>")
def server_static(filename):
    return static_file(filename, root="")
run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
