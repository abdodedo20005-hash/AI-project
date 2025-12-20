import tkinter as tk
import random
import time
from collections import deque

# =========================
# Search Algorithms
# =========================
class SearchAlgorithms:
    def __init__(self, room, start):
        self.room = room
        self.start = start
        self.rows = len(room)
        self.cols = len(room[0])
        self.moves = [(-1,0),(1,0),(0,-1),(0,1)]

    def is_goal(self, room):
        return all(room[r][c] == 0 for r in range(self.rows) for c in range(self.cols))

    def bfs(self):
        queue = deque([(self.start, self.copy_room(self.room), [self.start])])
        visited = set()
        nodes = 0

        while queue:
            (r,c), room, path = queue.popleft()
            nodes += 1

            state = (r,c, tuple(map(tuple, room)))
            if state in visited:
                continue
            visited.add(state)

            if room[r][c] == 1:
                room[r][c] = 0

            if self.is_goal(room):
                return path, nodes

            for dr,dc in self.moves:
                nr,nc = r+dr, c+dc
                if 0<=nr<self.rows and 0<=nc<self.cols:
                    queue.append(((nr,nc), self.copy_room(room), path+[(nr,nc)]))

        return None, nodes

    def dfs(self):
        stack = [ (self.start, self.copy_room(self.room), [self.start]) ]
        visited = set()
        nodes = 0

        while stack:
            (r,c), room, path = stack.pop()
            nodes += 1

            state = (r,c, tuple(map(tuple, room)))
            if state in visited:
                continue
            visited.add(state)

            if room[r][c] == 1:
                room[r][c] = 0

            if self.is_goal(room):
                return path, nodes

            for dr,dc in self.moves:
                nr,nc = r+dr, c+dc
                if 0<=nr<self.rows and 0<=nc<self.cols:
                    stack.append(((nr,nc), self.copy_room(room), path+[(nr,nc)]))

        return None, nodes

    def ids(self, max_depth=20):
        nodes = 0
        for limit in range(max_depth):
            res, n = self.dls(limit)
            nodes += n
            if res:
                return res, nodes
        return None, nodes

    def dls(self, limit):
        stack = [ (self.start, self.copy_room(self.room), [self.start]) ]
        visited = set()
        nodes = 0

        while stack:
            (r,c), room, path = stack.pop()
            nodes += 1
            if len(path)-1 > limit:
                continue

            state = (r,c, tuple(map(tuple, room)))
            if state in visited:
                continue
            visited.add(state)

            if room[r][c] == 1:
                room[r][c] = 0

            if self.is_goal(room):
                return path, nodes

            for dr,dc in self.moves:
                nr,nc = r+dr, c+dc
                if 0<=nr<self.rows and 0<=nc<self.cols:
                    stack.append(((nr,nc), self.copy_room(room), path+[(nr,nc)]))

        return None, nodes

    def copy_room(self, room):
        return [row.copy() for row in room]

# =========================
# Vacuum Cleaner App
# =========================
class VacuumApp:
    def __init__(self, root, size=6):
        self.root = root
        self.root.title("Team 8 - Vacuum Cleaner AI")
        self.size = size
        self.cell_size = 40
        self.room = []

        self.main_frame = tk.Frame(root)
        self.main_frame.pack(padx=10, pady=10)

        self.canvas = tk.Canvas(self.main_frame,
                                width=size*self.cell_size,
                                height=size*self.cell_size,
                                bg='white')
        self.canvas.pack(side=tk.LEFT)

        self.sidebar = tk.Frame(self.main_frame)
        self.sidebar.pack(side=tk.RIGHT, padx=10, fill=tk.Y)

        tk.Label(self.sidebar, text="Vacuum Cleaner Control",
                 font=("Arial", 12, "bold")).pack(pady=5)

        tk.Button(self.sidebar, text="Generate New Room",
                  command=self.generate_room).pack(fill=tk.X, pady=5)

        self.algos = [
            ("BFS", "bfs"),
            ("DFS", "dfs"),
            ("IDS", "ids"),
        ]

        for name, func in self.algos:
            tk.Button(self.sidebar, text=name,
                      command=lambda f=func, n=name: self.run_algo(f, n)
                      ).pack(fill=tk.X, pady=2)

        self.result_label = tk.Label(self.sidebar,
                                     text="Status: Ready",
                                     fg="blue", justify=tk.LEFT)
        self.result_label.pack(pady=20)

        self.generate_room()

    def generate_room(self):
        self.room = [[1 if random.random() < 0.3 else 0
                      for _ in range(self.size)] for _ in range(self.size)]
        self.room[0][0] = 0
        self.solver = SearchAlgorithms(self.room, (0,0))
        self.draw_room()
        self.result_label.config(text="Status: New Room Generated", fg="blue")

    def draw_room(self, path=None):
        self.canvas.delete("all")
        for r in range(self.size):
            for c in range(self.size):
                color = 'white'
                if self.room[r][c] == 1: color = '#cc9966'   # Dirty
                if (r,c) == (0,0): color = '#00cc00'        # Start
                self.canvas.create_rectangle(
                    c*self.cell_size, r*self.cell_size,
                    (c+1)*self.cell_size, (r+1)*self.cell_size,
                    fill=color, outline='gray'
                )

        if path:
            coords = []
            for r,c in path:
                coords.append(c*self.cell_size + self.cell_size/2)
                coords.append(r*self.cell_size + self.cell_size/2)
            self.canvas.create_line(coords, fill="blue", width=3)

    def run_algo(self, func_name, algo_name):
        self.draw_room()
        self.root.update()
        start_time = time.time()

        algo_func = getattr(self.solver, func_name)
        path, nodes = algo_func()

        elapsed = (time.time() - start_time) * 1000

        if path:
            self.draw_room(path)
            res = f"Algorithm: {algo_name}\nSteps: {len(path)-1}\nNodes: {nodes}\nTime: {elapsed:.2f} ms"
            self.result_label.config(text=res, fg="green")
        else:
            res = f"Algorithm: {algo_name}\nFailed\nNodes: {nodes}"
            self.result_label.config(text=res, fg="red")


# =========================
# Run App
# =========================
if __name__ == "__main__":
    print("Tkinter applications cannot be run directly in Google Colab's default environment.")
    print("To run this as a GUI, please execute the script in a local environment with a graphical display.")
    # Uncomment the lines below if running in a local environment with a display
    # root = tk.Tk()
    # root.geometry("750x550")
    # app = VacuumApp(root)
    # root.mainloop()