root = Tk()
root.title('YouTube Video Downloader')
root.geometry('1000x400')
root.resizable(0, 0)
root.config(bg='Red')


Label(root, text='YouTube Video Downloader', font=("Sans Serif", 15), bg='Red').place(relx=0.25, rely=0.0)


Label(root, text='Youtube video link:', font=("Times New Roman", 13), bg='Red').place(relx=0.05, rely=0.2)

link_strvar = StringVar(root)
link_entry = Entry(root, width=50, textvariable=link_strvar)
link_entry.place(relx=0.5, rely=0.2)


Label(root, text='Location to save the video to:', font=("Times New Roman", 13), bg='Red').place(relx=0.05, rely=0.4)

dir_strvar = StringVar(root)
dir_entry = Entry(root, width=50, textvariable=dir_strvar)
dir_entry.place(relx=0.5, rely=0.4)


Label(root, text='Enter the filename:', font=("Times New Roman", 13), bg='Red').place(relx=0.05, rely=0.6)

filename_strvar = StringVar(root)
filename_entry = Entry(root, width=50, textvariable=filename_strvar)
filename_entry.place(relx=0.5, rely=0.6)


download_button = Button(root, text='Download', font=7, bg='Red',
                      command=lambda: download(link_entry, dir_entry, filename_entry)).place(relx=0.3, rely=0.75)

reset_button = Button(root, text='Reset', font=7, bg='Aquamarine',
                   command=lambda: reset(link_strvar, dir_strvar, filename_strvar)).place(relx=0.5, rely=0.75)


root.update()
root.mainloop()
