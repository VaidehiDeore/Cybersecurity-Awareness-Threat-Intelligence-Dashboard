# 🛡️ Cybersecurity Awareness & Threat Intelligence Dashboard

> A defensive cybersecurity platform that combines Threat Intelligence, IOC Analysis, Risk & Confidence Scoring, MITRE ATT&CK Mapping, Vulnerability Awareness, SOC Alert Management, Threat Correlation, and Cybersecurity Awareness Training into one unified security dashboard.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-Vite-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Defensive-0EA5E9?style=for-the-badge)
![Threat Intelligence](https://img.shields.io/badge/Threat%20Intelligence-CTI-06B6D4?style=for-the-badge)
![Testing](https://img.shields.io/badge/Tests-35%20Passed-22C55E?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-22C55E?style=for-the-badge)

---

## 📌 Project Overview

The **Cybersecurity Awareness & Threat Intelligence Dashboard** is an end-to-end defensive cybersecurity project designed to demonstrate how threat intelligence can be collected, normalized, validated, enriched, scored, correlated, visualized, and transformed into actionable security awareness and SOC workflows.

The system combines technical threat intelligence capabilities with cybersecurity education in a single dashboard.

The project operates using **synthetic, fictional, sanitized, and locally generated defensive data**, allowing the complete platform to run locally without requiring interaction with suspicious infrastructure.

The primary workflow is:

    Threat Data
         ↓
    Data Collection
         ↓
    Normalization
         ↓
    IOC Extraction
         ↓
    IOC Validation
         ↓
    Threat Enrichment
         ↓
    Risk + Confidence Scoring
         ↓
    Threat Correlation
         ↓
    Alert Generation
         ↓
    SOC Triage
         ↓
    MITRE ATT&CK / Vulnerability Analysis
         ↓
    Security Dashboard
         ↓
    Cybersecurity Awareness
         ↓
    Defensive Action

---

## 🎯 Problem Statement

Modern security teams receive information from multiple sources such as threat feeds, vulnerability databases, IOC collections, analyst observations, alerts, and security-awareness resources.

When these sources are separated, it becomes difficult to:

- Understand threat context
- Prioritize risks
- Distinguish risk from confidence
- Correlate related observations
- Identify important vulnerabilities
- Reduce alert fatigue
- Communicate security information to non-technical users
- Convert threat intelligence into actionable defensive decisions

This project addresses the problem by providing a unified platform for:

**Threat Intelligence + IOC Analysis + Risk Assessment + SOC Workflow + Vulnerability Awareness + Cybersecurity Education**

---

## 🎯 Project Objectives

The major objectives are:

1. Build an end-to-end defensive Threat Intelligence dashboard.
2. Generate and analyze safe synthetic threat-intelligence records.
3. Validate multiple IOC types syntactically.
4. Normalize indicators into consistent formats.
5. Enrich indicators using local synthetic context.
6. Calculate separate risk and confidence scores.
7. Categorize threats according to severity.
8. Map justified threats to MITRE ATT&CK concepts.
9. Correlate related synthetic observations.
10. Provide vulnerability awareness and prioritization.
11. Generate and manage SOC-style alerts.
12. Demonstrate a defensive SOC workflow.
13. Provide cybersecurity awareness education.
14. Provide a cybersecurity awareness assessment.
15. Generate learning recommendations.
16. Provide an executive security view.
17. Maintain a safe local/offline demonstration environment.
18. Provide automated tests and professional documentation.

---

## 🏗️ System Architecture

    ┌──────────────────────────┐
    │ Synthetic Threat Data    │
    │ CSV / Local Sources      │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │ Data Collection           │
    │ Normalization             │
    │ Validation                │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │ IOC Extraction            │
    │ IP / Domain / URL / Hash  │
    │ CVE Validation            │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │ Threat Enrichment         │
    │ Context / Source / ATT&CK │
    └────────────┬─────────────┘
                 │
        ┌────────┴────────┐
        ▼                 ▼
    ┌──────────────┐  ┌────────────────┐
    │ Risk Scoring │  │ Confidence     │
    │ 0 - 100      │  │ 0 - 100        │
    └──────┬───────┘  └───────┬────────┘
           └──────────┬────────┘
                      ▼
    ┌──────────────────────────┐
    │ Threat Correlation       │
    │ Campaign / Context /     │
    │ Observation Relationships│
    └────────────┬─────────────┘
                 │
      ┌──────────┼──────────┐
      ▼          ▼          ▼
    ┌───────┐ ┌────────┐ ┌──────────────┐
    │ Alerts│ │ ATT&CK │ │ Vulnerability│
    │ & SOC │ │ Mapping│ │ Awareness    │
    └───┬───┘ └───┬────┘ └──────┬───────┘
        └─────────┼──────────────┘
                  ▼
    ┌──────────────────────────┐
    │ React Security Dashboard │
    └────────────┬─────────────┘
                 │
          ┌──────┴───────┐
          ▼              ▼
    ┌────────────┐ ┌─────────────────┐
    │ SOC /      │ │ Awareness       │
    │ Analyst    │ │ Center          │
    │ View       │ │ 15 Modules      │
    └────────────┘ └─────────────────┘

---

## 🔐 Cybersecurity Scope

The project focuses on defensive cybersecurity concepts including:

- Cybersecurity Awareness
- Cyber Threat Intelligence
- Indicators of Compromise
- Indicators of Attack
- Threat Enrichment
- Risk Assessment
- Confidence Assessment
- Threat Correlation
- MITRE ATT&CK
- Vulnerability Management
- SOC Operations
- Alert Triage
- Incident Response Awareness
- Security Analytics
- Defensive Security

---

## 🧠 Threat Intelligence

The dashboard manages structured threat-intelligence records containing:

- Threat ID
- Timestamp
- Threat name
- Threat category
- Indicator type
- Indicator value
- Source
- Confidence score
- Severity
- Risk score
- Status
- First seen
- Last seen
- Region
- Description
- MITRE ATT&CK tactic
- MITRE ATT&CK technique
- CVE reference

Supported threat statuses:

- `NEW`
- `UNDER_REVIEW`
- `MONITORING`
- `CLOSED`
- `FALSE_POSITIVE`

---

## 📊 Synthetic Threat Intelligence Dataset

The project uses a safe synthetic threat-intelligence dataset containing **2,000+ records**.

Dataset:

    data/threat_intelligence_dataset.csv

The records are generated for educational and defensive demonstration.

The dataset does not represent confirmed real-world compromises.

### Safe Synthetic Indicators

The project uses documentation-safe indicator ranges such as:

    192.0.2.0/24
    198.51.100.0/24
    203.0.113.0/24

Safe demonstration domains include:

    example.com
    example.org
    example.net
    *.invalid

Synthetic SHA-256 values are generated for demonstration purposes.

All demonstration records should be treated as:

    SYNTHETIC / DEMO ONLY

---

## 🔎 IOC Analysis

The platform supports syntactic validation of:

- IPv4
- IPv6
- Domain
- URL
- MD5
- SHA-1
- SHA-256
- CVE

IOC validation returns:

    valid
    indicator_type
    normalized_value
    validation_notes

### IOC Safety

IOC searches are performed against the **local database**.

The application does not automatically:

- Visit suspicious URLs
- Contact suspicious IP addresses
- Download suspicious files
- Execute files represented by hashes
- Scan external systems
- Perform exploitation
- Attack external infrastructure

IOC validation determines whether an indicator matches an expected syntax.

It does **not** prove maliciousness or compromise.

---

## 🧠 Threat Enrichment

The enrichment process adds locally available synthetic context including:

- Indicator type
- First seen
- Last seen
- Threat categories
- Confidence
- Severity
- Risk
- Related alerts
- Related indicators
- MITRE ATT&CK mapping where justified
- Analyst notes

The enrichment workflow is intentionally local and defensive.

---

## 📈 Risk Scoring

The project uses a weighted risk-scoring model.

| Factor | Weight |
|---|---:|
| Severity | 30% |
| Confidence | 25% |
| Recency | 15% |
| Observation Frequency | 10% |
| Source Reliability | 10% |
| Context / Correlation | 10% |

### Risk Classification

| Score | Classification |
|---:|---|
| 0–20 | INFORMATIONAL |
| 21–40 | LOW |
| 41–60 | MEDIUM |
| 61–80 | HIGH |
| 81–100 | CRITICAL |

---

## 🎯 Risk vs Confidence

Risk and confidence are intentionally treated as separate concepts.

Example:

    Risk:       90
    Confidence: 25

This means the potential impact may be high while the available evidence has limited confidence.

Another example:

    Risk:       70
    Confidence: 95

This indicates that the available evidence is highly reliable even though the calculated risk is below critical.

This separation helps prevent analysts from interpreting high risk as absolute certainty.

---

## 🏷️ Threat Categories

The system supports:

- Phishing
- Malware
- Ransomware
- Credential Theft
- Social Engineering
- Network Threats
- Web Threats
- Data Exposure
- Account Takeover Risk
- Vulnerability Exploitation Awareness

---

## 🏢 Threat Intelligence Types

The project demonstrates the following major CTI concepts:

### Strategic Intelligence

High-level information useful for understanding security priorities and business impact.

### Tactical Intelligence

Information related to attacker behaviors, techniques, and defensive patterns.

### Operational Intelligence

Information useful for understanding ongoing threat activity and investigation context.

### Technical Intelligence

Technical artifacts such as:

- IP addresses
- Domains
- URLs
- Hashes
- CVEs

The primary implementation focus is:

- Technical CTI
- Tactical CTI
- Cybersecurity Awareness

---

## 🎯 MITRE ATT&CK Mapping

The project provides defensive MITRE ATT&CK concepts and visualization where a synthetic threat record justifies the mapping.

The dashboard can visualize:

- Top tactics
- Top techniques
- Threats by tactic
- Technique frequency
- Associated synthetic threat records

The project clearly distinguishes:

    IOC = WHAT artifact was observed

    MITRE ATT&CK = HOW a behavior may occur

An IOC does not automatically prove a specific ATT&CK technique.

---

## 🐞 Vulnerability Awareness

The vulnerability section provides defensive awareness around:

- CVE ID
- Product category
- Severity
- CVSS score
- Published date
- Patch availability
- Demonstration exploitation status
- Description

Vulnerability prioritization considers:

- CVSS
- Asset criticality
- Exposure
- Known exploitation evidence
- Business context

The project does not provide exploitation functionality.

---

## 🔗 Threat Correlation

The correlation engine groups related synthetic observations using contextual relationships such as:

- Campaign ID
- Observation window
- Threat category
- Shared indicators
- Analyst correlation

Correlation helps analysts identify related observations and investigate them together.

Important:

    Correlation ≠ Attribution
    Correlation ≠ Confirmed Compromise

---

## ⏱️ Threat Timeline

The system supports a conceptual threat lifecycle:

    First Seen
        ↓
    New Observations
        ↓
    Risk Changes
        ↓
    Investigation
        ↓
    Monitoring
        ↓
    Closed

This helps demonstrate how a threat record can evolve throughout an investigation.

---

## 🚨 SOC Alert Management

The alert engine can identify defensive conditions such as:

- High-risk observations
- High-confidence indicators
- Repeated observations
- Correlated indicators
- High-priority vulnerabilities
- Threshold-based events

Alerts can contain:

- Alert ID
- Severity
- Risk score
- Status
- Observation count
- Reason
- Related indicators
- Analyst context

---

## 🔄 Alert Correlation & Alert Fatigue

The project demonstrates how repeated observations can be consolidated.

Example:

    100 observations in 5 minutes
                ↓
        Correlation Engine
                ↓
         1 consolidated alert
                ↓
        observation_count = 100

This reduces unnecessary alert duplication and helps analysts focus on meaningful security events.

---

## 🛡️ SOC Workflow

The defensive SOC workflow is:

    Threat Feed
         ↓
    IOC Extraction
         ↓
    IOC Validation
         ↓
    Enrichment
         ↓
    Risk + Confidence
         ↓
    Alert Generation
         ↓
    SOC Queue
         ↓
    Triage
         ↓
    Correlation
         ↓
    Investigation
         ↓
    Escalate / Monitor / Resolve / False Positive
         ↓
    Documentation

---

## ❌ False Positive Considerations

Threat intelligence can contain false positives because of:

- Shared infrastructure
- Cloud hosting
- Changing domains
- Stale indicators
- Feed disagreement
- Confidence differences
- Incomplete context

Therefore, the dashboard is designed to support analyst decisions rather than automatically declaring compromise.

---

## 📚 Cybersecurity Awareness Center

The project contains **15 awareness modules**.

| # | Module |
|---:|---|
| 1 | Phishing Awareness |
| 2 | Password Security |
| 3 | MFA & Passkeys |
| 4 | Social Engineering |
| 5 | Safe Browsing |
| 6 | Software Updates |
| 7 | Ransomware Awareness |
| 8 | USB & Removable Media Safety |
| 9 | Data Privacy |
| 10 | Secure Wi-Fi |
| 11 | Mobile Security |
| 12 | Remote Work Security |
| 13 | Cloud Account Security |
| 14 | Incident Reporting |
| 15 | AI-Enabled Scam Awareness |

Each module provides:

- What the topic means
- Warning signs
- Safe practices
- Recommended defensive actions

---

## 🧠 Cybersecurity Awareness Quiz

The platform includes a **35-question cybersecurity awareness assessment**.

The assessment covers topics such as:

- Phishing
- Password security
- MFA
- Privacy
- Social engineering
- Safe browsing
- Defensive security habits

The result includes:

- Overall score
- Category scores
- Awareness level
- Learning recommendations

### Awareness Score

| Score | Level |
|---:|---|
| 0–40 | Needs Improvement |
| 41–60 | Basic Awareness |
| 61–80 | Good Awareness |
| 81–100 | Strong Awareness |

Example educational result:

    43 / 100
    Basic Awareness

The score is intended for educational feedback and is not an employee competency or performance judgment.

---

## 📈 Executive Dashboard

The executive dashboard provides high-level security visibility through:

- Critical / High threats
- Active alerts
- Awareness trend
- Vulnerabilities
- Threat categories
- Recommended defensive priorities
- Awareness weaknesses

The executive view is designed for non-technical stakeholders and management-level security communication.

---

## 🔐 Security & Privacy

This project follows defensive cybersecurity principles.

### The application does NOT:

- Attack external systems
- Scan public networks
- Visit suspicious URLs
- Contact suspicious IP addresses
- Execute suspicious files
- Deploy malware
- Create phishing kits
- Harvest credentials
- Provide exploitation functionality
- Perform unauthorized access
- Collect unnecessary personal information

### Defensive Design Principles

- Synthetic datasets
- Local/offline analysis
- Input validation
- Data normalization
- Safe IOC searching
- Risk/confidence separation
- False-positive awareness
- Analyst-oriented workflow
- Environment-variable configuration
- Secure coding practices
- Defensive educational content

---

## 🧰 Technology Stack

### Frontend

- React
- Vite
- JavaScript
- CSS
- Recharts
- Lucide React

### Backend

- Python
- Flask / Python API services
- Pandas
- SQLite
- REST APIs

### Testing

- Pytest
- Automated service testing
- Project-level functional tests

### Security Analytics

- IOC validation
- Risk scoring
- Confidence scoring
- Threat enrichment
- Threat correlation
- MITRE ATT&CK concepts
- Vulnerability prioritization
- SOC alerting
- Security awareness analytics

---

## 🗂️ Project Structure

    Cybersecurity-Awareness-Threat-Intelligence-Dashboard/
    │
    ├── awareness/
    │   ├── modules.json
    │   └── quiz_questions.json
    │
    ├── backend/
    │   ├── app/
    │   │   ├── models/
    │   │   ├── routes/
    │   │   ├── services/
    │   │   └── utils/
    │   ├── requirements.txt
    │   ├── run.py
    │   └── server.py
    │
    ├── data/
    │   ├── generate_threat_data.py
    │   ├── threat_intelligence_dataset.csv
    │   └── vulnerabilities.csv
    │
    ├── docs/
    │
    ├── frontend/
    │   ├── src/
    │   │   ├── components/
    │   │   ├── pages/
    │   │   └── services/
    │   ├── index.html
    │   ├── package.json
    │   ├── package-lock.json
    │   └── vite.config.js
    │
    ├── reports/
    │   └── project-report.md
    │
    ├── screenshots/
    │   ├── 01_main_dashboard.png
    │   ├── 02_threat_intelligence.png
    │   ├── 03_ioc_analysis.png
    │   ├── 04_alerts.png
    │   └── 05_awareness_quiz_result.png
    │
    ├── tests/
    │   └── test_project.py
    │
    ├── .env.example
    ├── .gitignore
    └── README.md

---

## 🔌 REST API

The project provides REST endpoints for the major defensive workflows.

    GET    /api/threats
    GET    /api/threats/{id}
    POST   /api/threats
    PUT    /api/threats/{id}

    GET    /api/indicators/search

    GET    /api/dashboard/stats
    GET    /api/dashboard/trends

    GET    /api/alerts
    PUT    /api/alerts/{id}/status

    POST   /api/threats/{id}/notes

    GET    /api/vulnerabilities

    GET    /api/awareness/modules

    GET    /api/quiz
    POST   /api/quiz/submit

---

# ⚙️ Installation & Setup

## Prerequisites

Make sure the following are installed:

- Python 3.11+
- Node.js
- npm
- Git

---

## 1. Clone the Repository

    git clone https://github.com/<your-username>/Cybersecurity-Awareness-Threat-Intelligence-Dashboard.git

    cd Cybersecurity-Awareness-Threat-Intelligence-Dashboard

---

## 2. Create Python Virtual Environment

Windows PowerShell:

    python -m venv .venv

Activate:

    .\.venv\Scripts\Activate.ps1

---

## 3. Install Backend Dependencies

    pip install -r backend\requirements.txt

---

## 4. Generate Synthetic Threat Data

    python data\generate_threat_data.py

This generates the local synthetic threat-intelligence dataset used by the application.

No live threat feed is required for the core demonstration.

---

# ▶️ Run the Backend

From the project root:

    python backend\server.py

Alternatively:

    python backend\run.py

Use the backend URL displayed in the terminal.

---

# ▶️ Run the Frontend

Open another PowerShell terminal:

    cd frontend

Install dependencies:

    npm install

Start the development server:

    npm run dev

Open the URL displayed by Vite, typically:

    http://localhost:5173

---

# 🧪 Testing

Run the complete automated test suite:

    python -m pytest -q

Verified project result:

    ...................................
    35 passed in 2.85s

### Test Status

    35 / 35 Tests Passed
    100% Test Suite Passed

The tests validate important project functionality including defensive services, data processing, API behavior, validation, scoring, and related workflows.

---

# 🏗️ Production Build

To generate the production frontend build:

    cd frontend
    npm run build

The production build completes successfully.

Vite may report a chunk-size optimization warning because of the dashboard bundle size. This is a performance optimization recommendation and does not indicate a build failure.

---

# 📸 Screenshots

The repository includes five primary screenshots.

### 1. Main Dashboard

    screenshots/01_main_dashboard.png

Shows the primary security dashboard, KPIs, threat statistics, charts, and security overview.

### 2. Threat Intelligence

    screenshots/02_threat_intelligence.png

Shows threat records, severity, risk, confidence, categories, and threat intelligence information.

### 3. IOC Analysis

    screenshots/03_ioc_analysis.png

Shows indicator analysis, validation, enrichment, risk, confidence, and related security context.

### 4. SOC Alerts

    screenshots/04_alerts.png

Shows the SOC alert queue, alert severity, risk, status, filters, and analyst workflow.

### 5. Awareness & Quiz

    screenshots/05_awareness_quiz_result.png

Shows the cybersecurity awareness experience and assessment result.

---

# 📊 Project Results

The completed implementation demonstrates:

    2,000+ Synthetic Threat Records
            +
    IOC Validation
            +
    Local IOC Search
            +
    Threat Enrichment
            +
    Risk Scoring
            +
    Confidence Scoring
            +
    Threat Correlation
            +
    MITRE ATT&CK Mapping
            +
    Vulnerability Awareness
            +
    SOC Alert Management
            +
    Executive Dashboard
            +
    15 Awareness Modules
            +
    35-Question Awareness Assessment
            +
    35 Automated Tests
            +
    Production Frontend Build

---

# 🧪 Safe Demonstration Scenario

Example synthetic threat:

    Threat ID:
    THR-2026-001

    Threat Name:
    Synthetic Credential Phishing Campaign

    Category:
    PHISHING

    Indicator:
    login-check.invalid

    Severity:
    HIGH

    Risk:
    78

    Confidence:
    85

    Status:
    MONITORING

Related synthetic observation:

    198.51.100.25

The example is intentionally synthetic and uses documentation-safe indicators.

---

# ⚠️ Important Security Interpretation

The system intentionally distinguishes:

    OBSERVATION
    INDICATOR
    ALERT
    THREAT
    INCIDENT

These terms do not represent the same thing.

For example:

    IOC ≠ Confirmed Compromise

    Risk ≠ Certainty

    Correlation ≠ Attribution

    Alert ≠ Incident

    Threat Intelligence ≠ Proof of Breach

The dashboard supports analyst decision-making rather than automatically declaring a security incident.

---

# 🧑‍💼 SOC & Analyst Perspective

The platform demonstrates how an analyst could conceptually move from an observation to a defensive decision:

    1. Observe
           ↓
    2. Validate
           ↓
    3. Normalize
           ↓
    4. Enrich
           ↓
    5. Assess Risk
           ↓
    6. Assess Confidence
           ↓
    7. Correlate
           ↓
    8. Generate / Review Alert
           ↓
    9. Triage
           ↓
    10. Investigate
           ↓
    11. Monitor / Escalate / Resolve
           ↓
    12. Document

This workflow emphasizes that automated scoring supports analysts but does not replace human judgment.

---

# 📋 Database Concepts

The project architecture supports entities such as:

    THREATS
    INDICATORS
    SOURCES
    ATTACK_MAPPINGS
    VULNERABILITIES
    ALERTS
    ANALYST_NOTES
    AWARENESS_MODULES
    QUIZ_RESULTS

Relationships between these entities support:

- Threat investigation
- IOC lookup
- Alert correlation
- ATT&CK analysis
- Vulnerability awareness
- Awareness analytics

---

# 🔮 Future Improvements

Future defensive improvements can include:

- Authorized live threat feeds
- STIX/TAXII integration
- CISA KEV integration
- NVD/CVE integration
- EPSS-style prioritization
- IOC expiration and lifecycle management
- Advanced IOC deduplication
- Improved confidence models
- Advanced enrichment
- ATT&CK Navigator integration
- SIEM integration
- SOAR integration
- Email security integration
- Endpoint security integration
- Cloud security integrations
- Threat hunting workflows
- Executive reporting
- Role-based dashboards
- Docker deployment
- CI/CD integration
- Centralized logging
- Advanced correlation
- Detection tuning
- Security analytics improvements

All future improvements should remain within authorized and defensive environments.

---

# 🎓 Learning Outcomes

Through this project, the following practical concepts were implemented and demonstrated.

### Cybersecurity

- Cybersecurity fundamentals
- Defensive security
- Threat intelligence
- IOC analysis
- Threat enrichment
- Risk assessment
- Confidence assessment
- Vulnerability awareness
- SOC workflows
- Alert triage
- Incident response concepts

### Threat Intelligence

- Technical CTI
- Tactical CTI
- IOC normalization
- IOC validation
- Threat correlation
- Source reliability
- Risk scoring
- Confidence scoring
- MITRE ATT&CK concepts

### Development

- Python
- React
- Vite
- REST APIs
- SQLite
- Pandas
- JavaScript
- CSS
- Automated testing
- Git
- GitHub

### Security Awareness

- Phishing awareness
- Password security
- MFA
- Social engineering
- Safe browsing
- Ransomware awareness
- Data privacy
- Remote work security
- Cloud account security
- Mobile security
- AI-enabled scams

---

# 💼 Resume Description

### Cybersecurity Awareness & Threat Intelligence Dashboard

Developed an end-to-end defensive cybersecurity platform using Python and React to analyze synthetic threat intelligence, validate and enrich IOCs, calculate risk and confidence scores, correlate related threats, visualize MITRE ATT&CK mappings, manage SOC alerts, prioritize vulnerability awareness, and provide interactive cybersecurity awareness training.

---

# 📌 Resume Bullet Points

- Developed a defensive **Cyber Threat Intelligence dashboard** using Python and React for synthetic IOC validation, enrichment, risk/confidence scoring, threat correlation, and SOC alert management.
- Implemented **MITRE ATT&CK mapping, vulnerability awareness, threat timelines, alert correlation, and executive security analytics** to demonstrate practical SOC workflows.
- Built a **15-module cybersecurity awareness center and 35-question assessment**, supported by automated testing with **35/35 tests passing**.

---

# 🧑‍💻 Technical Skills Demonstrated

    Cybersecurity
    Threat Intelligence
    CTI
    SOC
    IOC Analysis
    Threat Enrichment
    Threat Correlation
    Risk Scoring
    Confidence Scoring
    MITRE ATT&CK
    Vulnerability Management
    Incident Response
    Security Awareness
    Security Analytics
    Python
    React
    Vite
    REST APIs
    SQLite
    Pandas
    Pytest
    Git
    GitHub
    Secure Coding

---

# 🌐 GitHub Repository Description

    Defensive cybersecurity dashboard combining threat intelligence, IOC analysis, risk and confidence scoring, MITRE ATT&CK mapping, vulnerability awareness, SOC workflows, threat correlation, and interactive security awareness training.

---

# 🏷️ Recommended GitHub Topics

    cybersecurity
    threat-intelligence
    cti
    soc
    ioc
    mitre-attack
    security-awareness
    python
    react
    vite
    vulnerability-management
    incident-response
    security-analytics
    defensive-security
    risk-scoring
    threat-correlation
    security-dashboard

---

# 🛡️ Ethical & Safety Disclaimer

This project is designed exclusively for **defensive cybersecurity education, threat-intelligence analysis, security awareness, and authorized security research**.

It does not execute, deploy, or interact with malicious payloads or unauthorized systems.

The project does not:

- Attack systems
- Scan public networks
- Perform exploitation
- Execute malware
- Deploy malware
- Create phishing kits
- Harvest credentials
- Contact suspicious infrastructure
- Automatically visit suspicious URLs

All demonstration threat data is synthetic, fictional, sanitized, or intended for authorized defensive use.

---

# 🚫 Project Limitations

The current implementation is intentionally designed as an educational defensive platform.

Therefore:

- Threat data is primarily synthetic.
- IOC enrichment is local.
- No live malicious infrastructure is contacted.
- Threat intelligence is not intended to establish real-world attribution.
- Risk scores are educational demonstrations rather than production risk decisions.
- ATT&CK mapping is only applied where justified by the available synthetic context.
- Vulnerability analysis is awareness-oriented.
- Alert correlation is demonstration-oriented.
- The awareness score is educational and should not be interpreted as an employee performance metric.

---

# 🚀 Project Development Philosophy

This project follows a consistent development standard:

    Executable
         +
    Beginner-Friendly
         +
    Industry-Oriented
         +
    Professionally Designed
         +
    Secure
         +
    Well Tested
         +
    Well Documented
         +
    GitHub-Ready
         +
    Placement-Ready

The objective is not only to build a working application, but to demonstrate practical understanding of how cybersecurity concepts can be transformed into a complete, testable, explainable, and presentable software project.

---

# ⭐ Key Project Highlights

    🛡️ Defensive Cybersecurity Platform
    🔎 IOC Validation & Local Search
    🧠 Threat Enrichment
    📊 Risk & Confidence Scoring
    🔗 Threat Correlation
    🎯 MITRE ATT&CK Mapping
    🐞 Vulnerability Awareness
    🚨 SOC Alert Management
    ⏱️ Threat Timeline
    📚 15 Cybersecurity Awareness Modules
    🧠 35-Question Awareness Assessment
    📈 Executive Security Dashboard
    🧪 35 Automated Tests Passed
    🔐 Synthetic & Safe Data
    ⚡ Local / Offline Demonstration
    💼 GitHub & Placement Ready

---

# 👩‍💻 Author

## Vaidehi Deore