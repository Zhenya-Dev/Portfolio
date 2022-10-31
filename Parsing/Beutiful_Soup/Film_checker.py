import requests
from bs4 import BeautifulSoup

# Variables by which the program enters the site
url = "https://uakino.club"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79',
    'accept': '*/*'}

# We give a request for which specifically he will enter
r = requests.get(url=url, headers=headers)

# Passing the request to the framework
soup = BeautifulSoup(r.text, 'lxml')

# write find or get to search
soup_all = soup.find('div', class_='movie-item short-item')

soup_title = soup_all.find('a', class_='movie-title')


data = []
header = ['Movie title', 'Video resolution', 'Rating', 'Genre', 'Year']
tab_counter = 1

for i in range(3):
    url = f'https://uakino.club/page/{tab_counter}/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79',
        'accept': '*/*'}
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, 'lxml')

    Soup_all = soup.find_all('div', class_='movie-item short-item')

    for soup_all in Soup_all:
        soup_title = soup_all.find('a', class_='movie-title')

        soup_link = soup_title.get('href')
        print("Link", soup_link)
        soup_name = soup_all.find('div', class_='deck-title').text
        print('Title', soup_name)
        soup_about = soup_all.find('span', class_='desc-about-text').text
        print('Review', soup_about)
        soup_qual = soup_all.find('div', class_='full-quality').text
        print('Video resolution', soup_qual)
        soup_many = soup_all.find('div', class_='movie-desc')\
            .find_all('div', class_='deck-value')
        head_many = ['Rating', 'Genre', 'Year', 'Actors']
        Head_many = dict(zip(head_many, soup_many))
        data.append([soup_name, soup_about, soup_qual])

        for i in Head_many.items():
            print(i[0], i[1].text)
        print('\n')
        data.append([soup_name, soup_qual, soup_many[0].text,
                    soup_many[1].text, soup_many[2].text])
    tab_counter += 1
    print('\n' * 3)
    print(f' Browser page {tab_counter}')
print(data)
