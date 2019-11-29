import requests
from bs4 import BeautifulSoup
import re

# TODO: Clean up code!
# TODO: Access data from firebase!

#################################################################################################
# Currencies
currency_ron = "RON"
currency_euro = "EUR"
currency_dollar = "USD"

# Categories
category_electronics = "Electronics"
category_vehicles = "Vehicles"
category_clothing = "Clothig"
category_sports = "Sports"
category_other = "Other"

url_emag = "https://www.emag.ro/bratara-fitness-xiaomi-mi-band-4-6934177710377/pd/DVG5SRBBM"
url_mediagalaxy = "https://mediagalaxy.ro/laptop-hp-pavilion-15-cs1005nq-intel-core-i7-8565u-" \
                  "pana-la-4-6ghz-15-6-full-hd-8gb-ssd-256gb-nvidia-geforce-mx150-2gb-free-dos-argintiu/cpd/LAP6PT41EA/"
url_flanco = "https://www.flanco.ro/apple-watch-series-5-gps-44mm-space-grey-aluminium-case-black-sport-band.html"
url_cel = "https://www.cel.ro/telefoane-mobile/telefon-mobil-apple-iphone-7-32gb-black-pMiYwMDMm-l"
url_dedeman = "https://www.dedeman.ro/ro/lance-pentru-k2-k3-karcher-vp120-2-642-724-0/p/1019260"
url_autovit = "https://www.autovit.ro/anunt/bmw-seria-1-120-ID7Gyoh2.html#74b248046e"
url_altex = "https://altex.ro/boxe-audio-5-0-jamo-s-628-hcs-negru/cpd/BOXS628HCSBA/"
url_evomag = "https://www.evomag.ro/resigilate-produse-resigilate/" \
             "samsung-televizor-led-samsung-125-cm-49-ue49mu8002-ultra-hd-4k-smart-tv-wifi-ci-3620864.html"
url_quickmobile = "https://www.quickmobile.ro/entertainment/" \
                  "boxe-portabile/harman-kardon-boxa-portabila-onyx-studio-6-albastru-206775"
url_gymbeam = "https://gymbeam.ro/kreatin-crea7in-300-g-gymbeam.html"
url_megaproteine = "https://www.megaproteine.ro/Accesorii/" \
                   "Manusi-antrenament-sala-pentru-barbati-Adidas-Essential-Gloves-Black-Grey/"
url_sportisimo = "https://www.sportisimo.ro/under-armour/cg-armour-mock/226188/"
url_footshop = "https://www.footshop.eu/ro/incaltaminte-pentru-el/24388-reebok-club-c-85-white-green.html"
url_marso = "https://www.marso.ro/produs/anvelopa/nokian/turisme/anvelopa-de-iarna/wr-d3/195-65-r15/35860"
url_intersport = "https://www.intersport.ro/pd/" \
                 "converse-pantofi-ct-as164882c-164882c-248833.htm?lang=ro&path=-760105428&color=2995"
url_ebay = "https://www.ebay.com/itm/Adidas-Ultraboost-J-Athletic-Running-Shoes-Trace-Blue-DB1427-NEW-Youth-4-5Y/" \
           "123975539042?_trkparms=aid%3D555018%26algo%3DPL.SIM%26ao%3D1%26asc%3D20190212102350%26meid%3Dca8e6a32430c" \
           "4c048e634c8ea5071844%26pid%3D100012%26rk%" \
           "3D2%26rkt%3D12%26sd%3D163920485799%26itm%3D123975539042%26pmt%3D1%26" \
           "noa%3D0%26pg%3D2047675&_trksid=p2047675.c100012.m1985"


#################################################################################################

def find_price(soup, tag, class_name):
    price = soup.find(tag, attrs={"class": class_name}).text.strip()
    return price


def find_title(soup, tag, class_name):
    title = soup.find(tag, attrs={"class": class_name}).text.strip()
    return title


def get_site_address(url):
    pattern = r'[a-zA-z]+\.ro+|[a-zA-z]+\.com+|[a-zA-z]+\.eu+'
    address = re.findall(pattern, url)
    address = address[0]
    return address


def print_product_info(title, price, currency, image):
    print("Product: " + title + "\nPrice(" + currency + "):", price, "\nImageURL: " + image)


