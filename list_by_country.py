import urllib.request
import json

# URL of the JSON file
url = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json"

# Read the JSON data from the URL
response = urllib.request.urlopen(url)
data = response.read()

# # Decode the JSON data
books = json.loads(data)
my_output={}
# unique_countries = {}
# unique_author = {}
# books = [
#   {
#     "author": "Chinua Achebe",
#     "country": "Nigeria",
#     "imageLink": "images/things-fall-apart.jpg",
#     "language": "English",
#     "link": "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",
#     "pages": 209,
#     "title": "Things Fall Apart",
#     "year": 1958
#   },
#   {
#     "author": "Chinua Achebe",
#     "country": "Nigeria",
#     "imageLink": "images/things-fall-apart.jpg",
#     "language": "English",
#     "link": "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",
#     "pages": 209,
#     "title": "Things Fall Apart",
#     "year": 1958
#   },
# ]

# author = book[0].get('author')
# country = book[0].get('country')
# title = book[0].get('title')
# language = book[0].get('language')
for book in books:
    author = book.get('author')
    country = book.get('country')
    title = book.get('title')
    language = book.get('language')

    if country not in my_output:
        my_output[country] = {}
    if author not in my_output[country]:
        my_output[country][author] = {'title':[], 'language':[]}
    my_output[country][author]['title'].append(title)
    my_output[country][author]['language'].append(language)
print(my_output)