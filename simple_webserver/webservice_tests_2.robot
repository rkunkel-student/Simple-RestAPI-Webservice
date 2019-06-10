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
    Result should be    False   # Cause a critical failure