# Gauntlex Python Curriculum

**Learn Python by solving problems, building projects, and explaining your decisions.**

A project-based Python curriculum designed for [Gauntlex](https://gauntlex.vercel.app/), with **409 challenges across 23 sections**. Start with your first terminal program, develop reusable functions and reliable applications, and finish with projects that combine data, persistence, APIs, and automation.

**[Visit Gauntlex](https://gauntlex.vercel.app/)** · **[Explore the learning path](GAUNTLEX_LEARNING_PATH.md)** · **[Read the complete curriculum](GAUNTLEX_PYTHON_CURRICULUM.md)**

## About this repository

This repository contains the assignments, starter files, and existing checks for the Gauntlex Python curriculum. It gives learners a structured path from basic Python syntax to building useful software, with clear requirements and practical examples at each step.

The focus is on understanding how a program behaves: what it receives, what it produces, how it handles boundaries, and why its design makes sense. Small exercises introduce individual skills; larger projects bring those skills together into working applications.

The curriculum can be explored directly from this repository. It is maintained separately from the Gauntlex platform application.

## Who it is for

- **New programmers** looking for a guided route into Python through hands-on practice.
- **Self-taught developers** who want to strengthen their foundations and work toward larger projects.
- **Educators and mentors** looking for organized assignments with explicit learning contracts.
- **Python developers** revisiting topics such as asynchronous programming, databases, algorithms, and application design.

## What you will learn

| Area | Topics |
|---|---|
| Python foundations | Terminal programs, variables, input and output, numbers, strings, conditions, and loops |
| Collections and functions | Lists, dictionaries, sets, parameters, return values, nested data, and reusable operations |
| Algorithms and problem solving | Searching, sorting, recursion, matrices, sliding windows, graph traversal, and performance targets |
| Text and files | Parsing, validation, CSV, JSON, dates, UTF-8, paths, and file handling |
| Object-oriented programming | Classes, methods, properties, invariants, stateful objects, queues, and caches |
| Command-line applications | Stream processing, structured output, command handling, and persistent tools |
| Data and statistics | Population statistics, vectors, scaling, regression, prediction metrics, and categorical encoding |
| HTTP and web interfaces | URLs, headers, request and response bodies, local HTTP services, WSGI, routing, and middleware |
| Databases | SQLite schemas, constraints, CRUD operations, joins, aggregation, and atomic transactions |
| Asynchronous programming | Coroutines, concurrent work, timeouts, retries, queues, events, locks, and concurrency limits |
| Testing and delivery | Assertions, exception behavior, output capture, test reports, configuration, versions, and package metadata |
| Architecture and security | Dependency graphs, permissions, event replay, idempotency, hashing, authentication helpers, and sensitive-data handling |

The [learning path](GAUNTLEX_LEARNING_PATH.md) breaks these areas into all 23 sections and links to every challenge.

## Learn through projects

Nine project challenges turn individual concepts into applications with clear commands, data formats, and observable behavior.

| Project | What you build |
|---|---|
| [Persistent Task Tracker](gauntlex/18-capstones/311-task-tracker/README.md) | A SQLite-backed CLI for adding, completing, listing, and deleting tasks |
| [Streaming Log Inspector](gauntlex/18-capstones/312-log-analyzer/README.md) | A log-processing tool that validates records and summarizes activity by severity and date |
| [Expense Ledger](gauntlex/18-capstones/313-expense-ledger/README.md) | A persistent expense tracker with category summaries and integer-cent accounting |
| [A Minimal HTTP Service](gauntlex/18-capstones/314-http-api-server/README.md) | A local JSON API with health, echo, and not-found responses |
| [Inventory Manager](gauntlex/18-capstones/405-inventory-manager/README.md) | A stock-management CLI that persists inventory and prevents negative quantities |
| [Contact Directory](gauntlex/18-capstones/406-contact-book/README.md) | A searchable contact book with case-insensitive email uniqueness |
| [CSV Data Pipeline](gauntlex/18-capstones/407-csv-etl-pipeline/README.md) | A tool that validates, deduplicates, and transforms CSV records into JSON Lines |
| [Event-Sourced Wallet](gauntlex/18-capstones/408-event-sourced-wallet/README.md) | A wallet whose balances can be reconstructed from an append-only event history |
| [Local Link Inspector](gauntlex/18-capstones/409-markdown-link-checker/README.md) | A Markdown link checker that reports missing local targets and paths escaping the project root |

Core projects **311–314** follow the foundational and application-design sections. Extension sections deepen those skills before the final projects **405–409**.

## How the challenges work

Each challenge has a learner-facing README explaining the goal, requirements, tips, and example behavior. Its package also includes metadata, an intentionally incomplete starter, and existing checks.

```text
challenge-directory/
├── README.md
├── metadata.json
├── starter/
│   └── main.py or solution.py
└── tests/
```

Some challenges ask you to return a value from a function. Others ask you to build a terminal program, a stateful object, or a complete project. Read the required interface carefully: exact output, ordering, error handling, and input assumptions are part of the assignment.

## Getting started

1. Install **Python 3.11 or later** and make sure you can run a Python script from your terminal.
2. Open the [ordered learning path](GAUNTLEX_LEARNING_PATH.md) and begin with challenge **001**. If you already know Python, use the section introductions to choose a suitable starting point.
3. Read the challenge README, inspect the starter, and work through the examples before implementing your approach.
4. Work inside that challenge's directory and preserve its supplied filenames and public interface.
5. Run its existing checks, review any failures, and explain why your implementation satisfies the requirements before moving on.

The existing checks use pytest. Install it in your Python environment if needed:

```sh
python -m pip install pytest
```

From an individual challenge directory, run:

```sh
python -m pytest tests -q
```

Unfinished starters are expected to fail. The checks provide feedback, while the README defines the assignment contract. Most exercises use only the Python standard library; follow the dependencies and constraints stated in each brief.

## Find your way around

| Location | Purpose |
|---|---|
| [`gauntlex/`](gauntlex/README.md) | The 409 challenge packages and section overview |
| [`GAUNTLEX_LEARNING_PATH.md`](GAUNTLEX_LEARNING_PATH.md) | Recommended progression, topic introductions, and challenge links |
| [`GAUNTLEX_PYTHON_CURRICULUM.md`](GAUNTLEX_PYTHON_CURRICULUM.md) | All learner-facing briefs in one document |
| [`CURRICULUM_ORDER.md`](CURRICULUM_ORDER.md) | The challenge index and preserved source-activity inventory |
| [`UNIFIED_PYTHON_CURRICULUM.md`](UNIFIED_PYTHON_CURRICULUM.md) | Compatibility navigation to the maintained curriculum documents |
| [`CURRICULUM_AUDIT_REPORT.md`](CURRICULUM_AUDIT_REPORT.md) | Per-challenge review records, corrections, and known limitations |
| [`gauntlex/QUALITY_AND_RELEASE.md`](gauntlex/QUALITY_AND_RELEASE.md) | Verification scope and future release criteria |
| [`scripts/`](scripts/) | Existing curriculum audit and verification utilities |
| [`tools/`](tools/) | Curriculum documentation and publishing utilities |

The repository also retains source collections and review records for provenance. Their licenses, acknowledgments, and review notes remain alongside the relevant material; see [the source review notes](gauntlex/SOURCE_REVIEW_NOTES.md).

## Improving the curriculum

Useful contributions include clearer explanations, corrected examples, broken-link fixes, and well-supported reports of differences between a brief and its existing checks. Include the challenge ID, the specific issue, and the expected behavior when reporting a problem.

Keep assignments approachable for their intended level, preserve existing public interfaces, and avoid adding complete solutions to learner-facing documentation. Changes to grading behavior should be discussed explicitly rather than introduced as documentation edits.

---

**Build your Python skills one challenge at a time.** Explore the platform at **[gauntlex.vercel.app](https://gauntlex.vercel.app/)**.
