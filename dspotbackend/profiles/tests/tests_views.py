from django.test import TestCase, Client as TestClient
from profiles.models import Profile
from model_bakery import baker


class ProfileTest(TestCase):
    def setUp(self):
        domain = 'example.com'
        self.client = TestClient(HTTP_ORIGIN=domain)

    def test_list(self):
        # todo Test to check method to list all profiles
        url = '/profiles/profiles/'
        for i in range(1, 10):
            baker.make(Profile,
                       first_name='Profile ' + str(i),
                       last_name='Last Profile ' + str(i),
                       city='City ' + str(i))
        response = self.client.get(url)
        data_response = response.json()
        count = len(data_response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 9)

    def test_get_profile_by_id(self):
        # todo Test to check method, given a profile id, list its details
        url = '/profiles/profiles/'
        profile = baker.make(Profile,
                             first_name='Profile',
                             last_name='Last Profile',
                             city='City ')
        response = self.client.get(url + str(profile.id) + '/')
        data_response = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(profile.id, data_response['id'])

    def test_get_friends_by_profile_id(self):
        # todo Test to check method, given a profile id, list its friends
        url = '/profiles/profiles/friends/?profile_id='
        profile = baker.make(Profile,
                             first_name='Profile',
                             last_name='Last Profile',
                             city='City ')
        for i in range(1, 10):
            friend = baker.make(Profile,
                                first_name='Profile ' + str(i),
                                last_name='Last Profile ' + str(i),
                                city='City ' + str(i))
            profile.friends.add(friend)
        response = self.client.get(url + str(profile.id))
        data_response = response.json()
        count = len(data_response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(count, 9)
