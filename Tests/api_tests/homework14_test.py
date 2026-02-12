import pytest

from lesson_14.homework_14 import log_event

@pytest.mark.positive
def test_success():
    log_event("Alex", "success")
def test_expired():
    log_event("Ivan", "expired")
def test_failed():
    log_event("Petro", "failed")

@pytest.mark.negative
def test_expired_negative():
    log_event("Ivan", "expird")