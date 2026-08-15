import calendar
import tkinter as tk
from datetime import datetime

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Calendar")
        self.root.geometry("420x500")

        self.year = datetime.now().year
        self.month = datetime.now().month

        title = tk.Frame(root)
        title.pack(pady=10)

        tk.Button(title, text="◀", command=self.previous_month).pack(side="left")

        self.month_label = tk.Label(
            title, text="", font=("Arial", 20, "bold"), width=18
        )
        self.month_label.pack(side="left")

        tk.Button(title, text="▶", command=self.next_month).pack(side="left")

        self.calendar_frame = tk.Frame(root)
        self.calendar_frame.pack(padx=10)

        tk.Button(
            root,
            text="Today",
            command=self.today,
            font=("Arial", 12)
        ).pack(pady=15)

        self.show_calendar()

    def show_calendar(self):
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()

        month_name = calendar.month_name[self.month]
        self.month_label.config(text=f"{month_name} {self.year}")

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

        for col, day in enumerate(days):
            tk.Label(
                self.calendar_frame,
                text=day,
                font=("Arial", 11, "bold"),
                width=5
            ).grid(row=0, column=col, pady=5)

        month_data = calendar.monthcalendar(self.year, self.month)

        for row, week in enumerate(month_data, start=1):
            for col, day in enumerate(week):
                text = str(day) if day != 0 else ""

                tk.Label(
                    self.calendar_frame,
                    text=text,
                    font=("Arial", 14),
                    width=5,
                    height=2,
                    relief="ridge"
                ).grid(row=row, column=col, padx=1, pady=1)

    def previous_month(self):
        self.month -= 1

        if self.month == 0:
            self.month = 12
            self.year -= 1

        self.show_calendar()

    def next_month(self):
        self.month += 1

        if self.month == 13:
            self.month = 1
            self.year += 1

        self.show_calendar()

    def today(self):
        now = datetime.now()
        self.year = now.year
        self.month = now.month
        self.show_calendar()


root = tk.Tk()
app = CalendarApp(root)
root.mainloop()