import urllib.request
import requests
from bs4 import BeautifulSoup
from firebase import firebase
import re

#################################################################################################

# 1.
# emag
# price: tag = "p" | class = "product-new-price"
# title: tag = "h1" | class = "page-title"
# image = soup.find("div", attrs={"class": "ph-body"}).img['data-src']
emag_url = "https://www.emag.ro/bratara-fitness-xiaomi-mi-band-4-6934177710377/pd/DVG5SRBBM"

# 2.
# dedeman: tag = "div" | class = "product-price large"
dedeman_url = "https://www.dedeman.ro/ro/lance-pentru-k2-k3-karcher-vp120-2-642-724-0/p/1019260"

# 3.
# price: tag = "div" | class = "Price-current"
# title: tag = "h1" | class = "font-bold leading-none text-black m-0 text-center text-base lg:text-3xl bg-gray-lighter lg:bg-transparent -mx-15px lg:mx-auto px-3 pt-4 pb-3 lg:p-0 border-b lg:border-b-0"
# image = soup.find("div", attrs={"class": "ph-body"}).img['data-src']
mediagalaxy_url = "https://mediagalaxy.ro/laptop-hp-pavilion-15-cs1005nq-intel-core-i7-8565u-" \
                  "pana-la-4-6ghz-15-6-full-hd-8gb-ssd-256gb-nvidia-geforce-mx150-2gb-free-dos-argintiu/cpd/LAP6PT41EA/"
# 4.
# cel: tag = "div" | class = "pret_info"
# cel: tag = "span" | class = "productPrice"
cel_url = "https://www.cel.ro/telefoane-mobile/telefon-mobil-apple-iphone-7-32gb-black-pMiYwMDMm-l"

# 5.
# mobile.de: tag = span | class = "h3 rbt-prime-price"
mobile_url = "https://suchen.mobile.de/fahrzeuge/details.html?id=285844936&damageUnrepaired=NO_DAMAGE_UNREPAIRED" \
         "&isSearchRequest=true&makeModelVariant1.makeId=3500&makeModelVariant1.modelId=59&pageNumber=1&scopeId=C" \
         "&sfmr=false&action=topInCategory&searchId=4dd6fbed-e436-25fe-4696-fa56110350c4"

# 6.
# autovit: tag = "span" | class = "offer-price__number"
autovit_url = "https://www.autovit.ro/anunt/bmw-seria-1-120-ID7Gyoh2.html#74b248046e"

# 7.
# facebook marketplace: tag = "div" | class = "_5_md  _2iel"
facebook_marketplace_url = "https://www.facebook.com/marketplace/item/330169417907484/"

# 8.
# ebay: tag = "span" | class = "notranslate"
ebay_url = "https://www.ebay.com/itm/Adidas-Ultraboost-J-Athletic-Running-Shoes-Trace-Blue-DB1427-NEW-Youth-4-5Y/" \
           "123975539042?_trkparms=aid%3D555018%26algo%3DPL.SIM%26ao%3D1%26asc%3D20190212102350%26meid%3Dca8e6a32430c" \
           "4c048e634c8ea5071844%26pid%3D100012%26rk%3D2%26rkt%3D12%26sd%3D163920485799%26itm%3D123975539042%26pmt%3D1%26" \
           "noa%3D0%26pg%3D2047675&_trksid=p2047675.c100012.m1985"

# 9.
# FLANCO: tag = "div" | class = "produs-price"
flanco_url = "https://www.flanco.ro/apple-watch-series-5-gps-44mm-space-grey-aluminium-case-black-sport-band.html"

# 10.
# ALTEX: tag = "div" | class = "Price-current"
altex_url = "https://altex.ro/boxe-audio-5-0-jamo-s-628-hcs-negru/cpd/BOXS628HCSBA/"

# 11.
# PC GARAGE: tag = "p" | class = "ps-sell-price"
pcgarage_url = "https://www.pcgarage.ro/monitoare-led/aoc/gaming-c27g1-curbat-27-inch-1-ms-black-freesync-144hz/"

# 12.
# EVOMAG: tag = "div" | class = "pret_rons"
evomag_url = "https://www.evomag.ro/resigilate-produse-resigilate/samsung-televizor-led-samsung-125-cm-49-ue49mu8002-ultra-hd-4k-smart-tv-wifi-ci-3620864.html"

