import subprocess

# Command to run the Stanford NER using ner.sh script
stanford_ner_command = [
    "./ner.sh",  # Replace with the actual path to ner.sh
    "wikipedia.txt",  # Input file containing Wikipedia text
]

# Run Stanford NER for Wikipedia text and redirect the output
with open("stanford-wikipedia.txt", "w", encoding="utf-8") as output_file:
    subprocess.call(stanford_ner_command, stdout=output_file)

# Command to run the Stanford NER for Fanwiki text
stanford_ner_command = [
    "./ner.sh",  # Replace with the actual path to ner.sh
    "fanwiki.txt",  # Input file containing Fanwiki text
]

# Run Stanford NER for Fanwiki text and redirect the output
with open("stanford-fanwiki.txt", "w", encoding="utf-8") as output_file:
    subprocess.call(stanford_ner_command, stdout=output_file)

print("Stanford NER processing completed.")
