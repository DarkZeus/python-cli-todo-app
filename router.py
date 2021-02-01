from task import Tasks


def fill_screen():
    actions = ['Get all tasks', 'Get specific task', 'Add new task', 'Archive a task']
    for i, item in enumerate(actions):
        print(f"{i + 1}. {item}")

    action = int(input("What will you choose? "))
    if action == 1 or action == 'all':
        index()

    elif action == 2 or action == 'specific':
        show()

    elif action == 3 or action == 'create':
        create()

    elif action == 4 or action == 'delete':
        delete()

    else:
        print("Goodbye!")


def index():
    for task in Tasks().all():
        print(
            f"{'✅' if task['is_done'] == 1 else '❌'} {task['id']}. {task['title']}",
        )

    task_to_complete = int(input("Enter a task_id to complete specific task: "))
    if task_to_complete:
        Tasks().complete(task_to_complete)


def show():
    task = Tasks().find(int(input("Enter a correct task_id: ")))
    print(
        f">>> {'✅' if task['is_done'] == 1 else '❌'} {task['id']}. {task['title']}",
    )


def create():
    Tasks().create((input("Enter correct title for your task: "), 1))


def delete():
    Tasks().delete(int(input("Enter correct task_id to archive: ")))