# 13.
# QUICKMOBILE: tag = "div" | class = "priceFormat total-price price-fav product-page-price"
quickmobile_url = "https://www.quickmobile.ro/entertainment/boxe-portabile/harman-kardon-boxa-portabila-onyx-studio-6-albastru-206775"

# 14.
# F64: tag = "div" | class = "productPrice"
f64_url = "https://www.f64.ro/canon-ef-600mm-f-4l-is-ii-usm/p?idsku=132629"

# 15.
# GYM BEAM: tag = "span" | class = "price"
gymbeam_url = "https://gymbeam.ro/kreatin-crea7in-300-g-gymbeam.html"

# 16.
# olx_url: tag = "div" | class = "price-label"
olx_url = "https://www.olx.ro/oferta/google-pixel-2-black-IDcVstC.html#8b8cb9bb94"

# 17.
# MEGAPROTEINE: tag = "span" | class = "pret"
megaproteine_url = "https://www.megaproteine.ro/Accesorii/Manusi-antrenament-sala-pentru-barbati-Adidas-Essential-Gloves-Black-Grey/"

# 18.
# FASHION DAYS: tag = "span" | class = "new-price"
fashiondays_url = "https://www.fashiondays.ro/p/pantofi-sport-slip-on-tricotati-pentru-alergare-nrgy-neko-femei-puma-p2134085-1/"

# 19.
# H&M: tag = "span" | class = "price-value"
hm_url = "https://www2.hm.com/ro_ro/productpage.0720504004.html"

# 20.
# SPORTISIMO: tag = "p" | class = "price"
# tag = re.sub("cu TVA", '', tag)
sportisimo_url = "https://www.sportisimo.ro/under-armour/cg-armour-mock/226188/"

# 21.
# DECATHLON: tag = "span" | class = "real_price_value"
decathlon_url = "https://www.decathlon.ro/jacheta-sh100-x-warm-barbati-id_8526084.html?opeco=opeco:HPShops-ppt-reco6&type=opeco"

# 22.
# ELEFANT: tag = "div" | class = "current-price  sale-price"
elefant_url = "https://www.elefant.ro/apa-de-parfum-euphoria-100-ml-pentru-femei_07e29b2d-9cd9-491e-b46f-9fcc86605fff"

# 23.
# FOOTSHOP: tag = "p" | class = "ProductProperties_price_1rMbi"
# tag = re.sub("cu TVA", '', tag)
footshop_url = "https://www.footshop.eu/ro/incaltaminte-pentru-el/24388-reebok-club-c-85-white-green.html"

# 24.
# MOLO SPORT: tag = "" | class = ""
molosport_url = "https://www.molo-sport.ro/vans/sk8-hi/180021/"

# 25.
# MARSO: tag = "div" | class = "retail-price-brutto"
marso_url = "https://www.marso.ro/produs/anvelopa/nokian/turisme/anvelopa-de-iarna/wr-d3/195-65-r15/35860"

# 26.
# HERVIS: tag = "div" | class = "big-price"
hervis_url = "https://www.hervis.ro/store/Echipamente/Rachete-%26-Accesorii/Tenis-de-Masa/Schildkr%C3%B6t/Carbotec-900/p/COLOR-2072619"

# 27.
# INTERSPORT: tag = "span" | class = "price"
intersport_url = "https://www.intersport.ro/pd/converse-pantofi-ct-as164882c-164882c-248833.htm?lang=ro&path=-760105428&color=2995"

# 28.
# SPORTSDIRECT: tag = "div" | class = ""
sportsdirect_url = "https://ro.sportsdirect.com/adidas-predator-191-mens-sg-football-boots-193009#colcode=19300916"

# 29.
# AMAZON: tag = "span" " class = "priceblock_ourprice"
amazon_url = "https://www.amazon.de/dp/B01LWMQDRQ?pf_rd_p=3fd79cda-4f47-4515-9585-b6087d8f2668&pd_rd_wg=a2paN&pf_rd_r=ZC6VASCBN7EPRQPXVSKA&ref_" \
             "=pd_gw_unk&pd_rd_w=t2euo&pd_rd_r=73e57509-2957-498c-b330-44956712a5ed"

# 30.
# BUZZ SNEAKERS: tag = "div" | class = "product-price current-price  has-discount"
buzzsneakers_url = "https://www.buzzsneakers.com/RON_ro/pantofi-sport/67896-ozweego"

