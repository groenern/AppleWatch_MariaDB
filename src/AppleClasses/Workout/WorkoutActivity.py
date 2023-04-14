class WorkoutActivity:
    def __init__(self, activity, workoutKey):
        self.workoutKey = workoutKey
        self.uuid = activity.get('uuid')
        self.startDate = activity.get('startDate')
        self.endDate = activity.get('endDate')
        self.duration = activity.get('duration')
        self.durationUnit = activity.get('durationUnit')

    def getValues(self):
        values = [self.workoutKey, self.uuid, self.startDate, self.endDate, self.duration, self.durationUnit]
        return [f"'{val}'" if isinstance(val, str) else 'NULL' if val is None else val for val in values]
    
    @staticmethod
    def getColumns():
        return ['WorkoutKey', 'uuid', 'StartDate', 'EndDate', 'Duration', 'DurationUnit']
    
    @staticmethod
    def getColumnConstraints():
        return ['VARCHAR(64) NOT NULL', 'VARCHAR(64)', 'VARCHAR(32)', 'VARCHAR(32)', 'FLOAT', 'VARCHAR(16)']
    