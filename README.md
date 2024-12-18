# Chatterbox

<div align="center">
   <img src="misc/banner/banner.png" width=500">
</div>

---

<div align="center">
   <b>⚠️⚠️⚠️ CHATTERBOX IS CURRENTLY UNDER ACTIVE DEVELOPMENT, AND THE DOCUMENTATION MAY NOT BE FULLY UP-TO-DATE. LAST DOCUMENTATION UPDATE: 19.12.2024 ⚠️⚠️⚠️</b>
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
   - [Local Setup](#local-setup)  
   - [Setup Using Docker and Devcontainer (for development)](#setup-using-docker-and-devcontainer-for-development)  
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
- **Environment**: Docker-based devcontainer for isolated development

## 📦 Installation

### Prerequisites

- Python 3.10+
- Docker (optional; for Devcontainer)

### Local setup

1. **Install Dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Initialize the Database**:
   ```bash
   python3 init_db.py
   ```

3. **Run the Application**:
   ```bash
   python3 app.py
   ```
   The application will be accessible at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Setup Using Docker and Devcontainer (for development)

1. Open the project in a development environment that supports Devcontainers (e.g., Visual Studio Code).
2. Follow prompts to build and open the container.
3. The enviroment will be set up automatically based on the `devcontainer.json`.
4. Run `python3 init_db.py`, and then `python3 app.py`.

## 🧑‍💻 Usage

1. Open the application in your browser.
2. Register a new user account.
3. Log in using your credentials.
4. Start chatting!

## 📂 File Structure

```
chatterbox/
│
├── app.py                # Main application logic
├── models.py             # Database models
├── init_db.py            # Database initialization script
├── requirements.txt      # Python dependencies
├── helpers.py            # Helper functions and decorators
├── event_handlers.py     # Event handling logic
├── .gitignore            # Gitignore file
├── README.md             # Project documentation
├── LICENSE               # Project license
│
├── instance/
│   └── chatterbox.db     # SQLite database file
│
├── templates/            # HTML templates
│   ├── layout.html       # Base layout template
│   ├── home.html         # Homepage template
│   ├── login.html        # Login page template
│   ├── register.html     # Registration page template
│   ├── chat.html         # Chat page template
│   └── author.html       # Author information page
│
├── static/               # Static files
│   ├── favicon.ico       # Favicon
│   ├── logo.png          # Logo image
│   ├── scripts.js        # JavaScript for the website
│   ├── websocket.js      # WebSocket JavaScript
│   └── styles.css        # CSS for styling
│
├── misc/                 # Miscellaneous files
│
└── .devcontainer/        # Dev container configuration
```

## 🚀 Future Enhancements

- **Easier Deployment**: Simplify deployment process using Docker.
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
