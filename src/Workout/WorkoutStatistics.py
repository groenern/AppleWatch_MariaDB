class WorkoutStatistics:
    def __init__(self, statistic):
        self.type = statistic.get('type')
        self.startDate = statistic.get('startDate')
        self.endDate = statistic.get('endDate')
        self.average = statistic.get('average')
        self.minimum = statistic.get('minimum')
        self.maximum = statistic.get('maximum')
        self.sum = statistic.get('sum')
        self.unit = statistic.get('unit')
                                  