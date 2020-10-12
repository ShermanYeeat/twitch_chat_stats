from chat_replay_downloader import get_chat_replay, get_youtube_messages, get_twitch_messages


emotes = ['TriHard', 'LUL', '<3', 'PogChamp', 'cmonBruh', 'Nam', 'Clap', 'FeelsGoodMan',
        'gachiBASS', 'OMEGALUL', 'pepeD', 'monkaS', 'AYAYA', 'pepeJAM', 'pepeL', 'Pog',
        'KEKW', 'PogU', 'monkaW', 'WeirdChamp', 'Pepega', 'Yep', 'PepeHands', 'PepeLaugh'
        'forsenCD', 'Sadge']
twitch_messages = get_chat_replay('https://www.twitch.tv/videos/766290997', start_time = 600, end_time = 660)

top_users = {}
top_emotes = {}
for item in twitch_messages:
    user_log = list(item.values())[3: 5] # [timestamp, time text, time in seconds, author, message]
    author = user_log[0]
    message = user_log[1]
    if 'bot' in author:
        continue
    elif author in top_users:
        top_users[author] += 1
    else:
        top_users[author] = 1

    words = message.split()
    for word in words:
        if word in emotes:
            if word in top_emotes:
                top_emotes[word] += 1
            else:
                top_emotes[word] = 1

    

top_users = sorted(top_users.items(), key=lambda x: x[1], reverse=True)
print(top_users[:10])

top_emotes = sorted(top_emotes.items(), key=lambda x: x[1], reverse=True)
print(top_emotes[:10])

