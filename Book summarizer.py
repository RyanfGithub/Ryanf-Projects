import tkinter as tk
import customtkinter
from openai import OpenAI

customtkinter.set_appearance_mode("System")  # Initial mode: "System" (standard), "Dark" or "Light")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Book Summarizer")
        self.geometry("1000x1200")

        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(4, weight=1)

        # create sidebar frame with dark/light mode toggle button
        self.sidebar_frame = customtkinter.CTkFrame(self, width=240, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")

        self.mode_toggle_button = customtkinter.CTkButton(self.sidebar_frame, text="Toggle Mode", command=self.toggle_mode, font=("Arial", 14))
        self.mode_toggle_button.grid(row=0, column=0, padx=20, pady=20)

        # create main entry and button
        self.entry_city = customtkinter.CTkEntry(self, placeholder_text="What book would you like me to summarize?", font=("Arial", 14))
        self.entry_city.grid(row=1, column=1, padx=(20, 20), pady=(20, 10), sticky="nsew", columnspan=4)

        self.entry_shops = customtkinter.CTkEntry(self, placeholder_text="How long would you like the summary to be?", font=("Arial", 14))
        self.entry_shops.grid(row=2, column=1, padx=(20, 20), pady=(10, 10), sticky="nsew", columnspan=4)

        self.button_submit = customtkinter.CTkButton(self, text="Summarize", command=self.on_submit, font=("Arial", 14))
        self.button_submit.grid(row=3, column=1, padx=(20, 20), pady=(10, 20), sticky="nsew", columnspan=4)

        # create textbox (using CTkTextbox instead of Text)
        self.textbox = customtkinter.CTkTextbox(self, font=("Arial", 14))
        self.textbox.grid(row=4, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew", columnspan=4, rowspan=2)

    def on_submit(self):
        Book = self.entry_city.get()
        Length = self.entry_shops.get()

        if Book and Length:
            result = self.find_places(Book, Length)
            self.textbox.insert("0.0", result + "\n\n")
            self.textbox.see("end")  # Scroll to the bottom after updating text

    def find_places(self, Book, Length):
        client = OpenAI(api_key="<OpenAi API key>")

        system_data = [{
            "role": "system",
            "content": f"You are a book summarizing assistant that summarizes books in a huaman like way in."
        }, {
            "role": "user",
            "content": f"Summarize the book {Book} in {Length}."
        }]

        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=system_data)
        assistant_response = response.choices[0].message.content

        return "Summary Assistant: \n" + str(assistant_response)

    def toggle_mode(self):
        current_mode = customtkinter.get_appearance_mode()
        if current_mode == "Dark":
            customtkinter.set_appearance_mode("Light")
        else:
            customtkinter.set_appearance_mode("Dark")


if __name__ == "__main__":
    app = App()
    app.mainloop()
