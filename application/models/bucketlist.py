""" This is the main module for the bucketlist """
import uuid

class Bucketlist(object):
    """This is the main class"""

    def __init__(self, title, intro, bucket_id=None):
        self.title = title
        self.intro = intro
        self.bucket_id = str(uuid.uuid4().hex if bucket_id is None else bucket_id)
        # self.items = {}


    # def create_bucketlist(self):
    #     """Method used for creating a bucketlist"""
    #     # creates an object of bucketlist and saves it
    #     self.all_bucketlists[self._id] = {'titleself.title}
    # # def create_item(self, item_name, intro, bucketlist_id):
    #     """method used for creating an item"""
    #     item = Item(
    #         item_name=item_name,
    #         intro=intro,
    #         bucketlist_id=bucketlist_id
    #     )
    #     # this saves items
    #     item.save_into_item()

    # def update_bucket_item(self, item_name, intro, bucketlist_id):
    #     """Method used to update a bucketlist item"""
    #     my_item = Data.all_items
    #     for num in range(0, len(my_item)):
    #         if bucketlist_id == my_item[num]['bucketlist_id']:
    #             # gives the bucketlist index and keys whose value are updated
    #             my_item[num]['item_name'] = item_name
    #             my_item[num]['intro'] = intro
    #             break
    #     return "Item successfully updated"

    # def bucketlist_data(self):
    #     """Returns data to be saved in the all_bucketlist list"""
    #     return {
    #         '_id': self._id,
    #         'title': self.title,
    #         'intro': self.intro
    #         }

    # def save_into_bucketlist(self):
    #     """Method saves into bucketlist """
    #     Data.all_bucketlists.append(self.bucketlist_data())
