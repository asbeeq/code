from mail_ru import get_attributes
from bs4 import BeautifulSoup
from input import FILES_HTML, LOCATION_DIRECTORY, FILES_EXTENSION


for file_html in FILES_HTML:
    with open(f'{LOCATION_DIRECTORY}{file_html}.{FILES_EXTENSION}', encoding='utf-8', newline='') as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')

        df = get_attributes(soup)
        print(df)

        df.to_excel('metki1.xlsx', sheet_name='er')  #write to excel