import uuid

class WorkoutStatistics:
    def __init__(self, statistic, workoutKey):
        self.statisticKey = str(uuid.uuid4())
        self.type = statistic.get('type')
        self.startDate = statistic.get('startDate')
        self.endDate = statistic.get('endDate')
        self.average = statistic.get('average')
        self.minimum = statistic.get('minimum')
        self.maximum = statistic.get('maximum')
        self.sum = statistic.get('sum')
        self.unit = statistic.get('unit')
        self.workoutKey = workoutKey

    def getValues(self):
        values = [self.statisticKey, self.type, self.startDate, self.endDate, self.average, self.minimum, self. maximum, self.sum, self.unit, self.workoutKey]
        return [f"'{val}'" if isinstance(val, str) else 'NULL' if val is None else val for val in values]
    
    @staticmethod
    def getColumns():
        return ['EventKey', 'Type', 'StartDate', 'EndDate', 'Average', 'Min', 'Max', 'Sum', 'Unit', 'WorkoutKey']
    
    @staticmethod
    def getColumnConstraints():
        return ['VARCHAR(64) NOT NULL PRIMARY KEY', 'VARCHAR(64)', 'VARCHAR(64)', 'VARCHAR(64)', 'FLOAT', 'FLOAT', 'FLOAT', 'FLOAT', 'VARCHAR(16)', 'VARCHAR(64)']
    