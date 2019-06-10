*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
...
...               All tests contain a workflow constructed from keywords in
...               ``WebserviceLibrary.py``.
...
Library           WebserviceLibrary.py
Library           Process
Suite Setup       Start Process     flask   run
Suite Teardown    Terminate All Processes

*** Test Cases ***
Sanity
    [Documentation]    This basically makes sure the setup / teardown are functional
    [Tags]  dummy
    Sanity
    Result should be    1

Sanity
    [Documentation]    This basically makes sure the setup / teardown are functional
    [Tags]  dummy
    Sanity
    Result should be    0

Query all tasks
    [Documentation]    REST API for webservice - ensures query all is functional
    [Tags]  coding-challenge
    Query all tasks
    Result should be    True

Query specific task
    [Documentation]    REST API for webservice - ensures query specific is functional
    [Tags]  coding-challenge
    Query specific task     1
    Result should be    True

Query invalid task
    [Documentation]    REST API for webservice - query specific negative test
    [Tags]  coding-challenge
    Query specific task     2
    Result should be    False

Create new task
    [Documentation]    REST API for webservice - ensures ability to create task
    [Tags]  coding-challenge
    Create new task     'Go to college'   'DigiPen: Institute of Technology'
    Result should be    True

Update task
    [Documentation]    REST API for webservice - ensures ability to update task
    [Tags]  coding-challenge
    Update specific task    2    done=True
    Result should be    True

Update invalid task
    [Documentation]    REST API for webservice - update task negative test
    [Tags]  coding-challenge
    Update specific task    -99    done=True
    Result should be    False

Delete specific task
    [Documentation]    REST API for webservice - ensures ability to delete task
    [Tags]  coding-challenge
    Delete specific task    2
    Result should be    True

Delete invalid task
    [Documentation]    REST API for webservice - delete task negative test
    [Tags]  coding-challenge
    Delete specific task    2
    Result should be    False