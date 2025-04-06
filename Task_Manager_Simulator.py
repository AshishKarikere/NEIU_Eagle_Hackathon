class Task:
    def __init__(self, title, priority, time_estimate):
        self.title = title
        self.priority = priority  # 1=High, 2=Medium, 3=Low
        self.time_estimate = time_estimate
        self.next = None

    def __str__(self):
        # Map numeric priority to a string
        priority_map = {1: "High", 2: "Medium", 3: "Low"}
        return f"{self.title} (Priority: {priority_map[self.priority]}, Time: {self.time_estimate} mins)"

class TaskManager:
    def __init__(self):
        self.head = None
        # For undo: store tuples ("add", task) or ("remove", task, previous_node)
        self.undo_stack = []

    def add_task(self, title, priority, time_estimate):
        new_task = Task(title, priority, time_estimate)
        self.undo_stack.append(("add", new_task))  # record the action for undo

        # Insert task so that list stays sorted (first by priority then by time)
        if self.head is None or priority < self.head.priority or \
           (priority == self.head.priority and time_estimate < self.head.time_estimate):
            new_task.next = self.head
            self.head = new_task
        else:
            current = self.head
            while current.next and ((current.next.priority < priority) or
                   (current.next.priority == priority and current.next.time_estimate <= time_estimate)):
                current = current.next
            new_task.next = current.next
            current.next = new_task
        print("Task added successfully!")

    def view_tasks(self):
        print("Tasks:")
        if not self.head:
            print("(No tasks to display)")
            return
        pos = 1
        curr = self.head
        while curr:
            print(f"{pos}. {curr}")
            pos += 1
            curr = curr.next

    def complete_task(self, title):
        if not self.head:
            print("No tasks to complete.")
            return
        curr = self.head
        prev = None

        # Find the task with the given title
        while curr and curr.title != title:
            prev = curr
            curr = curr.next

        if curr is None:
            print("Task not found.")
            return

        # Record the removal so it can be undone
        self.undo_stack.append(("remove", curr, prev))
        if prev:
            prev.next = curr.next
        else:
            self.head = curr.next
        print(f'Task "{curr.title}" completed successfully!')

    def undo_last_action(self):
        if not self.undo_stack:
            print("Nothing to undo!")
            return

        action = self.undo_stack.pop()
        if action[0] == "add":
            # Undo adding a task by removing it
            task = action[1]
            curr = self.head
            prev = None
            while curr and curr != task:
                prev = curr
                curr = curr.next
            if curr == task:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
            print("Last action undone successfully!")
        elif action[0] == "remove":
            # Undo removal by re-inserting the task
            task = action[1]
            prev_node = action[2]
            if prev_node:
                task.next = prev_node.next
                prev_node.next = task
            else:
                task.next = self.head
                self.head = task
            print("Last action undone successfully!")


def get_valid_int(prompt, valid_values=None):
    while True:
        try:
            num = int(input(prompt))
            if valid_values is not None and num not in valid_values:
                raise ValueError
            return num
        except ValueError:
            print("Invalid input. Please try again.")


def main():
    manager = TaskManager()
    print("Welcome to Task Manager Simulator!")
    while True:
        print("\n1. Add a Task")
        print("2. View All Tasks")
        print("3. Complete a Task")
        print("4. Undo Last Action")
        print("5. Exit")
        option = get_valid_int("Choose an option: ", valid_values=range(1, 6))
        
        if option == 1:
            title = input("Enter task title: ")
            priority = get_valid_int("Enter priority (1 = high, 2 = medium, 3 = low): ", valid_values=[1, 2, 3])
            time_estimate = get_valid_int("Enter time estimate (minutes): ")
            manager.add_task(title, priority, time_estimate)
        elif option == 2:
            manager.view_tasks()
        elif option == 3:
            if not manager.head:
                print("No tasks to complete.")
                continue
            title = input("Enter the title of the task to complete: ")
            manager.complete_task(title)
        elif option == 4:
            manager.undo_last_action()
        elif option == 5:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()