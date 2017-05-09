#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader
from yaml import load 
from datetime import datetime, timezone
from git import Repo
import os
import sys

repo_path = os.path.dirname(os.path.realpath(__file__))
repo = Repo( repo_path )

changedFiles = [ item.a_path for item in repo.index.diff(None) ]

if len(changedFiles) > 0:
  print("There are changed files; please commit and run build.py again")
  sys.exit(1)

env = Environment(
  loader=FileSystemLoader('.'))

with open('items.yaml') as f:
  items = load(f)

template = env.get_template('podcast.xml.j2')

with open('podcast.xml', 'w') as f:
  f.write(template.render(build_date=datetime.now(timezone.utc), items=list(reversed(items))))


