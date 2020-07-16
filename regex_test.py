import re

# Define a body of text
text = '''
[Joan] is a bishop who lives in <Shaley Village>. She woke up one morning to a loud explosion outside *her hut*. 
Four goblins raided her house and stole her {mother’s tapestry}! 

She could hear the mutterings of [Saal Mor], the evil sorcerer, outside her door. She grabbed her sword and dashed out 
the door. She was determined to &kill Saal# and &get her tapestry back from the goblins#
'''

def gather_items(matches):
  for match in matches:
    yield match.group(0)

# Define regexes that pull desired information
r_characters = r'(?<=\[).*?(?=\])'
r_locations = r'(?<=\<).*?(?=\>)'
r_places = r'(?<=\*).*?(?=\*)'
r_items = r'(?<=\{).*?(?=\})'
r_objectives = r'(?<=&).*?(?=#)'

# Run patterns against the body of text
things = re.compile(r_places)
matches = things.finditer(text)
result = gather_items(matches)

# Print a pattern to the screen
for x in result:
  print(x)