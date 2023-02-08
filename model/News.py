from bs4 import BeautifulSoup
import requests


class News:
    def __init__(self, title, image, url_news):
        self.__title = title
        self.__image = image
        self.__url_news = url_news

    def __repr__(self):
        return {
            "title": self.__title,
            "image": self.__image,
            "url_news": self.__url_news
        }

    @staticmethod
    def get_news():
        news = []
        try:
            url = "https://noticiasdatv.uol.com.br/bbb/bbb-23"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            header_news = soup.find("div", "col-12 px-0 px-md-3 item-artigo")
            href = header_news.find('a').get("href")
            url_news = requests.compat.urljoin(url, href)
            title = header_news.findAll("p")[1].getText()
            img = header_news.find("img")
            src = img.get("src")
            image = requests.compat.urljoin(url, src)

            news.append(News(title, image, url_news))

            divs = soup.findAll("div", "col-12 col-sm-6 pt-md-0 item-artigo")
            imgs = soup.findAll("img", "img-fluid")[1:6]

            for index, div in enumerate(divs):
                title = div.getText().split('\n')[1]
                src = imgs[index].get("src")
                image = requests.compat.urljoin(url, src)
                a = div.find('a')
                href = a.get("href")
                url_news = requests.compat.urljoin(url, href)
                news.append(News(title, image, url_news))
        except:
            print("Error in create news")

        return news
