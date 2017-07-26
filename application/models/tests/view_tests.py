"""This is the main module for testing flask"""
from unittest import TestCase
from application.views import BucketlistData, app

class TestBucketApp(TestCase):
    """This tests the app functionalities"""
    def setUp(self):
        self.client = app.test_client(self)
        # create default user
        BucketlistData.all_users = {'rose@email.com': 'testtest'}

    def test_register_new_user(self):
        """Test to regitster a user"""
        data = {'email': 'test@test.com', 'password':'12345678', 'confirm_password':'12345678'}
        # user dict should only have one user
        self.assertEqual(len(BucketlistData.all_users), 1)
        # taking the data created and submitting it to the endpoint /registration
        response = self.client.post('/registration', data=data)
        # user dict should now have 2 users
        self.assertEqual(len(BucketlistData.all_users), 2)
        # for the new user created the email and password should be from the data provided
        self.assertEqual(BucketlistData.all_users[data['email']], data['password'])
        # the status code should be 302 because the user is redirected to the login page
        self.assertEqual(response.status_code, 302)

    def test_create_bucketlist(self):
        """Test for creating s bucketlist"""
        data = {'title': 'Bucket 1', 'intro':'My new bucketlist'}
        # bucket dict should be empty
        self.assertEqual(len(BucketlistData.all_bucketlists), 0)
        # login user to create the session
        response = self.client.post('/index', data={'email': 'rose@email.com',
                                                    'password': 'testtest'})
        # user is redirected to create bucketlist
        self.assertEqual(response.status_code, 302)
        # taking the data created and submitting it to the endpoint /create_list
        response = self.client.post('/create_list', data=data)
        # user dict should now have 1 bucketlist
        self.assertEqual(len(BucketlistData.all_bucketlists), 1)
        # the status code should be 200
        self.assertEqual(response.status_code, 200)
