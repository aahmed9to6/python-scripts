from bs4 import BeautifulSoup
import requests

download_suffix = '/download/video'

base_url = 'https://symfonycasts.com'
course_url = '/screencast/symfony'

def get_page_dom():
    url = base_url + course_url
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.181 Safari/537.36'
    }
    r = requests.get(url=url,headers=headers)
    return r.text

def get_links(html):
    chapter_list = html.find('div',class_='chapter-list')
    chapter_list_item = chapter_list.find_all('li')
    for item in chapter_list_item:
        yield item.div.div.a['href']

def generate_download_link(dl):
    for i in dl:
        yield base_url + i + download_suffix

def save_to_file(links):
    links = generate_download_link(links)
    

def Main():
    html = BeautifulSoup(get_page_dom(), 'html.parser')
    download_links = get_links(html)

    save_to_file(download_links)

if __name__ == '__main__':
    Main()