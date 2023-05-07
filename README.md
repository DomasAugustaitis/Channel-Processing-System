# Channel Processing System
Submitted by Domas Augustaitis </br>
augustaitis.domas@gmail.com </br>
07500681193

## Aplication description

The application is a python app that uses numpy for array manipulation and pytest for unit tests. The application is controlled using main.py with the help of user inputs within the console.

## What's included in the submission

The root folder contains channel processor files and test files. Channel processor files are:
- channel_processor.py - main channel processor class that contains the functions and channels / parameters. When instantiated it reads the parameters within the parameters.txt and channels.txt files.
- main.py - main application controller. Uses command line to get user inputs and execute actions.
- Dockerfile - docker description to build the python image

Test files are:
- test_channel_processor.py - pytest script that tests our function for the existing inputs within the test_files folder (test_files/channels.txt and test_files/parameters.txt)

## How to run the application

1. Application can be run locally from the root folder:
```
pip install numpy
python main.py
```
2. Application can be built and ran as a container. From inside the root folder run:
```
docker build -t cps .
docker run -i --name cps-container cps
```

## How to test the application
From the root folder:
```
pip install pytest
pytest
```

## How can we find metric b using channel processor function and given parameters/channels?

1. Use function 1 to calculate channel Y using given m, c and X
2. use function 3 to calculate channel A using X
3. use function 2 to calculate channel B using A and Y from functions 1 and 3. Calculate b as the mean of B. b = 6.269852166777007
