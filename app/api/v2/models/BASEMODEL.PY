from app.api.v2.utils.condb import CrudDatabase

execCommand = CrudDatabase.ConnectToDB
class DBManipulateBase():
    def CreateTable(self, query):
        execCommand(query)

    def CreateRow(self, query):
        execCommand(query)

    def Update_Row(self, query):
        execCommand(query)
    
    def Read_Row_all(self, query):
        execCommand(query)

    def Read_Row_one(self, query):
        execCommand(query)
