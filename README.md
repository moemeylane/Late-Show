
# Episodes and Guests API

## Description
The Episodes and Guests API is a RESTful web service designed to manage data related to episodes of a show, guest appearances, and their associations. This API allows users to create, read, update, and delete entries for episodes and guests, providing an interface for developers to integrate episode and guest management functionalities into their applications.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)

## Features
- **Episode Management**: Create, retrieve, update, and delete episodes.
- **Guest Management**: Manage guest data, including their names and occupations.
- **Appearance Management**: Link guests to episodes through appearances and manage ratings for these appearances.
- **Validation**: Ensure that appearance ratings are within an acceptable range (1 to 5).

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone git@github.com:moemeylane/Late-Show.git
   cd Late-Show
Create a virtual environment:

bash

`python3 -m venv virtual`
Activate the virtual environment:

bash

`source virtual/bin/activate`
Install dependencies:

bash

`pip install -r requirements.txt`
Initialize the database and seed data:

bash

`run seed.py`
Usage
To run the application, execute the following command:

bash

`python run.py`
The application will be available at `http://127.0.0.1:5555/.`

API Endpoints
Episodes
GET /episodes - Retrieve a list of all episodes.
GET /episodes/<id> - Retrieve an episode by ID.
POST /episodes - Create a new episode.
PATCH /episodes/<id> - Update an episode by ID.
DELETE /episodes/<id> - Delete an episode by ID.
Guests
GET /guests - Retrieve a list of all guests.
GET /guests/<id> - Retrieve a guest by ID.
POST /guests - Create a new guest.
PATCH /guests/<id> - Update a guest by ID.
DELETE /guests/<id> - Delete a guest by ID.
Appearances
POST /appearances - Associate a guest with an episode and create a new appearance.
Database Schema
The following tables are used in the database:

Episodes: Contains the episode entries.

Columns: id, date, number
Guests: Contains the guest entries.

Columns: id, name, occupation
Appearances: Association table linking guests to episodes with ratings.

Columns: id, rating, episode_id, guest_id
