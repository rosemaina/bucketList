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
    def test_register_new_user(self):
        """Test to regitster a user"""
        self.register_user()
        data = {'test@test.com':'12345678'}
        self.assertEqual((BucketlistData.all_users), data)
    
    def test_same_email(self):
        """Test if same email registered msg returned"""
        self.register_user()
        data = {'email': 'test@test.com', 'password':'12345678'}
        self.assertEqual(data, 'Email is not available. Choose another name')
    
    def test_same_password(self):
        """Tests if passwords match"""
        self.register_user()
        data = {'test@test.com': '87654321'}
        self.assertEqual((BucketlistData.all_users),data)
    
    def test_create_bucketlist(self):
        """Test for creating s bucketlist"""
        self.register_user()
        self.login_user()
        created_bucket = self.create_bucketlist()
        # bucket dict should have one bucket with title
        self.assertEqual(BucketlistData.all_bucketlists.values()[0].title, 'bucket1')
    
    def test_delete_bucketlist(self):
        """Test for deleteing a bucketlist"""
        self.register_user()
        self.login_user()
        # deleting the bucket using the bucket id
        response = self.client.get('/delete_bucket/' + BucketlistData.all_bucketlists.keys()[0])
        # the status code should be 302
        self.assertEqual(response.status_code, 302)
