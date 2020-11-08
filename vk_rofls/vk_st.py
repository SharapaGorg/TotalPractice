import re
import requests
from lxml import html
from LogPython import LogManager; LogManager = LogManager()
from bs4 import BeautifulSoup
from config import settings
import vk_api

_session = vk_api.VkApi(login = settings['email'], password = settings['password'])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language':'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate, br',
    'Connection':'keep-alive',
    # 'DNT':'1',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'navigate',       
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'iframe',
    'Referer': 'https://vk.com/',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}
###########################################################
session = requests.Session()
url = 'https://login.vk.com/?act=login'

auth_response = session.get(url, headers = headers, verify=False)

f23 = open('main.txt', 'w', encoding='utf-8')
f23.write(auth_response.text)

_soup = BeautifulSoup(auth_response.text, 'lxml')

act = _soup.find('input', {
        'name' : 'act', 
        'id' : "act"
    }).attrs['value']

role = _soup.find('input', {
        'name' : 'role',
}).attrs['value']

expire = _soup.find('input', {
        'name' : 'expire'
        # 'id' : 'index_expire_input'
}).attrs['value']

_origin = _soup.find('input', {
        'name' : '_origin'
}).attrs['value']

ip_h = _soup.find('input', {
        'name' : 'ip_h'
}).attrs['value']

ig_h = _soup.find('input', {
    'name' : 'lg_h'
}).attrs['value']

to = _soup.find('input', {
    'name' : 'to'
}).attrs['value']

# email = _soup.find('input', {
#     'name' : 'email',
#     'id' : 'index_email'
# }).attrs['value']

# password = _soup.find('input', {
#     'name' : 'pass',
#     'id' : 'index_pass'
# })

a = session.post('https://login.vk.com/?act=login', data = {'act' : act, 
                                                            'role' : role,
                                                            'expire' : '',
                                                            '_origin' : _origin,
                                                            'ip_h' : ip_h,
                                                            'ig_h' : ig_h,
                                                            'to' : 'aW5kZXgucGhw',
                                                            'email' : settings['email'],
                                                            'pass' : settings['password']}, headers = headers, verify=False)

output = open('auth.txt', 'w', encoding = "utf-8")

output.write(a.text)

###########################################################

response = session.get('https://vk.com/' + input(), headers = headers, verify=False)

parsed_body = html.fromstring(response.text)

f = open('output.txt', 'w', encoding = "utf-8")


# regex = r"settings\s*\=\s*\{\s*\'TOKEN\'\s*:\s*\'(.*)\'\w*\, 'PREFIX': 'ShG_site_default_prefix'}"

regex = r'<span class="pp_last_activity_text">'

print(response.text, file = f)
LogManager.debug(parsed_body.xpath(".//div[@class=profile_online_lv]/text()"))

fr = open('output.txt', 'r', encoding = "utf-8").read()

if '<span class="pp_last_activity_text">Online</span>' in response.text:
    LogManager.warning('User Online')
elif '<span class="pp_last_activity_text">' in response.text:
    LogManager.warning('User Offline [lxml]')

soup = BeautifulSoup(fr, 'lxml')

res = str()

for i in soup.text:
    res += i

resp, res = str(soup.title).replace('<title>', '').replace("</title>", "").split(), res.replace('\n', ' ').split()

for i in range(len(res)):
    if res[i] == 'заходил' or res[i] == 'заходила':
        LogManager.warning("User offline [bs4]")
    elif res[i] == 'online':
        LogManager.warning("User online [bs4]")

LogManager.info(*resp)
LogManager.info(res)

#<span class="pp_last_activity_text">