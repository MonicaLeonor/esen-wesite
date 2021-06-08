from core.pyba_logic import PybaLogic


class PersonLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getAllPerson(self):
        database = self.databaseObj
        sql = self.createDatabaseObj()
        sql = "SELECT * FROM person;"
        results = database.executeQuery(sql)
        return results


    def insertPerson(self, person):
        database = self.databaseObj
        sql = (
            "INSERT INTO `testdb`.`person` "
            + f"(`id`,`name`,`age`) "
            + f"VALUES(0, '{person['name']}', {person['age']});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getPersonById(self, id):
        database = self.databaseObj
        sql = f"SELECT * FROM testdb.person where id={id};"
        result = database.executeQuery(sql)
        return result

    def updatePerson(self, id, person):
        database = self.databaseObj
        sql = (
            "UPDATE `testdb`.`person` "
            + f"SET `name` = '{person['name']}', `age` = {person['age']} "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deletePerson(self, id):
        database = self.databaseObj
        sql = f"DELETE FROM `testdb`.`person` WHERE id={id};"
        rows = database.executeNonQueryRows(sql)
        return rows
