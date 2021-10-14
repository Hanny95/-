from bs4 import BeautifulSoup

def searchH1TagString(filePath):
    with open(filePath, 'r', encoding='UTF-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    h1 = soup.html.body.h1

    print(f'h1 : {h1.string}')


if __name__ == '__main__':
    path = 'C:/chh_scraping/download/'
    fileName = 'tempHtml.html'

    searchH1TagString(path + fileName)