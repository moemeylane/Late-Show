import csv
from app import db
from app.models import Episode, Guest, Appearance

def seed_db():
    # Paths to your CSV files
    episodes_csv_path = 'app/episodes.csv'
    guests_csv_path = 'app/guests.csv'
    appearances_csv_path = 'app/appearances.csv'

    # Seed episodes
    try:
        with open(episodes_csv_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                episode = Episode(date=row['date'], number=int(row['number']))  # Ensure number is an integer
                db.session.add(episode)
        db.session.commit()  # Commit after adding all episodes
    except Exception as e:
        print(f"Error seeding episodes: {e}")
        db.session.rollback()  # Rollback if there's an error

    # Seed guests
    try:
        with open(guests_csv_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                guest = Guest(name=row['name'], occupation=row['occupation'])
                db.session.add(guest)
        db.session.commit()  # Commit after adding all guests
    except Exception as e:
        print(f"Error seeding guests: {e}")
        db.session.rollback()  # Rollback if there's an error

    # Seed appearances
    try:
        with open(appearances_csv_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                rating = int(row['rating'])  # Ensure rating is an integer
                appearance = Appearance(rating=rating, episode_id=row['episode_id'], guest_id=row['guest_id'])
                db.session.add(appearance)
        db.session.commit()  # Commit after adding all appearances
    except Exception as e:
        print(f"Error seeding appearances: {e}")
        db.session.rollback()  # Rollback if there's an error
