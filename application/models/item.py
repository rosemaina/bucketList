"""This is the item module"""
import uuid


class Item(object):
    """This is the main item class"""

    def __init__(self, item_name, description, bucket_id):
        self.item_name = item_name
        self.description = description
        self.bucket_id = bucket_id
        self.item_id = str(uuid.uuid4())

    # def item_data(self):
    #     """Returns data to be saved in the all_items list"""
    #     return {
    #         'item_name': self.item_name,
    #         'intro': self.intro,
    #         'bucketlist_id': self.bucketlist_id
    #         }
    # # saves item data into item's list

    # def save_into_item(self):
    #     """Method saves into item"""
    #     Data.all_items.append(self.item_data())
