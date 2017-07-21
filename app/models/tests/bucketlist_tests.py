"""This module tests my bucketlist class"""
import unittest
from app.models.bucketlist import Bucketlist
from app.models.data import Data


class Testbucketlist(unittest.TestCase):
    """Bucketlist test class"""
    def setUp(self):
        self.data = Data()
        self.item1 = {'bucketlist_id': '',
                      'item_name': 'skinny dipping',
                      'intro': 'will jump at Sagana-River Tana'
                      }

    def test_create_item(self):
        """Tests if a new  item has been created"""
        bucket = Bucketlist('bucket 1', 'test intro', '4444')
        bucket.create_item('skinny dipping', 'item introduction', '4444')
        result = len(self.data.all_items)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
