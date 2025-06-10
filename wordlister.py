import itertools

def collect_inputs():
    print("\n💡 Enter target info (press Enter to skip optional ones)\n")
    data = {
        'first_name': input("First Name: ").strip(),
        'last_name': input("Last Name: ").strip(),
        'nickname': input("Nickname: ").strip(),
        'birth_year': input("Birth Year (YYYY): ").strip(),
        'birth_month': input("Birth Month (MM): ").strip(),
        'birth_day': input("Birth Day (DD): ").strip(),
        'pet_name': input("Pet Name: ").strip(),
        'father_name': input("Father’s Name: ").strip(),
        'mother_name': input("Mother’s Name: ").strip(),
        'fav_team': input("Favorite Team: ").strip(),
        'lucky_number': input("Lucky Number: ").strip(),
        'custom_words': input("Any custom keywords (comma-separated): ").strip().split(',')
    }
    return {k: v for k, v in data.items() if v and v != ['']}

def generate_variations(info):
    keywords = set()

    for k, v in info.items():
        if isinstance(v, list):
            for word in v:
                if word.strip(): keywords.add(word.strip().lower())
        else:
            keywords.add(v.lower())

    # Add combos like name+birth, pet+year etc.
    combos = set()
    for a, b in itertools.permutations(keywords, 2):
        combos.add(a + b)
        combos.add(b + a)
        combos.add(a + b + "123")
        combos.add(a + b + "!")
        combos.add(a + b + "@123")

    # Add some classic suffixes
    suffixes = ["123", "1234", "!", "2024", "@", "@123", "786", "007"]
    final_words = set()

    for word in keywords.union(combos):
        final_words.add(word)
        for suf in suffixes:
            final_words.add(word + suf)

    return sorted(final_words)

def save_wordlist(words, first_name, filename=None):
    if not filename:
        filename = f"output_{first_name.lower()}.txt"
    with open(filename, "w") as f:
        for word in words:
            f.write(word + "\n")
    print(f"\n✅ Wordlist generated with {len(words)} entries → {filename}")

def main():
    print("\n🔮 Wordlister - Hacker's choice 😈\n")
    info = collect_inputs()
    wordlist = generate_variations(info)
    
    custom_filename = input("\n📝 Enter output filename (press Enter to use default): ").strip()
    save_wordlist(wordlist, info.get('first_name', 'default'), custom_filename if custom_filename else None)

if __name__ == "__main__":
    main()
