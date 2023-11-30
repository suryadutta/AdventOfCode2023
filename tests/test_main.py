from src.main import run_main_task


def test_run_main_task(caplog):
    run_main_task()

    assert "Running main task" in caplog.text
    assert "Finished running main task" in caplog.text
