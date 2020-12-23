import requests
import json
import urllib.parse

class ValorantAPI(object):
  access_token = None
  cookies = None
  entitlements_token = None

  def __init__(self, username, password):
    self.username = username
    self.password = password

    self.cookies = self.get_cookies()

    self.access_token = self.get_access_token()

    self.entitlements_token = self.get_entitlements_token()

    self.user_info = self.get_user_info()

  def get_cookies(self):
    data = {
    'client_id': 'play-valorant-web-prod',
    'nonce': '1',
    'redirect_uri': 'https://beta.playvalorant.com/opt_in',
    'response_type': 'token id_token',
    'scope': 'account openid',
    }
    r = requests.post('https://auth.riotgames.com/api/v1/authorization', json=data)
    cookies = r.cookies

  def get_access_token(self):
    data = {
      'type': 'auth',
      'username': self.username,
      'password': self.password
    }
  
    r = requests.put('https://auth.riotgames.com/api/v1/authorization', json=data, cookies=self.cookies)
    uri = r.json()['response']['parameters']['uri']
    jsonUri = urllib.parse.parse_qs(uri)

    access_token = jsonUri['https://beta.playvalorant.com/opt_in#access_token'][0]

    return access_token

  def get_entitlements_token(self):
    headers = {
      'Authorization': f'Bearer {self.access_token}',
    }
    r = requests.post('https://entitlements.auth.riotgames.com/api/token/v1', headers=headers, json={}, cookies=self.cookies)

    entitlements_token = r.json()['entitlements_token']

    return entitlements_token

  def get_user_info(self):
    headers = {
      'Authorization': f'Bearer {self.access_token}',
    }
    r = requests.post('https://auth.riotgames.com/userinfo', headers=headers, json={})
    user_info = r.json()['sub']

    return user_info

  def get_match_history(self):
    # TODO: Allow different regions besides NA
    headers = {
      'Authorization': f'Bearer {self.access_token}',
      'X-Riot-Entitlements-JWT': f'{self.entitlements_token}'
    }
    r = requests.get(f'https://pd.na.a.pvp.net/mmr/v1/players/{self.user_info}/competitiveupdates?startIndex=0&endIndex=20', headers=headers)

    jsonData = r.json()

    return jsonData