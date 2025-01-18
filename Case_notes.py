import tkinter as tk
from tkinter import messagebox
import pyperclip

class CaseEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Case Entry Application")

        self.entries = []

        self.create_widgets()

    def create_widgets(self):
        self.instructions_label = tk.Label(self.root, text="Please fill out the following fields:")
        self.instructions_label.pack()

        self.fields = [
            
            "Summary and problem statement",
            "Testing performed (including steps to duplicate)",
            "KBs used",
            "Conclusion",
            "Action plan/ Next steps"
        ]

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        for i, field in enumerate(self.fields):
            tk.Label(self.frame, text=field).grid(row=i, column=0, sticky='e', pady=5)
            entry = tk.Entry(self.frame, width=50)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries.append(entry)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.pack(pady=20)

    def submit(self):
        answers = [entry.get() for entry in self.entries]

        if any(not answer for answer in answers):
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return

        formatted_answers = []
        for field, answer in zip(self.fields, answers):
            formatted_answers.append(f"{field}: {answer}")

        qa_text = "\n".join(formatted_answers)
        pyperclip.copy(qa_text)
        
        messagebox.showinfo("Submission Successful", "All entries have been copied to the clipboard.")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = CaseEntryApp(root)
    root.mainloop()
