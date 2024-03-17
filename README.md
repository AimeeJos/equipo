
# About Project
This project have two assignments
## Assignment 1
Implemented a script to parse the data from the following website HCPC Codes into a csv format. All the codes available under the 17 categories of code are parsed and downloaded to csv files.

<i>Since it takes more time, Only the first 10 records of 17 categories are downloaded.</i> 

## Assignment 2
Implemented a UI to generate a downloadable consultation report in pdf format.

 
 

## Tech Stack

##### Frontend
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

##### Backend

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

##### Database

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## Run Locally

Clone the project

```bash
  git clone https://github.com/AimeeJos/equipo.git
  cd equipo
```

Build docker image.

```bash
  docker compose build
```

Start the server

```bash
  docker compose up
```
##### Run the server:

Home Page showing two options: 
- Assignment 1
- Assignment 2

```bash
  https://localhost:8000
```

###### Assignment 1.

We can download the codes
like button name: Download HCPC 'A' Codes
<i>First 10 records of each category are downloaded.</i>
```bash
  http://localhost:8000/assign1/
```

###### Assignment 2.
We can download the consultation report automatically after submitting the form by clicking Generate Report button.

```bash
http://localhost:8000/assign2/
```
