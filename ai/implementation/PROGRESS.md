# Implementation Progress Board

## Navigation & Agent Guide
This board manages the project state using a Jira-like sprint flow, focusing on **one step at a time**.

- **Sprint Flow**: We divide each step into actionable sub-tasks and manage them through `Backlog` -> `To Do` -> `In Progress` -> `In Review` -> `Done`.
- **Step Folder Sync**: The active step's detailed todo list must be maintained in `ai/implementation/step_##/todo.md`. Its scope and rules live in `explainer.md`, and its completion summary lives in `outcome.md`.
- **Completion Protocol**: Once an entire step is complete, all of its granular sub-tasks are cleared from this board. In the `Done` section, we only leave the **Step Name**, a **short description** of what was achieved, and links to the step folder files.

> **⚠️ Context Optimization Rule (For AI Agent):**
> Do **NOT** read historical step folders linked in the "Done" section by default. Only read historical step files if you explicitly identify a dependency or require specific context to complete the task in-hand. Read nothing more, nothing less.

---

## 📋 Backlog
*(Sub-tasks for future steps or overflow from the current step)*
- 

## 📝 To Do
*(Actionable sub-tasks for the current step)*
- 

## 🚧 In Progress
*(What is actively being worked on right now)*
- 

## 🔍 In Review
*(Sub-tasks that are executed but pending verification/evaluation)*
- 

## ✅ Done
*(Completed steps. Link to step folder files here. Clear out granular sub-tasks once the whole step is done.)*
- 
