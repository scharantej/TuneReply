
from flask import Flask, render_template, request, redirect, url_for, flash
import music_player
import auto_reply

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/play', methods=['POST'])
def play():
    track_id = request.form['track_id']
    music_player.play(track_id)
    return redirect(url_for('index'))

@app.route('/pause', methods=['POST'])
def pause():
    music_player.pause()
    return redirect(url_for('index'))

@app.route('/skip', methods=['POST'])
def skip():
    music_player.skip()
    return redirect(url_for('index'))

@app.route('/stop', methods=['POST'])
def stop():
    music_player.stop()
    return redirect(url_for('index'))

@app.route('/create_playlist', methods=['POST'])
def create_playlist():
    playlist_name = request.form['playlist_name']
    music_player.create_playlist(playlist_name)
    return redirect(url_for('index'))

@app.route('/search_music', methods=['POST'])
def search_music():
    query = request.form['query']
    results = music_player.search_music(query)
    return render_template('index.html', results=results)

@app.route('/auto_reply', methods=['POST'])
def auto_reply():
    trigger = request.form['trigger']
    message = request.form['message']
    auto_reply.set_auto_reply(trigger, message)
    return redirect(url_for('settings'))

@app.route('/disable_auto_reply', methods=['POST'])
def disable_auto_reply():
    auto_reply.disable_auto_reply()
    return redirect(url_for('settings'))

@app.route('/share_music', methods=['POST'])
def share_music():
    track_id = request.form['track_id']
    email = request.form['email']
    message = request.form['message']
    music_player.share_music(track_id, email, message)
    return redirect(url_for('index'))

@app.route('/connect_streaming', methods=['POST'])
def connect_streaming():
    service = request.form['service']
    music_player.connect_streaming(service)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
