import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import subprocess
import os

class ConversionThread(threading.Thread):
    def __init__(self, input_file, output_audio, language, output_mp4, optional_picture):
        threading.Thread.__init__(self)
        self.input_file = input_file
        self.output_audio = output_audio
        self.language = language
        self.output_mp4 = output_mp4
        self.optional_picture = optional_picture

    def run(self):
        try:
            # Mapping language codes to actual language names
            language_map = {
                "iw": "hebrew",
                "hi": "hindi"
            }

            # Constructing the command based on inputs
            output_dir = "/home/abasiscus/jinn/prompts/tts/finished"
            output_path = os.path.join(output_dir, self.output_mp4)
            
            command = f"python3 speak2.py -i {self.input_file} -o {self.output_audio} -l {self.language} && "
            command += f"ffmpeg -stream_loop 1 -i {self.optional_picture} -i {self.output_audio} "
            command += f"-c:v libx264 -preset fast -crf 22 -c:a aac -b:a 192k -t 5:00 -pix_fmt yuv420p -vf 'scale=1280:720' {self.output_mp4} && mv {self.output_mp4} {output_path}"
            
            # Running the command using subprocess
            subprocess.run(command, shell=True, check=True)
            messagebox.showinfo("Conversion Complete", "File conversion completed successfully.")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Conversion Tool")

        # Variables for input fields
        self.input_file_var = tk.StringVar()
        self.output_audio_var = tk.StringVar()
        self.language_var = tk.StringVar()
        self.output_mp4_var = tk.StringVar()
        self.optional_picture_var = tk.StringVar()

        self.language_options = {
            "Hebrew": "iw",
            "Hindi": "hi"
        }

        self.create_widgets()

    def browse_file(self, label_text, entry_var):
        filename = filedialog.askopenfilename()
        entry_var.set(filename)

    def create_conversion_thread(self):
        input_file = self.input_file_var.get()
        output_audio = self.output_audio_var.get()
        language = self.language_var.get()
        output_mp4 = self.output_mp4_var.get()
        optional_picture = self.optional_picture_var.get()

        if not input_file or not output_audio or not output_mp4 or not optional_picture:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Start a new thread for conversion
        conversion_thread = ConversionThread(input_file, output_audio, language, output_mp4, optional_picture)
        conversion_thread.start()

        # Show processing message
        self.show_processing_message()

    def show_processing_message(self):
        self.processing_label = tk.Label(self, text="Processing...", font=("Arial", 12, "italic"), fg="blue")
        self.processing_label.grid(row=6, column=1, pady=10)
        self.update_idletasks()  # Ensure the label is displayed immediately

    def create_widgets(self):
        # Input file
        tk.Label(self, text="Input File:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.input_file_var, width=50).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self, text="Browse", command=lambda: self.browse_file("Select Input File", self.input_file_var)).grid(row=0, column=2, padx=5, pady=5)

        # Output audio file
        tk.Label(self, text="Output Audio File:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.output_audio_var, width=50).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(self, text="Browse", command=lambda: self.browse_file("Select Output Audio File", self.output_audio_var)).grid(row=1, column=2, padx=5, pady=5)

        # Language option
        tk.Label(self, text="Language:").grid(row=2, column=0, padx=5, pady=5)
        language_dropdown = tk.OptionMenu(self, self.language_var, *self.language_options.values())
        language_dropdown.grid(row=2, column=1, padx=5, pady=5)
        self.language_var.set(self.language_options["Hebrew"])  # Default to Hebrew

        # Output MP4 file
        tk.Label(self, text="Output MP4 File:").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.output_mp4_var, width=50).grid(row=3, column=1, padx=5, pady=5)

        # Optional picture file
        tk.Label(self, text="Optional Picture File:").grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(self, textvariable=self.optional_picture_var, width=50).grid(row=4, column=1, padx=5, pady=5)
        tk.Button(self, text="Browse", command=lambda: self.browse_file("Select Optional Picture File", self.optional_picture_var)).grid(row=4, column=2, padx=5, pady=5)

        # Convert button
        tk.Button(self, text="Convert", command=self.create_conversion_thread).grid(row=5, column=1, pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()

