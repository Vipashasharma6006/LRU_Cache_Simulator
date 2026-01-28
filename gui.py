import tkinter as tk
from tkinter import messagebox
from lru_cache import LRUCache  # This uses the backend logic you already wrote
from tkinter import font


class LRUCacheGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("LRU Cache Simulator")
        # Set font
        self.font_style = font.Font(family="Segoe UI", size=10)
        # Dark mode tracking variable
        self.dark_mode = tk.BooleanVar()


# Add padding between rows
        self.root.configure(padx=10, pady=10)


        self.cache = None

        # Cache Size Input
        #tk.Label(root, text="Enter Cache Size:").grid(row=0, column=0)
        tk.Label(root, text="Enter Cache Size:", font=self.font_style).grid(row=0, column=0, sticky="w", pady=5)

        #self.size_entry = tk.Entry(root)
        self.size_entry = tk.Entry(root, font=self.font_style)

        self.size_entry.grid(row=0, column=1)
        #tk.Button(root, text="Initialize Cache", command=self.init_cache).grid(row=0, column=2)
        tk.Button(root, text="Initialize Cache", font=self.font_style, command=self.init_cache).grid(row=0, column=2, pady=5)

        # Key and Value Input
        #tk.Label(root, text="Key:").grid(row=1, column=0)
        tk.Label(root, text="Key:", font=self.font_style).grid(row=1, column=0, sticky="w", pady=5)

        self.key_entry = tk.Entry(root,font=self.font_style)
        self.key_entry.grid(row=1, column=1)

        #tk.Label(root, text="Value:").grid(row=2, column=0)
        tk.Label(root, text="Value:", font=self.font_style).grid(row=2, column=0, sticky="w", pady=5)

        self.value_entry = tk.Entry(root,font=self.font_style)
        self.value_entry.grid(row=2, column=1)

        # Buttons
        tk.Button(root, text="Put", font=self.font_style, command=self.put_value).grid(row=3, column=0, pady=5)
        tk.Button(root, text="Get", font=self.font_style, command=self.get_value).grid(row=3, column=1, pady=5)
        tk.Button(root, text="Display Cache", font=self.font_style, command=self.display_cache).grid(row=3, column=2, pady=5)
        tk.Checkbutton(
        root, text="Dark Mode", variable=self.dark_mode,
        font=self.font_style, command=self.toggle_theme).grid(row=5, column=0, sticky="w", pady=5)

        # Output Display
        #self.output_text = tk.Text(root, height=10, width=50)
        self.output_text = tk.Text(root, height=10, width=60, font=("Consolas", 10), bg="#f9f9f9")

        self.output_text.grid(row=4, column=0, columnspan=3, pady=10)
        #self.output_text = tk.Text(root, height=10, width=60, font=("Consolas", 10), bg="#f9f9f9")


    def init_cache(self):
        size = self.size_entry.get()
        if size.isdigit() and int(size) > 0:
            self.cache = LRUCache(int(size))
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"✅ Cache initialized with size {size}\n")
        else:
            messagebox.showerror("Error", "Please enter a valid positive number for cache size.")

    def put_value(self):
        if not self.cache:
            messagebox.showwarning("Warning", "Initialize cache first.")
            return

        key = self.key_entry.get()
        value = self.value_entry.get()

        if key == "" or value == "":
            messagebox.showwarning("Warning", "Enter both key and value.")
            return

        # self.cache.put(key, value)
        # self.output_text.insert(tk.END, f"Put ({key}, {value})\n")
        evicted = self.cache.put(key, value)
        self.output_text.insert(tk.END, f"Put ({key}, {value})\n")
        if evicted:
            self.output_text.insert(tk.END, f"⚠️ Evicted: {evicted} (Least Recently Used)\n")
   

    def get_value(self):
        if not self.cache:
            messagebox.showwarning("Warning", "Initialize cache first.")
            return

        key = self.key_entry.get()
        if key == "":
            messagebox.showwarning("Warning", "Enter key to get value.")
            return

        result = self.cache.get(key)
        if result != -1:
            self.output_text.insert(tk.END, f"Get {key} → {result}\n")
        else:
            self.output_text.insert(tk.END, f"{key} not found in cache\n")

    def display_cache(self):
        if not self.cache:
            messagebox.showwarning("Warning", "Initialize cache first.")
            return

        self.output_text.insert(tk.END, "Cache state (MRU → LRU):\n")
        current = self.cache.head.next
        while current != self.cache.tail:
            self.output_text.insert(tk.END, f"{current.key}: {current.val}  ")
            current = current.next
        self.output_text.insert(tk.END, "\n\n")
    def toggle_theme(self):
        widgets = [
            self.size_entry,
            self.key_entry,
            self.value_entry,
            self.output_text
        ]

        buttons = self.root.grid_slaves()
        labels = [child for child in buttons if isinstance(child, tk.Label)]
        controls = [child for child in buttons if isinstance(child, tk.Button)]
        checkbuttons = [child for child in buttons if isinstance(child, tk.Checkbutton)]

        if self.dark_mode.get():
        # 🌑 Dark Theme
            self.root.configure(bg="#1e1e1e")
            for widget in widgets:
                widget.configure(bg="#2e2e2e", fg="#ffffff", insertbackground="#ffffff")

            for label in labels:
                label.configure(bg="#1e1e1e", fg="#ffffff")

            for button in controls + checkbuttons:
                button.configure(bg="#3a3a3a", fg="#ffffff", activebackground="#444444", activeforeground="#ffffff")

            self.output_text.configure(bg="#252526", fg="#d4d4d4")
        else:
        # ☀️ Light Theme
            self.root.configure(bg="#f0f0f0")
            for widget in widgets:
                widget.configure(bg="white", fg="black", insertbackground="black")

            for label in labels:
                label.configure(bg="#f0f0f0", fg="black")

            for button in controls + checkbuttons:
                button.configure(bg="SystemButtonFace", fg="black", activebackground=None, activeforeground=None)

            self.output_text.configure(bg="#f9f9f9", fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = LRUCacheGUI(root)
    root.mainloop()
