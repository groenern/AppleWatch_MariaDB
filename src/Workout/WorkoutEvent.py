class WorkoutEvent:
    def __init__(self, event):
        self.type = event.get('type')
        self.date = event.get('date')
        self.duration = event.get('duration')
        self.durationUnit = event.get('durationUnit')