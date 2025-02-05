# OSRS Highscore Lookup

**A simple and intuitive app for looking up player highscores in the popular MMORPG Old School Runescape (OSRS).**

![OSRS Highscore Lookup Demo](https://i.imgur.com/nL2UJ5C.gif)


---

## 🚀 Overview

**OSRS Highscore Lookup** is a Python-based application that fetches highscore data from the OSRS Runescape API and presents it in a visually appealing and user-friendly interface. The app allows users to:

- Look up any OSRS player's skill levels.
- View the player's activity and combat achievements (e.g., boss kills, minigame completions).
- Navigate between skill and activity views seamlessly.

This project was developed as a learning exercise to explore the **Custom Tkinter** module, improve Python programming skills, and create a practical tool for OSRS players.

---

## ✨ Key Features

- **Player Skill Stats**: Displays a player's levels in all OSRS skills (e.g., Attack, Strength, Magic, etc.).
- **Activity & Combat Achievements**: Shows the number of boss kills, minigame completions, and other in-game activities.
- **User-Friendly Interface**: Built with **Custom Tkinter** for a modern and responsive GUI.
- **Easy to Use**: Simply enter a username and view the results instantly.

---

## 🛠️ Technologies Used

- **Python**: The core programming language used for the application.
- **Custom Tkinter**: A modern and customizable GUI framework for creating a sleek user interface.
- **Pillow (PIL)**: Used for image processing and handling (e.g., icons, logos).
- **Requests**: For making HTTP requests to the OSRS Highscores API.
- **JSON**: For parsing and handling API responses.

---

## 🚀 How It Works

1. **User Lookup**: Enter the username of an OSRS player into the input field and click "Submit."
2. **Fetch Data**: The app sends a request to the OSRS Highscores API to retrieve the player's data.
3. **Display Results**:
   - The **Skill Stats** tab shows the player's levels in all skills.
   - The **Activity & Achievements** tab displays combat achievements and activity completions.
4. **Navigation**: Use the navbar to switch between skill and activity views.

---

## 🛡️ Future Enhancements

Here are some ideas for future improvements to the app:

1. **Player Comparison**: Add a feature to compare the stats of two players side-by-side.
2. **Graphical Visualizations**: Include charts or graphs to visualize skill progress or activity trends.
3. **Save User Data**: Allow users to save and revisit previously searched profiles.
4. **Dark Mode**: Add a dark mode option for better usability in low-light environments.
5. **Export Data**: Enable users to export highscore data as a CSV or PDF file.
6. **Mobile-Friendly Version**: Develop a mobile-compatible version or a web-based interface.

---

## 🧑‍💻 Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of Python and pip.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HeadPilgrim/OSRSHighscoreLookup.git
   ```
2. Navigate to the project directory:
   ```bash
   cd OSRSHighscoreLookup
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python main.py
   ```

---

## 📂 Project Structure

```
OSRSHighscoreLookup/
├── main.py                # Entry point of the application; initializes and runs the app.
├── app.py                 # Main application script; handles the GUI setup and navigation.
├── requirements.txt       # Lists all Python dependencies required to run the application.
├── api/                   # Contains modules for interacting with the OSRS Highscores API.
│   └── api_client.py      # Handles API requests and fetches user data from the OSRS Highscores API.
├── frames/                # Contains modules for different views/frames in the application.
│   ├── activity_frame.py  # Defines the structure and logic for the activity/combat achievements view.
│   ├── compare_frame.py   # Placeholder for future implementation of player comparison functionality.
│   └── levels_frame.py    # Defines the structure and logic for the skill levels view.
├── assets/                # Stores static files such as images, icons, and other resources.
│   └── logo.png           # Application logo used in the GUI.
├── README.md              # Project documentation; provides an overview, setup instructions, and usage details.
└── ...                    # Other files or directories as needed.
```

---

## 🙏 Acknowledgments

- Thanks to Jagex for providing the OSRS Highscores API.
- Shoutout to the creators of **Custom Tkinter** for making GUI development in Python more enjoyable.
- Inspired by the OSRS community and their love for tracking progress and achievements.

---
