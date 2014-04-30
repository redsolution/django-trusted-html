import unittest
from django.contrib.auth.models import User
from django.test import Client
from django.test.testcases import TestCase
from example.models import MyModel, ExternalModel


class ViewsTest(unittest.TestCase):
    def test_views(self):
        client = Client()
        self.assertEqual(client.get('/response').status_code, 200)
        self.assertEqual(client.get('/notfound').status_code, 404)
        self.assertEqual(client.get('/error').status_code, 500)
        self.assertEqual(client.get('/redirect_response').status_code, 302)
        self.assertEqual(client.get('/redirect_notfound').status_code, 302)
        self.assertEqual(client.get('/redirect_redirect_response').status_code, 302)
        self.assertEqual(client.get('/redirect_cicle').status_code, 302)
        self.assertEqual(client.get('/permanent_redirect_response').status_code, 301)
        self.assertEqual(client.get('/http404').status_code, 404)
        self.assertRaises(Exception, client.get, '/http500')
        self.assertEqual(client.get('/request_true_response').content, 'True')
        self.assertEqual(client.get('/request_false_response').content, 'False')
        self.assertEqual(client.get('/doesnotexists').status_code, 404)
        self.assertEqual(client.get('/').status_code, 404)


class AdminTest(TestCase):

    XSS_TEXT = r'''<IMG SRC="javascript:alert('XSS');">%s test'''
    TRUSTED_TEXT = '<p>%s test</p>'

    def test_direct_changes(self):
        MyModel.objects.create(html=self.XSS_TEXT)
        self.assertEqual(MyModel.objects.get().html, self.XSS_TEXT)

    def login(self):
        User.objects.create_superuser(
            username='admin', email='admin@example.com', password='admin')
        self.assertTrue(self.client.login(username='admin', password='admin'))

    def test_trusted_text_field(self):
        self.login()
        response = self.client.post(
            '/admin/example/mymodel/add/',
            data={
                'html': self.XSS_TEXT % 'html',
                'short': self.XSS_TEXT % 'short',
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(MyModel.objects.get().html, self.TRUSTED_TEXT % 'html')
        self.assertEqual(MyModel.objects.get().short, self.TRUSTED_TEXT % 'short')

    def test_trusted_models(self):
        self.login()
        response = self.client.post(
            '/admin/example/externalmodel/add/',
            data={
                'name': self.XSS_TEXT % 'name',
                'description': self.XSS_TEXT % 'description',
                'not_trusted': self.XSS_TEXT % 'not_trusted',
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ExternalModel.objects.get().name, self.TRUSTED_TEXT % 'name')
        self.assertEqual(ExternalModel.objects.get().description, self.TRUSTED_TEXT % 'description')
        self.assertEqual(ExternalModel.objects.get().not_trusted, self.XSS_TEXT % 'not_trusted')
