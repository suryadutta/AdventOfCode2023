from unittest.mock import patch

from src.run import run_code


@patch("importlib.import_module")
def test_run_main_task(mock_import_module, caplog, monkeypatch):
    mock_import_module.return_value.run_part_a.return_value = "part_a_mock_answer"
    mock_import_module.return_value.run_part_b.return_value = "part_b_mock_answer"

    monkeypatch.setenv("AOC_DAY", "1")

    run_code()

    assert "Part A Answer: part_a_mock_answer" in caplog.text
    assert "Part B Answer: part_b_mock_answer" in caplog.text
