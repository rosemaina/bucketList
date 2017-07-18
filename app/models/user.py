"""This is the user module"""
from app.models.bucketlist import Bucketlist
from app.models.data import Data
class User(object):
    """The main user class"""
    def __init__(self, username, email, password, _id=None):
        self.username = username
        self.email = email
        self.password = password
        self._id = _id

    @staticmethod
    def user_existence(email):
        """Method checks whether the user exixts"""
        # checks if index in dictionary matches email in list and return T/F
        exist = [x['email'] for x in Data.all_users if email == x['email']]
        return "".join(exist) == email
    def create_bucketlist(self, title, intro, user_id):
        """Method used for creating a bucketlist"""
        bucketlist = Bucketlist(
            title=title,
            intro=intro,
            user_id=self._id
            )
        # this saves bucketlists
        bucketlist.save_into_bucketlist()

    @classmethod
    def register_user(cls, username, email, password):
        """Method registers a user"""
        user = cls.user_existence(email)
        if user is False:
            new_user = cls(username, email, password)
            new_user.save_into_user()
            return True
        else:
            return False


    def user_data(self):
        """Returns data to be saved in the all_users list"""
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            '_id': self._id
            }

    @staticmethod
    def create_bucket_item(bucketlist_id, item_name, intro):
        """Method used to create bucketlist items"""
        bucketlist_info = [n for n in Data.all_bucketlists if bucketlist_id == n['_id']]
        bucketlist_data = bucketlist_info[0]
        bucketlist = Bucketlist(bucketlist_data['title'],
                                bucketlist_data['intro'],
                                bucketlist_data['user_id'],
                                bucketlist_data['_id']
                               )
        bucketlist.create_item(
            item_name=item_name,
            intro=intro
        )

    def save_into_user(self):
        """Method saves into user"""
        # adds the method for getting user data into the users' list
        Data.all_users.append(self.user_data())
