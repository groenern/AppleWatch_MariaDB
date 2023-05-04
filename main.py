from src.Util.mariaDBConnector import MariaDBConnector
from src.Util.mariaDBHandler import MariaDBHandler
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    mariaDBConfig = config['mariaDB']

    mariaDBHost = mariaDBConfig['host']
    mariaDBUser = mariaDBConfig['user']
    mariaDBPass = mariaDBConfig['pass']
    mariaDBDatabase = mariaDBConfig['database']

    myConn = MariaDBConnector(mariaDBHost, mariaDBUser, mariaDBPass, mariaDBDatabase)
    
    # Create MariaDBHandler and Connect
    myHandler = MariaDBHandler(myConn)
    myHandler.connect()

    # Populate MariaDB Database
    myHandler.populateData()
    myHandler.createTables()
    myHandler.populateTables()
    
    # Upload Workout Data to Google Sheets
    myHandler.uploadWorkoutData()
    
    # End Connection
    myHandler.closeConnection()

    # SELECT R.Type FROM Records R JOIN RecordWorkoutKey RWK ON R.RecordKey = RWK.RecordKey WHERE RWK.WorkoutKey = 'f9c4d507-812a-4adb-8e2d-84bba5ba2942';
    # INSTLAL XUBUNTU
    
if __name__ == "__main__":
    main()
