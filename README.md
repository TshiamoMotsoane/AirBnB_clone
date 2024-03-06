#AirBnB clone - The console

##Project description
This project aims to create a version of the popular vacation rental online
market place, AirBnB. The project involves building a command-line interface
(CLI) for managing properties, users, bookings, and other functionalities
similar to AirBnB. The implementation will include HTML/CSS templating for the
frontend, database storage and data persistenve, API for communication between
frontend and backend intergration of frontend components.

##Description of the command interpreter
The command interpreter serves as the main interface for interacting with AirBnB clone functionalities. It allows users to perform various actions such as:
-creating
-updating
-deleting properties
-managing users
-searching for properties
-making bookings

##How to use the CMI
.`create <model>`: Create a new instance of model(e,g.,property, user).
.`update <model> <id>`: Update the attributes of an existing model instance.
.`destroy <model> <id>`: Delete a model instance.
.`show <model> <id>`: Display details of a specific model instance.
.`all <model>`: List all instances of a model.
.`help`: Display help information about available commands and their usage.

##How to start
-Clone the repository to your local machine:
git clone https://github.com/yourusername/airbnb-clone.git

-Navigate to the project directory:
cd airbnb-clone
-Thereafter you will then be able to create files that will allow the program
to work

-Consol.py
The main executable of the project.

-models/engin/file_storage.py
Class that serializes instances to a JSON file and deserializes JSON file to
instances

-models/__init__.py
A unique FileStorage instance for the application

-models/base_model.py
A class that defines all common attributes/methods for other classes.

-models/user.py
User class that inherits from BaseModel

-models/state.py
State class that inherits from BaseModel

-models/city.py
City class that inherits from BaseModel

-models/amenity.py
Amenity class that inherits from BaseModel

-models/place.py
Place class that inherits from BaseModel

-models/review.py
Review class that inherits from BaseModel


##How to use it
It can work in both Interactive and Non-interactive mode

Interactive mode

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

-Non-interactive mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
