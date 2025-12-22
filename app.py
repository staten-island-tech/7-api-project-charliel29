import requests
import tkinter as tk


def Fruit():
    y=search_entry.get()
    response = requests.get(f"https://www.fruityvice.com/api/fruit/{y}")
    if response.status_code!=200:
        print("Error fetching data!")
        return None
    data=response.json()
    return{
        "protein": data["nutritions"]["protein"],
        "sugar": data["nutritions"]["sugar"],
        "calories": data["nutritions"]['calories'],
        "fat": data["nutritions"]["fat"]
        }
    
result_label.comfig(text=data)
window = tk.Tk()
window.title("Fruit search") 
window.geometry("800x500") 
window.resizable(False, False)
prompt = tk.Label(window, text="What fruit would you like to search up?",
font=("Arial", 16))
prompt.pack(pady=10)
result_label = tk.Label(window, text="", font=("Arial", 14, "bold"),
fg="blue")
result_label.pack(pady=15)
search_entry = tk.Entry (window,font=("Arial", 14),width=30,)
search_entry.pack(pady=10,)
button = tk.Button(
window,text="Search",
width=15, height= 2,command=Fruit)
button.pack(pady=10)
window.mainloop()























































