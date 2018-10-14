import sys
from unittest import TestCase
sys.path.append('../')

from DAL.Signup import User_signup
from DAL.Check_Acc_from_DB import DB_access

class TestUserRegistration(TestCase):

    def testUserRegisterSuccess(self):
        signup = User_signup()

        # create test user
        username = "user_test2"
        password = "pass_test"

        # insert it to db
        signup.insertUser(username, password)

        # check if nasa db ung user
        rows = DB_access.getUserByUserPass(username, password)

        # since nag insert. dapat more than 1 ung length nung rows
        self.assertGreater(len(rows), 0)

        # kunin ung one and only row.
        row = rows[0]

        # kunin ung username at pass na nakuha mula sa db
        (db_username, db_password) = (row[1], row[2])

        # dapat equal ung niregister na user at ung nakuha sa db na user
        self.assertEqual(username, db_username)
        self.assertEqual(password, db_password)



