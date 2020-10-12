from flask import Flask, jsonify
from chat_replay_downloader import get_chat_replay, get_youtube_messages, get_twitch_messages
import time
import json

app = Flask(__name__)

@app.route('/time')

def get_current_time():
    return {'time': time.time()}


@app.route('/test')
def test():
    twitch_messages = get_chat_replay('https://www.twitch.tv/videos/766290997', start_time = 600, end_time = 660)
    top_users = {}
    for item in twitch_messages:
        author = list(item.values())[3] # [timestamp, time text, time in seconds, author, message]
        if 'bot' in author:
            continue
        elif author in top_users:
            top_users[author] += 1
        else:
            top_users[author] = 1

    top_users = sorted(top_users.items(), key=lambda x: x[1], reverse=True)[:10]
    userValues = []
    for user, messages in top_users:
        userValues.append({'user': user, 'messages': messages})
    return jsonify(userValues)



@app.route('/test2')
def test2():
    emotes = ['TriHard', 'LUL', 'Love', 'PogChamp', 'cmonBruh', 'Nam', 'Clap', 'FeelsGoodMan',
        'haHAA', 'gachiBASS', 'OMEGALUL', 'pepeD', 'monkaS', 'AYAYA', 'pepeJAM', 'pepeL', 'Pog',
        'KEKW', 'PogU', 'monkaW', 'WeirdChamp', 'Pepega', 'Yep', 'PepeHands', 'PepeLaugh'
        'forsenCD', 'Sadge', '5Head']
    twitch_messages = get_chat_replay('https://www.twitch.tv/videos/766290997', start_time = 600, end_time = 660)

    top_emotes = {}
    for item in twitch_messages:
        message = list(item.values())[4] # [timestamp, time text, time in seconds, author, message]
        words = message.split()
        for word in words:
            if word in emotes:
                if word in top_emotes:
                    top_emotes[word] += 1
                else:
                    top_emotes[word] = 1

    top_emotes = sorted(top_emotes.items(), key=lambda x: x[1], reverse=True)[:10]
    emoteValues = []
    for emote, messages in top_emotes:
        emoteValues.append({'emote': emote, 'messages': messages})

    return jsonify(emoteValues)
