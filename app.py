import requests
import tkinter


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
window.geometry("400x250") 
window.resizable(False, False)
prompt = tk.Label(window, text="Type what you want to find on ambiibo below",
font=("Arial", 14))
prompt.pack(pady=10)
entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)
