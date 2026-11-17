# Version 2: Formatted student information using string methods

# Ask for student details and remove extra leading/trailing spaces
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
favorite_subject = input("Enter favorite subject: ").strip()

# Combine and format strings
full_name = f"{first_name} {last_name}".title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_subject = favorite_subject.title()
character_count = len(full_name)

# Display formatted output
print("\nFormatted Output:")
print(f"Name: {full_name}")
print(f"Name Code: {name_code}")
print(f"Section: {formatted_section}")
print(f"Favorite Subject: {formatted_subject}")
print(f"Character Count: {character_count}")