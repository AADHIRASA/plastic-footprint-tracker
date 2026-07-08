"""
Unit tests for project.py
Run with: pytest test_project.py
"""

import io
from project import calculate_footprint, generate_summary, get_int


def test_calculate_footprint_zero():
    usage = {"bottles": 0, "bags": 0, "straws": 0, "cups": 0, "packets": 0}
    results = calculate_footprint(usage)
    assert results["total"]["items"] == 0
    assert results["total"]["co2_g"] == 0
    assert results["total"]["weight_g"] == 0


def test_calculate_footprint_typical():
    usage = {"bottles": 3, "bags": 2, "straws": 0, "cups": 0, "packets": 0}
    results = calculate_footprint(usage)
    assert results["total"]["items"] == 5
    # 3 bottles * 82.8 + 2 bags * 10.0 = 268.4
    assert round(results["total"]["co2_g"], 1) == 268.4
    assert results["bottles"]["count"] == 3
    assert results["bags"]["count"] == 2


def test_generate_summary_contains_totals():
    usage = {"bottles": 1, "bags": 1, "straws": 1, "cups": 1, "packets": 1}
    results = calculate_footprint(usage)
    summary = generate_summary(results)
    assert "Total items used today" in summary
    assert "5" in summary


def test_get_int_valid(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("7\n"))
    result = get_int("Enter number: ")
    assert result == 7


def test_get_int_rejects_negative_then_accepts(monkeypatch):
    monkeypatch.setattr("sys.stdin", io.StringIO("-1\n4\n"))
    result = get_int("Enter number: ")
    assert result == 4
