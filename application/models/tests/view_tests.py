"""This is the main module for testing flask"""
from unittest import TestCase
from application.views import BucketlistData, app
from application.models.bucketlist import Bucketlist

class TestBucketApp(TestCase):
    """This tests the app functionalities"""
    def setUp(self):
        # method creates a new test client
        self.client = app.test_client(self)
        self.bucket1 = Bucketlist("Bucket 1", "Intro 1")
        # self.item1 = I
        # this acts as a dummy web broswer
        # self.app = app.test_client()
        # with self.app as app_:
        #     # this cretes a session
        #     with app_.session_transaction() as session:
        #         session['user'] = 'rose@email.com'

        # # create default user
        # BucketlistData.all_users = {'rose@email.com': 'testtest'}
        # new_blist = Bucketlist('bucket 1', 'A new bucket')

        # # BucketlistData.all_bucketlists[new_blist.bucket_id] = new_blist
    def register_user(self):
        """Method that registers a user"""
        data = {'email': 'test@test.com', 'password':'12345678', 'confirm_password':'12345678'}
        return self.client.post('/registration', data=data)

    def login_user(self):
        """Method that logins a user"""
        data = {'email':'test@test.com', 'password':'12345678'}
        return self.client.post('/index', data=data)

    def create_bucketlist(self):
        """Method creates a new bucketlist"""
        # new_bucket = Bucketlist('bucket1', 'new bucket')
        data = {'title':'bucket1',  'intro': 'butcketigbgb'}

        return self.client.post('/create_list', data=data)

    # TESTS FOR THE CLASS
    # def test_register_new_user(self):
    #     """Test to regitster a user"""
    #     self.register_user()
    #     data = {'test@test.com':'12345678'}
    #     self.assertEqual((BucketlistData.all_users), data)
    
    def test_same_email(self):
        """Test if same email registered msg returned"""
        pass
    
    # def test_same_

    def test_create_bucketlist(self):
        """Test for creating s bucketlist"""
        self.register_user()
        self.login_user()
        created_bucket = self.create_bucketlist()
        # bucket dict should have one bucket
        self.assertEqual(BucketlistData.all_bucketlists.values()[0].title, 'bucket1')
    
    def test_delete_bucketlist(self):
        """Test for deleteing a bucketlist"""
        self.register_user()
        self.login_user()
        # created_bucket = self.create_bucketlist()
        # deleting the bucket using the bucket id
        response = self.client.post('/delete_bucket/' + BucketlistData.all_bucketlists.keys()[0])
        # user dict should now have 0 buckets
        # self.assertEqual(BucketlistData.all_bucketlists)
        # the status code should be 200
        self.assertEqual(response.status_code, 200)



    #     data = {'title': 'Bucket 1', 'intro':'My new bucketlist'}
    #     # bucketlist should have only one bucket
    #     self.assertEqual(len(BucketlistData.all_bucketlists), 1)


