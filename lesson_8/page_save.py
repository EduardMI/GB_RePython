import requests
import aiohttp
import asyncio
from bs4 import BeautifulSoup


def get_links(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                             ' (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

    response = requests.get(url, headers=headers)
    dom = BeautifulSoup(response.text, 'html.parser')

    links_list = dom.find_all('a', {'class': 'nav-link'})
    links_list = [f'{url}{item.get("href")}' for item in links_list if 'category' in item.get('href')]

    return links_list


async def get_html_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            name_file = f'{url.split("/")[-2]}-{url.split("/")[-1]}'
            with open(f'{name_file}.html', 'w', encoding='utf-8') as file:
                file.write(data)


def main(url):
    links_dict = get_links(url)
    futures = [get_html_page(u) for u in links_dict]
    loop = asyncio.new_event_loop()
    loop.run_until_complete(asyncio.wait(futures))


if __name__ == '__main__':
    URL = 'http://127.0.0.1:8000'
    main(URL)
