class Device:
    def __init__(self, deviceString):
        self.deviceKey = None
        self.name = None
        self.manufacturer = None
        self.model = None
        self.hardware = None
        self.software = None

        if deviceString:
            self.deviceKey = deviceString.split(":")[1].split(">")[0]
            
            # Split the input string by comma and iterate over each element
            for element in deviceString.split(","):
                element = element.strip()  # Remove leading/trailing spaces
                
                # Check if element starts with a valid attribute name
                if element.startswith("name:"):
                    self.name = element.split(":")[1]
                elif element.startswith("manufacturer:"):
                    self.manufacturer = element.split(":")[1]
                elif element.startswith("model:"):
                    self.model = element.split(":")[1]
                elif element.startswith("hardware:"):
                    self.hardware = element.split(":")[1]
                elif element.startswith("software:"):
                    self.software = element.split(":")[1].rstrip(">")
        else:
            self.deviceKey = 'NULL'
            self.name = 'NULL'
            self.manufacturer = 'NULL'
            self.model = 'NULL'
            self.hardware = 'NULL'
            self.software = 'NULL'

    def getValues(self):
        values = [self.deviceKey, self.name, self.manufacturer, self.model, self.hardware, self.software]
        return [val if val is None else f'"{val}"' if isinstance(val, str) and not (val.startswith("'") and val.endswith("'")) else val for val in values]
    
    @staticmethod
    def getColumns():
        return ['DeviceKey', 'Name', 'Manufacturer', 'Model', 'Hardware', 'Software']
    
    def getColumnConstraints():
        return ['VARCHAR(32) NOT NULL', 'VARCHAR(16)', 'VARCHAR(16)', 'VARCHAR(8)', 'VARCHAR(16)', 'VARCHAR(8)']