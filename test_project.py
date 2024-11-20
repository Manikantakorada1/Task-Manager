from project import add_task, complete_task, list_tasks, remove_task

def test_add_task():
    tasks = []
    add_task(tasks, "Home Work")
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Home Work"
    assert not tasks[0]["completed"]

def test_complete_task():
    tasks = [{"task": "Home Work", "completed": False}]
    complete_task(tasks, 0)
    assert tasks[0]["completed"]

def test_list_task(capsys):
    tasks = [{"task": "Home Work", "completed": True},
            {"task": "Drawing", "completed": True}]

    list_tasks(tasks)
    captured = capsys.readouterr()
    assert "1. Home Work - Completed" in captured.out
    assert "2. Drawing - Completed" in captured.out

def test_remove_task():
    tasks = [{"task": "Home Work", "completed": False},
             {"task": "Drawing", "completed": False}]

    remove_task(tasks, 0)
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Drawing"
