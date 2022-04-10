import PySimpleGUI as sg
import shutil
import os
import urllib.request
import math

url='https://github.com/TI0360/BER-PNGS/releases/latest/download/armor_png.zip'
save_name='armor_png.zip'

if os.path.exists("armor_png") == False:
    urllib.request.urlretrieve(url, save_name)
    shutil.unpack_archive('armor_png.zip', 'armor_png')
    os.remove('armor_png.zip')
else:
    pass

sg.theme('LightBlue')

layout = [
        [sg.Text('相手の装備', font=('Arial',20))],
        [sg.Button('', image_filename='armor_png\leather_helmet.png', key="elh"), sg.Button('', image_filename='armor_png\golden_helmet.png', key="egh"), sg.Button('', image_filename='armor_png\iron_helmet.png', key="eih"), sg.Button('', image_filename='armor_png\chainmail_helmet.png', key="ech"), sg.Button('', image_filename='armor_png\diamond_helmet.png', key="edh")],
        [sg.Button('', image_filename='armor_png\leather_chestplate.png', key="elc"), sg.Button('', image_filename='armor_png\golden_chestplate.png', key="egc"), sg.Button('', image_filename='armor_png\iron_chestplate.png', key="eic"), sg.Button('', image_filename='armor_png\chainmail_chestplate.png', key="ecc"), sg.Button('', image_filename='armor_png\diamond_chestplate.png', key="edc")],
        [sg.Button('', image_filename='armor_png\leather_leggings.png', key="ell"), sg.Button('', image_filename='armor_png\golden_leggings.png', key="egl"), sg.Button('', image_filename='armor_png\iron_leggings.png', key="eil"), sg.Button('', image_filename='armor_png\chainmail_leggings.png', key="ecl"), sg.Button('', image_filename='armor_png\diamond_leggings.png', key="edl")],
        [sg.Button('', image_filename='armor_png\leather_boots.png', key="elb"), sg.Button('', image_filename='armor_png\golden_boots.png', key="egb"), sg.Button('', image_filename='armor_png\iron_boots.png', key="eib"), sg.Button('', image_filename='armor_png\chainmail_boots.png', key="ecb"), sg.Button('', image_filename='armor_png\diamond_boots.png', key="edb")],
        [sg.Text('')],
        [sg.Text('自身の装備', font=('Arial',20))],
        [sg.Button('', image_filename='armor_png\leather_helmet.png', key="olh"), sg.Button('', image_filename='armor_png\golden_helmet.png', key="ogh"), sg.Button('', image_filename='armor_png\iron_helmet.png', key="oih"), sg.Button('', image_filename='armor_png\chainmail_helmet.png', key="och"), sg.Button('', image_filename='armor_png\diamond_helmet.png', key="odh")],
        [sg.Button('', image_filename='armor_png\leather_chestplate.png', key="olc"), sg.Button('', image_filename='armor_png\golden_chestplate.png', key="ogc"), sg.Button('', image_filename='armor_png\iron_chestplate.png', key="oic"), sg.Button('', image_filename='armor_png\chainmail_chestplate.png', key="occ"), sg.Button('', image_filename='armor_png\diamond_chestplate.png', key="odc")],
        [sg.Button('', image_filename='armor_png\leather_leggings.png', key="oll"), sg.Button('', image_filename='armor_png\golden_leggings.png', key="ogl"), sg.Button('', image_filename='armor_png\iron_leggings.png', key="oil"), sg.Button('', image_filename='armor_png\chainmail_leggings.png', key="ocl"), sg.Button('', image_filename='armor_png\diamond_leggings.png', key="odl")],
        [sg.Button('', image_filename='armor_png\leather_boots.png', key="olb"), sg.Button('', image_filename='armor_png\golden_boots.png', key="ogb"), sg.Button('', image_filename='armor_png\iron_boots.png', key="oib"), sg.Button('', image_filename='armor_png\chainmail_boots.png', key="ocb"), sg.Button('', image_filename='armor_png\diamond_boots.png', key="odb")],
        [sg.Text('')],
        [sg.Text('装備差ダメージ', font=('Arial',13))],
        [sg.Button('計算', key="end")],
        [sg.Text('')],
        [sg.Text('サキュバスで吸える体力', font=('Arial',13))],
        [sg.Text('最大体力　'), sg.InputText("", size=(10, 1), key="ehp")],
        [sg.Button('計算', key="send")],
        [sg.Text('')],
        [sg.Text('ランバージャック理論値', font=('Arial',13))],
        [sg.Text('攻撃人数　'), sg.InputText("", size=(10, 1), key="peo")],
        [sg.Text('攻撃時間　'), sg.InputText("", size=(10, 1), key="att")],
        [sg.Text('命中率　　'), sg.InputText("", size=(10, 1), key="pro")],
        [sg.Button('計算', key="lend")]
    ]
