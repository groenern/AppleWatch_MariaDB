class WorkoutStatistics:
    def __init__(self, statistic, workoutKey):
        self.workoutKey = workoutKey
        self.type = statistic.get('type')
        self.startDate = statistic.get('startDate')
        self.endDate = statistic.get('endDate')
        self.average = statistic.get('average')
        self.minimum = statistic.get('minimum')
        self.maximum = statistic.get('maximum')
        self.sum = statistic.get('sum')
        self.unit = statistic.get('unit')

    def getValues(self):
        values = [self.workoutKey, self.type, self.startDate, self.endDate, self.average, self.minimum, self. maximum, self.sum, self.unit]
        return [f"'{val}'" if isinstance(val, str) else 'NULL' if val is None else val for val in values]
    
    @staticmethod
    def getColumns():
        return ['WorkoutKey', 'Type', 'StartDate', 'EndDate', 'Average', 'Min', 'Max', 'Sum', 'Unit']
    
    @staticmethod
    def getColumnConstraints():
        return ['VARCHAR(64) NOT NULL', 'VARCHAR(64)', 'VARCHAR(64)', 'VARCHAR(64)', 'FLOAT', 'FLOAT', 'FLOAT', 'FLOAT', 'VARCHAR(16)']