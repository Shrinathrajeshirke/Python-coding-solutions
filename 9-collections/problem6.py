# Using deque with maxlen:

# Implement a recent activity tracker
# Keep only last 5 activities
# Automatically removes oldest when new added
# Show statistics

from collections import deque

class ActivityTracker:
    def __init__(self, maxlen):
        self.maxlen = maxlen
        self.activities = deque(maxlen=maxlen)
        self.removed = []
        self.total_activities_tracked = 0

    def add(self, activity):
        if not self.activities:
            print("No activities tracked yet!")
        if len(self.activities) == self.activities.maxlen:
            self.removed.append(self.activities.popleft())
        self.activities.append(activity)
        self.total_activities_tracked += 1
    
    def show(self):
        print("Output:")
        print("Recent 5 activities: ")
        for i, active in enumerate(self.activities):
            print(f"{i+1}. {active}")
        print("")
        print(f"Total activities tracked: {self.total_activities_tracked}")
        print("")
        print(f"Oldest removed: {", ".join(self.removed)}")
tracker = ActivityTracker(maxlen=5)
tracker.add("Login")
tracker.add("View Dashboard")
tracker.add("Edit Profile")
tracker.add("Upload File")
tracker.add("Send Message")
tracker.add("Logout")
tracker.add("Login Again")
tracker.show()