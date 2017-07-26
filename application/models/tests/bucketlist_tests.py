"""This module tests my bucketlist class"""
import unittest
from app.models.bucketlist import Bucketlist
from app.models.data import Data


class Testbucketlist(unittest.TestCase):
    """Bucketlist test class"""
    def setUp(self):
        self.data = Data()
        self.bucket101 = Bucketlist('bronches bucketlist',
                                    'summer activities', '1010')
        self.bucketlist1 = {'title': 'bucket list 101',
                            'intro': 'my first bucketlist',
                            '_id': 12345}
        self.item1 = {'item_name': 'skinny dipping',
                      'intro': 'will jump at Sagana-River Tana',
                      'bucketlist_id': ''}

    def test_create_item(self):
        """Tests if a new  item has been created"""
        bucket = Bucketlist('bucket 1', 'test intro', '4444')
        bucket.create_item('skinny dipping', 'item introduction', '4444')
        result = len(self.data.all_items)
        self.assertEqual(result, 1)

    def test_update_bucket_item(self):
        """Tests if a bucketlist item can be updated"""
        self.data.all_items.append(self.item1)
        result = self.bucket101.update_bucket_item('learn python',
                                                   'study tdd', '1010')
        self.assertEqual(result, 'Item successfully updated')


if __name__ == '__main__':
    unittest.main()
