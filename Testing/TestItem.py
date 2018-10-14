import random
import sys
from unittest import TestCase
sys.path.append('../Source Code')

from DAL.Write2MainDB import Add2MainDB
from UI.MainDB import MainDatabase


class TestItem(TestCase):

    def testAddItemForLoggedUserIdInShared(self):
        self.assertTrue(True)
        mainDB = MainDatabase()

        # NOTE: Kung kaninong UserId ung nasa Shared/LoggedUser.txt
        #       para sa kanya nasesave ung items

        # generate ng random item at quantity
        # para madali icheck, since nag-a-add sya sa previous value
        randInt = random.randint(69,696969)
        itemName = "item ng mama mo " + str(randInt)
        quantity = randInt

        # save sa db
        Add2MainDB.Write2DB(itemName, quantity)

        # kunin natin lahat ng data
        rows = mainDB.fetchData()

        # kailangan ma-find natin ung ininsert natin. mula sa rows
        # use tuple nlng
        self.assertIn((itemName, quantity), rows, itemName + " is in the database")

