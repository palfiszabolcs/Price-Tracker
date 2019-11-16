import requests
from bs4 import BeautifulSoup
import re
#################################################################################################

# 1.
# emag: tag = "p" | class = "product-new-price"
emag_url = "https://www.emag.ro/bratara-fitness-xiaomi-mi-band-4-6934177710377/pd/DVG5SRBBM"

# 2.
# dedeman: tag = "div" | class = "product-price large"
dedeman_url = "https://www.dedeman.ro/ro/lance-pentru-k2-k3-karcher-vp120-2-642-724-0/p/1019260"

# 3.
# media: tag = "div" | class = "Price-current"
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
ebay_url = "https://www.ebay.com/itm/Adidas-UltraBoost-4-0-Mens-Running-Shoes-Tech-Ink-Glow-Blue-Size-9-5-G54002/163920485799" \
       "?epid=10033867920&hash=item262a6c1da7:g:0EIAAOSwVc9dtdHe"

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
olx_url = "https://www.olx.ro/oferta/canon-5d-mark-iii-5d-mark-3-IDcZmYd.html"

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
#################################################################################################

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


def FindPrice(url, tag, class_name):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    price = soup.find(tag, attrs={"class": class_name}).text.strip()
    # print(price)
    return price

#################################################################################################

html_content = requests.get(mobile_url).text
# print(html_content)
soup = BeautifulSoup(html_content, "html.parser")
# tag = soup.find("span", attrs={"class:", "h3 rbt-prime-price"}).text.strip(
print(soup)
# tag = re.sub("cu TVA", '', tag)
# print(tag)

# price = FindPrice(sportisimo_url, "p", "price")
# print(price)

# print("\n1.Emag:")
# FindPrice(emag_url, "p", "product-new-price")
# print("\n2.Dedeman:")
# FindPrice(dedeman_url, "div", "product-price large")
# print("\n3.MG:")
# FindPrice(mediagalaxy_url, "div", "Price-current")
# print("\n4.Cel:")
# FindPrice(cel_url, "span", "productPrice")
# print("\n5.Mobile " + "nem megy meg")
# print("\n6.Autovit:")
# FindPrice(autovit_url, "span", "offer-price__number")
# print("\n7.FaceBook Marketplace: " + "nem megy meg")
# print("\n8.Ebay:")
# FindPrice(ebay_url, "span", "notranslate")

#FindPrice(flanco_url, "div", "produs-price")




# making a list of the tags
# tags = [tag.name for tag in soup.find_all()]
# tags = [str(tag) for tag in soup.find_all()]
# print(tags)

# # regex
# price_pattern = r'[a-zA-z]*[pP]rice[a-zA-z]*'
# current_price_pattern = r'[a-zA-z]*[pP]rice[a-zA-z]*[cC]urrent[a-zA-z]*'
# price_regex = re.compile(price_pattern)
# current_price_regex = re.compile(current_price_pattern)
#
# # request / soup
# html_content = requests.get(autovit_url).text
# soup = BeautifulSoup(html_content, "html.parser")
# result = soup.find("span", attrs={"class": price_regex})
# print(result.text)

# result2 = result.find("div", attrs={"class": regex})
# print(result2)

# searching for a specific price

# regex az arra, lassad ha kiadja

# bmw_regex = r'[a-zA-z]*BMW[a-zA-z]*'
# bmw_pattern = re.compile(bmw_regex)
# html_content = requests.get(autovit_url).text
# soup = BeautifulSoup(html_content, "html.parser")
# result = soup.find_all(any, text=bmw_pattern)
# print(result)
# for tag in result:
#     print(tag.text)

# price = "9 999"
# html_content = requests.get(autovit_url).text
# soup = BeautifulSoup(html_content, "html.parser")
# result = soup.find_all()
#
# price_regex = r'[a-zA-z]*[pP]rice[a-zA-z]*'
# price_pattern = re.compile(price_regex)
#
# results = []
# for tag in result:
#     txt = tag.text.strip()
# #     # print("######################",txt)
#     if price in txt:
#         # print("####", tag.attrs)
#         results.append(tag)
#
# results2 = []
# for tag in results:
#     # print("@@@@", tag.text)
#     if "price" in tag.text:
#         # print("$$$$", tag.name, tag.text.strip())
#         results2.append(tag)
#
# results3 = soup.find_all(attrs={"class": price_pattern})
# # print(results3.text.strip())
# for tag in results3:
#     # print(tag.text.strip())
#     if price in tag.text:
#         print("^^^^", tag.name)
#
# # results4 = soup.findChildren(attrs={"class": price_pattern})
# results4 = soup.findChildren(attrs={"class": price_pattern})
# print("number of items in results4:", len(results4))
# for tag in results4:
#     print("%%%%", tag.text)

# regex test
# text = "this is the product-new-price " \
#        " Price-current is something  " \
#        "product-price large not"
# pattern = r'[a-zA-z]*[pP]rice[a-zA-z]*'
# pattern2 = r'[a-zA-Z]'
# regex = re.compile(pattern2)
# matches = regex.finditer(text)
# for match in matches:
#     print(match.string)


