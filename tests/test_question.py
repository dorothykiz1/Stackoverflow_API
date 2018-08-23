import unittest
import json
from flask import jsonify
from api.question import app

class QuestionTestCase(unittest.TestCase):
    """This class represents the Question test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.client = self.app.test_client
        self.question = {'description': 'What is the difference between AI and Machine Learning'}

        
    def test_question_creation(self):
        """Test API can create a question (POST request)"""
        result = self.client().post('/api/v1/questions', data=self.question)
        message = jsonify(result.data)
        self.assertEqual(result.status_code, 201)
        self.assertEqual(message['message'],'Question successfully created')

    def test_api_can_get_all_questions(self):
        """Test API can get all Questions (GET request)."""
        result = self.client().post('/api/v1/questions', data=self.question)
        self.assertEqual(result.status_code, 201)
        result = self.client().get('/api/v1/questions')
        message = jsonify(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(message['message'],'Questions all retrieved')

    def test_api_can_get_question_by_id(self):
        """Test API can get a single question while using id attached"""
        result= self.client().post('/api/v1/questions', data=self.question)
        self.assertEqual(result.status_code, 201)
        result_in_json = json.loads(result.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/bucketlists/{}'.format(result_in_json['id']))

        message = jsonify(result.data)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(message['message'],'Question with id {} is retrieved'.format(id))
    

    
    def test_delete_question(self):
        """Test API can delete an existing question"""
        result = self.client().post(
            '/api/v1/questions',
            data=self.question)
        self.assertEqual(result.status_code, 201)
        res = self.client().delete('/api/v1/questions/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/api/v1/questions/1')
    
        self.assertEqual(result.status_code, 404)

#execute tests

if __name__ == "__main__":
     unittest.main()
  