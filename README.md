# projetoSi

Note: Please someone update this Readme

How to run:
Requirements:
python 3.10

virtualenv
pip install virtualenv

piptools
pip install pip-tools==1.8.0

Create a virtualenv following the command:
virtualenv venv -p python3.10

Acess the virtualenv copping the command:
On linux:
source venv/bin/activate

On windows:
venv/Scripts/activate

Download the libraries used by the command:
pip install -r requirements.txt

Create the .env file and copy the contents of the .env.example file

Our app must have a connection to a rabbitmq queue. To create and run a rabbitmq server in a simple way, I suggest the following docker command:
sudo docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
