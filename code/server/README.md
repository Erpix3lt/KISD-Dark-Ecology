# Server
As of May we introduced a different architecture, where we are using a personal pc as a server instance, running object detection providing only guiding args to the robot in response. This helps with faster runtimes and makes developing more clear.

### VENV
Go into the server directory: `cd code/server`

Create a new env: `python3 -m venv _env_dark_eco`

Activate the env: `source _env_dark_eco/bin/activate`

Now we can use python and pip as usual.

Install all dependencies: `pip install -r requirements.txt`

