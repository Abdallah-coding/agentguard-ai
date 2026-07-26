import pytest
from pydantic import ValidationError

from agentguard.schemas import (
    PolicyDecision,
    PolicyDecisionType,
    RiskLevel,
    ToolRequest,
)


def test_valid_tool_request_can_be_created():
    tool_request = ToolRequest(
        request_id="REQ-001",
        user_role="doctor",
        tool_name="get_patient_data",
        arguments={
            "patient_id": "P-102",
            "field": "appointments",
        },
        reason="The doctor needs to check the patient's appointments.",
    )

    assert tool_request.request_id == "REQ-001"
    assert tool_request.user_role == "doctor"
    assert tool_request.tool_name == "get_patient_data"
    assert tool_request.arguments["patient_id"] == "P-102"
    assert tool_request.reason == "The doctor needs to check the patient's appointments."


def test_empty_request_id_is_rejected():
    with pytest.raises(ValidationError):
        ToolRequest(
            request_id="",
            user_role="doctor",
            tool_name="get_patient_data",
            arguments={"patient_id": "P-102"},
            reason="The doctor needs to check the patient's appointments.",
        )
def test_valid_policy_decision_can_be_created():
    decision = PolicyDecision(
        decision=PolicyDecisionType.REQUIRE_APPROVAL,
        risk_level=RiskLevel.HIGH,
        reasons=[
            "The request accesses patient data.",
            "The request contains a patient identifier.",
        ],
        safe_alternative="Ask for approval before accessing the patient record.",
    )

    assert decision.decision == PolicyDecisionType.REQUIRE_APPROVAL
    assert decision.risk_level == RiskLevel.HIGH
    assert len(decision.reasons) == 2
    assert decision.safe_alternative == "Ask for approval before accessing the patient record."


def test_policy_decision_requires_at_least_one_reason():
    with pytest.raises(ValidationError):
        PolicyDecision(
            decision=PolicyDecisionType.BLOCK,
            risk_level=RiskLevel.CRITICAL,
            reasons=[],
        )
      
