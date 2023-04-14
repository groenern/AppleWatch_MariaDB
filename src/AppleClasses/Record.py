from src.AppleClasses.Device import Device

class Record:
    def __init__(self, recordElem):
        self.type = recordElem.get('type')
        self.unit = recordElem.get('unit')
        self.value = recordElem.get('value')
        self.sourceName = recordElem.get('sourceName')
        self.sourceVersion = recordElem.get('sourceVersion')
        self.creationDate = recordElem.get('creationDate')
        self.startDate = recordElem.get('startDate')
        self.endDate = recordElem.get('endDate')

        self.device = Device(recordElem.get('device'))

    def getValues(self):
        values = [self.type, self.unit, self.value, self.sourceName, self.sourceVersion, self.device.device, self.creationDate, self.startDate, self.endDate]
        return [f"'{val}'" if isinstance(val, str) else 'NULL' if val is None else val for val in values]
    
    @staticmethod
    def getColumns():
        return ['Type', 'Unit', 'Value', 'SourceName', 'SourceVersion', 'Device', 'CreationDate', 'StartDate', 'EndDate']
    
    @staticmethod
    def getColumnConstraints():
        return ['VARCHAR (64) NOT NULL', 'VARCHAR(16)', 'VARCHAR(64)', 'VARCHAR(24)', 'VARCHAR(24)', 'VARCHAR(64)', 'VARCHAR(64)', 'VARCHAR(64)', 'VARCHAR(64)']