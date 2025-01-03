from fake_useragent import FakeUserAgent
from requests import get
from bs4 import BeautifulSoup

url = 'http://www.insecam.org/en/jsoncountries/'
headers = {'User-Agent': FakeUserAgent().random}
countries = get(url=url, headers=headers).json()
if countries.get('status') == 'success':
    country = countries.get('countries')
    for key, value in country.items():
        print(f'Код: [{key}] - {value.get('country')} / ({value.get('count')})')

    user_choice = input('Введите код выбранной вами страны (регистр не учитывается): ').upper()
    page_code = get(url=f'http://www.insecam.org/en/bycountry/{user_choice}', headers=headers).text

    soup = BeautifulSoup(page_code, 'lxml')
    count_of_pages = soup.find(name='ul', class_='pagination').find('script').text.strip().split(', ')[1]
    for page in range(int(count_of_pages)):
        page_code = get(url=f'http://www.insecam.org/en/bycountry/{user_choice}/?page={page}', headers=headers).text
        soup = BeautifulSoup(page_code, 'lxml')
        ips = soup.find_all(class_='thumbnail-item__img img-responsive')
        with open(file=f'{user_choice}.txt', mode='a', encoding='utf-8') as file:
            for ip in ips:
                file.write(f'http://{ip.get('src').split('/')[2]}\n')
    print(f'Список IP-адресов был сохранён в файл {user_choice}.txt')
    # Hello from author
