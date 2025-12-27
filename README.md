# ⚙️ GearGuard - Industrial Asset Management System

**GearGuard** is a comprehensive web-based facility management solution designed to streamline industrial operations. It allows facility managers to track machinery assets, organize maintenance teams, and manage repair requests through an intuitive dashboard.

> **Status:** ✅ Active | **Version:** 1.0.0

## 🚀 Key Features

### 🔹 Dashboard & Analytics
* **Real-time Overview:** View total assets, active breakdowns, and team efficiency at a glance.
* **Visual Data:** Interactive charts powered by Chart.js to track maintenance trends.
* **Actionable Insights:** "Attention Needed" counters highlight urgent repair requests.

### 🔹 Asset Management
* **Digital Inventory:** Register machinery with serial numbers, locations, and departments.
* **Smart Search:** Filter assets by name or ID instantly.
* **Status Tracking:** Monitor if machines are "Operational" or "Scrapped".

### 🔹 Maintenance Workflow
* **Request Portal:** Log breakdowns with detailed descriptions and priority levels.
* **Kanban Tracking:** Move requests through stages: `New` → `In Progress` → `Repaired`.
* **Team Assignment:** Automatically link assets to specific technical teams (Mechanical, Electrical, IT).

### 🔹 User Security
* **Secure Authentication:** User Signup & Login system.
* **Data Protection:** Passwords are hashed using PBKDF2 (Werkzeug security).
* **Session Management:** Protected routes ensure only logged-in managers can access data.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend** | Python 3, Flask (Microframework) |
| **Database** | SQLite 3 (Relational DB) |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Icons & Charts** | FontAwesome 6, Chart.js |
| **Templating** | Jinja2 |

---

## 💻 Installation & Setup

Follow these steps to run GearGuard locally on your machine.

### 1. Prerequisites
Ensure you have **Python 3.x** installed.
```bash
python --version
