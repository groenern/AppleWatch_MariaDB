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
        self.device = workoutElement.get('device')
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

        # TODO __STR__