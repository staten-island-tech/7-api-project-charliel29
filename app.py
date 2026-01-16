
import requests
import tkinter as tk


def search_fruit():
    fruit_name = search_entry.get().lower()

    if fruit_name == "":
        result_label.config(text="Please enter a fruit name.")
        return

    try:
        response = requests.get(
            f"https://www.fruityvice.com/api/fruit/{fruit_name}"
        )

        if response.status_code != 200:
            result_label.config(text="Fruit not found")
            return

        data = response.json()
        nutrition = data["nutritions"]

        result_text = (
            f"Fruit: {data['name']}\n"
            f"Calories: {nutrition['calories']}\n"
            f"Protein: {nutrition['protein']} g\n"
            f"Sugar: {nutrition['sugar']} g\n"
            f"Fat: {nutrition['fat']} g"
        )

        result_label.config(text=result_text)

    except requests.exceptions.RequestException:
        result_label.config(text="Error connecting to the API.")



window = tk.Tk()
window.title("Fruit Search")
window.geometry("400x350")
window.resizable(False, False)

title = tk.Label(
    window,
    text="Fruit Nutrition Search",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

search_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=25
)
search_entry.pack(pady=10)

search_button = tk.Button(
    window,
    text="Search",
    font=("Arial", 12),
    width=12,
    command=search_fruit
)
search_button.pack(pady=10)

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    fg="blue",
    justify="left"
)
result_label.pack(pady=15)

window.mainloop()


























