from behave import given, when, then
from todo_list import ToDoList

# Instancia global del ToDoList para todos los pasos
to_do_list = ToDoList()

@given('the to-do list is empty')
def step_impl(context):
    global to_do_list
    to_do_list = ToDoList()

@given('the to-do list contains tasks')
def step_impl(context):
    global to_do_list
    to_do_list = ToDoList()
    for row in context.table:
        to_do_list.add_task(row['Task'])

@given('the to-do list contains tasks with status')
def step_impl(context):
    global to_do_list
    to_do_list = ToDoList()
    for row in context.table:
        to_do_list.add_task(row['Task'])
        # Asume que las tareas están "Pending" por defecto

@when('the user adds a task "{task}"')
def step_impl(context, task):
    global to_do_list
    to_do_list.add_task(task)

@when('the user lists all tasks')
def step_impl(context):
    global to_do_list
    context.listed_tasks = to_do_list.list_tasks()

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    global to_do_list
    context.mark_result = to_do_list.mark_task_completed(task)

@when('the user clears the to-do list')
def step_impl(context):
    global to_do_list
    to_do_list.clear_tasks()

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    global to_do_list
    descriptions = [t.description for t in to_do_list.list_tasks()]
    assert task in descriptions

@then('the output should contain')
def step_impl(context):
    global to_do_list
    listed_tasks = to_do_list.list_tasks()
    output = [task.description for task in listed_tasks]
    for row in context.table:
        assert row['Task'] in output

@then('the task "{task}" should be marked as completed')
def step_impl(context, task):
    global to_do_list
    for t in to_do_list.list_tasks():
        if t.description == task:
            assert t.completed
            return
    assert False, "Task not found"

@then('the to-do list should be empty')
def step_impl(context):
    global to_do_list
    assert len(to_do_list.list_tasks()) == 0

@then('the to-do list should contain 2 tasks named "Study"')
def step_impl(context):
    global to_do_list
    count = sum(1 for t in to_do_list.list_tasks() if t.description == "Study")
    assert count == 2

@then('the task should not be found')
def step_impl(context):
    assert context.mark_result is False
