import requests
from bs4 import BeautifulSoup
# import lxml
import re

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

def FindPrice(url, tag, class_name):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    price = soup.find(tag, attrs={"class": class_name}).text.strip()
    print(price)

def FP(url, tag, class_name):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")
    tag = soup.find_all(tag)
    print(tag)
    # price = soup.find(tag, attrs={"class": class_name}).text.strip()
    # print(price)
#################################################################################################


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

price = "9 999"
html_content = requests.get(autovit_url).text
soup = BeautifulSoup(html_content, "html.parser")
result = soup.find_all()

price_regex = r'[a-zA-z]*[pP]rice[a-zA-z]*'
price_pattern = re.compile(price_regex)

results = []
for tag in result:
    txt = tag.text.strip()
#     # print("######################",txt)
    if price in txt:
        # print("####", tag.attrs)
        results.append(tag)

results2 = []
for tag in results:
    # print("@@@@", tag.text)
    if "price" in tag.text:
        # print("$$$$", tag.name, tag.text.strip())
        results2.append(tag)

results3 = soup.find_all(attrs={"class": price_pattern})
# print(results3.text.strip())
for tag in results3:
    # print(tag.text.strip())
    if price in tag.text:
        print("^^^^", tag.name)

# results4 = soup.findChildren(attrs={"class": price_pattern})
results4 = soup.findChildren(attrs={"class": price_pattern})
print("number of items in results4:", len(results4))
for tag in results4:
    print("%%%%", tag.text)

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
