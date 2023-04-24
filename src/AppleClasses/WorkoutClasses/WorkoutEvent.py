import uuid

class WorkoutEvent:
    def __init__(self, event, workoutKey):
        self.activityKey = str(uuid.uuid4())
        self.type = event.get('type')
        self.date = event.get('date')
        self.duration = event.get('duration')
        self.durationUnit = event.get('durationUnit')
        self.workoutKey = workoutKey

    def getValues(self):
        values = [self.activityKey, self.type, self.date, self.duration, self.durationUnit, self.workoutKey]
        return [f"'{val}'" if isinstance(val, str) else 'NULL' if val is None else val for val in values]
    
    @staticmethod
    def getColumns():
        return ['EventKey', 'Type', 'Date', 'Duration', 'DurationUnit', 'WorkoutKey']
    
    @staticmethod
    def getColumnConstraints():
        return ['VARCHAR(64) PRIMARY KEY', 'VARCHAR (32)', 'VARCHAR(64)', 'FLOAT', 'VARCHAR (16)', 'VARCHAR(64)']