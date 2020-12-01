from invoke import task
from datetime import datetime

@task
def run(c, day):
  with c.cd(day):
    c.run(f"python3 main.py")

@task
def init(c, day):
  c.run(f"mkdir -p {day}")
  c.run(f"cp template/* {day}/")

@task
def readme(c):
  c.run("""
    printf "# [Advent of Code 2020](https://adventofcode.com/2020)\n\n" > README.md
    cd leaderboard; python3 main.py --user me >> ../README.md
  """)

@task
def leaderboard(c, team=None, user=None):
  with c.cd('leaderboard'):
    c.run(f"python3 main.py --team {team} --user {user}")