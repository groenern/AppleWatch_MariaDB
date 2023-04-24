import uuid

class WorkoutActivity:
    def __init__(self, activity, workoutKey):
        self.activityKey = str(uuid.uuid4())
        self.workoutKey = workoutKey
        self.uuid = activity.get('uuid')
        self.startDate = activity.get('startDate')
        self.endDate = activity.get('endDate')
        self.duration = activity.get('duration')
        self.durationUnit = activity.get('durationUnit')

    def getValues(self):
        values = [self.activityKey, self.uuid, self.startDate, self.endDate, self.duration, self.durationUnit, self.workoutKey]
        return [f"'{val}'" if isinstance(val, str) else 'NULL' if val is None else val for val in values]
    
    @staticmethod
    def getColumns():
        return ['ActivityKey', 'uuid', 'StartDate', 'EndDate', 'Duration', 'DurationUnit', 'WorkoutKey']
    
    @staticmethod
    def getColumnConstraints():
        return ['VARCHAR(64) NOT NULL PRIMARY KEY', 'VARCHAR(64)', 'VARCHAR(32)', 'VARCHAR(32)', 'FLOAT', 'VARCHAR(16)', 'VARCHAR(64)']
    