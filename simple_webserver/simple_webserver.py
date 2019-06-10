''' Mock REST api Tests

# query all tasks
curl -i http://localhost:5000/todo/api/v1.0/tasks

# query one task
curl -i http://localhost:5000/todo/api/v1.0/tasks/1
# invalid query
curl -i http://localhost:5000/todo/api/v1.0/tasks/2

# create new task
curl -i -H "Content-Type: application/json" -X POST -d "{"""title""":"""Go to college""", """description""":"""DigiPen: Institute of Technology"""}" http://localhost:5000/todo/api/v1.0/tasks
# verify task creation
curl -i http://localhost:5000/todo/api/v1.0/tasks/2

# modify existing task
curl -i -H "Content-Type: application/json" -X PUT -d "{"""done""":true}" http://localhost:5000/todo/api/v1.0/tasks/2
# verify change
curl -i http://localhost:5000/todo/api/v1.0/tasks/2

# delete task
curl -X DELETE http://localhost:5000/todo/api/v1.0/tasks/2
# delete non-existing task
curl -X DELETE http://localhost:5000/todo/api/v1.0/tasks/2
# verify task is deleted
curl -i http://localhost:5000/todo/api/v1.0/tasks/2

# hire_candidate
curl -i http://localhost:5000/todo/api/v1.0/hire_candidate
curl -u some_one_else:python3 -i http://localhost:5000/todo/api/v1.0/hire_candidate
curl -u rkunkel:python3 -i http://localhost:5000/todo/api/v1.0/hire_candidate

'''

from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}