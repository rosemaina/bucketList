"""This module tests my  user class"""
import unittest
from app.models.user import User
from app.models.data import Data


class Testuser(unittest.TestCase):
    """User test class"""
    def setUp(self):
        self.data = Data()
        self.maleget = User('Maleget Maina', 'maleget@email.com', 'twittie')
        self.user1 = {'username': 'Rose Maina',
                      'password': '12345',
                      'email': 'rossie@email'}
        self.bucketlist1 = {'title': 'bucketlist before 40!',
                            'intro': 'what i want to do before 40',
                            '_id': '4444',
                            'username': 'Jane Doe'}
        self.item1 = {'bucketlist_id': '',
                      'item_name': 'skinny dipping',
                      'intro': 'will jump at Sagana-River Tana'}
        self.del_bucketlist = {'bucketlist_id': '9999'}

        del self.data.all_users[:]
        del self.data.all_bucketlists[:]
        del self.data.all_items[:]

    def test_user_existence(self):
        """Tests whether the user exists"""
        User.register_user('Rose maina', 'rossie@email', '9999')
        User.register_user('Rose maina', 'rossie@email', '9999')
        response = User.register_user('Rose maina', 'rossie@email', '9999')
        self.assertEqual(response, "User already exists")

    def test_get_username(self):
        """Test returns a username"""
        result = User.get_username('jdoe@email')
        self.assertEqual(result, '')

    def test_register_user(self):
        """Tests registration of the user"""
        # self.data.all_users.append(self.user1)
        # User.register_user('Rose Maina', 'rossie@email', '9999')
        result = User.register_user('Jane Doe', 'jdoe@email', '4444')
        self.assertEqual(result.email, 'jdoe@email')

    

    def test_create_bucketlist(self):
        """Tests if a bucketlist has been created"""
        user = User('Jane Doe', 'jdoe', '9876')
        user.create_bucketlist('bucketlist before 40!',
                               'what i want to do before 40', '4444')
        result = len(self.data.all_bucketlists)
        self.assertEqual(result, 1)

    def test_update_bucket(self):
        """Tests if a bucketlist can be updated"""
        self.data.all_bucketlists.append(self.bucketlist1)
        result = self.maleget.update_bucketlist('bucket list 101',
                                                'my second list', '12345')
        self.assertEqual(result, 'Bucketlist successfully updated')

    def test_del_bucketlist(self):
        """Test if a bucketlist has been deleted"""
        user = User('Rose Maina', 'rossie@email', 'password')
        user.create_bucketlist("learn python", "learn data types", '9999')
        count = len(self.data.all_bucketlists)
        user.del_bucketlist('9999')
        new_count = count - len(self.data.all_bucketlists)
        self.assertEqual(new_count, 1)

    def test_create_bucket_item(self):
        """Test if an item has been created in the bucketlist"""
        self.data.all_bucketlists.append(self.bucketlist1)
        user = User('Jane Doe', 'jdoe', '9876')
        user.create_bucket_item('bucketlist before 40!',
                                'what i want to do before 40', '4444')

        result = len(self.data.all_items)
        self.assertEqual(result, 1)

    def test_del_bucket_item(self):
        """Tests if an item in buckelist can be deleted"""
        user = User('Rose Maina', 'rossie@email', 'password')
        user.create_bucketlist("learn python", "learn data types", '9999')
        user.create_bucket_item('strings',
                                'strings are good', '9999')
        count = len(self.data.all_items)
        user.del_bucket_item('9999')
        new_count = count - len(self.data.all_items)
        self.assertEqual(new_count, 1)

if __name__ == '__main__':
    unittest.main()
