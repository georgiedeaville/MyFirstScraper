# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# The next line is importing the scraper wiki library
import scraperwiki
import lxml.html

## the lines above imports the library

print("hello")
## prints the word hello

html = scraperwiki.scrape("http://foo.com")
## grabs html from the webpage
print(html)
## displays the html of the webpage

# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
## html is being used as an ingredient by the function fromstring which is part of the lxml.html library
## root is the new variable
print(root.cssselect("div#footer"))
## lxml.html is using the root variable
print(root)

listofmatches=root.cssselect("a")
for match in listofmatches:
      print(match)
      print(lxml.html.tostring(match))

# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
