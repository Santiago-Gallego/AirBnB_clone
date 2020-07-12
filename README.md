<img src="abnb.png" width="500" align="right">

# Holberton School - AirBnB_clone
This project is the first phase to get a complete AirBnB clone.<br>The main object is to create a command line interpreter to manage AirBnB objects.
JSON files are used to organize and save the information.

----

## INSTALLATION

1. Git clone this repository

```bash
 $ git clone https://github.com/AlejoCasti/AirBnB_clone.git
```

2. Execute

```bash
 $ ./console.py
```

## USAGE

### INTERACTIVE MODE

Interactive mode allows you to enter as many commands as you want.
Also allows you to exit in two ways, writing ```quit```

To run console of AirBnB just execute the command below

```bash
 $ ./console.py
```

It will display this screen that means you are inside
```bash
 $ (hbnb)
```
```bash
 $ ./console.py
 $ help
 
 Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

 $ (hbnb)
```
## AVAILABLE COMMANDS

| Command | Description  |
| ------- | --- |
| quit | Exit console AirBnB|
| help (command) | Display help documentation of every command |
| all (className) | Display all objects, if you give a class it'll display all objects from that class |
| create (className) | Create a object from that class |
| destroy (id) | Destroy a object where id is the same |
| show (id) | Display the information of a specific object got from your id |
| update (id, name_of_attribute, value_attribute) | Update information of an object |

This commands also can be used in this way:
```bash
$ (hbnb) className.create()
$ (hbnb) className.all()
$ (hbnb) className.destroy(<id>)
$ (hbnb) className.show(<id>)
$ (hbnb) className.update(<id>, <attribute name>, <attribute value>)
```

## EXAMPLES

### create

```bash
$ (hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```

### all
```bash

$ (hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293),
'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```
### show
```bash

$ (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293),
'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```
### update
```bash

$ (hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
```
### show
```bash

$ (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907',
'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```
### destroy
```bash

$ (hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
```
### show
```bash

$ (hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```

## FILES AND DIRECTORIES

### DIRECTORIES

| Directory | Description  |
| ------- | --- |
| models | Models of every class included manage files |
| models/engine | Manage file storage |
| test | testing of the program |

### FILES

| File | Description  |
| ------- | --- |
| console.py| Executable file to start console |
| models/*.py | Classes files |
| models/base_model.py | Base model to create another class |
| models/engine/file_storage.py | Manage of file storage |

## AUTHORS

Santiago Gallego - @Santiago-Gallego<br>
Alejandro Castiblanco @AlejoCasti
