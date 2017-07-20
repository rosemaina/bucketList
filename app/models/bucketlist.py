""" This is the main module for the bucketlist """
from app.models.item import Item
from app.models.data import Data
class Bucketlist(object):
    """This is the main class"""

    def __init__(self, title, intro, _id):
        self.title = title
        self.intro = intro
        self._id = _id

    def create_item(self, item_name, intro, bucketlist_id):
        """method used for creating an item"""
        item = Item(
            item_name=item_name,
            intro=intro,
            bucketlist_id=bucketlist_id
        )
        # this saves items
        item.save_into_item()
    
    # def del_bucketitems(self, bucketlist_id):
    #     """ A function for deleting bucket activities """
    #     # Checks if the bucket list item to be deleted is in the bucket list
    #     item = [bucketlist_id for bucketlist_id in Data.all_bucketlists if
    #             bucketlist_id in Data.all_bucketlists]
    #     del item['bucket_id']

    def bucketlist_data(self):
        """Returns data to be saved in the all_bucketlist list"""
        return {
                '_id': self._id,
                'title': self.title,
                'intro': self.intro
               }

    def save_into_bucketlist(self):
        """Method saves into bucketlist """
        Data.all_bucketlists.append(self.bucketlist_data())
