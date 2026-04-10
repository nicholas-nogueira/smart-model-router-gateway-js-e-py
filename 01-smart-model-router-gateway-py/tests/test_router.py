import os

import pytest
from fastapi.testclient import TestClient

pytestmark = pytest.mark.skipif(
    not os.getenv("OPENROUTER_API_KEY"),
    reason="OPENROUTER_API_KEY is not set",
)

QUESTION = "What is the capital of France?"
EXPECTED_MODEL = "nvidia/nemotron-3-nano-30b-a3b:free"


def test_routes_to_cheapest_model_by_default(make_client: TestClient):
    response = make_client("price").post("/chat", json={"question": QUESTION})
    expected_model = "gpt-5-mini"

    assert response.status_code == 200
    body = response.json()
    assert body["response"]["content"] is not None
    assert expected_model in body["response"]["model"]


def test_routes_to_throughput_model_by_default(make_client: TestClient):
    response = make_client("throughput").post("/chat", json={"question": QUESTION})
    expected_model = "google/gemini-3-flash-preview"

    assert response.status_code == 200
    body = response.json()
    assert body["response"]["content"] is not None
    assert expected_model in body["response"]["model"]


def test_routes_to_latency_model_by_default(make_client: TestClient):
    response = make_client("latency").post("/chat", json={"question": QUESTION})
    expected_model = "google/gemini-3-flash-preview"

    assert response.status_code == 200
    body = response.json()
    assert body["response"]["content"] is not None
    assert expected_model in body["response"]["model"]
