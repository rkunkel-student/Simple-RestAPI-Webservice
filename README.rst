Specifics

* Write a test suite that will validate 5 web service test cases 

	- State Pass determines deployment
	- 100% Pass Rate before proceeding deployment 

* Generate a report 

	- Number Passed
	- Number Failed
	- Failures must include some detail as to cause 

* Deliverables

	- Files associated with the suite 
	- Provide suite showcasing 5 simple mock tests that run and provide results
	- Run a deploy job in jenkins upon 100% pass

* REST api - Tests

    - query all 'tasks'
    - query one 'task'
    - create new 'task'
    - modify existing 'task'
    - delete 'task'

* Website Frontend - Tests

    - I was going to use selenium with the chrome / gecko driver time pending. I ran out of time however...

* Note
	
	- Where it states "run a deploy job in jenkins" a stub fuction is fine or even comment stating "deploy to jenkins here"
	- I'm familiar with unittest but want to challenge myself with the robot framework; they look similar.
	- This should take no more than 6 hours to complete

* Extra Credit - Report Severities

    - sev 1 vs sev 2 errors
    
Running the test suite

1. python3 -m venv venv 
2. (activate venv on your OS)
3. (venv) python -m pip install -r requirements.txt
4. (venv) cd simple_webserver
5. (venv) python run_tests.py

- Reports are generated as both .xml and .html files
- See ExpectedOutput.txt for an example of the test suite performance
- See ExampleReports\ for examples of the generated .xml and .html files