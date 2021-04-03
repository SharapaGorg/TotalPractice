from Tools_rand import Identities

from bs4 import BeautifulSoup
import requests
import random

class perem:
    anime_list = ["Yuno", "Ayumu Kasuga Osaka", "Kiri Komori", "Asuka Soryu Langley", "Kotonoha Katsura", "Machi", "Rika Furude", "Ai Enma", "Nausicaä", "Yoko Littner", "Hitagi Senjougahara", "Ika Musume", "Rena Ryuuguu", "Anna Kurauchi", "Miyako", "Poplar Taneshima", "Akira Amatsume", "Himeko Katagiri", "Suiseiseki", "Hitoha Marui", "Ayumu Nishizawa", "Nadeko Sengoku", "Lum", "Aono Morimiya", "Shion Fujino", "Shiki Ryougi", "Lina Inverse", "Aoi Yamada", "Haruko Haruhara", "Yuki Nagato", "Kaede Fuyou", "Chiri Kitsu", "Ayumi Yamada", "Misaki Nakahara", "Megumi Noda", "Hanyuu Furude", "Kafuka Fuura", "Faye Valentine", "Tomoko Kuroki", "Tamaki Kawazoe", "Kino", "Ayu Tsukimiya", "Mion Sonozaki", "Excel", "Fuuko Ibuki", "Rin Kaga", "Kou", "Celty Sturluson", "Ana Coppola", "Nino", "Sayoko Kurosaki",
                "Tsukasa Hiiragi", "Guchuko", "Sun Seto", "Shouko Kirishima", "Balalaika", "Ukyo Kuonji", "Aika Granzchesta", "Nobue Itoh", "Rebecca Miyamoto", "Alice Carroll", "Isumi Saginomiya", "Ichijou", "Chizuru Minamoto", "Chiaki Minami", "Suigintou", "Marii Buratei", "Nano Shinonome", "Akari Akaza", "Murasaki Kuhouin", "Horo", "Konata Izumi", "Riza Hawkeye", "Sora Kajiwara", "Himeko Inaba", "Dorm Leader", "Risa Koizumi", "Sakaki", "Futaba Marui", "Satsuki Kitaoji", "Nori", "Nagisa Furukawa", "Mahoro Andou", "Rakka", "Chihiro Shindou", "Rei Ayanami", "Haruhi Fujioka", "Yuuko Ichihara", "Mai Kawasumi", "Maki Umezaki", "Tsuyuri", "Kana Minami", "Tsumugi Kotobuki", "Mamimi Samejima", "Olivier Mira Armstrong", "Nanami Aoyama", "Kuro Kagami", "Mashiro Shiina", "Yakumo Tsukamoto", "Matsurika Shinouji"]

    genders = ['Agender', 'Androgyne', 'Androgynous', 'Bigender', 'Cis', 'FTM', 'Gender Fluid', 'Gender Nonconforming', 'Gender Questioning',
            'Gender Variant', 'Genderqueer', 'Neither', 'Neutrois', 'Non-binary', 'Other', 'Pangender', 'Two-spirit', 'Anongender', 'Cavusgender',
            'Zodiacgender', 'Aesthetgender', 'Affectugender', 'Digigender', 'Egogender']

    da_net = ["Да", "Нет"]

def Genders(*args):
    res = perem.genders
    
    if len(args) != 0:
        return random.choice(res)
    else:  
        return res

def RandomStations(*args):
    resp = requests.get("http://www.metro.ru/stations/codes/").text
    
    _soup = BeautifulSoup(resp, "lxml")
    
    _text, res = _soup.find_all("td"), list()
    
    for i in range(len(_text)):
        if (i + 1) % 3 != 0:
            res.append(str(_text[i]).replace("<td>", "").replace("</td>", ""))
        
    if len(args) != 0:
        return random.choice(res)
    else:
        return res                                              
    
def RandomWords(*args):
    url = "https://klavogonki.ru/vocs/203/"

    spl1 = "<div class=words>"
    spl2 = "</table>"
    spl3 = "<table cellspacing=0 cellpadding=0>"
    c = requests.get(url)
    text = c.text
    list_ = []
    text = text.split(spl1)[1]
    text = text.split(spl2)[0]
    text = text.split(spl3)[1]

    for i in text.split("\n"):
        if len(i) < 3:
            continue
        elif "алый" in i:
            break

        list_.append(i.strip().split(">")[2].split("<")[0] )          
        
    if len(args) != 0:
        return random.choice(list_)
    else:
        return list_         
    
def RandomRes(qan = 5):
    gl_list = list()
    
    for i in Identities.AnimeNames():
        gl_list.append(i)

    for j in RandomWords():
        gl_list.append(j)
    
    res = str()
    
    if qan == 0:
        for i in range(random.randint(4, 70)):
            res += random.choice(gl_list)
            res += ' '
    else:    
        for i in range(qan):
            res += random.choice(gl_list)
            res += ' '
    
    return res