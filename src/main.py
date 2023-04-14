from Util import xmlParser

myXMLParser = xmlParser.XMLParser('export.xml')
myXMLParser.parse()
workouts = myXMLParser.getWorkouts()
records = myXMLParser.getRecords()