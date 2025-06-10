# 🔐 W0rdL1st3r

**W0rdL1st3r** is a customizable wordlist generation tool for ethical hackers, penetration testers, and cybersecurity enthusiasts. It generates targeted wordlists based on personal or contextual information — ideal for social engineering simulations and password testing in authorized environments.

---

## 🚀 Features

- Interactive input collection for personal details (names, dates, keywords, etc.)
- Automatic generation of permutations and combinations
- Common password suffixes and mutations added
- Output to a customizable file (or defaults to `output_<firstname>.txt`)
- Lightweight and easy to run

---

## 📸 Demo

```
🔮 Wordlister - Hacker's choice 😈

💡 Enter target info (press Enter to skip optional ones)

First Name: Alice
Last Name: Smith
Nickname: ali
Birth Year (YYYY): 1990
...
📝 Enter output filename (press Enter to use default): 

✅ Wordlist generated with 3824 entries → output_alice.txt
```

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/VulnEdge/W0rdL1st3r.git
cd W0rdL1st3r

# Run the tool (make sure Python 3 is installed)
python3 wordlister.py
```

---

## 🧠 Use Cases

- Ethical hacking & penetration testing
- Red team operations
- CTF challenges
- Custom brute-force attack wordlists (with proper authorization)

> ⚠️ **Disclaimer**: This tool is intended for **educational** and **authorized** security testing only. Unauthorized use is strictly prohibited.

---

## ✍️ To-Do

- Add password length filters
- Include leetspeak transformations (e.g., `a` → `@`, `s` → `$`)
- Save input profiles for later reuse
- GUI version (Tkinter or web-based)

---

## 🤝 Contributing

Feel free to fork this project and submit PRs. Suggestions and improvements are welcome!

---

## 🧑‍💻 Author

Developed with 🖤 by [VulnEdge](https://github.com/VulnEdge)
