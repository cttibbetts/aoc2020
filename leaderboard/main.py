import sys
import json
import math
from argparse import ArgumentParser
from datetime import timedelta, datetime
from tabulate import tabulate

DEBUG = False

teams = {
  'nma': [
    'Christopher Tibbetts',
    'Taybin Rutkin',
    'Matthew Doherty',
    'Khaled Asaad',
    'Phuongnhat Nguyen',
    'Micah Abresch',
    'Shawn Whitney',
    'Elise Thorsen',
    'Jacob Coakwell',
    'David Cyprian',
    'Marc Engelson'
  ],
  'boston': [
    'Matthew Doherty',
    'Douglas Bodkin',
    'Ben Goldin',
    'Nicholas Davis',
    'Philippe Mimms',
    'Taybin Rutkin',
    'Christopher Tibbetts',
    'Phuongnhat Nguyen',
    'Nicholas Chounlapane',
    'Adam Mantell',
    'David Dulczewski',
    'Michael Singleton',
    'Brendan Terrio',
    'Daniel St. George',
    'Melissa Blotner',
    'Nathaniel Bowditch',
    'Kraig Boates',
    'Steven Keith',
    'Geoffrey Sullivan',
    'Christopher Regan',
    'Steve Carlon',
  ]
}

whitelist = None
# whitelist = teams['nma']
# whitelist = teams['boston']

def to_relative_seconds(day_number, timestamp):
  day_number -= 1 # offset by one
  dec_1 = 1575176400
  day_delta = 86400
  return timestamp - (dec_1 + day_number * day_delta)

def print_ts(delta):
  return str(timedelta(seconds=delta))

def get_median_solve(user):
  score = 0
  try:
    half = math.floor(len(user['scores'])/2)

    if len(user['scores']) % 2 == 0:
      score = math.ceil((user['scores'][half-1] + user['scores'][half]) / 2)
    else:
      score = user['scores'][half]
  except:
    pass
  return score

def get_middle_scores(user):
  scores = user['scores']
  half = math.floor(len(scores)/2)
  return scores[half-1:half+2]

def sort_users(user):
  return user['stars'], -user['median_score']

def process_user(user):
  user['scores'] = sorted([
    to_relative_seconds(int(day), int(score['2']['get_star_ts']))
    for day, score in user['completion_day_level'].items()
    if '2' in score
  ])
  user['median_score'] = get_median_solve(user)
  if (user['name'] == 'Christopher Tibbetts' and DEBUG):
    print([print_ts(s) for s in user['scores']])
  return user

def get_user_markdown(user_list, name):
  for user in user_list.values():
    if user['name'] == name:
      process_user(user)
      scores = user['completion_day_level']
      print(f"{user['name']} - Median solve time: {print_ts(user['median_score'])}\n")
      print("| Day | Star 1 | Star 2 |")
      print("| --- | --- | --- |")
      days = sorted([int(s) for s in scores.keys()])
      for day in days:
        score = scores[str(day)]
        star1 = to_relative_seconds(day, int(score['1']['get_star_ts']))
        star2 = to_relative_seconds(day, int(score['2']['get_star_ts']))
        print(f"| {day} | {print_ts(star1)} | {print_ts(star2)} |")
      break


if __name__ == '__main__':
  parser = ArgumentParser()
  parser.add_argument('--team', type=str)
  parser.add_argument('--user', type=str)
  args = parser.parse_args()

  with open('leaderboard.json') as input:
    scoreboard = json.loads(input.readline())
  users = scoreboard['members']

  if args.user != 'None':
    user = 'Christopher Tibbetts' if args.user == 'me' else args.user
    get_user_markdown(users, user)
    exit()
  if args.team != 'None':
    whitelist = teams.get(args.team)

  users = sorted(
    [process_user(u) for u in users.values()],
    key=sort_users,
    reverse=True
  )

  table = [
    ([i+1, user['name'], user['stars'] * '*', print_ts(user['median_score']), *[print_ts(ts) for ts in get_middle_scores(user)]])
    for i, user in enumerate(users)
    if user['stars'] > 0 and (user['name'] in whitelist if whitelist is not None else True)
  ]
  print(tabulate(table, headers=["Place", "Name", "Stars", "Median Solve Time", "better", "current", "worse"]))
