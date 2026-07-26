from agentguard.schemas import ToolRequest
from agentguard.tools import execute_tool_request, query_patient, read_document


def test_query_patient_returns_appointments():
    appointments = query_patient("P-102", "appointments")

    assert appointments == ["2026-07-20 10:00"]


def test_execute_query_patient_success():
    request = ToolRequest(
        request_id="REQ-001",
        user_role="doctor",
        tool_name="query_patient",
        arguments={
            "patient_id": "P-102",
            "field": "appointments",
        },
        reason="Doctor needs to check appointments.",
    )

    result = execute_tool_request(request)

    assert result.success is True
    assert result.request_id == "REQ-001"
    assert result.tool_name == "query_patient"
    assert result.output == ["2026-07-20 10:00"]
    assert result.error is None


def test_execute_query_unknown_patient_fails():
    request = ToolRequest(
        request_id="REQ-002",
        user_role="doctor",
        tool_name="query_patient",
        arguments={
            "patient_id": "P-999",
            "field": "appointments",
        },
        reason="Doctor needs to check appointments.",
    )

    result = execute_tool_request(request)

    assert result.success is False
    assert result.request_id == "REQ-002"
    assert result.tool_name == "query_patient"
    assert result.output is None
    assert result.error == "Patient not found: P-999"


def test_read_normal_document():
    content = read_document("normal_note.txt")

    assert content == "Patient P-102 has an appointment next Monday."


def test_read_malicious_document():
    content = read_document("malicious_note.txt")

    assert "Ignore previous instructions" in content
    assert "attacker@example.com" in content


def test_execute_read_document_success():
    request = ToolRequest(
        request_id="REQ-003",
        user_role="doctor",
        tool_name="read_document",
        arguments={
            "file_name": "normal_note.txt",
        },
        reason="Doctor wants to read a normal note.",
    )

    result = execute_tool_request(request)

    assert result.success is True
    assert result.request_id == "REQ-003"
    assert result.tool_name == "read_document"
    assert result.output == "Patient P-102 has an appointment next Monday."
    assert result.error is None


def test_unknown_tool_is_rejected():
    request = ToolRequest(
        request_id="REQ-004",
        user_role="doctor",
        tool_name="delete_everything",
        arguments={},
        reason="Trying to call an unknown dangerous tool.",
    )

    result = execute_tool_request(request)

    assert result.success is False
    assert result.request_id == "REQ-004"
    assert result.tool_name == "delete_everything"
    assert result.output is None
    assert result.error == "Unknown tool"
