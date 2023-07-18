import unittest
from pages import todo
from pages.todo import TodoPage
from utils import get_driver
import json

"""
Todo
    text 
    actions:
        Complete
        Delete
        edit
        Clear Completed

list Todos
    Filter by
        All
        active
        completed

Happy path:
X    add Todo
X    mark todo completed
    delete TODO


"""

class TestTodoMVC(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
    def tearDown(self) -> None:
        r  = self.driver.execute_script("return window.__coverage__");
        with open("coverage1.json","w") as f:
            f.write(json.dumps(r))

        self.driver.quit()

    def test_add_todo(self):
        todo_list = TodoPage(self.driver)
        todo_list.add('Task 1')
        self.assertTrue(todo_list.exists_todo('Task 1') == True)

    def test_mark_todo_complete(self):
        todo_list = TodoPage(self.driver)
        todo_list.add("Task 1")
        task_name = "Task 2"
        todo_list.add(task_name)
        todo_list.completed(task_name)
        self.assertTrue(todo_list.is_completed(task_name) == True)
        self.assertRaises(todo_list.ElementNotFound, todo_list.is_completed, 'Task 3')


if __name__ == "__main__":
    unittest.main(verbosity=1)
