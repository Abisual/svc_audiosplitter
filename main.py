import os
from pydub import AudioSegment
from tkinter import Tk, Button, Checkbutton, Entry, Label, messagebox, BooleanVar
from tkinter.filedialog import askopenfilenames, askdirectory

def validate_number(input_value):
    if not input_value:
        return False

    try:
        value = int(input_value)
        if value < 1:
            raise ValueError("The number must be greater than or equal to 1")
    except ValueError:
        return False

    return True

def select_files():
    filenames = askopenfilenames(title="Select audio files", filetypes=[("Audio Files", "*.mp3 *.wav *.ogg")])
    return filenames

def select_folder():
    folder = askdirectory(title="Select a folder to save")
    return folder

def split_audio(input_file, output_folder, chunk_duration, delete_input_files):
    audio = AudioSegment.from_file(input_file)
    duration = len(audio)
    chunk_size = int(chunk_duration) * 1000

    if duration <= chunk_size:
        output_file = os.path.join(output_folder, os.path.basename(input_file))
        audio.export(output_file, format="wav")
    else:
        num_chunks = duration // chunk_size
        remainder = duration % chunk_size

        for i in range(num_chunks):
            start_time = i * chunk_size
            end_time = start_time + chunk_size
            chunk = audio[start_time:end_time]

            output_file = os.path.join(output_folder, f"{os.path.basename(input_file)}_{i}.wav")
            chunk.export(output_file, format="wav")

        if remainder > 0:
            start_time = num_chunks * chunk_size
            end_time = start_time + remainder
            chunk = audio[start_time:end_time]

            output_file = os.path.join(output_folder, f"{os.path.basename(input_file)}_{num_chunks}.wav")
            chunk.export(output_file, format="wav")

    if delete_input_files and os.path.exists(input_file):
        os.remove(input_file)

def process_files():
    delete_input_files = delete_var.get()
    input_files = select_files()
    output_folder = select_folder()

    chunk_duration_value = chunk_duration.get()
    if not validate_number(chunk_duration_value):
        messagebox.showerror("Error", "Enter a valid number greater than or equal to 1")
        return

    for input_file in input_files:
        split_audio(input_file, output_folder, int(chunk_duration_value), delete_input_files)

        if delete_input_files and os.path.exists(input_file):
            os.remove(input_file)

    root.quit()

root = Tk()
root.title("Splitting audio files")

label_duration = Label(root, text="Fragment duration (in seconds):")
label_duration.grid(row=0, column=0, padx=10, pady=10)
chunk_duration = Entry(root)
chunk_duration.insert(0, "10")
chunk_duration.grid(row=0, column=1, padx=10, pady=10)

delete_var = BooleanVar()
delete_checkbox = Checkbutton(root, text="Delete Source files", variable=delete_var)
delete_checkbox.grid(row=1, column=0, columnspan=2)

process_button = Button(root, text="Process Files", command=process_files)
process_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()