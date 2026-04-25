# Using deque:

# Implement a simple browser history
# Operations:

# visit(url) - visit new page
# back() - go back
# forward() - go forward
# show_history() - show all pages

from collections import deque

class BrowserHistory:
    def __init__(self):
        self.history = deque()
        self.current = None
        self.future = deque()

    def visit(self, url):
        if self.current:
            self.history.append(self.current)
        self.current = url
        self.future.clear()
        print(f"visited: {url}")

    def back(self):
        if not self.history:
            print("can't go back")
            return
        self.future.appendleft(self.current)
        self.current = self.history.pop()

        print(f"Back to: {self.current}")

    def forward(self):
        if not self.future:
            print("can't go forward")
        
        self.history.append(self.current)
        self.current = self.future.popleft()

        print(f"forward to: {self.current}")
    
    def show_history(self):
        for page in self.history:
            print(f"<- {page}")
        print(f"-> {self.current} (current)")
        for page in self.future:
            print(f"   {page}")

browser = BrowserHistory()
browser.visit("google.com")
browser.visit("youtube.com")
browser.visit("github.com")
browser.back()
browser.back()
browser.forward()
browser.show_history()
