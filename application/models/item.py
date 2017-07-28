"""This is the item module"""
import uuid


class Item(object):
    """This is the main item class"""

    def __init__(self, item_name, description, bucket_id):
        self.item_name = item_name
        self.description = description
        self.bucket_id = bucket_id
        self.item_id = str(uuid.uuid4())
