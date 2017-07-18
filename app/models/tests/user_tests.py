"""This module tests my  user class"""
import unittest
from app.models.user import User
from app.models.data import Data
class Testuser(unittest.TestCase):
    """User test class"""
    def setUp(self):
        self.data = Data()
        self.user1 = {'username': 'Rose Maina',
                      '_id': '495048345748',
                      'password': '12345',
                      'email': 'rossie@email'
                     }
        self.bucketlist1 = {'title' : 'bucketlist before 40!',
                            'intro' : 'what i want to do before 40',
                            '_id' : '485983354754',
                            'username' : 'Jane Doe',
                           }
        # self.item1 = {'bucketlist_id' : '',
        #               'item_name' : 'skinny dipping',
        #               'intro' : 'will jump at Sagana-River Tana'
        #              }
        self.data = Data()
        del self.data.all_users[:]
        del self.data.all_bucketlists[:]


    def test_user_existence(self):
        """Tests whether the user exists"""
        self.data.all_users.append(self.user1)
        result = User.user_existence('rossie@email')
        self.assertTrue(result)
        result1 = User.user_existence('jdoe@email')
        self.assertFalse(result1)

    def test_register_user(self):
        """Tests registration of the user"""
        self.data.all_users.append(self.user1)
        result = User.register_user('Jane Doe', 'jdoe@email', '9876')
        self.assertTrue(result)
        result1 = User.register_user('Rose Maina', 'rossie@email', '12345')
        self.assertFalse(result1)
    def test_create_bucketlist(self):
        """Tests if a bucketlist has been created"""
        user = User('Jane Doe', 'jdoe', '9876', _id=None)
        user.create_bucketlist('bucketlist before 40!',
                               'what i want to do before 40', '485983354754')
        result = len(self.data.all_bucketlists)
        self.assertEqual(result, 1)
    def test_create_bucket_item(self):
        """Test if an item has been created in the bucketlist"""
        self.data.all_bucketlists.append(self.bucketlist1)
        user = User('Jane Doe', 'jdoe', '9876', _id=None)
        user.create_bucket_item('485983354754', 'bucketlist before 40!',
                                'what i want to do before 40'
                               )
        result = len(self.data.all_items)
        self.assertEqual(result, 1)



if __name__ == '__main__':
    unittest.main()
