# 🛡️ GearGuard: The Ultimate Maintenance Tracker

GearGuard is a modern **Maintenance Management System (CMMS)** designed to bridge the gap between industrial assets, maintenance teams, and repair requests. It replaces chaotic paper trails with a structured digital workflow.

## 🚀 Project Overview

[cite_start]The objective of this project is to allow companies to track assets (machines, vehicles) and manage the lifecycle of maintenance requests[cite: 4].

* **Problem:** Breakdowns are often unreported, and preventive maintenance schedules are missed.
* [cite_start]**Solution:** A centralized dashboard that connects **Equipment** (what is broken) with **Teams** (who fixes it) and **Requests** (the work to be done)[cite: 5].

## ✨ Key Features

### 1. 🏭 Asset Management (The "Brain")
* Centralized database of all company machinery.
* [cite_start]**Smart Buttons:** View live maintenance counts directly on the equipment page[cite: 71].
* [cite_start]**Scrap Logic:** Automatically marks equipment as "Scrapped" (Red Status) if a repair request fails[cite: 74].

### 2. 🔧 Corrective Maintenance (Flow 1)
* Report breakdowns instantly.
* [cite_start]**Kanban Board:** A visual drag-and-drop style workflow (`New` -> `In Progress` -> `Repaired`)[cite: 53].
* Technicians can log hours spent and resolution notes.

### 3. 📅 Preventive Maintenance (Flow 2)
* Schedule routine checkups to prevent failure.
* [cite_start]**Calendar View:** A visual monthly schedule powered by FullCalendar.js so no job is missed[cite: 61].

### 4. 👥 Team Management
* [cite_start]Organize technicians into specialized teams (e.g., Mechanical, Electrical, IT)[cite: 20].

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML5, CSS3, Bootstrap 5 (Responsive Design)
* **Dynamic Features:** FullCalendar.js, FontAwesome Icons
* **Database:** *Currently using In-Memory Data Structures (Python Lists) for rapid prototyping.*
