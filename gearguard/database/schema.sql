CREATE DATABASE gearguard;
USE gearguard;

-- Maintenance Teams
CREATE TABLE teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL
);

-- Equipment Table
CREATE TABLE equipment (
    equipment_id INT AUTO_INCREMENT PRIMARY KEY,
    equipment_name VARCHAR(100),
    serial_number VARCHAR(100),
    department VARCHAR(100),
    location VARCHAR(100),
    team_id INT,
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- Maintenance Requests
CREATE TABLE requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    equipment_id INT,
    team_id INT,
    issue TEXT,
    request_type ENUM('Corrective', 'Preventive'),
    status ENUM('New','In Progress','Repaired','Scrap') DEFAULT 'New',
    scheduled_date DATE,
    hours_spent INT,
    FOREIGN KEY (equipment_id) REFERENCES equipment(equipment_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);
