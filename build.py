#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader
from yaml import load 
from datetime import datetime, timezone

env = Environment(
  loader=FileSystemLoader('.'))

with open('items.yaml') as f:
  items = load(f)

template = env.get_template('podcast.xml.j2')

with open('podcast.xml', 'w') as f:
  f.write(template.render(build_date=datetime.now(timezone.utc), items=list(reversed(items))))


