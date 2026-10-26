"""Smoke tests for process health; business acceptance tests are tracked separately."""
import os

# Provide safe import-time settings for test collection. Tests never connect to this DB.
os.environ.setdefault(
    "DATABASE_URL",
    "postgresql+psycopg2://test_user:test_password@127.0.0.1:5432/test_db",
)
os.environ.setdefault("SECRET_KEY", "test-only-secret-key-not-for-production-123456789")
os.environ.setdefault("DEBUG", "false")

from fastapi.testclient import TestClient  # noqa: E402
from app.main import app  # noqa: E402


def test_health_endpoint_returns_ok():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"]
    assert body["version"]
