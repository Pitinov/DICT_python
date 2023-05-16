"""Web page scraper"""
from urllib.parse import urlparse
import string
import os
from bs4 import BeautifulSoup
import requests
from pageinfo import PageInfo


def save_to_file(page: int, info: PageInfo):
    """Save article to file"""
    path = f"Pages/Page_{page}"
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = info.title.translate(str.maketrans('', '', string.punctuation))
    file_name = file_name.replace(' ', '_')
    with open(f"{path}/{file_name}.md", 'w', encoding='utf-8') as file:
        file.write(info.as_markdown())


def parse_article(url: str) -> PageInfo:
    """Parse article from url"""
    page = requests.get(url, timeout=5).content
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.find('h1').text.strip()
    teaser = soup.find('div', {'class': 'c-article-teaser-text'})
    non_full_text = soup.find('p', {'class': 'article__teaser'})
    full_text = soup.find('div', {'class': 'c-article-body'})
    if teaser:
        teaser = teaser.text.strip()
    if non_full_text:
        non_full_text = non_full_text.text.strip()
    if full_text:
        full_text = full_text.text.strip()
    return PageInfo(title, teaser, non_full_text, full_text)


def get_articles(url: str, theme: str):
    """Get articles from url"""
    page = requests.get(url, timeout=5)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.findAll('article')
    for result in results:
        rtype = result.find('span', attrs={'data-test': 'article.type'})
        if rtype.find('span').text.lower() != theme.lower():
            continue
        surl = result.find('a', attrs={'data-track-action': 'view article'})
        yield parse_article(f"https://{urlparse(url).netloc}{surl['href']}")


def get_pages(count: int, theme: str):
    """Get pages from url"""
    for i in range(count):
        url = f"https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={i+1}"
        for article in get_articles(url, theme):
            save_to_file(i, article)


def main():
    """Main function"""
    count = int(input("Enter number of pages: "))
    theme = input("Enter theme: ")
    get_pages(count, theme)
    print("Done")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nCutting off the internet cable")