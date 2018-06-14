from requests_html import HTMLSession
session = HTMLSession()
import csv

my_domain = input('your domain: ')
kw_file = input('Name of your file: ')




def file(filename):
    with open(f'{filename}', 'r+') as f:
        kw_list = [x.strip() for x in f.readlines()]
        print(kw_list)
    for kw in kw_list:
        resp = session.get(f'https://www.google.com/search?q={kw}&num=100&hl=en')
        links = resp.html.xpath('//h3/a/@href')
        # domains = [x.split('/')[2] for x in links if 'http' in x]

        with open('result.csv', 'a') as res:
            for c, lnk in enumerate(links, 1):
                    if my_domain in lnk:
                        row = [c, kw, my_domain, lnk]
                        writer = csv.writer(res, delimiter =',')
                        writer.writerow(row)

file(kw_file)