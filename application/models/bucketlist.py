""" This is the main module for the bucketlist """


import uuid


class Bucketlist(object):
    """This is the main class"""

    def __init__(self, title, intro):
        self.title = title
        self.intro = intro
        self.bucket_id = str(uuid.uuid4().hex)
