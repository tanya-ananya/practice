from tkinter import Tk, Entry, Label, Button, Canvas, Text

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def create_circular(n):
    head = Node(n)
    current = head
    for i in range(1, n):
        current.next = Node(i)
        current = current.next
    current.next = head
    return head

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title('One Potato, Two Potato')

        self.n = None
        self.k = None
        self.head = None
        self.remaining_players = None

        self.label_n = Label(root, text='Enter a value for N (1--12)')
        self.label_n.grid(row=0, column=0, padx=10, pady=5)
        self.entry_n = Entry(root)B
        self.entry_n.grid(row=0, column=1, padx=10, pady=5)

        self.label_k = Label(root, text='Enter a value for k (>=1)')
        self.label_k.grid(row=0, column=0, padx=10, pady=5)
        self.entry_k = Entry(root)
        self.entry_k.grid(row=0, column=1, padx=10, pady=5)

        self.start_button = Button(root, text='Start', command=self.start_game)
        self.start_button.grid(row=2, columnspan=2, pady=10)

        self.eliminate_button = Button(root, text='Eliminate', command=self.eliminate_game)
        self.eliminate_button.grid(row=2, columnspan=2, pady=10)

        self.canvas = Canvas(root, width=400, height=400)
        self.canvas.grid(row=4, columnspan=2, padx=10, pady=10)

        self.text = Text(root, width=40, height=10)
        self.text.grid(row=5, columnspan=2, padx=10, pady=10)

    def start_game(self):
        try:
            n_input = self.entry_n.get()
            k_input = self.entry_k.get()
            
        except Exception as e:
            self.text.insert('end', f"Error: {e}\n")