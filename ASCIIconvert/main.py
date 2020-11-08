import sys
import re

from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint 
from pyfiglet import figlet_format
import click

fonts = ['doh', 'isometric1', 'isometric2', 'isometric3', 'isometric4', 'ivrit', 'jazmine', 'italic',
         'jerusalem', 'katakana', 'kban', 'larry3d', 'lcd', 'letters', 'linux', 'lockergnome', 'madrid',
         'marquee', 'maxfour', 'mike', 'mini', 'mirror', 'mnemonic', 'morse', 'moscow', 'nancyj-fancy',
         'nancyj-underlined', 'nancyj', 'nipples', 'ntgreek', 'o8', 'ogre', 'pawp', 'peaks', 'pebbles', 'pepper',
         'poison', 'puffy', 'pyramid', 'rectangles', 'relief', 'relief2', 'rev', 'roman', 'rot13', 'rounded', 
         'rowancap', 'rozzo', 'runic', 'runyc', 'sblood', 'script', 'serifcap', 'shadow', 'short', 'slant',
         'slide', 'slscript', 'small', 'smisome1', 'smkeyboard', 'smscript', 'smshadow', 'smslant', 'smtengwar', 
         'speed', 'stampatello', 'standard', 'stellar', 'stop', 'straight', 'tanja', 'tengwar', 'term', 'thick',
         'threepoint', 'ticks', 'ticksslant', 'tinker-toy', 'tombstone', 'trek', 'tsalagi', 'twopoint','univers',
         'usaflag', 'weird', 'doh', 'hollywood', 'graffiti', 'gothic', 'goofy', 'fuzzy', 'fourtops', 'fender',
         'epic', 'eftiwater', 'eftiwall', 'eftitalic', 'eftirobot', 'eftipiti', 'eftifont', 'eftichess', 'drpepper',
         'dotmatrix', 'doom', 'doh', 'digital', 'diamond', 'cybersmall', 'cybermedium', 'cyberlarge', 'cricket', 
         'cosmike', 'cosmic', 'contrast', 'contessa', 'computer', 'colossal', 'coinstak', 'chunky', 'catwalk', 
         'caligraphy', 'calgphy2', 'bulbhead', 'bubble', 'block', 'binary', 'bigchief', 'big', 'bell', 'basic', 'barbwire',
         'banner4', 'banner3', 'banner3-D', 'banner', 'avatar', 'alphabet', 'alligator2', 'alligator', 'acrobatic', 
         '5lineoblique', '3x5', '3-d', 'starwars']

res = "hah"
font = "doh"

def SetRes(change, *args):
    f = open(__file__, 'r', encoding = "utf-8")
    
    regex = r'res\s*\=\s*\"(.*)\"'
    current = f.read()

    f.close()
    
    
    r = re.search(regex, current).group(1)
    
    current = current.replace(r, change)

    f = open(__file__, "w", encoding = "utf-8")
    f.write(current)
    f.close()

def SetFont(change):
    f = open(__file__, 'r', encoding = "utf-8")
    
    regex = r'font\s*\=\s*\"(.*)\"'
    current = f.read()

    f.close()
    
    
    r = re.search(regex, current).group(1)
    
    current = current.replace(r, change)

    f = open(__file__, "w", encoding = "utf-8")
    f.write(current)
    f.close()

@click.command()
@click.option("--font", default = ":0)", help = "Set font")
@click.option("--res", help = "Set desired title")
def main(res, font):
    if font != "help":
        for f in fonts:
            if font == f:
                SetFont(f)
    else:
        for i in range(len(fonts)):
            if i % 5 != 0:
                print(fonts[i], end = " ")
            else:
                print("")
                print(fonts[i], end = " ")
    
    if res:
        SetRes(res)
    else:
        SetRes("hah")
        
def Result():
    cprint(figlet_format(res, font=font),
        'yellow', 'on_red', attrs=['bold'])

Result()

if __name__ == "__main__":
    main()
    
