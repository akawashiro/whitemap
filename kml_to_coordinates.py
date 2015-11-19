import xml.etree.ElementTree as ET
import sys

prefix = "{http://www.opengis.net/kml/2.2}"

if __name__ == '__main__':
    f = open(sys.argv[1])
    root = ET.fromstring(f.read())
    print root.find(prefix+"Document").find(prefix+"Placemark").find(prefix+"LineString").find(prefix+"coordinates").text
    
