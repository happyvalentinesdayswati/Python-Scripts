from xml.dom import minidom
import csv 
import sys
import io

data = dict()

reload(sys)
sys.setdefaultencoding('utf-8')


xmldoc = minidom.parse('strings.xml')
itemlist = xmldoc.getElementsByTagName('string')
print(len(itemlist))
for s in itemlist:
	data[s.childNodes[0].nodeValue] = s.attributes['name'].value
    #print(s.attributes['name'].value)
    #print(s.childNodes[0].nodeValue)


for i in data:
    print i, data[i]

defaultStartString = "<?xml version=\"1.0\" encoding=\"utf-8\"?><resources>"+"\n"

with io.FileIO("foobar.txt", "a") as file:
  file.write(defaultStartString)

f = open(sys.argv[1], "rb")
reader = csv.reader(f)
for row in reader:
  with io.FileIO("foobar.txt", "a") as file:
    file.write("<string name=\""+data.get(row[0], None)+"\">"+row[1]+"</string>"+"\n")

with io.FileIO("foobar.txt", "a") as file:
  file.write("</resources>")
    

f.close()