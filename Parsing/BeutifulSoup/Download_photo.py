import requests
from bs4 import BeautifulSoup

image_number = 0
strong_number = 1
link = "https://zastavok.net/"

response = requests.get(f'{link}/{strong_number}').text
soup = BeautifulSoup(response, 'lxml')

block = soup.find('div', class_='block-photo')
all_image = soup.find_all('div', class_='short_full')

for image in all_image:
    # Find link
    image_link = image.find('a').get('href')
    download_storage = requests.get(f'{link}{image_link}').text
    download_soup = BeautifulSoup(download_storage, 'lxml')
    download_block = download_soup.find(
        'div', class_='image_data').find(
        'div', class_='block_down')
    result_link = download_block.find('a').get('href')

    # Download photo
    image_bytes = requests.get(f'{link}{result_link}').content

    # bite string
    with open(f'image/{image_number}.jpg', 'wb') as file:
        file.write(image_bytes)
    image_number += 1
    print("Изображение успешно скачано")
