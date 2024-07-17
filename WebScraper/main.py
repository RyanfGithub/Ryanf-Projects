import requests
from bs4 import BeautifulSoup
from time import sleep
import tkinter as tk
from tkinter import messagebox

# Function to create a popup window
def show_popup(new_price):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Price Changed", f"The new price is: {new_price}")
    root.destroy()

price_before = ''

while True:
    print("Previous price:", price_before)

    try:
        url = "<Insert Website URL>"
        results = requests.get(url)
        results.raise_for_status()  # Check if the request was successful

        doc = BeautifulSoup(results.text, 'html.parser')

        # Extract the price text
        price_element = doc.find('<Price Element HTML object Type>')
        if price_element is None:
            print("Price element not found.")
            continue

        price = price_element.text

        if price != price_before:
            print("Price has changed!")
            print("New price:", price)
            show_popup(price)  # Show popup with the new price
            price_before = price
        else:
            print("Price remains the same.")

    except requests.exceptions.RequestException as e:
        print("Error fetching the webpage:", e)

    sleep(10)
