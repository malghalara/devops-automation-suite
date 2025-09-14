# Real-World Monitoring & Deployment Automation

This project is part of my internship deliverables, where I consolidated multiple DevOps and automation concepts into a hands-on setup.  
It covers **system monitoring, log monitoring, Nginx deployment, file handling, and remote configuration using Ansible**.

---

## 📌 Features

### 1. Log Monitoring & Alerting (Python)
- Script: `log_monitor.py`
- Monitors `/var/log/syslog` (or any log file you specify).
- Alerts for errors/warnings by printing and logging them.
- Helps detect issues in real-time.

### 2. System Resource Monitoring (Python + psutil)
- Script: `system_monitor.py`
- Monitors **CPU, memory, and disk usage**.
- Thresholds:
  - CPU > 75%
  - Memory > 80%
  - Disk > 85%
- Prints metrics and logs warnings in `system_monitor.log`.

### 3. Nginx Server Deployment (Python + Paramiko)
- Script: `deploy.py`
- Automates remote Nginx installation on worker nodes.
- Connects via SSH and executes commands (using private key).
- Verifies deployment by checking Nginx status.

### 4. File Handling & OS Automation (Python)
- Script: `file_handler.py`
- Automates:
  - Creating and writing to files.
  - Copying and moving files.
  - Deleting files safely.
- Useful for day-to-day DevOps automation.

### 5. Remote Configuration with Ansible
- Inventory file: `inventory.ini`
- Playbook: `install_nginx.yml`
- Automates installation of Nginx (or any package) on remote nodes.
- Validates connection using `ansible -m ping`.

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
````

### 2. Install Dependencies

```bash
pip install paramiko psutil
sudo apt install ansible -y
```

### 3. Run Scripts

#### Log Monitoring

```bash
python3 log_monitor.py
```

#### System Monitoring

```bash
python3 system_monitor.py
```

#### Deploy Nginx via SSH

```bash
python3 deploy.py
```

#### File Handling

```bash
python3 file_handler.py
```

#### Ansible Deployment

```bash
ansible -i inventory.ini workers -m ping
ansible-playbook -i inventory.ini playbooks/install_nginx.yml
```

---

## 📂 Project Structure

```
real-world-monitoring/
│
├── log_monitor.py          # Python script for log monitoring & alerting
├── system_monitor.py       # Python script for system resource monitoring with thresholds
├── file_handler.py         # Python script for file handling & OS automation
├── ansible/
│   ├── inventory.ini       # Ansible inventory file with target hosts
│   └── playbooks/
│       └── install_nginx.yml  # Ansible playbook to install & manage Nginx
└── README.md               # Project documentation

```

---

## 🛠️ Tools & Technologies

* **Python** (automation)
* **Paramiko** (SSH automation)
* **psutil** (system monitoring)
* **Nginx** (web server)
* **Ansible** (remote configuration & automation)
* **Linux** (Ubuntu-based environment)

---

