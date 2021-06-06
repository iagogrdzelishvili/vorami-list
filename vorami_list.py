"""ათწლეულების განმავლობაში უამრავი ბავშვი "ჩაჭრა" შეკითხვამ
იმის შესახებ თუ "კაი ბიჭების" რომელ სიაში ეწერენ.
და აი დადგა ნანატრი მომენტიც,
 უკვე არსებობს არა მხოლოდ კაი ბიჭების, არამდედ ქურდების სიაც.
ამ კოდით კი გთავაზობთ მციერე ამონარიდს "ქურდების" იმ სიიდან რომელიც,
 რუსულ საიტზე, primecrime.ru-ზეა განთავსებული"""


import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint

f = open('vorami_list.csv', 'w', encoding='utf-8_sig')
heading = 'ქურდების სია'
f.write(heading)
ind = 1
while ind < 600:
    URL = 'https://www.primecrime.ru/characters/nationality/?nationality=%E3%F0%F3%E7%E8%ED&sort=fio&order=asc&page='+ str(ind)
    r = requests.get(URL)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    gruzini = soup.find_all('tr', {'class': 'ntrt'})

    for varami in gruzini:
        vor_info = varami.a.text
        print(vor_info)
        f.write(vor_info)

    ind += 100
    sleep(randint(15, 20))
