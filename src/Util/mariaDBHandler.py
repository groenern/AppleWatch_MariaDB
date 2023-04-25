from src.Util.mariaDBConnector import MariaDBConnector
from src.Util.xmlParser import XMLParser
from src.AppleClasses.WorkoutClasses import Workout
from src.AppleClasses.Record import Record
from src.AppleClasses.Device import Device
import configparser
from src.Util.GoogleHandler import GoogleHandler

class MariaDBHandler:
    def __init__(self, mariaDBConnector):
        self.connector = mariaDBConnector
        self.workouts = []
        self.records = []
        self.uniqueDevices = []
        self.workoutRecords = {}
        self.gHandler = None

    def connect(self):
        self.connector.connect()

    def populateData(self):
        myXMLParser = XMLParser('export.xml')
        myXMLParser.parse()
        self.workouts = myXMLParser.getWorkouts()
        self.records = myXMLParser.getRecords()
        self.linkWorkoutRecords()

    def createTables(self):
        print("Creating Tables...")
        self.connector.createTable('Workouts', Workout.Workout.getColumns(), Workout.Workout.getColumnConstraints()) 
        self.connector.createTable('Records', Record.getColumns(), Record.getColumnConstraints())
        self.connector.createTable('Devices', Device.getColumns(), Device.getColumnConstraints())
        self.connector.createTable('Activities', Workout.WorkoutActivity.getColumns(), Workout.WorkoutActivity.getColumnConstraints())
        self.connector.createTable('Events', Workout.WorkoutEvent.getColumns(), Workout.WorkoutEvent.getColumnConstraints())
        self.connector.createTable('Statistics', Workout.WorkoutStatistics.getColumns(), Workout.WorkoutStatistics.getColumnConstraints())
        
        self.createForeignKeys('Workouts', 'fk_DeviceWorkouts', 'DeviceKey', 'Devices')
        # self.createForeignKeys('Records', 'fk_DeviceRecords', 'DeviceKey', 'Devices') Doesn't Work Currently
        self.createForeignKeys('Activities', 'fk_WorkoutActivities', 'WorkoutKey', 'Workouts')
        self.createForeignKeys('Events', 'fk_WorkoutEvents', 'WorkoutKey', 'Workouts')
        self.createForeignKeys('Statistics', 'fk_WorkoutStats', 'WorkoutKey', 'Workouts')

        # Create a RecordWorkoutKey table to link Records to Workouts 
        columns = ['RecordKey', 'WorkoutKey']
        columnConstraints = ['VARCHAR(64) NOT NULL PRIMARY KEY', 'VARCHAR(64)']

        self.connector.createTable('RecordWorkoutKey', columns, columnConstraints)
        self.createForeignKeys('RecordWorkoutKey', 'fk_WorkoutKey', 'WorkoutKey', 'Workouts')

    def createForeignKeys(self, tableName, constraintName, foreignKeyName, referenceTableName):
        query = f"""ALTER TABLE {tableName}
                    ADD CONSTRAINT {constraintName}
                    FOREIGN KEY ({foreignKeyName}) REFERENCES {referenceTableName}({foreignKeyName});"""
        self.connector.executeQuery(query)

    def populateTables(self):
        # Find Unique Devices
        self.getUniqueDevices()
        self.connector.populateTable('Devices', self.uniqueDevices)
        
        # Easiest to populate
        self.connector.populateTable('Workouts', self.workouts)
        self.connector.populateTable('Records', self.records)
        
        # Populate RecordWorkoutKey
        print("Populating RecordWorkoutKey...")
        failCount = 0
        queryCount = 0

        for recordKey in self.workoutRecords:
            sqlQuery = f'INSERT INTO RecordWorkoutKey VALUES (\'{recordKey}\', \'{self.workoutRecords[recordKey]}\');'

            if(self.connector.executeQuery(sqlQuery)):
                queryCount += 1
            else:
                failCount += 1
        
        print(f"{queryCount} queries executed sucessfully, {failCount} queries failed")

        # Populate WorkoutActivities, Events, Statistics
        workoutActivities = []
        workoutEvents = []
        workoutStats = []

        for workout in self.workouts:
            if workout.workoutActivityList != []:
                for activity in workout.workoutActivityList:
                    workoutActivities.append(activity)
            
            if workout.workoutEventList != []:
                for event in workout.workoutEventList:
                    workoutEvents.append(event)

            if workout.workoutStatisticList != []:
                for statistic in workout.workoutStatisticList:
                    workoutStats.append(statistic)
        
        self.connector.populateTable('Activities', workoutActivities)
        self.connector.populateTable('Events', workoutEvents)
        self.connector.populateTable('Statistics', workoutStats)

    def getUniqueDevices(self):
        uniqueDeviceValues = []

        # Create Unique Devices List
        for workout in self.workouts:
            device = workout.getDevice()
            deviceValues = device.getValues()

            if deviceValues not in uniqueDeviceValues:
                self.uniqueDevices.append(device)
                uniqueDeviceValues.append(deviceValues)

    def closeConnection(self):
        self.connector.closeConnection()

    def linkWorkoutRecords(self):

        for r in self.records:
            for w in self.workouts:
                if r.creationDate == w.creationDate and r.startDate >= w.startDate and r.endDate <= w.endDate:
                    self.workoutRecords[r.recordKey] = w.workoutKey

    def uploadWorkoutData(self):
        print("Connecting to Google Sheets...")
        config = configparser.ConfigParser()
        config.read('config.ini')

        email = config['user']['email']
        credentials = config['user']['credentials']
        spreadsheetName = config['spreadsheet']['title']
            
        self.gHandler = GoogleHandler(email, credentials,spreadsheetName)

        # create and populates workouts
        numRows = len(self.workouts)
        numCols = 7

        self.gHandler.createWorksheet("Workouts", numRows, numCols)
        self.gHandler.populateWorksheet("Workouts", self.workouts)

        print(str(self.gHandler))
