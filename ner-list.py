import re
def get_string_joined(persons,orgs,locs):
  pers_1 = []
  for s in persons:
    s = s.replace('/PERSON','')
    pers_1.append(s)

  org_1 = []
  for s in orgs:
    s = s.replace('/ORGANIZATION','')
    org_1.append(s)

  loc_1 = []
  for s in locs:
    s = s.replace('/LOCATION','')
    loc_1.append(s)

  named_entitylist = []

  named_entitylist = [item for sublist in [pers_1, org_1, loc_1] for item in sublist]

  return named_entitylist

def get_named_entitylist(input_file):
  # Define the pattern for entities (ORGANIZATION, PERSON, LOCATION)
  entity_pattern_person = re.compile(r'\w+/PERSON(?:\s*[^/]+/PERSON)*')
  entity_pattern_org = re.compile(r'\w+/ORGANIZATION(?:\s*[^/]+/ORGANIZATION)*')
  entity_pattern_loc = re.compile(r'\w+/LOCATION(?:\s*[^/]+/LOCATION)*')

  with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()
  
  # Find all matching patterns in the text
  person_matches = re.findall(entity_pattern_person, text)
  org_matches = re.findall(entity_pattern_org, text)
  loc_matches = re.findall(entity_pattern_loc, text)

  entities = get_string_joined(person_matches,org_matches,loc_matches)
  return entities


def get_outputtxt(input_file,output_file):
  named_entities = get_named_entitylist(input_file)
  with open(output_file, 'w') as file:
    for ent in named_entities:
      file.write(f'{ent}\n')
      print(f'{ent}\n')

get_outputtxt('stanford-wikipedia.txt','ner-list-wikipedia.txt')
get_outputtxt('stanford-fanwiki.txt','ner-list-fanwiki.txt')