window = sg.Window('Annihilation Calc', layout, size=(230, 760), finalize=True)

eh = 0
ec = 0
el = 0
eb = 0

oh = 0
oc = 0
ol = 0
ob = 0

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == "lend":
        try:
            D = 40 * int(values["peo"]) * float(values["att"]) * float(values["pro"])
            sg.popup(f"与えることのできる耐久値へのダメージは{D}です。")
        except:
            sg.popup("入力されていない項目があります。")

    if event == "send":
        try:
            hp = float(values["ehp"]) * 0.3
            ohp = math.floor(hp)
            sg.popup(f"{ohp}HPならば吸収できます。")
        except:
            sg.popup("最大体力が入力されていません。")
            
    if event == "elh":
        eh = 1

    if event == "egh":
        eh = 2

    if event == "eih":
        eh = 2
    
    if event == "ech":
        eh = 2

    if event == "edh":
        eh = 3
    
    if event == "elc":
        ec = 3

    if event == "egc":
        ec = 5

    if event == "eic":
        ec = 6

    if event == "ecc":
        ec = 5

    if event == "edc":
        ec = 8

    if event == "ell":
        el = 2

    if event == "egl":
        el = 3

    if event == "eil":
        el = 5

    if event == "ecl":
        el = 4

    if event == "edl":
        el = 6
    
    if event == "elb":
        eb = 1

    if event == "egb":
        eb = 1

    if event == "eib":
        eb = 2

    if event == "ecb":
        eb = 1

    if event == "edb":
        eb = 3

    
    if event == "olh":
        oh = 1

    if event == "ogh":
        oh = 2

    if event == "oih":
        oh = 2
    
    if event == "och":
        oh = 2

    if event == "odh":
        oh = 3
    
    if event == "olc":
        oc = 3

    if event == "ogc":
        oc = 5

    if event == "oic":
        oc = 6

    if event == "occ":
        oc = 5

    if event == "odc":
        oc = 8

    if event == "oll":
        ol = 2

    if event == "ogl":
        ol = 3

    if event == "oil":
        ol = 5

    if event == "ocl":
        ol = 4

    if event == "odl":
        ol = 6
    
    if event == "olb":
        ob = 1

    if event == "ogb":
        ob = 1

    if event == "oib":
        ob = 2

    if event == "ocb":
        ob = 1

    if event == "odb":
        ob = 3
    
    if event == "end":
        oout = oh + oc + ol + ob
        eout = eh + ec + el + eb
        ber = (eout - oout) / 2.5
        sg.popup(f"追加ダメージは{ber}ダメージです。")
        eh = 0
        ec = 0
        el = 0
        eb = 0
        oh = 0
        oc = 0
        ol = 0
        ob = 0
    
window.close()

'''
Copyright © 2001-2021 Python Software Foundation; All Rights Reserved

© Copyright 2021 PySimpleGUI

https://github.com/TI0360/anni-calc/tree/main

[LGPL3]
https://github.com/TI0360/anni-calc/blob/main/LICENCE
'''