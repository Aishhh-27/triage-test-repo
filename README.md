**GitHub Issue Triage Automation**
A developer support workflow automation tool that classifies, prioritizes, deduplicates, and analyzes GitHub issues using a Python-based triage engine backed by PostgreSQL.
This system simulates real-world support engineering workflows used in large-scale backend platforms.

**Features**
Automated GitHub issue ingestion via REST API
Rule-based issue classification (auth, storage, database, realtime, edge functions)
Severity assignment (P1 / P2 / P3 SLA framework)
Duplicate issue detection using similarity scoring
Automatic GitHub label assignment
Auto-commenting with reproduction templates
PostgreSQL-backed issue tracking and analytics
Markdown daily triage report generation
Cross-session issue trend analysis
CLI-based execution workflow

**Architecture**

GitHub API → Python CLI → Classification Engine
                     ↓
            Duplicate Detection
                     ↓
          PostgreSQL Storage Layer
                     ↓
     Markdown Reports + Analytics
                     ↓
        GitHub Labels + Comments

**Triage Logic**
Category Classification

Issues are classified into:

auth
storage
database
realtime
edge-functions

Keyword-based rule engine maps issue text to categories.

**Severity Model**

**Severity	Meaning**
P1	Critical failure (data loss, auth broken, outage)
P2	Major feature degraded or unstable
P3	Minor bug, documentation gap, or workaround exists

**Duplicate Detection**

Uses fuzzy string matching to detect similar issues:

Compares new issue titles against existing issues
Uses similarity threshold (>85%)
Flags potential duplicates for consolidation

**Database Schema (PostgreSQL)**
issues
github_issue_id
issue_number
title
body
category
severity
duplicate_of
timestamps
issue_events
action logs
triage decisions
metadata tracking
**Analytics**
SQL-based insights include:

Top error categories per month
Severity distribution trends
Recurring issue patterns
Unresolved P1 issue tracking
Mean time to triage
**Setup Instructions**
**1. Clone Repository**
git clone https://github.com/your-username/github-triage-automation.git
cd github-triage-automation
**2. Create Virtual Environment**
python3 -m venv venv
source venv/bin/activate
**3. Install Dependencies**
pip install -r requirements.txt
**4. Configure Environment Variables**

Create .env file:

GITHUB_TOKEN=your_github_token
GITHUB_OWNER=your_username
GITHUB_REPO=your_repo_name

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/triage_db
**5. Start PostgreSQL (via Docker)**
docker-compose up -d
**6. Initialize Database**
psql -U postgres -d triage_db -f sql/schema.sql
**7. Run Triage Engine**
python main.py
**Example Output**
GitHub Labeling
type:auth
severity:P1
Auto Comment Example
Please provide:

- SDK version
- Auth provider
- JWT flow details
- Minimal reproduction steps
Markdown Report Sample
# Daily Triage Report

## Issue #42
- Title: Auth login failing with JWT expired
- Category: auth
- Severity: P1
**Workflow**
Fetch open GitHub issues
Classify issue type
Assign severity level
Detect duplicates
Apply labels
Post reproduction template comment
Store in PostgreSQL
Generate reports
**Key Engineering Features**
Rate-limit safe GitHub API integration
Structured logging pipeline
SLA-based prioritization system
Cross-session persistence via PostgreSQL
Automated support response templates
Daily triage report generation
Extensible rule-based classification engine
**Tech Stack**
Python 3
GitHub REST API
PostgreSQL
Docker
Markdown
Bash
RapidFuzz (similarity scoring)
Click CLI framework
 **Future Improvements**
ML-based issue classification (embeddings)
Slack/Discord alert integration
GitHub Actions automation pipeline
Grafana dashboard for issue analytics
Vector-based semantic duplicate detection (pgvector)
Web UI dashboard for triage review
**License**
MIT License

**Author**

Built as a developer support engineering system demonstrating backend automation, incident triage workflows, and API integration skills.
