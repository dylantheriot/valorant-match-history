from flask import Flask, render_template, request, redirect, url_for
import json
from .valApi import ValorantAPI
import time

app = Flask(__name__)

match_movement_hash = {
  'INCREASE': 'Increase',
  'MINOR_INCREASE': 'Minor Increase',
  'MAJOR_INCREASE': 'Major Increase',
  'DECREASE': 'Decrease',
  'MAJOR_DECREASE': 'Major Decrease',
  'MINOR_DECREASE': 'Minor Decrease',
  'PROMOTED': 'Promoted',
  'DEMOTED': 'Demoted'
}

@app.before_request
def before_request():
    scheme = request.headers.get('X-Forwarded-Proto')
    if scheme and scheme == 'http' and request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

@app.route('/')
def home():
  return render_template('login.html')
  # return '<h1>Hello World<h1>'

#   return Response(json_res, mimetype="application/json")

@app.route('/match_history', methods=['GET'])
def redirect_to_login():
  return redirect(url_for('home'))

@app.route('/match_history', methods=['POST'])
def display_match_history():
  try:
    username = request.form['username']
    password = request.form['password']

    valorant = ValorantAPI(username, password)
    print('hello world')

    json_res = valorant.get_match_history()

    posts = []
    for match in json_res['Matches']:
      # print(match)
      if match['CompetitiveMovement'] == 'MOVEMENT_UNKNOWN':
        continue
      game_outcome = 'Victory' if 'INCREASE' in match['CompetitiveMovement'] or 'PROMOTED' in match['CompetitiveMovement'] else 'Defeat'
      lp_change = ''

      tier = 'images/ranks/' + str(match['TierAfterUpdate']) + '.png'
      epoch_time = match['MatchStartTime'] // 1000
      date = time.strftime('%m-%d-%Y', time.localtime(epoch_time))

      before = match['TierProgressBeforeUpdate']
      after = match['TierProgressAfterUpdate']

      if match['CompetitiveMovement'] == 'PROMOTED':
        lp_change = '+' + str(after + 100 - before)
        match_data = {
          'lp_change': lp_change,
          'current_lp': after,
          'game_outcome': game_outcome,
          'movement': match_movement_hash[match['CompetitiveMovement']],
          'tier': tier,
          'date': date
        }
      elif match['CompetitiveMovement'] == 'DEMOTED':
        lp_change = '-' + str(before + 100 - after)
        match_data = {
          'lp_change': lp_change,
          'current_lp': after,
          'game_outcome': game_outcome,
          'movement': match_movement_hash[match['CompetitiveMovement']],
          'tier': tier,
          'date': date
        }
      else:
        if before < after:
          # won
          lp_change = '+' + str(after - before)
        else:
          # lost
          lp_change = str(after - before)

        match_data = {
          'lp_change': lp_change,
          'current_lp': after,
          'game_outcome': game_outcome,
          'movement': match_movement_hash[match['CompetitiveMovement']],
          'tier': tier,
          'date': date        
        }
      posts.append(match_data)
    # print(posts)
    return render_template('match_history.html', posts=posts, name=valorant.game_name)
  except:
    return render_template('error.html')