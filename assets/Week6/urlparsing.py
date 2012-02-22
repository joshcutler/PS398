from urlparse import *

url1 = urljoin("http://www.duke.edu", "bob/test.html")
url2 = urljoin("http://www.duke.edu", "/")
url3 = urljoin("http://www.duke.edu", "http://www.fark.com")
url4 = urljoin("http://www.duke.edu", "http://www.fark.com/test.html")

for url in [url1, url2, url3, url4]:
  p = urlparse(url)
  print "{0}://{1}{2}: {3}".format(p.scheme, p.hostname, p.path, "is duke" if (p.hostname == "www.duke.edu") else "is not duke")
