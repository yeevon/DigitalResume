# Digital Resume – Jose Miguel de Lima

A dynamic, responsive digital resume built with Django, Tailwind CSS, HTMX, and Docker. This project showcases QA leadership and full-stack skills, featuring interactive UI, API integration, and modern design principles.

**🌐 Live Site:** https://www.jmdelima.cv
---

## ✨ Recent Enhancements
- GitHub API Integration – Public repos are fetched dynamically and sorted by last updated date.

- Dark Mode Toggle – Accessible via a UI button with responsive positioning.

- Tailored CSS Adjustments – Improved mobile handling, fixed layout shifting, better spacing, and consistent component alignment.

- Mobile UI Fixes – Resolved scroll bleed, adjusted icon layout, and enhanced modal readability.

- Manual AWS Deployment – Project hosted via EC2, styled assets served statically, deployed without automated CI/CD for full control.
---

## 🚀 Tech Stack

- **Backend**: Python 3, Django
- **Frontend**: HTMX, Tailwind CSS (via CDN), Alpine.js
- **Containerization**: Docker & Docker Compose
- **Package Management**: npm
- **CSS Build**: Tailwind CLI with DaisyUI (with fallback to CDN for simplicity)
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
 - Django architecture, views, routing

 - GitHub API integration via requests

 - Dockerfile and Docker Compose configuration

 - Environment isolation

#### 🎨 Frontend
 - Tailwind CSS v4 + DaisyUI

 - Dark mode via Tailwind’s dark class strategy

 - Responsive, mobile-first design

 - Font Awesome icons

#### ⚙️ Interactivity & UX
 - HTMX for component-level updates

 - Alpine.js for lightweight reactivity

 - Custom modal behavior, dynamic sorting, accessibility improvements

 -----------------------------

## 📂 Key Structure
- manage.py – Django entry point

- requirements.txt – Python dependencies

- Dockerfile / docker-compose.yml – Container setup

- src/ – Tailwind custom input (if used)

- templates/ – Base layout, reusable components

- static/ – Custom images and styling

- core/views.py – API logic and dynamic content handling

--------------------------
## 📬 Contact: Jose Miguel de Lima
[📧 Email:](delimajm@gmail.com) | 
[💻 GitHub]() | 
[🔗 LinkedIn:](linkedin.com/in/jose-de-lima-aa8a5a23)

---------------
© 2025 Jose Miguel de Lima. All rights reserved.
