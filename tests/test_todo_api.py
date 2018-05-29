import os
import json
import unittest
from app import create_app

class TodoTestCase(unittest.TestCase):
	# Todo list test class
	
	def setUp(self):
		# Initialize test variables
		self.app = create_app(config_name="testing")
		self.client = self.app.test_client

	def test_api_can_get_all_todos(self):
		# Test API can get all todos
		res = self.client().get("/todo/api/v1.0/tasks")
		self.assertEqual(res.status_code, 200)
		self.assertIn("tasks", str(res.data))

	def test_api_to_get_single_data_item(self):
		# Test API to get single data using id
		res = self.client().get("/todo/api/v1.0/tasks/{}".format(2))
		self.assertEqual(res.status_code, 200)
		self.assertIn("task", str(res.data))
