from src.Util import xmlParser, mariaDB
import configparser

def connectToDatabase():
    # Create Config Object and parse
    config = configparser.ConfigParser()
    config.read('config.ini')

    mariaDBConfig = config['mariaDB']

    mariaDBHost = mariaDBConfig['host']
    mariaDBUser = mariaDBConfig['user']
    mariaDBPass = mariaDBConfig['pass']
    mariaDBDatabase = mariaDBConfig['database']

    # Connect to MariaDB
    myConn = mariaDB.MariaDBConnector(mariaDBHost, mariaDBUser, mariaDBPass, mariaDBDatabase)
    myConn.connect()

    return myConn

def populateData():
    # Parse and populate workouts/records
    myXMLParser = xmlParser.XMLParser('export.xml')
    myXMLParser.parse()
    workouts = myXMLParser.getWorkouts()
    records = myXMLParser.getRecords()
    
    return workouts, records

def getUniqueDevices(workouts):
    uniqueDevices = []
    uniqueDeviceValues = []

    # Create Unique Devices List
    for workout in workouts:
        device = workout.getDevice()
        deviceValues = device.getValues()

        if deviceValues not in uniqueDeviceValues and '"NULL"' not in deviceValues:
            uniqueDevices.append(device)
            uniqueDeviceValues.append(deviceValues)

    return uniqueDevices

def main():
    workouts, records = populateData()

    myConn = connectToDatabase()
    
    # TODO Add Enum of Tables so no string literals 
    myConn.populateTable('Workouts', workouts)
    myConn.populateTable('Records', records)

    uniqueDevices = getUniqueDevices(workouts)
    myConn.populateTable('Devices', uniqueDevices)
    
    # Populate WorkoutActivities, Events, Statistics
    workoutActivities = []
    workoutEvents = []
    workoutStats = []

    for workout in workouts:
        if workout.workoutActivityList != []:
            for activity in workout.workoutActivityList:
                workoutActivities.append(activity)
        
        if workout.workoutEventList != []:
            for event in workout.workoutEventList:
                workoutEvents.append(event)

        if workout.workoutStatisticList != []:
            for statistic in workout.workoutStatisticList:
                workoutStats.append(statistic)
    
    myConn.populateTable('Activities', workoutActivities)
    myConn.populateTable('Events', workoutEvents)
    myConn.populateTable('Statistics', workoutStats)

    # Create Workout Records Table 

    myConn.closeConnection()

if __name__ == "__main__":
    main()