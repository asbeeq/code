import pandas as pd


def get_attributes(soup):
    headline = []
    href = []

    for v in soup.find_all('div', {'class': 'lIeSh41 svelte-4ej3uz news-item_mqx_sm'}):
        headline.append(v.text.replace('\xa0', ' ').strip())
        href.append(v.a['href'])

    # print(src)
    # print(len(src))

    dict = {
        'headline': headline,
        'href': href,
    }

    df = pd.DataFrame.from_dict(dict)

    return df