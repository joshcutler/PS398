#First install BeautifulSoup: pip install BeautifulSoup
import urllib2
from BeautifulSoup import BeautifulSoup

#Open a webpage
webpage = urllib2.urlopen('http://polisci.duke.edu/graduate')
#Parse it
soup = BeautifulSoup(webpage.read())

#Print out the target destinations for the links
print "Links\n********************"
for link in soup('a'):
  print str(link['href'])
  
print "Headers\n********************"
for header in soup(['h1', 'h2', 'h3']):
  print "{0}: {1}".format(header.name, header.string)
  
#Crawl the next 3 links?
 
