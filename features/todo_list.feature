Feature: To-Do List Manager

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task        |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      | Task        |
      | Buy groceries |
      | Pay bills     |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks with status:
      | Task         | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the task "Buy groceries" should be marked as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task        |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Add a duplicate task
    Given the to-do list is empty
    When the user adds a task "Study"
    And the user adds a task "Study"
    Then the to-do list should contain 2 tasks named "Study"

  Scenario: Mark non-existent task as completed
    Given the to-do list is empty
    When the user marks task "NonExistent" as completed
    Then the task should not be found
