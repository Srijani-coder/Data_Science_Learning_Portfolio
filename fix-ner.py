import spacy
def fix_ner_tags(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    fixed_text = []
    
    for token in doc:
        if token.is_punct and token.ent_iob_ != 'O':
            fixed_text.append(token.text + "/O")
        else:
            fixed_text.append(token.text + "/" + token.ent_iob_ + token.ent_type_)
    
    return " ".join(fixed_text)
def get_fixner_applied(input_file,output_file):
  with open(input_file, 'r', encoding='utf-8') as file:
        file_content = file.read()
  wtext = fix_ner_tags(file_content)
  textlist = wtext.split(' ')
  newlist = []
  for tex in textlist:
      if tex == '//O':
          tex.replace('//O','/ O')
      else:
          if tex != '/ O':
              tex.replace('/','')
      newlist.append(tex)

  with open(output_file, 'w', encoding='utf-8') as files:
    for tp in newlist:
        files.write(f'{tp}\n')

  return output_file

import subprocess

# Command to run the Stanford NER using ner.sh script
stanford_ner_command = [
    "./ner.sh",  # Replace with the actual path to ner.sh
    "wikipedia.txt",  # Input file containing Wikipedia text
]

# Run Stanford NER for Wikipedia text and redirect the output
with open("stanford-wikipedia2.txt", "w", encoding="utf-8") as output_file:
    subprocess.call(stanford_ner_command, stdout=output_file)

# Command to run the Stanford NER for Fanwiki text
stanford_ner_command = [
    "./ner.sh",  # Replace with the actual path to ner.sh
    "fanwiki.txt",  # Input file containing Fanwiki text
]

# Run Stanford NER for Fanwiki text and redirect the output
with open("stanford-fanwiki2.txt", "w", encoding="utf-8") as output_file:
    subprocess.call(stanford_ner_command, stdout=output_file)

print("Stanford NER processing completed.")


get_fixner_applied("stanford-wikipedia2.txt", "wikipedia_gold2.txt")
get_fixner_applied("stanford-fanwiki2.txt","fanwiki_gold2.txt")
        