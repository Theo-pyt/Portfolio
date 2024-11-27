from bs4 import BeautifulSoup


def main():
    soup = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", "html.parser")

    print(soup.prettify())

if __name__ == '__main__':
    main()