def get_info(url):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    address = get_site_address(url)

    if address == "emag.ro":
        print("Emag:")
        title = find_title(soup, "h1", "page-title")
        price = soup.find("p", attrs={"class": "product-new-price"}).text.strip()
        s = list(price)
        s.insert(-6, ",")
        price = "".join(s)
        price = re.sub("Lei", '', price)
        price = re.sub(",", ".", price)
        price = float(price)
        currency = "LEI"
        image = soup.find("div", attrs={"class": "ph-body"}).img['data-src'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "mediagalaxy.ro":
        print("Mediagalaxy:")
        title = find_title(soup, "h1", "font-bold leading-none text-black m-0"
                                       " text-center text-base lg:text-3xl bg-gray-lighter "
                                       "lg:bg-transparent -mx-15px lg:mx-auto px-3"
                                       " pt-4 pb-3 lg:p-0 border-b lg:border-b-0")
        price = find_price(soup, "div", "Price-current")
        price = re.sub("\.", '', price)
        price = re.sub(",", ".", price)
        price = re.sub("lei", '', price)
        price = float(price)
        currency = currency_ron
        image = soup.find("div", attrs={"class": "slick-slide slick-active slick-current"}).img['src'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "flanco.ro":
        print("Flanco:")
        title = soup.find("h1", attrs={"id": "product-title"}).text.strip()
        price = find_price(soup, "div", "produs-price")
        price = re.sub("\.", '', price)
        price = re.sub(",", ".", price)
        price = re.sub("lei", '', price)
        price = float(price)
        currency = currency_ron
        image = soup.find("img", attrs={"class": "product-main-image-img desktop"})['data-lazy']
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "cel.ro":
        print("Cel:")
        title = find_title(soup, "h1", "productName")
        price = find_price(soup, "span", "productPrice")
        price = float(price)
        currency = currency_ron
        image = soup.find("img", attrs={"id": "main-product-image"})['src'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "dedeman.ro":
        print("Dedeman:")
        title = find_title(soup, "h1", "no-margin-bottom product-title")
        price = soup.find("div", attrs={"class": "product-price large"}).span.text.strip()
        price = float(price)
        currency = currency_ron
        image = soup.find("img", attrs={"class": "slider-product-image img-responsive"})['src'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "autovit.ro":
        print("Autovit:")
        title = find_title(soup, "span", "offer-title big-text fake-title")
        price = find_price(soup, "span", "offer-price__number")
        price = re.sub("EUR", '', price)
        price = re.sub(" ", '', price)
        price = float(price)
        currency = currency_euro
        image = soup.find("div", attrs={"class": "photo-item"}).img['data-lazy'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "altex.ro":
        print("Altex:")
        title = find_title(soup, "h1", "font-bold leading-none text-black m-0 text-center text-base lg:text-3xl bg-gray-lighter lg:bg-transparent -mx-15px lg:mx-auto px-3 pt-4 pb-3 lg:p-0 border-b lg:border-b-0")
        price = find_price(soup, "div", "Price-current")
        price = re.sub("\.", '', price)
        price = re.sub(",", ".", price)
        price = re.sub("lei", '', price)
        price = float(price)
        currency = currency_ron
        image = soup.find("div", attrs={"class": "slick-slide slick-active slick-current"}).img['src'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "evomag.ro":
        print("Evomag:")
        title = find_title(soup, "h1", "product_name")
        price = find_price(soup, "div", "pret_rons")
        price = re.sub("\.", '', price)
        price = re.sub(",", ".", price)
        price = re.sub("Lei", '', price)
        price = float(price)
        currency = currency_ron
        image = soup.find("a", attrs={"class": "fancybox fancybox.iframe"}).img['src'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "quickmobile.ro":
        print("QuickMobile:")
        title = find_title(soup, "div", "product-page-title page-product-title-wth")
        price = find_price(soup, "div", "priceFormat total-price price-fav product-page-price")
        price = re.sub("Lei", '', price)
        price = float(price)
        currency = currency_ron
        image = soup.find("img", attrs={"class": "img-responsive image-gallery"})['src'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "gymbeam.ro":
        print("GymBeam:")
        title = find_title(soup, "h1", "page-title")
        price = find_price(soup, "span", "price")
        price = re.sub(",", '.', price)
        price = re.sub("Lei", '', price)
        price = float(price)
        currency = currency_ron
        image = soup.find("div", attrs={"class": "product media"}).img['data-src'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "megaproteine.ro":
        print("MegaProteine:")
        title = soup.find("h1").text.strip()
        price = find_price(soup, "span", "pret")
        price = re.sub(",", '.', price)
        price = re.sub("lei", '', price)
        price = float(price)
        currency = currency_ron
        image = soup.find("link", attrs={"rel": "image_src"})['href'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "sportisimo.ro":
        print("Sportisimo:")
        title = soup.find("h1").text.strip()
        price = soup.find("p", attrs={"class": "price"}).text.strip()
        price = re.sub("Lei cu TVA", '', price)
        # price = re.sub(" ", '%', price)
        price = re.sub(",", ".", price)
        price = price.replace(u'\xa0', u'')
        price = re.findall(r'[0-9]*\.[0-9]*', price)
        price = float(price[0])
        currency = currency_ron
        image = soup.find("div", attrs={"class": "gallery_image slide"}).img['src'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "footshop.eu":
        print("Footshop:")
        title = soup.find("h1").text.strip()
        price = soup.find("p", attrs={"class": "ProductProperties_price_1rMbi"}).text.strip()
        price = re.sub("cu TVA", '', price)
        price = re.sub("Lei", '', price)
        price = float(price)
        currency = currency_ron
        image = "no image"
        # image = soup.find("img", attrs={"class": "ImageSlider_image_2Vl4h"}).text.strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "marso.ro":
        print("Marso:")
        title = soup.find("title").text.strip()
        price = find_price(soup, "div", "retail-price-brutto")
        price = re.sub("LEI", '', price)
        price = re.sub(",", '.', price)
        price = float(price)
        currency = currency_ron
        image = soup.find("img", attrs={"class": "product-image ui centered middle aligned image"})['src'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    if address == "intersport.ro":
        print("Intersport")
        title = soup.find("title").text.strip()
        price = find_price(soup, "span", "price")
        price = re.sub("LEI", '', price)
        price = re.sub(",", '.', price)
        price = float(price)
        currency = currency_ron
        image = soup.find("div", attrs={"class": "image-container"}).img['src'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image

    # !!!!! Resolve exception when advert is no longer active !!!!
    if address == "ebay.com":
        print("Ebay:")
        title = soup.find("title").text.strip()
        price = soup.find("span", attrs={"id": "prcIsum"}).text.strip()
        price = re.sub("US",'', price)
        price = re.sub("\$",'', price)
        price = float(price)
        currency = currency_dollar
        image = soup.find("img", attrs={"id": "icImg"})['src'].strip()
        print_product_info(title, price, currency, image)
        return title, price, currency, image


def push_data(user, url, prod_category):
    from firebase import firebase
    from datetime import date

    product_data = get_info(url)
    title = product_data[0]
    price = product_data[1]
    currency = product_data[2]
    image = product_data[3]
    cur_date = date.today()

    firebase = firebase.FirebaseApplication("https://price-tracker-7cfd7.firebaseio.com/", None)
    check = [(price, cur_date)]
    data = {
        'URL': url,
        'Category': prod_category,
        'Name': title,
        'Currency': currency,
        'Image': image,
        'Checks': check
    }
    res = firebase.post("Users/" + user, data)
    return res


# ############################################ - TEST BENCH - ####################################################

# 1.1
url = url_mediagalaxy
category = category_electronics
result = push_data("Termiantor T1000", url, category)
print(result)

# 1.2
url = url_cel
category = category_electronics
result = push_data("Termiantor T1000", url, category)
print(result)

# 1.3
url = url_autovit
category = category_vehicles
result = push_data("Termiantor T1000", url, category)
print(result)

# 2.1
url = url_marso
category = category_vehicles
result = push_data("Valaki mas", url, category)
print(result)

# 2.2
url = url_marso
category = category_vehicles
result = push_data("Valaki mas", url, category)
print(result)

# 3.1
url = url_footshop
category = category_clothing
result = push_data("En", url, category)
print(result)

# ############################################ - TEST BENCH - ####################################################
