"""This is the user module"""


from app.models.bucketlist import Bucketlist
from app.models.data import Data


class User(object):
    """The main user class"""
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    @staticmethod
    def user_existence(email):
        """Method checks whether the user exists"""

        if email in [user['email'] for user in Data.all_users]:
            return 'User already exists'
        else:
            return False

    @staticmethod
    def get_username(email):
        """Method used for getting username"""
        # checks if email given matches to  key email
        username = [user['username'] for user in
                    Data.all_users if email == user['email']]
        return "".join(username)

    @classmethod
    def register_user(cls, username, email, password):
        """Method registers a user"""
        # checks if a user exists if F creates a new user
        user = cls.user_existence(email)
        if user is False:
            new_user = cls(username, email, password)
            new_user.save_into_user()
            return new_user
        else:
            return user

    def user_data(self):
        """Returns data to be saved in the all_users list"""
        # this how data will be saved as dict in a list
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password
            }

    def save_into_user(self):
        """Method saves into user"""
        # adds the method for getting user data into the users' list
        Data.all_users.append(self.user_data())

    def create_bucketlist(self, title, intro, _id):
        """Method used for creating a bucketlist"""
        # creates an object of bucketlist and saves it
        bucketlist = Bucketlist(
            title=title,
            intro=intro,
            _id=_id
            )
        # this saves bucketlists

        bucketlist.save_into_bucketlist()

    def update_bucketlist(self, title, intro, _id):
        """Method for updating bucketlists"""
        my_bucket = Data.all_bucketlists
        # gives the index of bucketlist from the list
        for num in range(0, len(my_bucket)):
            if _id == my_bucket[num]['_id']:
                # gives the bucketlist index and keys whose value is updated
                my_bucket[num]['title'] = title
                my_bucket[num]['intro'] = intro
                break
        return "Bucketlist successfully updated"

    def del_bucketlist(self, _id):
        """Method deletes a bucketlist from list"""
        # checks if id in dict matches id given and removes first bucketlist
        blist = [bucket_list for bucket_list in Data.all_bucketlists if
                 _id == bucket_list['_id']]

        Data.all_bucketlists.remove(blist[0])
        return True

    @staticmethod
    def create_bucket_item(item_name, intro, bucketlist_id):
        """Method used to create bucketlist items"""
        # checks if id matches picks the first list item creates object of
        # bucket list and creates item
        try:
            bucketlist_info = [item for item in Data.all_bucketlists if
                               bucketlist_id == item['_id']]
            bucketlist_data = bucketlist_info[0]
            bucketlist = Bucketlist(bucketlist_data['title'],
                                    bucketlist_data['intro'],
                                    bucketlist_data['_id'])
            bucketlist.create_item(item_name=item_name,
                                   intro=intro,
                                   bucketlist_id=bucketlist._id)
        except IndexError:
            return 'Item not found'

    def del_bucket_item(self, bucketlist_id):
        """Method for deleting  item from bukcet list"""
        # checks whether bucketlist key id matches id given, removes firsr item
        bitem = [item for item in Data.all_items if
                 bucketlist_id == item['bucketlist_id']]
        Data.all_items.remove(bitem[0])
        return True
