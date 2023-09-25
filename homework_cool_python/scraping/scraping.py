import requests
from bs4 import BeautifulSoup
import fake_headers
import json
from tqdm import tqdm

if __name__ == '__main__':
    url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&page=0'
    headers_gen = fake_headers.Headers(browser='opera', os='win')
    response = requests.get(url=url, headers=headers_gen.generate())
    html_data = response.text

    all_vacancy = BeautifulSoup(html_data, features='lxml')

    vacancy_tags = all_vacancy.find('div', {'data-qa':
                                            'vacancy-serp__results'})
    vacancy_list = vacancy_tags.find_all('div',
                                         class_='vacancy-serp-item__layout')

    vacancy_dict = {}
    counter = 1
    for vacancy in tqdm(vacancy_list):
        article_tag = vacancy.find('h3', class_='bloko-header-section-3')

        href_tag = article_tag.find('a', class_='serp-item__title')
        href = href_tag['href']

        new_response = requests.get(url=href, headers=headers_gen.generate())
        new_html_data = new_response.text

        all_description = BeautifulSoup(new_html_data, features='lxml')
        vacancy_description = all_description.find('div',
                                                   {'data-qa':
                                                    'vacancy-description'})
        description = vacancy_description.text
        res_sear = description.find('Django')
        new_res_sear = description.find('django')

        res_sear_2 = description.find('Flask')
        new_res_sear_2 = description.find('flask')
        if (res_sear > 0 or new_res_sear > 0) and (res_sear_2 > 0 or
                                                   new_res_sear_2 > 0):
            article = str(article_tag.text)

            money_tag = vacancy.find('span',
                                     {'data-qa':
                                      'vacancy-serp__vacancy-compensation'})
            if money_tag:
                money = str(money_tag.text)
            else:
                money = 'No information about money'

            company_tag = vacancy.find('div', class_='vacancy-serp-item__'
                                                     'meta-info-company')
            company = str(company_tag.text)

            city_tag = vacancy.find('div', class_='vacancy-serp-item__info')
            city_tag = city_tag.find('div', {'data-qa':
                                             'vacancy-serp__vacancy-address'})
            city = str(city_tag.text)
            number = city.find(',')
            if number > 0:
                city = str(city[:number])

            vacancy_dict[f'vacancy_#{counter}'] = {'article': f'{article}',
                                                   'link': f'{href}',
                                                   'money': f'{money}',
                                                   'company': f'{company}',
                                                   'city': f'{city}'}
            counter += 1
    with open('vacancy.json', 'w', encoding='utf-8') as out_put:
        json.dump(vacancy_dict, out_put, indent=4, ensure_ascii=False)
