# Gpt-Researcher - Getting Started

**Pages:** 3

---

## Introduction

**URL:** https://docs.gptr.dev/docs/gpt-researcher/getting-started/introduction

**Contents:**
- Introduction
- Why GPT Researcher?​
- Architecture​
- Demo​
- Tutorials​
- Features​

GPT Researcher is an autonomous agent designed for comprehensive online research on a variety of tasks.

The agent can produce detailed, factual and unbiased research reports, with customization options for focusing on relevant resources, outlines, and lessons. Inspired by the recent Plan-and-Solve and RAG papers, GPT Researcher addresses issues of speed, determinism and reliability, offering a more stable performance and increased speed through parallelized agent work, as opposed to synchronous operations.

The main idea is to run "planner" and "execution" agents, whereas the planner generates questions to research, and the execution agents seek the most related information based on each generated research question. Finally, the planner filters and aggregates all related information and creates a research report. The agents leverage both gpt-4o-mini and gpt-4o (128K context) to complete a research task. We optimize for costs using each only when necessary. The average research task takes around 3 minutes to complete, and costs ~$0.1.

Let's get started here!

---

## Intro to the Frontends

**URL:** https://docs.gptr.dev/docs/gpt-researcher/frontend/introduction

**Contents:**
- Intro to the Frontends
- Choosing an Option​

The frontends enhance GPT-Researcher by providing:

These features aim to make the research process more efficient and user-friendly, complementing GPT-Researcher's powerful agent capabilities.

---

## Docker: Quickstart

**URL:** https://docs.gptr.dev/docs/gpt-researcher/getting-started/getting-started-with-docker

**Contents:**
- Docker: Quickstart
- Running with the Docker CLI​

Step 1 - Install & Open Docker Desktop

Follow instructions at https://www.docker.com/products/docker-desktop/

Step 2 - Follow this flow

This mainly includes cloning the '.env.example' file, adding your API Keys to the cloned file and saving the file as '.env'

In requirements.txt add the relevant langchain packages for the LLM your choose (langchain-google-genai, langchain-deepseek, langchain_mistralai for example)

Step 3 - Within root, run with Docker.

If that doesn't work, try running it without the dash:

Step 4 - By default, if you haven't uncommented anything in your docker-compose file, this flow will start 2 processes:

Visit localhost:3000 on any browser and enjoy researching!

If you want to run the Docker container without using docker-compose, you can use the following command:

This will run the Docker container and mount the /gptr_docs directory to the container's /my-docs directory for analysis by the GPTR API Server.

**Examples:**

Example 1 (bash):
```bash
docker-compose up --build
```

Example 2 (bash):
```bash
docker compose up --build
```

Example 3 (bash):
```bash
docker run -it --name gpt-researcher -p 8000:8000 --env-file .env  -v /absolute/path/to/gptr_docs:/my-docs  gpt-researcher
```

---
