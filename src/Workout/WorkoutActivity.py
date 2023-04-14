class WorkoutActivity:
    def __init__(self, activity):
        self.uuid = activity.get('uuid')
        self.startDate = activity.get('startDate')
        self.endDate = activity.get('endDate')
        self.duration = activity.get('duration')
        self.durationUnit = activity.get('durationUnit')
