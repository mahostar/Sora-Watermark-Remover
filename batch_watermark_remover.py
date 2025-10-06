import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import subprocess
import threading
from pathlib import Path
import queue

class WatermarkRemoverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Batch Watermark Remover - AI Powered")
        self.root.geometry("900x700")
        self.root.configure(bg="#1e1e1e")
        
        # Video list
        self.video_paths = []
        self.output_folder = ""
        self.processing = False
        self.log_queue = queue.Queue()
        
        self.create_ui()
        self.check_log_queue()
        
    def create_ui(self):
        # Title
        title = tk.Label(
            self.root, 
            text="🎬 Batch Watermark Remover", 
            font=("Arial", 24, "bold"),
            bg="#1e1e1e", 
            fg="#00ff88"
        )
        title.pack(pady=20)
        
        # Drag & Drop Area
        drop_frame = tk.Frame(self.root, bg="#2d2d2d", relief="groove", bd=3)
        drop_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        drop_label = tk.Label(
            drop_frame,
            text="📁 Drag & Drop MP4 Videos Here\n(or click to browse)",
            font=("Arial", 16),
            bg="#2d2d2d",
            fg="#ffffff",
            cursor="hand2"
        )
        drop_label.pack(expand=True, fill="both", pady=50)
        drop_label.bind("<Button-1>", self.browse_videos)
        
        # Enable drag and drop
        drop_frame.drop_target_register(DND_FILES)
        drop_frame.dnd_bind('<<Drop>>', self.drop_files)
        
        # Video List Display
        list_frame = tk.Frame(self.root, bg="#1e1e1e")
        list_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        tk.Label(
            list_frame,
            text="Videos Queue:",
            font=("Arial", 12, "bold"),
            bg="#1e1e1e",
            fg="#00ff88"
        ).pack(anchor="w")
        
        # Scrollable listbox
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.video_listbox = tk.Listbox(
            list_frame,
            font=("Consolas", 10),
            bg="#2d2d2d",
            fg="#ffffff",
            selectbackground="#00ff88",
            selectforeground="#000000",
            yscrollcommand=scrollbar.set,
            height=8
        )
        self.video_listbox.pack(fill="both", expand=True)
        scrollbar.config(command=self.video_listbox.yview)
        
        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#1e1e1e")
        btn_frame.pack(pady=10, padx=20, fill="x")
        
        # Clear button
        self.clear_btn = tk.Button(
            btn_frame,
            text="🗑️ Clear List",
            font=("Arial", 11, "bold"),
            bg="#ff4444",
            fg="white",
            command=self.clear_list,
            cursor="hand2",
            relief="raised",
            bd=2
        )
        self.clear_btn.pack(side="left", padx=5)
        
        # Output folder button
        self.output_btn = tk.Button(
            btn_frame,
            text="📂 Select Output Folder",
            font=("Arial", 11, "bold"),
            bg="#4444ff",
            fg="white",
            command=self.select_output_folder,
            cursor="hand2",
            relief="raised",
            bd=2
        )
        self.output_btn.pack(side="left", padx=5)
        
        # Output folder label
        self.output_label = tk.Label(
            btn_frame,
            text="No output folder selected",
            font=("Arial", 10),
            bg="#1e1e1e",
            fg="#ffaa00"
        )
        self.output_label.pack(side="left", padx=10)
        
        # Run button
        self.run_btn = tk.Button(
            btn_frame,
            text="▶️ START PROCESSING",
            font=("Arial", 14, "bold"),
            bg="#00ff88",
            fg="#000000",
            command=self.start_processing,
            cursor="hand2",
            relief="raised",
            bd=3,
            width=20
        )
        self.run_btn.pack(side="right", padx=5)
        
        # Progress Frame
        progress_frame = tk.Frame(self.root, bg="#1e1e1e")
        progress_frame.pack(pady=10, padx=20, fill="x")
        
        self.progress_label = tk.Label(
            progress_frame,
            text="Ready to process videos",
            font=("Arial", 11),
            bg="#1e1e1e",
            fg="#ffffff"
        )
        self.progress_label.pack()
        
        self.progress_bar = ttk.Progressbar(
            progress_frame,
            mode="determinate",
            length=800
        )
        self.progress_bar.pack(pady=5)
        
        # Log area
        log_frame = tk.Frame(self.root, bg="#1e1e1e")
        log_frame.pack(pady=5, padx=20, fill="both", expand=True)
        
        tk.Label(
            log_frame,
            text="Processing Log:",
            font=("Arial", 10, "bold"),
            bg="#1e1e1e",
            fg="#00ff88"
        ).pack(anchor="w")
        
        log_scroll = tk.Scrollbar(log_frame)
        log_scroll.pack(side="right", fill="y")
        
        self.log_text = tk.Text(
            log_frame,
            font=("Consolas", 9),
            bg="#0d0d0d",
            fg="#00ff00",
            height=6,
            yscrollcommand=log_scroll.set
        )
        self.log_text.pack(fill="both", expand=True)
        log_scroll.config(command=self.log_text.yview)
        
    def drop_files(self, event):
        files = self.root.tk.splitlist(event.data)
        for file_path in files:
            file_path = file_path.strip('{}')
            if file_path.lower().endswith('.mp4'):
                if file_path not in self.video_paths:
                    self.video_paths.append(file_path)
                    self.video_listbox.insert(tk.END, file_path)
                    self.log(f"Added: {os.path.basename(file_path)}")
            else:
                self.log(f"Skipped (not MP4): {os.path.basename(file_path)}", "warning")
    
    def browse_videos(self, event=None):
        files = filedialog.askopenfilenames(
            title="Select MP4 Videos",
            filetypes=[("MP4 Videos", "*.mp4"), ("All Files", "*.*")]
        )
        for file_path in files:
            if file_path not in self.video_paths:
                self.video_paths.append(file_path)
                self.video_listbox.insert(tk.END, file_path)
                self.log(f"Added: {os.path.basename(file_path)}")
    
    def clear_list(self):
        if not self.processing:
            self.video_paths.clear()
            self.video_listbox.delete(0, tk.END)
            self.log("Video list cleared")
    
    def select_output_folder(self):
        folder = filedialog.askdirectory(title="Select Output Folder")
        if folder:
            self.output_folder = folder
            self.output_label.config(text=f"Output: {folder}", fg="#00ff88")
            self.log(f"Output folder set: {folder}")
    
    def log(self, message, level="info"):
        self.log_queue.put((message, level))
    
    def check_log_queue(self):
        try:
            while True:
                message, level = self.log_queue.get_nowait()
                color_tag = "info" if level == "info" else "warning" if level == "warning" else "error"
                
                self.log_text.tag_config("info", foreground="#00ff00")
                self.log_text.tag_config("warning", foreground="#ffaa00")
                self.log_text.tag_config("error", foreground="#ff4444")
                
                self.log_text.insert(tk.END, f"[{level.upper()}] {message}\n", color_tag)
                self.log_text.see(tk.END)
        except queue.Empty:
            pass
        
        self.root.after(100, self.check_log_queue)
    
    def start_processing(self):
        if self.processing:
            messagebox.showwarning("Processing", "Already processing videos!")
            return
        
        if not self.video_paths:
            messagebox.showerror("Error", "No videos added! Drag & drop some MP4 files first.")
            return
        
        if not self.output_folder:
            messagebox.showerror("Error", "No output folder selected!")
            return
        
        # Create output folder if it doesn't exist
        os.makedirs(self.output_folder, exist_ok=True)
        
        # Start processing in separate thread
        self.processing = True
        self.run_btn.config(state="disabled", bg="#666666")
        self.clear_btn.config(state="disabled")
        self.output_btn.config(state="disabled")
        
        thread = threading.Thread(target=self.process_videos, daemon=True)
        thread.start()
    
    def process_videos(self):
        total = len(self.video_paths)
        success_count = 0
        
        for idx, video_path in enumerate(self.video_paths, 1):
            try:
                # Update progress
                progress = (idx / total) * 100
                self.progress_bar['value'] = progress
                
                video_name = os.path.basename(video_path)
                base_name = os.path.splitext(video_name)[0]
                output_path = os.path.join(self.output_folder, f"{base_name}_no_watermark.mp4")
                
                self.log(f"Processing ({idx}/{total}): {video_name}")
                self.progress_label.config(text=f"Processing: {video_name} ({idx}/{total})")
                
                # Run remwm.py using venv Python
                venv_python = os.path.join(os.path.dirname(os.path.abspath(__file__)), "venv", "Scripts", "python.exe")
                cmd = [
                    venv_python,
                    "remwm.py",
                    video_path,
                    output_path,
                    "--overwrite"
                ]
                
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    cwd=os.path.dirname(os.path.abspath(__file__))
                )
                
                if result.returncode == 0:
                    self.log(f"✅ SUCCESS: {video_name} → {os.path.basename(output_path)}")
                    success_count += 1
                else:
                    self.log(f"❌ FAILED: {video_name} - {result.stderr[:100]}", "error")
                    
            except Exception as e:
                self.log(f"❌ ERROR: {video_name} - {str(e)}", "error")
        
        # Finish
        self.progress_bar['value'] = 100
        self.progress_label.config(text=f"✅ DONE! Processed {success_count}/{total} videos successfully")
        self.log(f"\n{'='*50}")
        self.log(f"BATCH PROCESSING COMPLETE!")
        self.log(f"Success: {success_count}/{total}")
        self.log(f"Output folder: {self.output_folder}")
        self.log(f"{'='*50}\n")
        
        # Re-enable buttons
        self.processing = False
        self.run_btn.config(state="normal", bg="#00ff88")
        self.clear_btn.config(state="normal")
        self.output_btn.config(state="normal")
        
        # Show completion message
        messagebox.showinfo(
            "Complete!",
            f"Processing finished!\n\nSuccess: {success_count}/{total}\nOutput: {self.output_folder}"
        )

if __name__ == "__main__":
    try:
        root = TkinterDnD.Tk()
        app = WatermarkRemoverGUI(root)
        root.mainloop()
    except Exception as e:
        # Fallback if tkinterdnd2 not available
        print(f"Error: {e}")
        print("\nInstalling tkinterdnd2...")
        subprocess.run(["pip", "install", "tkinterdnd2"])
        print("\nPlease run the script again!")