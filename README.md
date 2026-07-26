# AgentGuard AI

AgentGuard AI is a runtime security gateway for tool-using AI agents.

It intercepts tool requests before execution, evaluates security risks such as prompt injection and sensitive-data leakage, and decides whether to allow, block, redact, or require human approval.

Current status
This project is currently in the early foundation stage.

Implemented so far:

Pydantic schemas for structured tool requests and policy decisions
Fake healthcare data
Fake tools that simulate patient queries, document reading, internal messages, and external emails
A tool registry
A tool execution function
Pytest tests for schemas and tools

Project goal
The final goal is to build a defensive security layer for AI agents that can:

intercept tool calls,
detect risky actions,
protect sensitive data,
detect prompt-injection attempts,
apply policy rules,
log decisions,
require human approval for dangerous actions,
and provide clear explanations for every decision.

Disclaimer
All data in this project is fake and used only for educational purposes.
This project does not use real patient data and does not interact with real systems.
