class WorkoutEvent:
    def __init__(self, event):
        self.type = event.get('type')
        self.date = event.get('date')
        self.duration = event.get('duration')
        self.durationUnit = event.get('durationUnit')

    def getValues(self):
        values = [self.type, self.date, self.duration, self.durationUnit]
        return [f"'{val}'" if isinstance(val, str) else 'NULL' if val is None else val for val in values]
    
    @staticmethod
    def getColumns():
        return ['Type', 'Date', 'Duration', 'DurationUnit']
    
    @staticmethod
    def getColumnConstraints():
        return ['VARCHAR (32) NOT NULL', 'VARCHAR(64)', 'FLOAT', 'VARCHAR (16)']
    