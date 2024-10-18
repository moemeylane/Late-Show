import csv
from app import db
from app.models import Episode, Guest, Appearance

def seed_db():
    # Paths to your CSV files
    episodes_csv_path = 'app/episodes.csv'
    guests_csv_path = 'app/guests.csv'
    appearances_csv_path = 'app/appearances.csv'
    
    # Seed episodes
    with open(episodes_csv_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            episode = Episode(date=row['date'], number=row['number'])
            db.session.add(episode)

    # Seed guests
    with open(guests_csv_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            guest = Guest(name=row['name'], occupation=row['occupation'])
            db.session.add(guest)

    # Seed appearances
    with open(appearances_csv_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            appearance = Appearance(rating=row['rating'], episode_id=row['episode_id'], guest_id=row['guest_id'])
            db.session.add(appearance)

    db.session.commit()
