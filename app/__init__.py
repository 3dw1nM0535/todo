from flask import Flask, jsonify, abort, make_response

from instance.config import app_config

def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)

	app.config.from_object(app_config[config_name])
	app.config.from_pyfile("config.py")

	# Todo lists data structure
	tasks = [
		{
			"id": 1,
			"task": "Clean up my room",
			"done": False
		},
		{
			"id": 2,
			"task": "Watch rugby match",
			"done": False
		},
		{
			"id": 3,
			"task": "Check on Mum",
			"done": False
		}
	]

	@app.route("/todo/api/v1.0/tasks", methods=["GET"])
	def get_tasks():
		return jsonify({ "tasks": tasks })

	@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods=["GET"])
	def get_task(task_id):
		if task_id > len(tasks):
			abort(404)
		task = []
		for item in tasks:
			if item["id"] == task_id:
				task.append(item)
				if len(task) == 0:
					abort(404)
		return jsonify({ "task": task[0] })

	@app.errorhandler(404)
	def not_found(error):
		return make_response(jsonify({ "error": "Not Found" }), 404)

	return app
