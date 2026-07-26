# Project Scope
## Goal

AgentGuard AI is a defensive runtime gateway for tool-using AI agents.

The goal is to intercept tool requests before execution and decide whether the request should be allowed, blocked, redacted, or sent for human approval.

## What the system protects against

The system is designed to protect against:

- unsafe tool use,
- sensitive-data leakage,
- unauthorized access to fake patient data,
- external exfiltration of private information,
- prompt-injection attempts,
- excessive agency by AI agents.

## What the system does not do

The system does not:

attack real systems,
exploit vulnerabilities,
use real patient data,
make medical decisions,
replace human review,
provide real healthcare advice.

## Fake tools available to the agent

The fake agent can eventually request these tools:

- 'query_patient'
- 'read_document'
- 'send_internal_message'
- 'send_external_email'

These tools are intentionally simple and unsafe at the beginning. Later, AgentGuard will control when they can or cannot run.

## Possible policy decisions

AgentGuard can return four possible decisions:

- 'allow'
- 'block'
- 'require_approval'
- 'redact'

Each decision must include a risk level and at least one explanation.

## Why this project matters
AI agents are becoming more capable because they can use tools, access data, and perform actions.

This creates new risks. A tool-using AI system should not be allowed to act freely without checks.

AgentGuard AI explores how to add a defensive layer between the agent and the tools it wants to use.
