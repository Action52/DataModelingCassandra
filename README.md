## Sparkify DB

Sparkify is now needing to answer some questions that could indicate how users interact with their system.
To achieve this, the proposal is to implement a Cassandra Database with specific tables that will quickly answer 
those queries.

### Requirements
To run this project on your local machine you will need:
* Python >= 3.7
* Docker
* Conda or mini conda to install the environment.

### Installation

To install the repository as a Python package open a new terminal window, cd to the root of this project and execute the
following commands.

``````
conda create --name dmc python=3.7 --no-default-packages  
conda activate dmc
``````

This commands will create and start a clean conda environment to run the project.
Once we have set the environment, we can install the repo by simply doing, on the root of this repo:
`pip install -e .` This command executes the _setup.py_ script and installs the dependencies.

### Starting the Postgres service
This project works with a docker-compose.yml file. To start the service, type on the same terminal as before:
`docker-compose up -d`, which will start a containerized Cassandra server while running on the background.
If you want to bring it down after using this repo, simply type `docker-compose down`.

### Running the data_modeling_cassandra.ipynb notebook

To run the notebook we first have to start a Jupyter notebook server with our env active, from the root of this project.
``````
conda activate dmc
jupyter notebook
``````
This will prompt us to a web page with our notebooks. If you are not prompted into the page, go to 
`localhost:8888` on your browser. This is the native Jupyter port.  
Once in the folder, you will be able to see the root folder of this project. Please access the 
"scripts" folder and double click on the "data_modeling_cassandra.ipynb" notebook.
This will open the notebook.

The schema for this db, since we are using Cassandra, is completely query-based. We want to answer 3 important questions
so we have to create 3 different tables.
#### Queries
- Artist, title, and length of a song by session_id and item_in_session.
This table represents the data related to the songs, such as the title, the artist_id, year and duration.
- Name of artist, song title (sorted by item_in_session), and (FN, LN) of the user, search by user_id and session_id.
This table contains the data of the artists, like name, location, altitude and longitude.
- User name (FN, LN) who listened to a specific song.
This table contains the reference for the timestamp on the logs. It is split into start_time, hour, day, week, month, year,
and weekday.

### References

* https://hub.docker.com/_/cassandra
* https://medium.com/swlh/building-a-python-data-pipeline-to-apache-cassandra-on-a-docker-container-fc757fbfafdd