# 31.
# LEROY MERLIN: tag = "div" | class = "product_price"
leroy_url = "https://www.leroymerlin.ro/products/parchet/556/parchet-laminat-pin-callustro-8-mm-forte/35856"

# 32.
# BRICO DEPOT: tag = "div" | class = "product-price"
brico_url = "https://www.bricodepot.ro/sali-de-baie/mobilier-baie/baza-suspendata-imandra-taupe-60-cm.html"

#################################################################################################

def find_price_emag(soup, tag, class_name):
    price = soup.find(tag, attrs={"class": class_name}).text.strip()
    s = list(price)
    s.insert(-6, ",")
    price = "".join(s)
    return price


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

def print_product_info(title, price, image):
    print("Product: " + title + "\nPrice: " + price + "\nImageURL: " + image)


def get_info(url):

    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    address = get_site_address(url)

    if address == "emag.ro":
        print("Emag:")
        title = find_title(soup, "h1", "page-title")
        price = find_price_emag(soup, "p", "product-new-price")
        image = soup.find("div", attrs={"class": "ph-body"}).img['data-src'].strip()
        print_product_info(title, price, image)

    if address == "mediagalaxy.ro":
        print("Mediagalaxy:")
        title = find_title(soup, "h1", "font-bold leading-none text-black m-0 text-center text-base lg:text-3xl bg-gray-lighter lg:bg-transparent -mx-15px lg:mx-auto px-3 pt-4 pb-3 lg:p-0 border-b lg:border-b-0")
        price = find_price(soup, "div", "Price-current")
        image = soup.find("div", attrs={"class": "slick-slide slick-active slick-current"}).img['src'].strip()
        print_product_info(title, price, image)

    if address == "flanco.ro":
        print("Flanco:")
        title = soup.find("h1", attrs={"id": "product-title"}).text.strip()
        price = find_price(soup, "div", "produs-price")
        image = soup.find("img", attrs={"class": "product-main-image-img desktop"})['data-lazy']
        print_product_info(title, price, image)


    if address == "cel.ro":
        print("Cel:")
        title = find_title(soup, "h1", "productName")
        price = find_price(soup, "span", "productPrice") + " Lei"
        image = soup.find("img", attrs={"id": "main-product-image"})['src'].strip()
        print_product_info(title, price, image)


    if address == "dedeman.ro":
        print("Dedeman:")
        title = find_title(soup, "h1", "no-margin-bottom product-title")
        price = soup.find("div", attrs={"class": "product-price large"}).span.text.strip() + " Lei"
        image = soup.find("img", attrs={"class": "slider-product-image img-responsive"})['src'].strip()
        print_product_info(title, price, image)


    if address == "autovit.ro":
        print("Autovit:")
        title = find_title(soup, "span", "offer-title big-text fake-title")
        price = find_price(soup, "span", "offer-price__number")
        image = soup.find("div", attrs={"class": "photo-item"}).img['data-lazy'].strip()
        print_product_info(title, price, image)


    if address == "altex.ro":
        print("Altex:")
        title = find_title(soup, "h1", "font-bold leading-none text-black m-0 text-center text-base lg:text-3xl bg-gray-lighter lg:bg-transparent -mx-15px lg:mx-auto px-3 pt-4 pb-3 lg:p-0 border-b lg:border-b-0")
        price = find_price(soup, "div", "Price-current")
        image = soup.find("div", attrs={"class": "slick-slide slick-active slick-current"}).img['src'].strip()
        print_product_info(title, price, image)


    if address == "evomag.ro":
        print("Evomag:")
        title = find_title(soup, "h1", "product_name")
        price = find_price(soup, "div", "pret_rons")
        image = soup.find("a", attrs={"class": "fancybox fancybox.iframe"}).img['src'].strip()
        print_product_info(title, price, image)


    if address == "quickmobile.ro":
        print("QuickMobile:")
        title = find_title(soup, "div", "product-page-title page-product-title-wth")
        price = find_price(soup, "div", "priceFormat total-price price-fav product-page-price")
        image = soup.find("img", attrs={"class": "img-responsive image-gallery"})['src'].strip()
        print_product_info(title, price, image)


    if address == "gymbeam.ro":
        print("GymBeam:")
        title = find_title(soup, "h1", "page-title")
        price = find_price(soup, "span", "price")
        image = soup.find("div", attrs={"class": "product media"}).img['data-src'].strip()
        print_product_info(title, price, image)

    # !!!!! Resolve exception when advert is no longer active !!!!
    if address == "olx.ro":
        print("OLX:")
        title = soup.find("div", attrs={"class": "offer-titlebox"}).h1.text.strip()
        price = find_price(soup, "div", "price-label")
        image = soup.find("img", attrs={"class": "vtop bigImage {nr:1}"})['src'].strip()
        print_product_info(title, price, image)


    if address == "megaproteine.ro":
        print("MegaProteine:")
        title = soup.find("h1").text.strip()
        price = find_price(soup, "span", "pret")
        image = soup.find("link", attrs={"rel": "image_src"})['href'].strip()
        print_product_info(title, price, image)

    if address == "sportisimo.ro":
        print("Sportisimo:")
        title = soup.find("h1").text.strip()
        price = soup.find("p", attrs={"class": "price"}).text.strip()
        price = re.sub("cu TVA", '', price)
        image = soup.find("a", attrs={"id": "product_slider_p226188_slide_0_link"}).img['src'].strip()
        print_product_info(title, price, image)


    if address == "footshop.eu":
        print("Footshop:")
        title = soup.find("h1").text.strip()
        price = soup.find("p", attrs={"class": "ProductProperties_price_1rMbi"}).text.strip()
        price = re.sub("cu TVA", '', price)
        # image = soup.find("img", attrs={"class": "ImageSlider_image_2Vl4h"}).text.strip()
        print_product_info(title, price, "no image")


    if address == "marso.ro":
        print("Marso:")
        title = soup.find("title").text.strip()
        price = find_price(soup, "div", "retail-price-brutto")
        image = soup.find("img", attrs={"class": "product-image ui centered middle aligned image"})['src'].strip()
        print_product_info(title, price, image)


    if address == "intersport.ro":
        print("Intersport")
        title = soup.find("title").text.strip()
        price = find_price(soup, "span", "price")
        image = soup.find("div", attrs={"class": "image-container"}).img['src'].strip()
        print_product_info(title, price, image)

    # !!!!! Resolve exception when advert is no longer active !!!!
    if address == "ebay.com":
        print("Ebay:")
        title = soup.find("title").text.strip()
        price = soup.find("span", attrs={"id": "prcIsum"}).text.strip()
        image = soup.find("img", attrs={"id": "icImg"})['src'].strip()
        print_product_info(title, price, image)


        # ebay: tag = "span" | class = "notranslate"

