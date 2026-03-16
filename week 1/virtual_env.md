 Virtual Environment 

it is used to create an isolated environment for each of your projects, where they can have only the necessary dependencies and the specific versions

it allows us to make different python environments

> pip install virtualenv  - to install virtual environments

Create a new folder for your project and initialize a virtual environment

> virtualenc project1_env  

it initialize a new virtual environment, and now we should activate before we put it to use

> source project1_env/bin/activate  - to activate the virtual environment

> which python  - this command shows the path we are in and the environment

if you enter > pip list command it will return 
pip
setuptools
(project1_env) - the environment that we are currently in

>Using pip command you can install the packeges you need for your project either manually or from a requirements file

> pip install -r requirements.txt

> deactivate  - it deactivate the virtual environment and adds you to the global environment

>rm -rf project1_env/  - it deletes the virtual environment file, which is already deactivated