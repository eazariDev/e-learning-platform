<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="log.png" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# E-LEARNING-PLATFORM

<em></em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/eazariDev/e-learning-platform?style=flat-square&logo=opensourceinitiative&logoColor=white&color=FF4B4B" alt="license">
<img src="https://img.shields.io/github/last-commit/eazariDev/e-learning-platform?style=flat-square&logo=git&logoColor=white&color=FF4B4B" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/eazariDev/e-learning-platform?style=flat-square&color=FF4B4B" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/eazariDev/e-learning-platform?style=flat-square&color=FF4B4B" alt="repo-language-count">

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat-square&logo=JSON&logoColor=white" alt="JSON">
<img src="https://img.shields.io/badge/Redis-FF4438.svg?style=flat-square&logo=Redis&logoColor=white" alt="Redis">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=flat-square&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
<img src="https://img.shields.io/badge/NGINX-009639.svg?style=flat-square&logo=NGINX&logoColor=white" alt="NGINX">
<img src="https://img.shields.io/badge/Django-092E20.svg?style=flat-square&logo=Django&logoColor=white" alt="Django">
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat-square&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat-square&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Tech Stack](#Tech-Stack)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Contributing](#contributing)

---

## Overview

A modern, scalable, and extensible web-based e-learning platform built with Django, Django REST Framework, Channels, and Docker. It supports course creation, student enrollment, real-time chat, and secure media handling—all containerized for seamless deployment.


---

## Tech Stack

* Backend: Django 5.0.4, Django REST Framework

* Async: Django Channels + Daphne + Redis

* Database: PostgreSQL

* Web Server: Nginx + uWSGI

* Containerization: Docker & Docker Compose

---

## Features

- 🧑‍🏫 Instructor & student workflows
- 🧵 Real-time chat using Django Channels + Redis
- 🎓 Course creation, enrollment, and progress tracking
- 🖼️ Media uploads and secure content access
- 🧱 Modular Django apps (courses, students, chat)
- 🐳 Full Dockerized setup with Nginx, PostgreSQL, Redis
- ⚙️ ASGI + Daphne for async support

|     | Component         | Details                                                                                                                            |
| :-- | :---------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Monolithic Django backend</li><li>ASGI with Channels</li><li>PostgreSQL + Redis</li><li>nginx reverse proxy</li></ul>      |
| 🔩  | **Code Quality**  | <ul><li>Modular Django apps</li><li>Good use of settings structure</li><li>Consistent dependency versions</li></ul>                |
| 🔌  | **Integrations**  | <ul><li>PostgreSQL</li><li>Redis (caching + Channels)</li><li>nginx</li><li>daphne</li></ul>                                       |
| 🧩  | **Modularity**    | <ul><li>Separate Django apps: courses, students, chat</li><li>Logical separation of static/media/configs</li></ul>                 |
| ⚡️  | **Performance**   | <ul><li>Redis caching layer</li><li>uwsgi for WSGI</li><li>daphne for ASGI</li></ul>                                               |
| 🛡️ | **Security**      | <ul><li>Environment-based secrets via `python-decouple`</li><li>nginx SSL config present</li><li>Prod config in settings</li></ul> |
| 📦  | **Dependencies**  | <ul><li>Django 5.0.4</li><li>Channels</li><li>DRF</li><li>Redis</li><li>Pillow</li></ul>                                           |
| 🚀  | **Scalability**   | <ul><li>Containerized via Docker</li><li>ASGI for real-time features</li><li>Decoupled db/cache services</li></ul>                 |

---

## Project Structure

```sh
└── e-learning-platform/
    ├── Dockerfile
    ├── config
    │   ├── nginx
    │   └── uwsgi
    ├── data
    │   ├── cache
    │   └── db
    ├── docker-compose.yml
    ├── educa
    │   ├── api_examples
    │   ├── chat
    │   ├── courses
    │   ├── educa
    │   ├── manage.py
    │   ├── media
    │   ├── ssl
    │   ├── static
    │   └── students
    ├── requirements.txt
    └── wait-for-it.sh
```


## Getting Started

### 🔧 Prerequisites
- Docker & Docker Compose
- Python 3.11+ (for local dev without containers)

### Installation (Using docker)

Build e-learning-platform from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/eazariDev/e-learning-platform
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd e-learning-platform
    ```

3. **Build and run containers:**

    ```sh
    ❯ docker-compose up --build
    ```
    
Visit http://localhost:8000 to start exploring the platform.




---

## Contributing

- **💬 [Join the Discussions](https://github.com/eazariDev/e-learning-platform/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/eazariDev/e-learning-platform/issues)**: Submit bugs found or log feature requests for the `e-learning-platform` project.
- **💡 [Submit Pull Requests](https://github.com/eazariDev/e-learning-platform/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/eazariDev/e-learning-platform
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/eazariDev/e-learning-platform/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=eazariDev/e-learning-platform">
   </a>
</p>
</details>




---
