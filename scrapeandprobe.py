import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

visited_urls = set()
count = 0

def spider_urls(url, keyword, max_urls):
    global count
    try:
        response = requests.get(url)
    except:
        print(f"request failed {url}")
        return []

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        a_tag = soup.find_all('a')
        urls = []
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)

        found_urls = []
        for keyword_urls in urls:
            if count >= max_urls:
                return found_urls
            if keyword_urls not in visited_urls:
                visited_urls.add(url)
                url_join = urljoin(url, keyword_urls)
                if keyword in url_join:
                    found_urls.append((url_join, False))  # Mark URL as not validated
                    count += 1
                    found_urls += spider_urls(url_join, keyword, max_urls)

        return found_urls
    else:
        return []

def main():
    url = input("Enter the URL you want to scrape: ")
    keyword = input("Enter the keyword you want to search for in the URL provided: ")
    max_urls = int(input("Enter the maximum amount of URLs you want from the scrape: "))
    found_urls = spider_urls(url, keyword, max_urls)

    validated_urls = []
    for url, _ in found_urls:
        try:
            response = requests.head(url)
            if response.status_code == 200:
                validated_urls.append(url)
        except requests.exceptions.RequestException:
            continue

    out_file = 'filtered_urls.txt'
    with open(out_file, 'w') as file:
        file.write('\n'.join(validated_urls))

    print(f"Saved validated URLs to {out_file}")

if __name__ == "__main__":
    main()
