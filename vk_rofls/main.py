import requests

def online(id):
    url = "https://vk.com/" + id
    split_online1 ='<span class="pp_last_activity_text">'
    split_online2 = '<'
    text = requests.get(url).text
    text = text.split(split_online1)[1].split(split_online2)[0]
    boolOnline = False
    if text.lower() == "online":
      boolOnline = True
    return text, boolOnline

print(online('id359925115'))