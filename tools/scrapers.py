import requests
from bs4 import BeautifulSoup


img_url_root = "https://www.yelp.com/biz_photos"


def get_title(_soup):
    return _soup.find("h1", {"class":"biz-page-title"}).text.strip()


def get_address(_soup):
    return _soup.find_all("address")[1].text.strip()


def yelp_scraper(restaurant, img_id):
    img_src = "https://s3-media4.fl.yelpcdn.com/bphoto/{}/o.jpg".format(img_id)
    img_url = "{}/{}?{}".format(img_url_root, restaurant, img_id)
    url = img_url.split("?")[0].replace("biz_photos", "biz")
    soup = BeautifulSoup(requests.get(url).text)
    result = {
        "restaurant": get_title(soup), "address": get_address(soup), "img_src": img_src
    }
    return result


if __name__ == "__main__":
    restaurant = "nan-xiang-xiao-long-bao-flushing"
    img_id = "ONP2DhsGDUKVScihhmaUGw"
    print(yelp_scraper(restaurant, img_id))