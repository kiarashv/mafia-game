from flask import Flask, render_template, request, redirect, url_for, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# List of all roles
roles = ["Mafia 1", "Mafia 2", "Mafia 3", "God Father", "Civilian 1", "Civilian 2", "Civilian 3", "Civilian 4", "Civilian 5", "Civilian 6", "Doctor", "Vigilante", "Detective", "Serial Killer", "Moderator"]
roles1 = [
    {"name": "Mafia 1", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/AEvted9QTGq._UX300_TTW__.jpg"},
    {"name": "Mafia 2", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/AEvted9QTGq._UX300_TTW__.jpg"},
    {"name": "Mafia 3", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/AEvted9QTGq._UX300_TTW__.jpg"},
    {"name": "God Father", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/7OBX1gvpRhWr._UX300_TTW__.jpg"},
    {"name": "Civilian 1", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/K0HABdw5QT6y._UX300_TTW__.jpg"},
    {"name": "Civilian 2", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/K0HABdw5QT6y._UX300_TTW__.jpg"},
    {"name": "Civilian 3", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/K0HABdw5QT6y._UX300_TTW__.jpg"},
    {"name": "Civilian 4", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/K0HABdw5QT6y._UX300_TTW__.jpg"},
    {"name": "Civilian 5", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/K0HABdw5QT6y._UX300_TTW__.jpg"},
    {"name": "Civilian 6", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/K0HABdw5QT6y._UX300_TTW__.jpg"},
    {"name": "Doctor", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/FaOhX5hSIav._UX300_TTW__.jpg"},
    {"name": "Vigilante", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/42Y2QvQRig._UX300_TTW__.jpg"},
    {"name": "Detective", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/ne9Qar7HQgG0._UX300_TTW__.jpg"},
    {"name": "Serial Killer", "image": "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/9fQh3cP4TdS0._UX300_TTW__.jpg"},
    {"name": "Moderator", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQoHxETATqlKvf5AfQBVSFOuTyBxE0Bo3LGA&s"}
]
images = {
        "Mafia 1" : "https://img.freepik.com/premium-vector/mafia-mascot-esport-logo-template_382438-727.jpg",
        "Mafia 2" : "https://thumbs.dreamstime.com/b/project-copy-152708468.jpg",
        "Mafia 3" : "https://cdn.vectorstock.com/i/500p/03/25/mafia-esport-mascot-logo-design-vector-50110325.jpg",
        "Mafia 4" : "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/AEvted9QTGq._UX300_TTW__.jpg",
        "God Father1" : "https://preview.redd.it/the-godfather-character-design-v0-2uiwnbgtuxsa1.png?width=640&crop=smart&auto=webp&s=b76462023f323ca0a532f489c3929a89749ab252",
        "God Father2" : "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/7OBX1gvpRhWr._UX300_TTW__.jpg",
        "God Father" : "https://images-cdn.fantasyflightgames.com/filer_public/24/7d/247d13ce-5542-43b7-82fa-0e8e317c4028/godfathercard.png",
        "Doctor1" : "https://img.freepik.com/premium-vector/vectorized-doctors-crafted-medical-stories-doctor-illustrations-vectors-health-mastery_772298-35714.jpg",
        "Doctor2" : "https://m.media-amazon.com/images/S/aplus-media/sc/2cd0eec5-b4e0-4bee-a0ba-e6b485ccdf6d.__CR0,0,744,744_PT0_SX300_V1___.jpg",
        "Doctor" : "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/FaOhX5hSIav._UX300_TTW__.jpg",
        "Vigilante1" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5NeVGoe1DiREriFSfbYCIdil8vKjl_JkWIw&s",
        "Vigilante" : "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/42Y2QvQRig._UX300_TTW__.jpg",
        "Detective2" : "https://audioboom.com/i/41517554/600x600/c.png",
        "Detective3" : "https://static.wikia.nocookie.net/mafia42/images/6/67/Jobcard_detective_new.png/revision/latest?cb=20180206084210",
        "Detective1" : "https://images-cdn.fantasyflightgames.com/filer_public/4a/81/4a815955-a64e-4366-90e4-4172368d06cf/detectivecard.png",
        "Detective" : "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/ne9Qar7HQgG0._UX300_TTW__.jpg",
        "Civilian 1" : "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/K0HABdw5QT6y._UX300_TTW__.jpg",
        "Civilian 2" : "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/K0HABdw5QT6y._UX300_TTW__.jpg",
        "Civilian 3" : "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/K0HABdw5QT6y._UX300_TTW__.jpg",
        "Civilian 4" : "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/K0HABdw5QT6y._UX300_TTW__.jpg",
        "Civilian 5" : "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/K0HABdw5QT6y._UX300_TTW__.jpg",
        "Civilian 6" : "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/K0HABdw5QT6y._UX300_TTW__.jpg",
        "Serial Killer1" : "https://images.squarespace-cdn.com/content/v1/5f59f5bb08078c5a7eb631a6/c7d74f32-da44-4cc2-a10a-9e478b7ce325/Untitled+design.jpg",
        "Serial Killer" : "https://m.media-amazon.com/images/S/aplus-seller-content-images-us-east-1/ATVPDKIKX0DER/A1UX6D2VNEE878/B00LGYO398/9fQh3cP4TdS0._UX300_TTW__.jpg"
    }
# In-memory storage to maintain the state of the game
game_state = {
    "selected_roles": [],
    "players": {},
    "moderator": None,
    "finished_selection": False,
    "votes": {},
    "voting_finished": {},
    "view_votes": False,
    "mafia_messages": [],
    "removed_players": [],
    "messages_to_moderator": []
}

@app.route('/')
def index():
    moderator = game_state['moderator']
    finished_selection = game_state['finished_selection']
    player_name = session.get('player_name', None)
    player_role = session.get('player_role', None)
    reveal = request.args.get('reveal', False)
    mafia_team = [name for name, role in game_state['players'].items() if role in ["Mafia 1", "Mafia 2", "Mafia 3", "God Father"]]
    return render_template('index.html', roles=roles, roles1=roles1, selected_roles=game_state['selected_roles'], players=game_state['players'], moderator=moderator, finished_selection=finished_selection, player_name=player_name, player_role=player_role, reveal=reveal, mafia_team=mafia_team, votes=game_state['votes'], voting_finished=game_state['voting_finished'], view_votes=game_state['view_votes'], mafia_messages=game_state['mafia_messages'], removed_players=game_state['removed_players'], messages_to_moderator=game_state['messages_to_moderator'])

@app.route('/set_moderator', methods=['POST'])
def set_moderator():
    name = request.form['moderator_name']
    game_state['moderator'] = name
    game_state['players'][name] = "Moderator"
    session['player_name'] = name
    session['player_role'] = "Moderator"
    return redirect(url_for('index'))

@app.route('/select_roles', methods=['POST'])
def select_roles():
    game_state['selected_roles'].clear()
    game_state['selected_roles'].extend(request.form.getlist('roles'))
    game_state['finished_selection'] = True
    return redirect(url_for('index'))

@app.route('/assign_role', methods=['POST'])
def assign_role():
    name = request.form['name']
    if name in game_state['players']:
        return f"Player {name} already has a role assigned."
    
    if not game_state['selected_roles']:
        return "No roles available to assign."
    
    role = random.choice(game_state['selected_roles'])
    game_state['selected_roles'].remove(role)
    game_state['players'][name] = role
    session['player_name'] = name
    session['player_role'] = role
    return redirect(url_for('index'))

@app.route('/reveal_roles', methods=['POST'])
def reveal_roles():
    if session.get('player_role') == "Moderator":
        return redirect(url_for('index', reveal=True))
    return redirect(url_for('index'))

@app.route('/reset_game', methods=['POST'])
def reset_game():
    game_state['selected_roles'].clear()
    game_state['players'].clear()
    game_state['moderator'] = None
    game_state['finished_selection'] = False
    game_state['votes'].clear()
    game_state['voting_finished'].clear()
    game_state['view_votes'] = False
    game_state['mafia_messages'].clear()
    game_state['removed_players'].clear()
    game_state['messages_to_moderator'].clear()
    session.clear()
    return redirect(url_for('index'))

@app.route('/vote', methods=['POST'])
def vote():
    voter = session.get('player_name')
    votes = request.form.getlist('votes')
    for vote in votes:
        if vote in game_state['votes']:
            game_state['votes'][vote].append(voter)
        else:
            game_state['votes'][vote] = [voter]
    game_state['voting_finished'][voter] = True
    return redirect(url_for('index'))

@app.route('/view_votes', methods=['POST'])
def view_votes():
    if session.get('player_role') == "Moderator":
        game_state['view_votes'] = True
    return redirect(url_for('index'))

@app.route('/reset_votes', methods=['POST'])
def reset_votes():
    game_state['votes'].clear()
    game_state['voting_finished'].clear()
    game_state['view_votes'] = False
    return redirect(url_for('index'))

@app.route('/send_mafia_message', methods=['POST'])
def send_mafia_message():
    if session.get('player_role') in ["Mafia 1", "Mafia 2", "Mafia 3", "God Father"]:
        message = request.form['message']
        player_name = session.get('player_name')
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        game_state['mafia_messages'].insert(0, {'player': player_name, 'message': message, 'timestamp': timestamp})
    return redirect(url_for('index'))

@app.route('/send_message_to_moderator', methods=['POST'])
def send_message_to_moderator():
    message = request.form['message']
    player_name = session.get('player_name')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    game_state['messages_to_moderator'].append({'player': player_name, 'message': message, 'timestamp': timestamp})
    return redirect(url_for('index'))

@app.route('/remove_players', methods=['POST'])
def remove_players():
    players_to_remove = request.form.getlist('remove')
    for player in players_to_remove:
        game_state['removed_players'].append(player)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
