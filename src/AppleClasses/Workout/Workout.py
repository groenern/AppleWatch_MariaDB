from src.AppleClasses.Workout.WorkoutStatistics import WorkoutStatistics
from src.AppleClasses.Workout.WorkoutEvent import WorkoutEvent
from src.AppleClasses.Workout.WorkoutActivity import WorkoutActivity
from src.AppleClasses.Device import Device
import uuid

class Workout:
    def __init__(self, workoutElement):
        self.workoutKey = str(uuid.uuid4())
        self.workoutActivityType = workoutElement.get('workoutActivityType')
        self.duration = workoutElement.get('duration')
        self.durationUnit = workoutElement.get('durationUnit')
        self.sourceName = workoutElement.get('sourceName')
        self.sourceVersion = workoutElement.get('sourceVersion')
        self.creationDate = workoutElement.get('creationDate')
        self.startDate = workoutElement.get('startDate')
        self.endDate = workoutElement.get('endDate')

        self.device = Device(workoutElement.get('device'))

        # Metadata
        self.indoorWorkout = ''
        self.averageMETs = ''
        self.elevationAscended = ''

        # Lists of Classes 
        self.workoutActivityList = []
        self.workoutEventList = []
        self.workoutStatisticList = []

        # Parse WorkoutActivity
        for activity in workoutElement.findall('.//WorkoutActivity'):
            self.workoutActivityList.append(WorkoutActivity(activity, self.workoutKey))

        # Parse WorkoutEvents
        for event in workoutElement.findall('.//WorkoutEvent'):
            self.workoutEventList.append(WorkoutEvent(event, self.workoutKey))

        # Parse WorkoutStatistics
        for statistic in workoutElement.findall('.//WorkoutStatistics'):
            self.workoutStatisticList.append(WorkoutStatistics(statistic, self.workoutKey))


        # TODO PARSE METADATA -> HKIndoorWorkout, METs only right now, can add Weather, Humidity, TimeZone
        metadataEntries = workoutElement.findall('.//MetadataEntry')

        for metadata in metadataEntries:
            if metadata.get('key') == 'HKIndoorWorkout':
                self.indoorWorkout = metadata.get('value')
            elif metadata.get('key') == 'HKAverageMETs':
                self.averageMETs = metadata.get('value')
            elif metadata.get('key') == 'HKElevationAscended':
                self.elevationAscended = metadata.get('value')

    def getDevice(self):
        return self.device

    # return object values as a list
    def getValues(self):
        values = [self.workoutKey, self.workoutActivityType, self.duration, self.durationUnit, self.sourceName, self.sourceVersion, 
                  self.device.deviceKey, self.creationDate, self.startDate, self.endDate, self.indoorWorkout, self.averageMETs, self.elevationAscended]
        return [f"'{val}'" if isinstance(val, str) else 'NULL' if val is None else val for val in values]

    @staticmethod
    def getColumns():
        columns = ['WorkoutKey', 'WorkoutActivityType', 'Duration', 'DurationUnit', 'SourceName', 'SourceVersion',
                    'DeviceKey', 'CreationDate', 'StartDate', 'EndDate', 'IndoorWorkout', 'AverageMETs', 'ElevationAscended']
        return columns
    
    @staticmethod
    def getColumnConstraints():
        columnDefinition = ['VARCHAR(64) NOT NULL', 'VARCHAR(128)', 'FLOAT', 'VARCHAR(8)', 'VARCHAR(24)', 'VARCHAR(24)',
                             'VARCHAR(64)', 'VARCHAR(64)', 'VARCHAR(64)', 'VARCHAR(64)','VARCHAR(4)', 'VARCHAR(64)', 'VARCHAR(32)']
        return columnDefinition