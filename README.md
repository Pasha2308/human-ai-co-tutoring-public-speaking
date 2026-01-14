# Human–AI Co-Tutoring System for Public Speaking

This repository contains a research prototype accompanying the paper:

**“Human–AI Co-Tutoring for Public Speaking Skill Development”**

The goal of this codebase is to demonstrate, in a minimal and transparent way,
how a Human–AI co-tutoring system can be implemented with clear role separation
between automated evaluation and human judgment.

---

## What This Repository Proves

This code explicitly demonstrates three claims made in the paper:

### 1. The system is NOT a chatbot
- There is no dialogue system
- No prompt-based interaction
- No conversational AI
- Learning is structured through a Skill Graph

### 2. AI evaluates only objective components
The AI component evaluates:
- Speech duration
- Filler word usage

These metrics are:
- Rule-based
- Explainable
- Auditable

The AI does **not** evaluate confidence, persuasion, emotion, or presence.

### 3. Humans appear only at final mastery validation
- AI guides practice and recommends mastery
- A human explicitly approves or rejects final mastery
- Human judgment cannot be bypassed by automation

---

## Repository Structure

```text
human-ai-co-tutoring-public-speaking/
│
├── skill_graph/            # Skill Graph definition (JSON)
├── ai/                     # AI evaluation logic (objective metrics only)
├── demo/                   # Streamlit demo application
├── human_validation/       # Final human approval logic
├── sample_audio/           # Example audio file
├── ethics.md               # Ethical considerations
├── requirements.txt        # Minimal dependencies
└── README.md
