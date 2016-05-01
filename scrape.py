#lol code
master_list = []
l = {}
import requests
import lxml.html
from lxml.cssselect import CSSSelector
counter=0
while counter < 30:#only 30 pages
    counter+=1
    print('Page',counter)
    lolcount = str(counter).zfill(2)
    theurl = "http://www.samair.ru/proxy/ip-address-{0}.htm".format(lolcount)
    print(theurl)
    r = requests.get(theurl)# get some html
    for x, line in enumerate(r.iter_lines()):
        if '/styles/' in str(line):
            print(x,line)
            print(line)
            derp = str(line)
            desu = derp.split('"')#get the css url
            print(desu[3])
            css = "http://www.samair.ru"+desu[3]
            break
    got_css = requests.get(css)
    CSS2 = got_css.text[:-1]#create seperate,usable variable
    for K, f in enumerate(CSS2.split('\n')):
        f = f.replace(":after {content:",",").replace(
            "}","").replace('"','').replace(#'makes the css more 'usable'
                "\n", '').replace("'", '').replace('b', '')
        x,y = f.split(',')#splits ports and html tags
        l[K] = x#list of tags in order
        K = str(K)+'A'
        l[K] = y#list of ports in order
    tree = lxml.html.fromstring(r.text)#DOM Tree
    for x in range(int(len(l)/2)):\
        sel = CSSSelector('span'+l[x])#create selector
        results = sel(tree)#match all 'css' tags
        x2 = str(x)+'A'
        data = [result.text +l[x2] for result in results if result != []]#list all matches
        master_list.extend(data)
        if data != []:
            print(data)
print(len(master_list), ' proxies saved.')
for proxy in master_list:
        with open("working.txt", "a") as myfile:
            myfile.write("{0}\n".format(proxy))
