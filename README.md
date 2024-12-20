# Chatterbox

<div align="center">
   <img src="misc/banner/banner.png" width=500">
</div>

---

<div align="center">
   <b>⚠️⚠️⚠️ CHATTERBOX IS CURRENTLY UNDER ACTIVE DEVELOPMENT, AND THE DOCUMENTATION MAY NOT BE FULLY UP-TO-DATE. LAST DOCUMENTATION UPDATE: 20.12.2024 ⚠️⚠️⚠️</b>
</div>

---

<div align="center">
   <img src="misc/mockup.png" width="500">
</div>

---

Chatterbox is a lightweight, real-time chat application built with robust technologies. It enables users to register, log in, and exchange messages seamlessly. The app is designed to be user-friendly, secure, and efficient, making it a great solution for quick and reliable communication.

## 📚 Table of Contents
1. [🌟 Features](#-features)
2. [🛠️ Technologies Used](#️-technologies-used)
3. [📦 Installation](#-installation)
   - [Prerequisites](#prerequisites)
   - [Docker Setup (Recommended)](#docker-setup-recommended)
   - [Local Setup (Without Docker)](#local-setup-without-docker)
   - [Setup Using Docker and Devcontainer (For Development)](#setup-using-docker-and-devcontainer-for-development)
4. [🧑‍💻 Usage](#-usage)
5. [📂 File Structure](#-file-structure)
6. [🚀 Future Enhancements](#-future-enhancements)
7. [🐞 Known Bugs](#-known-bugs)
8. [📜 License](#-license)
9. [🙏 Acknowledgments](#-acknowledgments)
10. [👤 Author](#-author)

## 🌟 Features

- 🔒 **User Authentication**: Secure registration, login, and logout functionality.
- ⚡ **Real-Time Messaging**: Chat seamlessly with real-time updates.
- 📱 **Responsive Design**: Optimized for monitors of all sizes.
- 🗂️ **Database**: Messages and user data are stored in a robust database.

## 🛠️ Technologies Used

- **Backend**: Python 3, Flask, SQLAlchemy, Socket.IO, Jinja2
- **Frontend**: HTML, JavaScript, CSS, Bootstrap
- **Database**: SQLite
- **Environment**: Docker

## 📦 Installation

### Prerequisites

- Python 3.10+
- Docker

### Docker Setup (Recommended)

1. **First Run (Setup)**:
   ```bash
   docker compose up -d --build
   docker compose exec app python3 init_db.py -f
   ```
   - `--build` ensures that the Docker image is rebuilt.
   - `init_db.py` initializes the database.

2. **Normal Run**:
   ```bash
   docker compose up -d
   ```
   The application will be accessible at [http://0.0.0.0:8081](http://0.0.0.0:8081).  
   To stop the application, run `docker compose down`.


### Local Setup (Without Docker)

1. **Install Dependencies (First Run Only)**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize the Database (First Run Only)**:
   ```bash
   python init_db.py
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```
   The application will be accessible at [http://127.0.0.1:5000](http://127.0.0.1:5000).  
   To stop the application, press `Ctrl + C` in the terminal running the app.

### Setup Using Docker and Devcontainer (For Development)

1. Open the project in a development environment that supports Devcontainers (e.g., Visual Studio Code).
2. Follow prompts to build and open the container.
3. The enviroment will be set up automatically based on the `devcontainer.json`.
4. Run `python init_db.py` (first run only), and then `python app.py`.

To stop the application, press `Ctrl + C` in the terminal running the app.

## 🧑‍💻 Usage

1. Open the application in your browser.
2. Register a new user account.
3. Log in using your credentials.
4. Start chatting!

## 📂 File Structure

```
chatterbox/
│
├── app.py                  # Main application logic
├── docker-compose.yaml     # Defines container(s) setup
├── Dockerfile              # Builds the Docker image
├── event_handlers.py       # Event handling logic
├── helpers.py              # Helper functions and decorators
├── init_db.py              # Database initialization script
├── LICENSE                 # Project license
├── models.py               # Database models
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── .gitignore              # Gitignore file
│
├── instance/
│   └── chatterbox.db       # SQLite database file
│
├── misc/                   # Miscellaneous files
│
├── static/                 # Static files
│   ├── favicon.ico         # Favicon
│   ├── logo.png            # Logo image
│   ├── scripts.js          # JavaScript for the website
│   ├── styles.css          # CSS for styling
│   └── websocket.js        # WebSocket JavaScript
│
├── templates/              # HTML templates
│   ├── author.html         # Author information page
│   ├── chat.html           # Chat page template
│   ├── home.html           # Homepage template
│   ├── layout.html         # Base layout template
│   ├── login.html          # Login page template
│   └── register.html       # Registration page template
│
└── .devcontainer/
    └── devcontainer.json   # Dev container configuration
```

## 🚀 Future Enhancements

- **User Profiles**: Add user profile pages and the ability to update account details.
- **Enhanced UI**: Improve the design and usability of the chat interface.
- **React Front-End (Optional)**: Migrate the front-end to React for a more dynamic and modern user experience.

## 🐞 Known Bugs
- The "Users" panel in "Chat" tab does not update in real time when a message is received from someone other than the current chat participant.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Harvard's CS50x course for inspiration and foundational knowledge.
- The Flask and Bootstrap communities for providing excellent documentation and tools.

## 👤 Author
Filip Rokita  
[www.filiprokita.com](https://www.filiprokita.com/)
