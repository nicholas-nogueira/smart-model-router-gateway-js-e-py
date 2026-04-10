import sys
from dataclasses import replace
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import app.main as main_app
from services.config import load_config
from services.openRouterService import OpenRouterService


class OpenRouterServiceAdapter:
    """Wraps a sync OpenRouterService to satisfy the async interface expected by app.main."""

    def __init__(self, config_override):
        self._service = OpenRouterService(config_override)

    async def generate(self, prompt: str):
        return self._service.generate(prompt)


@pytest.fixture
def make_client():
    """Factory fixture that builds a TestClient with a custom provider sort strategy.

    Restores the original service after each test via yield.
    """
    original_service = main_app.service

    def _build(sort_by: str) -> TestClient:
        base_config = load_config()
        custom_provider = {
            **base_config.provider,
            "sort": {**base_config.provider["sort"], "by": sort_by},
        }
        custom_config = replace(base_config, provider=custom_provider)
        main_app.service = OpenRouterServiceAdapter(custom_config)
        return TestClient(main_app.app)

    yield _build

    main_app.service = original_service
