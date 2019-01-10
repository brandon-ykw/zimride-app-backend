# zimride-app-backend
Zimride is a rideshare service used by many Cornell students. They do not operate a mobile application. Shane Yun, Nikita Lang and I decided to make one for them. Shane designed, Nikita created the frontend, and I developed the backend APIs, 

## Setup:
cd src # change directory 
virtualenv -p python3.6 venv # create a virtual environment
source venv/bin/activate # enter the virtual environment
pip install -r requirements.txt # install the required packages

## Running the App:
source venv/bin/activate # enter the virtual environment
sh run.sh # start running the app

## Testing: 
Use Postman to test the routes as in /src/routes.py
