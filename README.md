# 🧠 Digital Resume – Jose Miguel de Lima

A dynamic, responsive digital resume built with Django, Tailwind CSS, HTMX, and Docker. This project showcases QA leadership and full-stack skills, with a clean interface and progressive enhancement.

---

## 🚀 Tech Stack

- **Backend**: Python 3, Django
- **Frontend**: HTMX, Tailwind CSS, Alpine.js
- **Containerization**: Docker & Docker Compose
- **Package Management**: npm
- **CSS Build**: Tailwind CLI with DaisyUI
- **Database**: SQLite (for development)

---

## 🛠️ How to Run the Project Locally

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd digitalresume
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install frontend dependencies

```bash
npm install
```

### 4. Run Tailwind in watch mode (for development)

```bash
npm run tw:build
```
This compiles src/input.css into dist/output.css using Tailwind v4.

### 5. Run Django development server

```bash
python manage.py runserver
```
Then open http://localhost:8000 in your browser.

----------------------

## 🐳 Running with Docker
You can also containerize the app using Docker:

```bash
docker-compose up --build
```
This will:

 - Build the Django app

 - Run the web server

 - Compile Tailwind styles

 - Serve the app at localhost:8000

 ---------------------------------

 ## 💡 Skills Demonstrated

 #### 📦 Backend & DevOps
 - Python & Django project setup

 - ORM usage with SQLite

 - Dockerfile and Docker Compose configuration

 - Environment isolation

#### 🎨 Frontend
 - Tailwind CSS (v4 with @source)

 - DaisyUI components

 - Responsive, mobile-first design

 - Conditional rendering with Tailwind classes

#### ⚙️ Interactivity & UX
 - HTMX for dynamic page updates without full reloads

 - Alpine.js for lightweight reactivity

 - Accessible layout and icon design

 -----------------------------

## 📂 Project Structure Highlights
- manage.py: Django entry point

- package.json: Tailwind & npm setup

- Dockerfile*: Container configurations

- src/: Tailwind input CSS with directives and @source

- templates/: Django templates (includes and base layout)

--------------------------
## 📬 Contact: Jose Miguel de Lima
[📧 Email:](delimajm@gmail.com) | 
[💻 GitHub]() | 
[🔗 LinkedIn:](linkedin.com/in/jose-de-lima-aa8a5a23)

---------------
© 2025 Jose Miguel de Lima. All rights reserved.