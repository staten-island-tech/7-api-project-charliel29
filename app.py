import requests
import tkinter as tk


def amiibo():
    response = requests.get(f"https://www.amiiboapi.com/api/")
    if response.status_code!=200:
        print("Error fetching data!")
        return None
    data=response.json()
    return{

        "amiiboSeries" : data["amiiboSeries"],
        "character": data["character"],
		"gameSeries": data["gameSeries"],
		"type": data["type"],
        "image": data["image"],
    }


window = tk.Tk()
window.title("amiibo search") 
window.geometry("800x500") 
window.resizable(False, False)
prompt = tk.Label(window, text="What you want to find on ambiibo?",
font=("Arial", 16))
prompt.pack(pady=10)
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)
search_entry = tk.Entry (window,font=("Arial", 14),width=30,)
search_entry.pack(pady=10,)
tk.Button(
    window
    text="Submit",
    command=on_click,
    width=15,
    height=2,
    bg="lightblue",
    fg="black"
).pack()

window.mainloop()






















































