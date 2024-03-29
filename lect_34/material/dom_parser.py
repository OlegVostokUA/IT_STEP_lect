from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print(f"Root element : {collection.getAttribute('shelf')}")

# Get all the movies in the collection
movies = collection.getElementsByTagName("movie")

# Print detail of each movie.
for movie in movies:
   print("*****Movie*****")
   if movie.hasAttribute("title"):
      print(f"Title: {movie.getAttribute('title')}")

   type = movie.getElementsByTagName('type')[0]
   print(f"Type: {type.childNodes[0].data}")
   format = movie.getElementsByTagName('format')[0]
   print(f"Format: {format.childNodes[0].data}")
   rating = movie.getElementsByTagName('rating')[0]
   print(f"Rating: {rating.childNodes[0].data}")
   description = movie.getElementsByTagName('description')[0]
   print(f"Description: {description.childNodes[0].data}")
