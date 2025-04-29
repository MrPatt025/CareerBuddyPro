import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_jobs_empty():
    response = client.get("/jobs/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_and_read_job():
    job_data = {
        "title": "Test Job",
        "company": "Test Co",
        "date_applied": "2025-04-01T00:00:00",
        "status": "Applied"
    }
    response = client.post("/jobs/", json=job_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Job"
    
    response2 = client.get("/jobs/")
    assert response2.status_code == 200
    assert len(response2.json()) == 1
