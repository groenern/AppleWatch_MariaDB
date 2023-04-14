class Record:
    def __init__(self, recordElem):
        self.type = recordElem.get('type')
        self.unit = recordElem.get('unit')
        self.value = recordElem.get('value')
        self.sourceName = recordElem.get('sourceName')
        self.sourceVersion = recordElem.get('sourceVersion')
        self.device = recordElem.get('device')
        self.creationDate = recordElem.get('creationDate')
        self.startDate = recordElem.get('startDate')
        self.endDate = recordElem.get('endDate')