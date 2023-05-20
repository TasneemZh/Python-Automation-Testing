## About the Project

A round of GitHub testing to cover profile basic settings, main features used by developers to create repositories, the search functionality, and the star feature.

## Steps to run the project

- git clone [project-url]
- cd [project-folder]
- pip install -r requirements.txt
- touch app-config.properties

In the *app-config.properties* file, write the email and password in the following format:

> EMAIL=xxx@xxx.xxx
> 
> PASSWORD=xxxxxx

Mark *src* folder as the **Sources Root**.

Run the project by the following command and check that *run_command* in config.json is set to *true*:

`pytest -v -s --alluredir=.\allure-results .\src\tests\TestGitHub.py`

Run Allure server by the following command:

`allure serve`

To run the project using the IDE tools, right-click on the TestGitHub.py and click on *Run* after setting the *run_command* in config.json to *false*

## Warning

The tests have been created for learning purposes only.
