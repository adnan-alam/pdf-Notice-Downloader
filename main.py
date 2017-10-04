import requests
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlretrieve


notice_page = requests.get("url of notice page")

# e.g. ,
#cu_admission_notice = requests.get("http://admission.eis.cu.ac.bd/index.php?act=information/get_notices/all")
#kuet_admission_notice = requests.get("http://admission.kuet.ac.bd/Notice.aspx")


parsed_html = BeautifulSoup(notice_page.text,"lxml")

#e.g. ,
#parsed_html = BeautifulSoup(cu_admission_notice.text,"lxml")
#parsed_html = BeautifulSoup(kuet_admission_notice.text,"lxml")


all_links = parsed_html.find_all("a")


# list of download links of notices
download_links = []

website_url = ""
# e.g. website_url = "http://admission.kuet.ac.bd/"

for link in all_links:
    if ".pdf" in link["href"]:
        if website_url in link["href"]:
            download_links.append(link["href"])
        else:
            download_links.append(website_url + link["href"])
        

# downloader
for link in download_links:
    extension = link.split("/")[-1]
    urlretrieve(link,"directory path/{}".format(extension))
    # e.g. urlretrieve(link,"home/user/notices_folder/{}".format(extension))

