import wikipedia
import os

# Set the language for Wikipedia (e.g., "en" for English)
wikipedia.set_lang("en")

# Define the actor's name and minimum word count
actor_name = "Sigourney Weaver"
min_word_count = 500

# Extract the main text from the actor's Wikipedia page
try:
    actor_page = wikipedia.page(actor_name)
    content = actor_page.content
    words = content.split()
    
    # Check if the content has at least the minimum word count
    if len(words) >= min_word_count:
        # Save the content to wikipedia.txt
        with open("wikipedia.txt", "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Successfully saved Wikipedia data for {actor_name} to wikipedia.txt")
    else:
        print(f"The Wikipedia page for {actor_name} does not have enough content.")
except wikipedia.exceptions.PageError:
    print(f"Wikipedia page for {actor_name} not found.")
except wikipedia.exceptions.DisambiguationError as e:
    print(f"Disambiguation: {e.options}")
