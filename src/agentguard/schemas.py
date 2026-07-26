from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class PolicyDecisionType(str, Enum):
    ALLOW = "allow"
    BLOCK = "block"
    REQUIRE_APPROVAL = "require_approval"
    REDACT = "redact"


class ToolRequest(BaseModel):
    request_id: str = Field(min_length=1)
    user_role: str = Field(min_length=1)
    tool_name: str = Field(min_length=1)
    arguments: dict[str, Any]
    reason: str = Field(min_length=1)


class PolicyDecision(BaseModel):
    decision: PolicyDecisionType
    risk_level: RiskLevel
    reasons: list[str] = Field(min_length=1)
    safe_alternative: str | None = None


class ToolResult(BaseModel):
    request_id: str = Field(min_length=1)
    tool_name: str = Field(min_length=1)
    success: bool
    output: Any = None
    error: str | None = None
