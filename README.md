<div align="center">

# 🎯 AgentDecisionLab

*Reinforcement Learning and Game Theory Applied to AI Agents and Agentic Systems*

![Last Commit](https://img.shields.io/github/last-commit/Muhammad-Ahmed-Rayyan/AgentDecisionLab)
![languages](https://img.shields.io/github/languages/count/Muhammad-Ahmed-Rayyan/AgentDecisionLab)

<br>

Built with the tools and technologies:  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenAI Gym](https://img.shields.io/badge/Gymnasium-0081A1?style=for-the-badge&logo=openai&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Mermaid](https://img.shields.io/badge/Mermaid-FF3670?style=for-the-badge&logo=mermaid&logoColor=white)

</div>

---

## 🧠 Project Summary

**AgentDecisionLab** explores two decision-making frameworks — Reinforcement Learning and Game Theory — and applies them in two distinct ways:

1. **Reinforcement Learning:** a Q-Learning agent trained from scratch on OpenAI Gymnasium's FrozenLake environment, compared against a random-action baseline.
2. **Game Theory:** an applied analysis of a separate case study system, a Multi-Agent Incident Response & On-Call Triage System, modeling its six agents as players in a cooperative game with one embedded non-cooperative subgame.

Built as Task 5 of the AI Engineering Internship at Alphatron Technologies. The full write-up, theory, algorithm comparisons, and complete case study analysis are in [`report/technical-report.md`](./report/technical-report.md).

---

## 🚀 Features

- 🧊 **Q-Learning on FrozenLake**
  A Q-Learning agent trained from scratch on OpenAI Gymnasium's `FrozenLake-v1`, learning entirely through interaction with the environment with no labeled data or external supervision.

- 🎲 **Random-Action Baseline**
  A random-policy baseline run for direct comparison against the trained agent's performance.

- ♟️ **Game Theory Case Study**
  A separate, previously approved system — a Multi-Agent Incident Response & On-Call Triage System — analyzed as a cooperative game with one embedded non-cooperative subgame across its six agents.

- 📊 **Training Visualization**
  Reward-over-episodes plot and the final trained Q-table saved to `results/`.

- 🗺️ **Mermaid Diagrams**
  Architecture, workflow, flow, and state diagrams for the case study system, in `diagrams/diagrams.md`.

---

## 🗃️ Project Structure

```bash
AgentDecisionLab/
├── README.md
├── requirements.txt
├── scripts/
│   ├── 01_frozenlake_random_baseline.py   # random-action baseline on FrozenLake-v1
│   └── 02_qlearning_frozenlake.py         # Q-Learning implementation and evaluation
├── results/
│   ├── q_learning_rewards.png             # training progress plot
│   └── q_table.npy                        # final trained Q-table
├── report/
│   └── technical-report.md                # full technical report (all sections)
└── diagrams/
    └── diagrams.md                         # architecture, workflow, flow, and state diagrams (Mermaid)
```

---

## 📊 Results

| | Success Rate (1000 episodes) |
|---|---|
| Random-Action Baseline | 1.10% |
| Trained Q-Learning Agent | 74.50% |

The trained agent shows a clear, measurable improvement over random behavior, learned entirely through interaction with the environment with no labeled data or external supervision.

---

## 🔧 Setup & Installation

> Make sure Python 3.8+ is installed.

```bash
# Clone the repo
git clone https://github.com/Muhammad-Ahmed-Rayyan/AgentDecisionLab.git
cd AgentDecisionLab

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the random-action baseline
python scripts\01_frozenlake_random_baseline.py

# Run Q-Learning training and evaluation
python scripts\02_qlearning_frozenlake.py
```

---

## ♟️ Case Study Scope

The Game Theory analysis is applied to a separate, previously approved case study system — a Multi-Agent Incident Response & On-Call Triage System — rather than to the FrozenLake implementation. This system is not implemented in code as part of this task; only its Game Theory analysis is included, as detailed in the technical report and diagrammed in [`diagrams/diagrams.md`](./diagrams/diagrams.md).

---

<div align="center">

⭐ Found this project useful? Drop a star on GitHub!

</div>