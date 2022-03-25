import sqlite3 as sql
import unittest

class Checking_Employee_name(unittest.TestCase):
    def setUp(self):
        self.empname1="pradeep kumar"
        self.empcode1="21"
        self.empname2="shivadharashini"
        self.empcode2="20"
        self.connection=sql.connect("EmployeeManagement.db")

    def tearDown(self):
        self.empname=" "
        self.empcode=" "
        self.connection.close()

    def test_verify_emp1(self):
        result=self.connection.execute("select name from Employee where empcode="+self.empcode1)
        for i in result:
            fetchedemployee=i[0]
        self.assertEqual(fetchedemployee,self.empname1)

    def test_verify_emp2(self):
        result=self.connection.execute("select name from Employee where empcode="+self.empcode2)
        for i in result:
            fetchedemployee=i[0]
        self.assertEqual(fetchedemployee,self.empname2)

if __name__=="__main__":
    unittest.main()