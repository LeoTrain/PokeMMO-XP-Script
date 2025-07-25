import tkinter as tk
import subprocess
import threading

class PokeXpApp:
    def __init__(self):
        self.process = None
        self.expand = False
        self._init_tk()

    def _init_tk(self):
        self.root = tk.Tk()
        self.root.title("Toggle")
        self.root.geometry("650x60")
        self.root.configure(bg="#1c1c1c")
        self.root.resizable(False, False)
        self._construct_tk()

    def _construct_tk(self):
        self.main_frame = tk.Frame(self.root, bg="#1c1c1c")
        self.main_frame.pack(fill="both", expand=True, padx=6, pady=6)
        self.top_frame = tk.Frame(self.main_frame, bg="#1c1c1c")
        self.top_frame.pack(fill="x", anchor="n")
        self.bottom_frame = tk.Frame(self.main_frame, bg="#1c1c1c")
        self.bottom_frame.pack(fill="x", anchor="n", pady=(8, 0))
        self._add_action_button("Heal", self._on_heal_clicked)
        self._add_action_button("Center", self._on_center_clicked)
        self._add_action_button("Test", self._on_test_clicked)
        self.canvas = tk.Canvas(self.top_frame, width=60, height=60, bg="#1c1c1c", highlightthickness=0)
        self.canvas.pack(side="left")
        self.button_circle = self.canvas.create_oval(4, 4, 44, 44, fill="#E49273", outline="#E49273", width=2)
        self.canvas.tag_bind(self.button_circle, "<Button-1>", self._toggle_xp_script)
        self.status_var = tk.StringVar(value="Script inactif")
        self.status_label = tk.Label(
            self.top_frame,
            textvariable=self.status_var,
            font=("Helvetica", 11),
            fg="white",
            bg="#1c1c1c",
            anchor="w",
            justify="left"
        )
        self.status_label.pack(side="left", fill="both", expand=True, padx=8)
        self.toggle_arrow = tk.Label(
            self.top_frame,
            text="▼",
            font=("Helvetica", 14),
            fg="white",
            bg="#1c1c1c",
            cursor="hand2"
        )
        self.toggle_arrow.pack(side="right", padx=8)
        self.toggle_arrow.bind("<Button-1>", self._toggle_expand)

    def _add_action_button(self, label_text, command):
        container = tk.Frame(self.bottom_frame, bg="#1c1c1c")
        container.pack(side="left", padx=12)

        label = tk.Label(
            container,
            text=label_text,
            font=("Helvetica", 9),
            fg="white",
            bg="#1c1c1c"
        )
        label.pack(side="top", pady=(0, 2), anchor="center")
        button = tk.Button(
            container,
            text=label_text[0],
            font=("Helvetica", 9),
            bg="#333333",
            fg="white",
            activebackground="#555555",
            relief="flat",
            width=4,
            command=command
        )
        button.pack(side="top", anchor="center")

    def _toggle_expand(self, event=None):
        if not self.expand:
            self.root.geometry("650x200")
            self.toggle_arrow.config(text="▲")
        else:
            self.root.geometry("650x60")
            self.toggle_arrow.config(text="▼")
        self.expand = not self.expand

    def _read_log_loop(self):
        while self.process and self.process.stdout:
            line = self.process.stdout.readline()
            if not line:
                break
            self.status_var.set(line.strip())

    def _on_heal_clicked(self):
        self.status_var.set("Heal pressed")
        if self.process is None:
            self.status_var.set("Starting Healing script...")
            self._start_script("heal.py")
        else:
            self._stop_process()

    def _on_center_clicked(self):
        self.status_var.set("Center pressed")
        if self.process is None:
            self.status_var.set("Recentering position")
            self._start_script("center.py")
        else:
            self._stop_process()

    def _on_test_clicked(self):
        self.status_var.set("Test pressed")
        if self.process is None:
            self.status_var.set("Starting Test script...")
            self._start_script("test.py")
        else:
            self._stop_process()

    def _start_script(self, script:str):
        self.process = subprocess.Popen(
            ["python", f"srcs/{script}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        threading.Thread(target=self._read_log_loop, daemon=True).start()
        self.canvas.itemconfig(self.button_circle, fill="#A7C957", outline="#A7C957")
        self.status_var.set("Script running")

    def _stop_process(self):
        self.process.terminate()
        self.process = None
        self.canvas.itemconfig(self.button_circle, fill="#E49273", outline="#E49273")
        self.status_var.set("Script stopped")

    def _toggle_xp_script(self, event=None):
        if self.process is None:
            self._start_script("xp.py")
        else:
            self._stop_process()

    def run(self):
        self._read_log_loop()
        self.root.mainloop()
