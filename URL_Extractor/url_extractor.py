import tkinter as tk
from tkinter import messagebox
import requests as rq
from bs4 import BeautifulSoup


class URLExtractor:
    """
    Input the webpage URL
    Extract the webpage internal URL's
    Save the results in mylinks.txt file
    Display the results on GUI
    """
    def __init__(self, master):

        self.master = master
        self.master.title = "Link Extractor"

        def clicked():

            url = txt.get()
            try:
                if ("https" or "http") in url:
                    data = rq.get(url)
                else:
                    data = rq.get("https://" + url)
                soup = BeautifulSoup(data.text, "html.parser")
                links = []
                for link in soup.find_all("a"):
                    links.append(link.get("href"))

                with open("myLinks.txt", 'w') as saved:
                    print(links[:10], file=saved)

                listBox = tk.Text(master, width=100,height = 10)

                for i in range(10):
                    listBox.insert(tk.END, (i + 1))
                    listBox.insert(tk.END, "|")
                    listBox.insert(tk.END, links[i])
                    listBox.insert(tk.END, "\n")

                listBox.pack()

            except Exception  as e:
                messagebox.showerror(title='URL Error', message= "Invalid URL!!", parent=master)

        btn = tk.Button(window, text="Click To Extract",
                        bg="powder blue",
                        font=('arial', 15, 'bold'),
                        anchor = tk.S,
                        justify = tk.CENTER,
                        command=clicked)
        btn.pack()


if __name__ == '__main__':

    window = tk.Tk()
    w = '600'
    h = '800'

    #Frame Setup
    window.geometry('{}x{}'.format(w, h))
    window.title("Link Extract Program")
    window.configure(bg='powder blue')

    # Empty Label For Spacing
    empty_label = tk.Label(window, text=" ",
                           bg = "powder blue",
                           bd=10)
    empty_label.pack()

    #Title Label
    title_label = tk.Label(window, text = "Link Extractor",
                           bd = 1,
                           font = ('Anton', '24', 'bold'),
                           relief = "solid")
    title_label.pack()

    input_label = tk.Label(window, text="Enter WebPage URL Below ",
                           bg = "powder blue",
                           bd=40,
                           font = ('arial', 15, 'bold'),
                           anchor=tk.S,
                           justify=tk.CENTER)
    input_label.pack()

    txt = tk.Entry(window,width = 50)
    txt.pack()

    # Empty Label For Spacing
    empty_label = tk.Label(window, text=" ",
                           bg = "powder blue",
                           bd=10)
    empty_label.pack()

    gui = URLExtractor(window)
    window.mainloop()