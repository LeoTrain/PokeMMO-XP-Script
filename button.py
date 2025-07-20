import tkinter as tk
import subprocess
import threading

class App:
    def __init__(self):
        self.process = None
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
        self.canvas = tk.Canvas(self.main_frame, width=60, height=60, bg="#1c1c1c", highlightthickness=0)
        self.canvas.pack(side="left")
        self.button_circle = self.canvas.create_oval(4, 4, 44, 44, fill="#E49273", outline="#E49273", width=2)
        self.canvas.tag_bind(self.button_circle, "<Button-1>", self._toggle_script)
        self.status_var = tk.StringVar(value="Script inactif")
        self.status_label = tk.Label(
            self.main_frame,
            textvariable=self.status_var,
            font=("Helvetica", 11),
            fg="white",
            bg="#1c1c1c",
            anchor="w",
            justify="left"
        )
        self.status_label.pack(side="left", fill="both", expand=True, padx=8)

    def _read_log_loop(self):
        while self.process and self.process.stdout:
            line = self.process.stdout.readline()
            if not line:
                break
            self.status_var.set(line.strip())

    def _toggle_script(self, event=None):
        if self.process is None:
            self.process = subprocess.Popen(
                ["env/bin/python", "moving_script.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            threading.Thread(target=self._read_log_loop, daemon=True).start()
            self.canvas.itemconfig(self.button_circle, fill="#A7C957", outline="#A7C957")
            self.status_var.set("Script running")
        else:
            self.process.terminate()
            self.process = None
            self.canvas.itemconfig(self.button_circle, fill="#E49273", outline="#E49273")
            self.status_var.set("Script stopped")

    def run(self):
        self._read_log_loop()
        self.root.mainloop()

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()



