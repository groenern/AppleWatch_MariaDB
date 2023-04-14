import mariadb
from src.AppleClasses.Workout import Workout
from src.AppleClasses.Record import Record
from src.AppleClasses.Device import Device

class MariaDBConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
        self.connection = None
        self.cursor = None

    def connect(self):
        # Connect to MariaDB
        try:
            self.connection = mariadb.connect(
                host=self.host,
                user=self.user,
                password=self.password,
            )
            self.cursor = self.connection.cursor()

            print("Connected to MariaDB")
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            return

        # Set the Object Cursor to use MariaDBDatabase
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
        
        try:
            self.cursor.execute("USE " + self.database)

            print("Connected to " + self.database)
        except mariadb.Error as e:
            print(f"Error connecting to Database: {e}")
            return

        # Create Tables
        self.createTable('AppleWorkouts', Workout.Workout.getColumns(), Workout.Workout.getColumnConstraints())
        self.createTable('AppleRecords', Record.getColumns(), Record.getColumnConstraints())
        self.createTable('AppleDevices', Device.getColumns(), Device.getColumnConstraints())
        self.createTable('AppleWorkoutActivity', Workout.WorkoutActivity.getColumns(), Workout.WorkoutActivity.getColumnConstraints())
        self.createTable('AppleWorkoutEvent', Workout.WorkoutEvent.getColumns(), Workout.WorkoutEvent.getColumnConstraints())
        self.createTable('AppleWorkoutStatistics', Workout.WorkoutStatistics.getColumns(), Workout.WorkoutStatistics.getColumnConstraints())
    # https://www.mariadbtutorial.com/mariadb-basics/mariadb-create-table/
    def createTable(self, tableName, columnNames, columnDefinition):
        try:
            # Build the CREATE TABLE statement with column definitions
            columns = [f"{name} {definition}" for name, definition in zip(columnNames, columnDefinition)]
            sqlQuery = f"CREATE TABLE IF NOT EXISTS {tableName} ({','.join(columns)});"

            self.cursor.execute(sqlQuery)
            self.connection.commit()

            print(tableName + " table created")
        except mariadb.Error as e:
            print(f"Error creating table: {e}") 

    def populateTable(self, tableName, data):
        queryCount = 0
        failCount = 0

        for datum in data:
            sql = f"INSERT INTO {tableName} ({','.join(datum.getColumns())}) VALUES ({','.join(datum.getValues())});"

            if(self.executeQuery(sql)):
                queryCount += 1
            else:
                failCount += 1
        
        print(str(queryCount) + " queries executed sucessfully, " + str(failCount) + " queries failed")
        self.connection.commit()

    def executeQuery(self, query):
        try:
            self.cursor.execute(query)

            return True
        except mariadb.Error as e:
            print(f"Error executing query: {e}")
            
    def closeConnection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")

