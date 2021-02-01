print(
        "————— Main menu —————",
        "1. Get all tasks",
        "2. Get specific task",
        "3. Add new task",
        "4. Archive a task",
        sep="\n",
    )
    action = int(input("What will you choose? "))
    if action == 1 or action == 'all':
        for task in Tasks().all():
            print(
                f"{'✅' if task['is_done'] == 1 else '❌'} {task['id']}. {task['title']}",
            )

        task_to_complete = int(input("Enter a task_id to complete specific task: "))
        if task_to_complete:
            Tasks().complete(task_to_complete)

    elif action == 2 or action == 'specific':
        task = Tasks().find(int(input("Enter a correct task_id: ")))
        print(
            f">>> {'✅' if task['is_done'] == 1 else '❌'} {task['id']}. {task['title']}",
        )

    elif action == 3 or action == 'create':
        Tasks().create((input("Enter correct title for your task: "), 1))

    elif action == 4 or action == 'delete':
        Tasks().delete(int(input("Enter correct task_id to archive: ")))

    else:
        print("Goodbye!")
        break