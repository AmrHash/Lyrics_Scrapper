# Make HTTP requests
import requests
# Scrape data from an HTML document
from bs4 import BeautifulSoup
# I/O
import os
# Search and manipulate strings
import re


# Get artist object from Genius API
def request_artist_info(artist_name, page):
    base_url = 'https://api.genius.com/annotations/10225840'
    headers = {'Authorization': 'Bearer ' + 'Lo9Nx68t7EK-mqvYag2Gjtn8CAF3Y1o7f059ruStG9bYBZwu_gxyyxeiBtyCrSeL'}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response
# Get Genius.com song url's from artist object
def request_song_url(artist_name, song_cap):
    page = 1
    songs = []
    
    while True:
        response = request_artist_info(artist_name, page)
        json = response.json()
        # Collect up to song_cap song objects from artist
        
    
        # Collect song URL's from song objects
        song_cap = 200
        song_info = ""
        for song in song_info:
            if (len(songs) < song_cap):
                url = song['result']['url']
                songs.append(url)

            
            
        
    print('Found {} songs by {}'.format(len(songs), artist_name))
    return songs
    print(songs) 


    
# DEMO
request_song_url('Aesop Rock', 1)
print (request_song_url('Aesop Rock', 1))


# Scrape lyrics from a Genius.com song URL
def scrape_song_lyrics(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()
    #remove identifiers like chorus, verse, etc
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
    #remove empty lines
    lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])         
    return lyrics


def write_lyrics_to_file(artist_name, song_count):
    f = open('lyrics/' + artist_name.lower() + '.txt', 'wb')
    urls = request_song_url(artist_name, song_count)
    for url in urls:
        lyrics = scrape_song_lyrics(url)
        f.write(lyrics.encode("utf8"))
    f.close()
    num_lines = sum(1 for line in open('lyrics/' + artist_name.lower() + '.txt', 'rb'))
    print('Wrote {} lines to file from {} songs'.format(num_lines, song_count))
  
# DEMO  
write_lyrics_to_file('Kendrick Lamar', 100)