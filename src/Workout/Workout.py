from Workout import WorkoutActivity
from Workout import WorkoutEvent
from Workout import WorkoutStatistics

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
        # self.device = workoutElement.get('device') // TODO ADD Device Class and Add Handling
        self.creationDate = workoutElement.get('creationDate')
        self.startDate = workoutElement.get('startDate')
        self.endDate = workoutElement.get('endDate')


        # Lists of Classes 
        self.workoutActivityList = []
        self.workoutEventList = []
        self.workoutRouteList = []
        self.workoutStatisticsList = []

        # Parse WorkoutActivity
        for activity in workoutElement.findall('.//WorkoutActivity'):
            self.workoutActivityList.append(WorkoutActivity.WorkoutActivity(activity))

        # Parse WorkoutEvents
        for event in workoutElement.findall('.//WorkoutEvent'):
            self.workoutEventList.append(WorkoutEvent.WorkoutEvent(event))

        # Parse WorkoutStatistics
        for statistic in workoutElement.findall('.//WorkoutStatistics'):
            self.workoutStatisticsList.append(WorkoutStatistics.WorkoutStatistics(statistic))


        # TODO PARSE METADATA

    # return object values as a list
    def getValues(self):
        values = [self.workoutActivityType, self.duration, self.durationUnit, self.distance, self.distanceUnit, self.totalEnergyBurned, self.totalEnergyBurnedUnit, self.sourceName, self.sourceVersion, self.creationDate, self.startDate, self.endDate]
        return [f"'{val}'" if isinstance(val, str) else 'NULL' if val is None else val for val in values]

    @staticmethod
    def getColumns():
        columns = ['WorkoutActivityType', 'Duration', 'DurationUnit', 'Distance', 'DistanceUnit', 'EnergyBurned', 'EnergyUnit', 'SourceName', 'SourceVersion', 'CreationDate', 'StartDate', 'EndDate']
        return columns
    
    @staticmethod
    def getColumnDefinition():
        columnDefinition = ['VARCHAR(255) NOT NULL', 'FLOAT', 'VARCHAR(8)', 'FLOAT', 'VARCHAR(8)', 'FLOAT', 'VARCHAR(8)', 'VARCHAR(24)', 'VARCHAR(24)', 'VARCHAR(64)', 'VARCHAR(64)', 'VARCHAR(64)']
        return columnDefinition