import requests
from bs4 import BeautifulSoup
import codecs

def main():
    url = 'http://www.ximalaya.com/zhubo/8889234/'
    url = 'http://www.ximalaya.com/zhubo/10936615/'

    r = requests.get(url)

    # with codecs.open('test.html', 'w', 'utf-8') as fh:
        # fh.write(r.text)
        
    soup = BeautifulSoup(r.text, 'lxml')

    tag_warp = soup.find('div', class_='index_sounds_wrap'). \
            find('ul', class_='body_list mg10')
    # tag_warp["sound_ids"]


if __name__ == '__main__':
    main()