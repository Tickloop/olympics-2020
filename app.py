import requests
from bs4 import BeautifulSoup
import csv
import datetime

# tries to get the medal count, else returns 0
def get_medal_count(tr, medal):
    try: 
        # finding all the links 
        links = tr.find_all("a")
        
        # searching for the desired one to get the medal count
        for link in links:
            # if the title contains <medal> like Gold then it will contain the number of gold medals
            if medal in link['title']:
                # we can stop looking now
                return int(link.text)
    except:
        return 0

# creates a soup from our URL
def make_soup():
    # URL of the standings
    URL = 'https://olympics.com/tokyo-2020/olympic-games/en/results/all-sports/medal-standings.htm?utm_campaign=dp_google'

    # fetching data form the webpage to scrape
    r = requests.get(URL)
    
    # making the soup
    return BeautifulSoup(r.content, 'html5lib')

# creates a dictonary from a row of the table
def make_country(tr):
    # dictonary to store the standing for a country
    country = {}

    # country name
    ct = tr.find_next('td').find_next('td').div.text.strip()
    
    # 3 character coutnry code 
    ct_code = tr.find_next('td').find_next('td').div['country'].strip()

    # saving to corresponding keys in dictonary
    country['ct'] = ct
    country['ct_code'] = ct_code
    country['gold'] =  get_medal_count(tr,'Gold')
    country['silver'] = get_medal_count(tr,'Silver')
    country['bronze'] = get_medal_count(tr,'Bronze')

    return country

def main():
    # creating the soup to scrape
    soup = make_soup()

    # the table body that conatins all the rows
    tbody = soup.find('table', attrs={'id': 'medal-standing-table'}).tbody

    # will store all the standings in this list
    standings = []

    # look through all the rows of the table
    for tr in tbody.findAll('tr'):
        country = make_country(tr)

        # store them in our list of standings 
        standings.append(country)
    
    save_csv(standings)

# serialize standings, save them as csv
def save_csv(standings):
    # the name of the new file will be <year>-<month>-<day>-standings.csv
    d = datetime.datetime.now()
    filename = f"data/{d.year}-{d.month}-{d.day}-standings.csv"

    # writing all the standings to a csv
    with open(filename, mode='w') as new_csv:
        standings_writer = csv.writer(new_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        # prints out a new header
        standings_writer.writerow(['country', 'country_code', 'gold', 'silver', 'bronze'])
        
        # write out all the standings
        for c in standings:
            # the list comprehension is the same as [c['ct'], c['ct_code'], c['gold'], c['silver'], c['bronze']]
            standings_writer.writerow([c[key] for key in c])

if __name__ == "__main__":
    main()