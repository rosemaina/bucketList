"""This module tests my  user class"""
import unittest
from app.models.user import User
def test_user_existence(self):
    """Tests whether the user exists"""
    self.data.add_data(self.user1)
    result = User.user_existence('rossie@email')
    self.assertTrue(result)
    result1 = User.user_existence('jdoe@email')
    self.assertFalse(result1)

def test_register_user(self):
    """Tests registration of the user"""
    self.data.add_data(self.user1)
    result = User.register_user('Jane Doe', 'jdoe@email', '9876')
    self.assertTrue(result)
    result1 = User.register_user('Rose Maina', 'rossie@email', '12345')
    self.assertFalse(result1)

def test_create_bucketlist(self):
    """Tests if a bucketlist has been created"""
    user = User('Jane Doe', 'jdoe', '9876', _id=None)
    user.create_bucketlist('bucketlist before 40!',
                           'what i want to do before 40', 'sdf528drr0dab149eceedb14')
    result = len(self.data.bucketlists)
    self.assertEqual(result, 1)

def test_create_bucket_item(self):
    """Test if an item has been created in the bucketlist"""
    self.data.add_data(self.bucketlist1)
    user = User('Jane Doe', 'jdoe', '9876', _id=None)
    user.create_bucket_item('sdf528drr0dab149eceedb14', 'bungee jumping', 'will jump at sagana')
    result = len(self.data.items)
    self.assertEqual(result, 1)



if __name__ == '__main__':
    unittest.main()
