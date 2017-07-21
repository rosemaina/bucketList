"""This is the item module"""
from app.models.data import Data


class Item(object):
    """This is the main item class"""

    def __init__(self, item_name, intro, bucketlist_id, _id=None):
        self.item_name = item_name
        self.intro = intro
        self.bucketlist_id = bucketlist_id

    def item_data(self):
        """Returns data to be saved in the all_items list"""
        return {
            'item_name': self.item_name,
            'intro': self.intro,
            'bucketlist_id': self.bucketlist_id
            }
    # saves item data into item's list

    def save_into_item(self):
        """Method saves into item"""
        Data.all_items.append(self.item_data())
