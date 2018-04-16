import urllib2
import re
import csv
import sys
from bs4 import BeautifulSoup
from dateutil import parser
reload(sys)
sys.setdefaultencoding('utf8')


class MovieRatingScraper():

    def __init__(self):
        self.url = "http://www.imdb.com"
        self.subdomain = "/chart/toptv/?ref_=nv_tvv_250_3"
        self.movieList = []

    def __download_html(self, url):
        response = urllib2.urlopen(url)
        html = response.read()
        return html

    def scrape(self):

        html = self.__download_html(self.url+self.subdomain)
        bs = BeautifulSoup(html, 'lxml')
        table = bs.find('table')

        for row in table.findAll('tr'):
            str = row.text.split('\n')
            if (len(str)!=7):
                title = str[11].strip()
                anio = str[12].strip()[1:-1]
                rating = str[15].strip()
                movie = [title,anio,rating]
                self.movieList.append(movie)

    def data2csv(self, filename):

        file = open('../csv/' + filename,'w+')

        for i in range(len(self.movieList)):
            for j in range(len(self.movieList[i])):
                file.write(self.movieList[i][j]+';')
            file.write('\n');