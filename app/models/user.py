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
        if email in Data.all_users:
            return 'user already exists'
        else:
            return 'jdoe@email'

    @staticmethod
    def get_username(email):
        """Method used for getting username"""
        username = [i['username'] for i in Data.all_users if email == i['email']]
        return "".join(username)

    def create_bucketlist(self, title, intro, _id):
        """Method used for creating a bucketlist"""
        bucketlist = Bucketlist(
            title=title,
            intro=intro,
            _id=_id
            )
        # this saves bucketlists
        bucketlist.save_into_bucketlist()
    
    # def view_buckets(self, title):
    #     """Method to view a bucketlist"""
    #     view = [ title for title in Data.all_bucketlists]
    #     print view

    # def del_bucketlist(self, bucketlist_id):
    #     """Method deletes a bucketlist from list"""
    #     blist = [l for l in Data.all_bucketlists if
    #              bucketlist_id == l['bucketlist_id']]
    #     blist.remove()

    @classmethod
    def register_user(cls, username, email, password):
        """Method registers a user"""
        user = cls.user_existence(email)
        if user is False:
            new_user = cls(username, email, password)
            new_user.save_into_user()
            return new_user

    def user_data(self):
        """Returns data to be saved in the all_users list"""
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password
            }

    @staticmethod
    def create_bucket_item(item_name, intro, bucketlist_id):
        """Method used to create bucketlist items"""
        try:
            bucketlist_info = [n for n in Data.all_bucketlists if
                               bucketlist_id == n['_id']]
            bucketlist_data = bucketlist_info[0]
            bucketlist = Bucketlist(bucketlist_data['title'],
                                    bucketlist_data['intro'],
                                    bucketlist_data['_id']
                                   )
            bucketlist.create_item(item_name=item_name,
                                   intro=intro,
                                   bucketlist_id=bucketlist._id
                                  )
        except IndexError:
            return 'Item not found'

    # def view_items(self, item_name):
    #     """Method to view items in a bucketlist"""
    #     view = [item_name for item_name in Data.all_items]
    #     print view
    # def del_bucket_item(self, bucketlist_id):
    #     """Method deletes a bucketlist from list"""
    #     blist = [i for i in Data.all_items if
    #              bucketlist_id == i['bucketlist_id']]
    #     blist.remove()

    def save_into_user(self):
        """Method saves into user"""
        # adds the method for getting user data into the users' list
        Data.all_users.append(self.user_data())

    # def update_bucketitem(self, item_name, intro, bucketlist_id):
    #     """Method updates a item to list"""
    #     for item in Data.all_bucketlists:
    #         if bucketlist_id == item['_id']:
    #             self.item.all_bucketlists.update({item_name : item_name,
    #                                          intro: intro,
    #                                          bucketlist_id :bucketlist_id
    #                                         }
    #                                        )
