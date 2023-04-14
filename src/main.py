from Util import xmlParser, mariaDB
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

def main():
    workouts, records = populateData()

    myConn = connectToDatabase()

    # TODO Add Enum of Tables so no string literals 
    myConn.populateTable('Workouts', workouts)

    myConn.closeConnection()

if __name__ == "__main__":
    main()