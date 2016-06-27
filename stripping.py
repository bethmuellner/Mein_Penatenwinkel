import codecs

f = open("mein_penatenwinkel.xml", "r")

clean = f.strip()

with codecs.open("mein_penn_stripped", "w", "utf-8") as out:
	out.write(unicode(clean))
