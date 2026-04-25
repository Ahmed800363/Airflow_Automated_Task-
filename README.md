# Airflow_Automated_Task-

# 🌪️ Airflow-Sentinel: Multi-Operator Task Orchestration

## 📌 Project Overview
This project demonstrates the orchestration of a hybrid data workflow using **Apache Airflow**. The pipeline (DAG) is designed to automate a sequence of diverse tasks, including automated email alerts, system-level bash commands, and custom Python business logic.

---

## 🏗️ Pipeline Architecture (DAG Graph)
The following graph represents the entire workflow where tasks are executed in a strictly sequential order to ensure data consistency and process monitoring.

**Execution Flow:** `send_Email` ➡️ `task_bash` ➡️ `task_python`

![Full DAG Workflow](https://github.com/Ahmed800363/Airflow_Automated_Task-/blob/main/image/photo-1.png)

---

## 🔍 Task Execution & Logs
Each task in the pipeline was monitored for success. Below are the execution logs (Output) for each stage:

### 1. Task: `send_Email` (EmailOperator)
This task initiates the pipeline by sending an automated SMTP notification. It confirms the start of the workflow.
![Email Task Output](https://github.com/Ahmed800363/Airflow_Automated_Task-/blob/main/image/photo-2.png)

### 2. Task: `task_bash` (BashOperator)
Once the email is sent, this operator executes a system-level command to trigger external scripts or handle files.
![Bash Task Output](https://github.com/Ahmed800363/Airflow_Automated_Task-/blob/main/image/photo-3.png)

### 3. Task: `task_python` (PythonOperator)
The final stage runs a custom Python function (`fun1`) to execute specific data logic or calculations.
![Python Task Output](https://github.com/Ahmed800363/Airflow_Automated_Task-/blob/main/image/photo-4.png)

---

## 💻 Technical Implementation (Source Code)
The entire pipeline is containerized using **Docker** and developed in **Python**. The DAG is configured with a 5-minute schedule interval and strict dependency management.

**Code Preview:**
![VS Code Logic Implementation](https://github.com/Ahmed800363/Airflow_Automated_Task-/blob/main/image/photo-5.png)

---
### 🚀 Conclusion
By leveraging Airflow's powerful orchestration capabilities, this project showcases a scalable way to automate complex, multi-technology tasks within a single, monitorable pipeline.
