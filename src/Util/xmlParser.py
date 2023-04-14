import xml.etree.ElementTree as ET
from src.AppleClasses.Workout import Workout
from src.AppleClasses.Record import Record

class XMLParser:
    def __init__(self, fileName):
        self.fileName = fileName
        self.workouts = []
        self.records = []
        self.exportDate = ''

    def parse(self):
        tree = ET.parse(self.fileName)
        root = tree.getroot()

        print("Parsing " + self.fileName)

        # retrieve export date
        self.exportDate = root.find('ExportDate').get('value')
        print("Export Date: " + self.exportDate)

        self.workoutCount = 0

        # Find all Workout elements and append a Workout object for each one
        for workout in root.findall('.//Workout'):
            self.workouts.append(Workout.Workout(workout))
            self.workoutCount += 1

        print(str(self.workoutCount) + " workouts parsed")
        self.recordCount = 0

        # Find all record elements and append object
        for record in root.findall('.//Record'):
            self.records.append(Record(record))
            self.recordCount += 1
        
        print(str(self.recordCount) + " records parsed")

    def getExportDate(self):
        return self.exportDate
    
    def getWorkouts(self):
        return self.workouts
    
    def getRecords(self):
        return self.records