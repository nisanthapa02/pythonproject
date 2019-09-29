import os, requests, bs4

os.makedirs("D:\\xkcd", exist_ok=True)

url = "http://xkcd.com"

while not url.endswith("#"):
# for i in range(4):
    # Download page
    print("Downloading page {}...".format(url))
    r = requests.get(url)
    r.raise_for_status()
    soupObj = bs4.BeautifulSoup(r.text, "lxml")

    # find the url of comic image
    comicElem = soupObj.select("#comic img")
    if comicElem == []:
        print("could not find image")
    else:
        comicURL = comicElem[0].get("src")

    # download the image
        print("Downloading image http:{}...".format(comicURL))
        r = requests.get("http:" + comicURL)
        r.raise_for_status()

    # save image to folder
        imageFile = open('D:\\xkcd' + "\\" + os.path.basename(comicURL), "wb")
        for chunk in r.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # get prev button url
    prevLink = soupObj.select('a[rel="prev"]')
    url = "http://xkcd.com" + prevLink[0].get("href")

print("Done")
