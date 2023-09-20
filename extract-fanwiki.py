import fandom
fandom.set_wiki("jojo")
fandom.set_lang("en") # English

# Define your student number's last digit
student_number_last_digit = 9  # Replace with your last digit

# Define the character for your student number
characters = [
    "Jonathan Joestar",
    "Robert E. O. Speedwagon",
    "Dio Brando",
    "Jotaro Kujo",
    "Noriaki Kakyoin",
    "Jean Pierre Polnareff",
    "Iggy",
    "Hol Horse",
    "Josuke Higashikata",
    "Koichi Hirose",
]

# Get the character for your student number
character_name = characters[student_number_last_digit]

# Search for the character's page
result = fandom.search(character_name)
character_name, year_of_birth = result[1]
page = fandom.page(character_name)
tale = page.plain_text
with open("fanwiki.txt", "w", encoding="utf-8") as file:
    file.write(tale)