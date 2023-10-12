import requests
from bs4 import BeautifulSoup
import fake_headers

if __name__ == '__main__':
    url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'
    headers_gen = fake_headers.Headers(browser='opera', os='win')
    response = requests.get(url=url, headers=headers_gen.generate())
    html_data = response.text

    vacancy = BeautifulSoup(html_data, features='lxml')

    article_tags = vacancy.find('main', class_='vacancy-serp-content')
    article_list = article_tags.find_all('div', class_='serp-item')
    counter = 0

    for article_tag in article_list:
        counter += 1
        if counter < 3:
            continue
        header_text = article_tag.find('a', class_='serp-item__title')
        text = header_text.text
        print(text)

        link = header_text['href']
        print(link)

        my_response = requests.get(url=link, headers=headers_gen.generate())
        one_work = BeautifulSoup(my_response.text, features='lxml')

        spoon_tag = one_work.find('div', {'data-qa': 'vacancy-salary'})
        if spoon_tag is None:
            spoon_text = 'None'
        else:
            spoon_text = spoon_tag.text
        print(spoon_text)

        company_tag = one_work.find('span', {'data-qa': 'bloko-header-2'})
        company = company_tag.text
        print(company)



    # soup = BeautifulSoup(html_data, features='lxml')
    # works = soup.find(name='h1', class_='bloko-header-section-3')
    # print(works)
