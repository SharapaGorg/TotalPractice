import random
import json

import requests
from bs4 import BeautifulSoup

class perem:
    anime_list = ["Yuno", "Ayumu Kasuga Osaka", "Kiri Komori", "Asuka Soryu Langley", "Kotonoha Katsura", "Machi", "Rika Furude", "Ai Enma", "Nausicaä", "Yoko Littner", "Hitagi Senjougahara", "Ika Musume", "Rena Ryuuguu", "Anna Kurauchi", "Miyako", "Poplar Taneshima", "Akira Amatsume", "Himeko Katagiri", "Suiseiseki", "Hitoha Marui", "Ayumu Nishizawa", "Nadeko Sengoku", "Lum", "Aono Morimiya", "Shion Fujino", "Shiki Ryougi", "Lina Inverse", "Aoi Yamada", "Haruko Haruhara", "Yuki Nagato", "Kaede Fuyou", "Chiri Kitsu", "Ayumi Yamada", "Misaki Nakahara", "Megumi Noda", "Hanyuu Furude", "Kafuka Fuura", "Faye Valentine", "Tomoko Kuroki", "Tamaki Kawazoe", "Kino", "Ayu Tsukimiya", "Mion Sonozaki", "Excel", "Fuuko Ibuki", "Rin Kaga", "Kou", "Celty Sturluson", "Ana Coppola", "Nino", "Sayoko Kurosaki",
                "Tsukasa Hiiragi", "Guchuko", "Sun Seto", "Shouko Kirishima", "Balalaika", "Ukyo Kuonji", "Aika Granzchesta", "Nobue Itoh", "Rebecca Miyamoto", "Alice Carroll", "Isumi Saginomiya", "Ichijou", "Chizuru Minamoto", "Chiaki Minami", "Suigintou", "Marii Buratei", "Nano Shinonome", "Akari Akaza", "Murasaki Kuhouin", "Horo", "Konata Izumi", "Riza Hawkeye", "Sora Kajiwara", "Himeko Inaba", "Dorm Leader", "Risa Koizumi", "Sakaki", "Futaba Marui", "Satsuki Kitaoji", "Nori", "Nagisa Furukawa", "Mahoro Andou", "Rakka", "Chihiro Shindou", "Rei Ayanami", "Haruhi Fujioka", "Yuuko Ichihara", "Mai Kawasumi", "Maki Umezaki", "Tsuyuri", "Kana Minami", "Tsumugi Kotobuki", "Mamimi Samejima", "Olivier Mira Armstrong", "Nanami Aoyama", "Kuro Kagami", "Mashiro Shiina", "Yakumo Tsukamoto", "Matsurika Shinouji"]

    genders = ['Agender', 'Androgyne', 'Androgynous', 'Bigender', 'Cis', 'FTM', 'Gender Fluid', 'Gender Nonconforming', 'Gender Questioning',
            'Gender Variant', 'Genderqueer', 'Neither', 'Neutrois', 'Non-binary', 'Other', 'Pangender', 'Two-spirit', 'Anongender', 'Cavusgender',
            'Zodiacgender', 'Aesthetgender', 'Affectugender', 'Digigender', 'Egogender']

    da_net = ["Да", "Нет"]

def random_names(*args):
    resp = requests.get("https://kakzovut.ru/man.html").text
    _soup = BeautifulSoup(resp, "lxml")

    res = list()

    for i in _soup.find_all("div", {
        "class" : "nameslist"
    }):
        _st = str(i).find('.html">')
        _end = str(i).find('</a>')
        
        res.append(str(i)[_st + 7:_end])
        
    resp = requests.get("https://imena-znachenie.ru/imena/polskie/").text
    _soup = BeautifulSoup(resp, "lxml")
        
    if len(args) == 0:
        return res
    else:
        return random.choice(res)
        
def random_surnames(*args):
    resp = requests.get("http://imja.name/familii/pyatsot-chastykh-familij.shtml").text
    _soup = BeautifulSoup(resp, "lxml")
    
    res = list()
    
    for i in _soup.find_all("td",
                        {
                            "class" : "topin1"
                        }):
        _st = str(i).find('">')
        _end = str(i).find("</td>")
        
        res.append(str(i)[_st + 2: _end])
          
    res.sort(key = lambda x: x[0])
    res.remove(res[0]) 
    
    if len(args) == 0:
        return res
    else:   
        return random.choice(res)
        
def random_patronymic(*args):
    resp = requests.get("https://surnameonline.ru/patronymic-male.html").text
    _soup = BeautifulSoup(resp, "lxml")
    
    res = list()

    for i in _soup.find_all("li"):
        _st = str(i).find('html">')
        _end = str(i).find('</a>')
        
        
        res.append(str(i)[_st + 6: _end])
        
    if len(args) == 0:
        return res
    else:
        return random.choice(res)
    
def random_eng_names(*args):
    resp = requests.get("http://www.english-source.ru/english-linguistics/english-lexis/148-english-names").text
    _soup = BeautifulSoup(resp, "lxml")
    
    res = list()
    
    res = _soup.find_all("td")
    
    for l in range(len(res)):
        res[l] = str(res[l])
    
    out = list()
    
    for i in res:
       if "<br/>" in i:
           out.append(i.replace('<td colspan="1" style="text-align: center;">', '').replace('<td style="text-align: center;">', '').replace("<br/>", '').replace("</td>", ""))

    for name in range(len(out)):
        out[name] = out[name].replace("\r", "").replace("\n", "").replace("\t", "")    
       
    _out = list()   
        
    for i in range(len(out)):
        perem = str(out[i][0])
        out[i] = out[i].split(out[i][0])    
        
        for k in range(len(out[i])):
            out[i][k] = perem + out[i][k]
            _out.append(out[i][k])
                   
    for name in _out:
        if len(name) == 1:
            _out.remove(name)
            
    if len(args) != 0:
        return random.choice(_out)
    else:
        return _out
    
def FIO():
    fio = random_surnames("...") + " "\
        + random_names("...") + " "\
        + random_patronymic("...")

    return fio

def AnimeNames(*args):
    res = perem.anime_list
    
    if len(args) != 0:
        return random.choice(res)
    else:  
        return res