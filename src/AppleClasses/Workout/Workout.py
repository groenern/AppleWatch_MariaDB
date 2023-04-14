from src.AppleClasses.Workout.WorkoutStatistics import WorkoutStatistics
from src.AppleClasses.Workout.WorkoutEvent import WorkoutEvent
from src.AppleClasses.Workout.WorkoutActivity import WorkoutActivity
from src.AppleClasses.Device import Device

class Workout:
    def __init__(self, workoutElement):
        self.workoutActivityType = workoutElement.get('workoutActivityType')
        self.duration = workoutElement.get('duration')
        self.durationUnit = workoutElement.get('durationUnit')
        self.distance = workoutElement.get('totalDistance')
        self.distanceUnit = workoutElement.get('totalDistanceUnit')
        self.totalEnergyBurned = workoutElement.get('totalEnergyBurned')
        self.totalEnergyBurnedUnit = workoutElement.get('totalEnergyBurnedUnit')
        self.sourceName = workoutElement.get('sourceName')
        self.sourceVersion = workoutElement.get('sourceVersion')
        self.creationDate = workoutElement.get('creationDate')
        self.startDate = workoutElement.get('startDate')
        self.endDate = workoutElement.get('endDate')

        self.device = Device(workoutElement.get('device'))

        # Lists of Classes 
        self.workoutActivityList = []
        self.workoutEventList = []
        self.workoutStatisticList = []

        # Parse WorkoutActivity
        for activity in workoutElement.findall('.//WorkoutActivity'):
            self.workoutActivityList.append(WorkoutActivity(activity))

        # Parse WorkoutEvents
        for event in workoutElement.findall('.//WorkoutEvent'):
            self.workoutEventList.append(WorkoutEvent(event))

        # Parse WorkoutStatistics
        for statistic in workoutElement.findall('.//WorkoutStatistics'):
            self.workoutStatisticList.append(WorkoutStatistics(statistic))


        # TODO PARSE METADATA

    def getDevice(self):
        return self.device
    
    # return object values as a list
    def getValues(self):
        values = [self.workoutActivityType, self.duration, self.durationUnit, self.distance, self.distanceUnit, self.totalEnergyBurned, self.totalEnergyBurnedUnit, self.sourceName, self.sourceVersion, 
                  self.device.device, self.creationDate, self.startDate, self.endDate]
        return [f"'{val}'" if isinstance(val, str) else 'NULL' if val is None else val for val in values]

    @staticmethod
    def getColumns():
        columns = ['WorkoutActivityType', 'Duration', 'DurationUnit', 'Distance', 'DistanceUnit', 'EnergyBurned', 'EnergyUnit', 'SourceName', 'SourceVersion', 'Device', 'CreationDate', 'StartDate', 'EndDate']
        return columns
    
    @staticmethod
    def getColumnConstraints():
        columnDefinition = ['VARCHAR(255) NOT NULL', 'FLOAT', 'VARCHAR(8)', 'FLOAT', 'VARCHAR(8)', 'FLOAT', 'VARCHAR(8)', 'VARCHAR(24)', 'VARCHAR(24)', 'VARCHAR(64)', 'VARCHAR(64)', 'VARCHAR(64)', 'VARCHAR(64)']
        return columnDefinition