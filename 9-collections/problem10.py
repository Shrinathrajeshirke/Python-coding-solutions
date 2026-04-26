# Build a complete task management system:

# Uses ALL collections learned today
# Counter for task categories
# defaultdict for tasks by status
# deque for recent activity log
# namedtuple for Task structure
# Features:

# Add task
# Complete task
# Show dashboard

from collections import namedtuple, deque, Counter, defaultdict

Task = namedtuple('Task',['name', 'category', 'priority', 'status'])
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.tasks_by_status = defaultdict(list)
        self.activity_log = deque(maxlen=5)

    def add_task(self, name, category, priority):
        t = Task(name, category, priority, 'pending')
        self.tasks.append(t)
        self.tasks_by_status['pending'].append(t)
        self.activity_log.append(f"Added: {name}")
        print("Task added")

    def complete_task(self, name):
        for task in self.tasks_by_status['pending']:
            if task.name == name:
                self.tasks_by_status['pending'].remove(task)

                completed = Task(task.name, task.category, task.priority, 'completed')

                self.tasks_by_status['completed'].append(completed)

                self.activity_log.append(f"completed: {name}")
                self.tasks.append(completed)
                break

    def show_dashboard(self):
        print(f"=== Task Dashboard ===")

        print("\nTasks by status")
        for status in ['pending', 'completed']:
            tasks = self.tasks_by_status[status]
            print(f"{status.capitalize()}: {len(tasks)}")
            for task in tasks:
                print(f"   - {task.name} ({task.category}) - {task.priority}")

        print("\nTasks by Category:")
        categories = Counter(task.category for task in self.tasks)
        for category, count in categories.items():                print(f"{category}: {count}")

        print("\nRecent Activity (Last 5):")
        for activity in self.activity_log:
            print(activity)

        high_priority_count = 0
        for task in self.tasks:
            if task.priority == 'high':
                high_priority_count += 1
        print(f"\nHigh Priority Tasks: {high_priority_count}")
        
tm = TaskManager()
tm.add_task("Fix bug", "Development", "high")
tm.add_task("Write docs", "Documentation", "medium")
tm.add_task("Code review", "Development", "high")
tm.complete_task("Fix bug")
tm.show_dashboard()