#################################################################################################

# get_info(emag_url)
# get_info(mediagalaxy_url)
# get_info(flanco_url)
# get_info(cel_url)
# get_info(dedeman_url)
# get_info(autovit_url)
# get_info(altex_url)
# get_info(evomag_url)
# get_info(quickmobile_url)
# get_info(gymbeam_url)
# get_info(olx_url)
# get_info(megaproteine_url)
# get_info(sportisimo_url)

# get_info(footshop_url)

# get_info(marso_url)
# get_info(intersport_url)


get_info(ebay_url)
#
#
# TEST BENCH ######################


# html_content = requests.get(footshop_url).text
# soup = BeautifulSoup(html_content, "html.parser")
# image = soup.find("div", attrs={"class": "slick-slide slick-active slick-current"})
# print(image)
#
#
# urllib.request.urlretrieve(image, "000000001.jpg")
# TEST BENCH ######################




#################################################################################################

# price = find_price(ebay_url, "span", "notranslate")
# get_site_address(mediagalaxy_url)
# print(price)
#
# firebase = firebase.FirebaseApplication("https://price-tracker-7cfd7.firebaseio.com/", None)
# data = {
#     'Name': "Adidas",
#     'Price': price,
#     'Date': date
# }
#
# result = firebase.post('price-tracker-7cfd7/Pistike', data)
# result = firebase.post('price-tracker-7cfd7/Pistike', data)
# result = firebase.post('price-tracker-7cfd7/Pistike', data)
# result2 = firebase.post('price-tracker-7cfd7/John Connor', data)
# result2 = firebase.post('price-tracker-7cfd7/John Connor', data)
# print(result)
# print(result2)

#################################################################################################


#################################################################################################
