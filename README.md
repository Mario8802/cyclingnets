# 🚴‍♂️ CyclingNets

> [https://cyclingnets.onrender.com](https://cyclingnets.onrender.com) 
⚠️ **Note:** The server may go to sleep if inactive. The first request after a period of inactivity can take up to **50 seconds** to wake up. Please be patient when accessing the live demo.
---

## 🌐 About the Project

**CyclingNets** is a modern full-stack web application built for cycling enthusiasts.  
It enables users to create, join, and manage cycling events, discover new routes, and connect with fellow cyclists in a dynamic online community.

---

## 🌟 Key Features

- 📅 **Event Creation** – Organize and publish your own cycling events
- 🔍 **Event Discovery** – Explore events by location, time, and keywords
- 🧭 **Route Sharing** – View and add new routes from users
- 🧑‍🤝‍🧑 **Community** – Connect with other cyclists and join their events
- 🎨 **Responsive UI** – Built with Bootstrap 5 for a modern interface
- 🔗 **RESTful API** – Backend exposes a clean API for integration and future mobile support

---

## 🛠️ Tech Stack

### 🎨 Frontend
- HTML5  
- CSS3  
- JavaScript  
- Bootstrap 5  

### ⚙️ Backend
- Django  
- Django REST Framework  

### 🗄️ Database
- PostgreSQL  

---

## 🚀 Getting Started

Follow these instructions to run the project locally for development and testing purposes.

### ✅ Prerequisites

Make sure the following are installed on your system:

- [Python 3.10+](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)
- `pip` – Python package manager
- Virtual environment tool (`pipenv` or `virtualenv`)

---

### 🧰 Installation Guide

```bash
# Clone the repository
git clone https://github.com/Mario8802/cyclingnets.git
cd cyclingnets

# Create a virtual environment
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup the database (adjust credentials as needed)
psql -U postgres
CREATE DATABASE cyclingnets;

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
