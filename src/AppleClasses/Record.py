from src.AppleClasses.Device import Device
import uuid

class Record:
    def __init__(self, recordElem):
        self.recordKey = str(uuid.uuid4())
        self.type = recordElem.get('type')
        self.unit = recordElem.get('unit')
        self.value = recordElem.get('value')
        self.sourceName = recordElem.get('sourceName')
        self.sourceVersion = recordElem.get('sourceVersion')
        self.creationDate = recordElem.get('creationDate')[:10]
        self.startDate = recordElem.get('startDate')
        self.endDate = recordElem.get('endDate')

        self.deviceKey = Device(recordElem.get('device')).deviceKey
   
    def getValues(self):
        values = [self.recordKey, self.type, self.unit, self.value, self.sourceName, self.sourceVersion, self.deviceKey, self.creationDate, self.startDate, self.endDate]
        return [f"'{val}'" if isinstance(val, str) else 'NULL' if val is None else val for val in values]
    
    @staticmethod
    def __len__(self):
        return len(vars(self))
    
    @staticmethod
    def getColumns():
        return ['RecordKey', 'Type', 'Unit', 'Value', 'SourceName', 'SourceVersion', 'DeviceKey', 'CreationDate', 'StartDate', 'EndDate']
    
    @staticmethod
    def getColumnConstraints():
        return ['VARCHAR (64) NOT NULL PRIMARY KEY', 'VARCHAR (64)', 'VARCHAR(16)', 'VARCHAR(64)', 'VARCHAR(24)', 'VARCHAR(24)', 'VARCHAR(64)', 'VARCHAR(64)', 'VARCHAR(64)', 'VARCHAR(64)']