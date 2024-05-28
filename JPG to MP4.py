import tkinter as tk
from tkinter import filedialog
from imageio import get_writer, imread

def create_video():
    image_path = image_entry.get()
    duration = duration_entry.get()

    if not image_path or not duration:
        result_label.config(text='Please provide image and duration.')
        return

    try:
        dur = float(duration)
    except ValueError:
        result_label.config(text='Invalid duration value.')
        return

    save_path = filedialog.asksaveasfilename(defaultextension='.mp4')
    if not save_path:
        return

    try:
        fps = 25
        writer = get_writer(save_path, fps=fps)
        for _ in range(int(dur * fps)):
            image = imread(image_path)
            writer.append_data(image)
        writer.close()
        result_label.config(text='Video created successfully!')
    except Exception as e:
        result_label.config(text=f'Error: {str(e)}')


def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.png *.jpg *.jpeg')])
    if file_path:
        image_entry.delete(0, tk.END)
        image_entry.insert(tk.END, file_path)


root = tk.Tk()
root.title('JPG to MP4')
root.resizable(width=False, height=False)

try:
    #Ставим иконку для заголовка приложения
    root.iconbitmap(r'ico.ico')
except:
    #Если иконки в каталоге нет, то ничего не делаем
    pass

# Image selection
image_label = tk.Label(root, text='Image:')
image_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

image_entry = tk.Entry(root, width=30)
image_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = tk.Button(root, text='Browse', command=browse_image)
browse_button.grid(row=0, column=2, padx=5, pady=5)

# Duration input
duration_label = tk.Label(root, text='Duration (seconds):')
duration_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

duration_entry = tk.Entry(root, width=30)
duration_entry.grid(row=1, column=1, padx=5, pady=5)

# Create video button
create_button = tk.Button(root, text='Create Video', command=create_video)
create_button.grid(row=2, column=0, columnspan=3, padx=5, pady=10)

# Result label
result_label = tk.Label(root, text='')
result_label.grid(row=3, column=0, columnspan=3)

#Закрыть главное окно
def exit_root(event):
    root.quit()
#Закрыть главное окно и все дочерние окна через ESC
root.bind('<Escape>', exit_root)

root.mainloop()
