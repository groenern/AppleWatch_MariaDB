import gspread
from oauth2client.service_account import ServiceAccountCredentials
from src.AppleClasses.WorkoutClasses.Workout import Workout

class GoogleHandler:
    def __init__(self, userEmail, credentials, spreadSheetName):
        self.userEmail = userEmail

        # Authorize the client using the loaded credentials
        self.scope = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets']
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials, self.scope)
        self.client = gspread.authorize(self.credentials)
        print("Connected using Gspread")
    
        # Check if the spreadsheet name already exists
        self.spreadsheet = None
        for sheet in self.client.openall():
            if sheet.title == spreadSheetName:
                print("Spreadsheet already exists")
                self.spreadsheet = sheet
                break
        
        # If the spreadsheet name does not exist, create a new one and share
        if not self.spreadsheet:
            self.spreadsheet = self.client.create(spreadSheetName)
            self.spreadsheet.share(self.userEmail, perm_type='user', role='writer')

    def getWorksheet(self, worksheetName):
        # Get the worksheet with the specified name
        worksheet = self.spreadsheet.worksheet(worksheetName)

        return worksheet
    
    def createWorksheet(self, worksheetName, worksheetRows, worksheetCols):
        # Check "sheet1" exists and if it does rename it
        worksheet = None
        try:
            worksheet = self.spreadsheet.worksheet('Sheet1') 
            worksheet.update_title(worksheetName)
        except gspread.exceptions.WorksheetNotFound:
            pass
        
        # Check worksheetName to see if it exists
        worksheet = None
        try:
            worksheet = self.spreadsheet.worksheet(worksheetName)
        except gspread.exceptions.WorksheetNotFound:
            pass 

        # If the worksheet doesn't exist, create it
        if not worksheet:
            worksheet = self.spreadsheet.add_worksheet(worksheetName, worksheetRows, worksheetCols)
    
    # for passing workouts, runs, walks etc.
    def populateWorksheet(self, worksheetName, workouts):
        worksheet = self.spreadsheet.worksheet(worksheetName)
        worksheet.clear() 

        headers = ['Date', 'Workout Type']
        rows = [headers]

        for workout in workouts:
            row = [workout.creationDate, workout.workoutActivityType]
            rows.append(row)

        worksheet.insert_rows(rows)

    # Debugging and cleaning  up
    def deleteAllSpreadsheets(self): 
        spreadsheets = self.client.openall()

        for spreadsheet in spreadsheets:
            self.client.del_spreadsheet(spreadsheet.id)
    
    def printAllSpreadsheets(self):
        spreadsheets = self.client.openall()

        for spreadsheet in spreadsheets:
            print(spreadsheet)

    def __str__(self):
        # Get information about the spreadsheet
        id = self.spreadsheet.id
        url = self.spreadsheet.url
        titles = [worksheet.title for worksheet in self.spreadsheet.worksheets()]

        # Format the information as a string
        returnStr = f'Spreadsheet ID: {id}\n'
        returnStr += f'Spreadsheet URL: {url}\n'
        returnStr += 'Worksheets:\n'
        for title in titles:
            returnStr += f'- {title}\n'

        return returnStr