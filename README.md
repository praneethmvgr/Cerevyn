AI Web Dashboard

Welcome to the **AI Web Dashboard** project! This is a web application designed to help monitor AI systems and workflows in real-time, giving insights into logs, analytics, and system performance.

📝 Project Description

The AI Web Dashboard provides a unified interface to monitor AI systems, visualize analytics, and manage workflows. It’s ideal for developers and data scientists who want to keep track of their AI pipelines efficiently.

Inputs Provided:
- System logs and workflow analytics
- Backend API (mock implementation)

Expected Features:
- Interactive dashboard UI with charts and analytics
- Real-time updates for AI system metrics
- Control panel to manage AI workflows

Expected Deliverables:
- UI wireframes for the dashboard
- System architecture diagram
- API structure and endpoints

---

## 🚀 Features

- **Real-Time Monitoring:** Live updates from AI systems.
- **Analytics Dashboard:** Graphs and charts displaying logs, performance metrics, and workflow data.
- **Control Panel:** Easily start, stop, or manage AI workflows.
- **User-Friendly Interface:** Clean, intuitive layout for quick access to insights.

---

## 💻 Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Chart.js
- **Backend:** Django (Python)
- **Database:** SQLite (for development)
- **Version Control:** Git & GitHub

---

## ⚡ How to Run Locally

1. Clone the repository:
git clone https://github.com/praneethmvgr/Cerevyn.git
cd Cerevyn

2. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

3. Install dependencies:
pip install -r requirements.txt

4. Run the Django development server:
python manage.py runserver

5. Open your browser and go to:
http://127.0.0.1:8000/


## 🎨 UI Wireframes

View the wireframes here:  
[Figma Wireframe](https://www.figma.com/design/yo0DkEypwryg9FBXGui0Sq/Untitled?node-id=0-1&t=G3jX7qyO9f09hcPm-1)

## 🏗️ System Architecture

The system follows a simple client-server architecture:

- Logs and analytics data are processed by the Django backend.
- The backend exposes APIs that return data in JSON format.
- The frontend dashboard fetches this data and displays it using charts.
- Users interact with the dashboard to monitor AI workflows.

![System Architecture](https://github.com/praneethmvgr/Cerevyn/raw/main/System_Architecture.jpg)


Screenshots
![AI Dashboard Screenshot](https://github.com/user-attachments/assets/e16f9586-78c6-4151-9293-38346773f4c9)

📂 Project Structure
Cerevyn/
│
├─ ai_dashboard/        # Main Django app
├─ static/              # CSS, JS, images
├─ templates/           # HTML templates
├─ manage.py            # Django management script
├─ requirements.txt     # Python dependencies
└─ README.md



🔗 Live Deployment
https://praneeth1.pythonanywhere.com/
