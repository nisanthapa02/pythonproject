#! python3
# Python script to get Id of a movie or show in the format 'ttxxxxxx'

import re, requests, bs4, sys

# string = r'''function show_video1() {if($("#check_click").val() == 1){$("#tab1 .movieplay").html('<iframe src="https://oload.stream/embed/OnPKOlstdrE/The.Current.War.2019.HC.720p.HDRip.800MB.x264_GalaxyRG.E.mp4" frameborder="0" allowfullscreen></iframe>');}$("#check_click").val(1);}'''
# match = re.compile(r'<iframe src="(.+?)"')
# final = match.findall(string)
# print(final)

if len(sys.argv) < 2:
    print('Usage: get-imdb-id.py "name of movie or tv show" ')
    sys.exit()

searchTerm = sys.argv[1]

def getImdbId(searchTerm):
    imdbSearch = r'''https://imdb.com/find?q=''' + searchTerm + r'''&s=tt&exact=true''' # tt = title search all= all search
    r = requests.get(imdbSearch)
    titleObj = bs4.BeautifulSoup(r.text, 'lxml')
    title = titleObj.select('tr td a')[0].get('href')
    imdbId = re.compile(r'tt[0-9]+').findall(title)
    return imdbId

print(getImdbId(searchTerm))

