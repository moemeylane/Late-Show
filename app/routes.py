from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/episodes', methods=['GET'])
def get_episodes():
    from app import db
    from app.models import Episode  # Importing here to avoid circular imports
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

@main.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    from app import db
    from app.models import Episode
    episode = Episode.query.get(id)
    if episode:
        return jsonify(episode.to_dict()), 200
    return jsonify({"error": "Episode not found"}), 404

@main.route('/guests', methods=['GET'])
def get_guests():
    from app import db
    from app.models import Guest
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

@main.route('/appearances', methods=['POST'])
def create_appearance():
    from app import db
    from app.models import Appearance

    data = request.get_json()
    rating = data.get('rating')
    
    if rating is None or not (1 <= rating <= 5):
        return jsonify({"errors": ["Rating must be between 1 and 5."]}), 400

    try:
        new_appearance = Appearance(
            rating=rating,
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(new_appearance)
        db.session.commit()
        return jsonify(new_appearance.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": ["Failed to create appearance"]}), 400
