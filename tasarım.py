import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps, ImageEnhance
import cv2

class PhotoshopClone:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Design Studio")
        self.root.geometry("1000x700")

        self.image = None
        self.tk_image = None
        self.canvas = tk.Canvas(self.root, bg="#2c3e50")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.setup_ui()

    def setup_ui(self):
        menubar = tk.Menu(self.root)
        
        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Image", command=self.load_image)
        file_menu.add_command(label="Import Video Frame", command=self.load_video_frame)
        file_menu.add_command(label="Save As...", command=self.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Edit Menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Grayscale", command=lambda: self.apply_filter("grayscale"))
        edit_menu.add_command(label="Invert Colors", command=lambda: self.apply_filter("invert"))
        edit_menu.add_command(label="Brightness +20%", command=lambda: self.apply_filter("brightness"))
        menubar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menubar)

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")])
        if path:
            self.image = Image.open(path)
            self.render_canvas()

    def load_video_frame(self):
        path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
        if path:
            cap = cv2.VideoCapture(path)
            success, frame = cap.read()
            if success:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.image = Image.fromarray(frame)
                self.render_canvas()
            cap.release()

    def save_image(self):
        if self.image:
            path = filedialog.asksaveasfilename(defaultextension=".png", 
                                               filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
            if path:
                self.image.save(path)
        else:
            messagebox.showwarning("Warning", "Nothing to save.")

    def apply_filter(self, filter_type):
        if not self.image: return
        
        if filter_type == "grayscale":
            self.image = ImageOps.grayscale(self.image).convert("RGB")
        elif filter_type == "invert":
            self.image = ImageOps.invert(self.image.convert("RGB"))
        elif filter_type == "brightness":
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(1.2)
        
        self.render_canvas()

    def render_canvas(self):
        if self.image:
            # Resize for preview while maintaining aspect ratio
            display_size = (self.root.winfo_width() - 50, self.root.winfo_height() - 50)
            preview_img = self.image.copy()
            preview_img.thumbnail(display_size, Image.Resampling.LANCZOS)
            
            self.tk_image = ImageTk.PhotoImage(preview_img)
            self.canvas.delete("all")
            self.canvas.create_image(
                self.root.winfo_width()//2, 
                self.root.winfo_height()//2, 
                image=self.tk_image
            )

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoshopClone(root)
    root.mainloop()
import numpy as np
from PIL import ImageDraw

class PhotoshopClone:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Design Studio")
        self.root.geometry("1000x700")

        self.layers = []  # List of PIL Image objects (RGBA)
        self.current_layer_idx = -1
        self.brush_size = 5
        self.brush_color = "black"
        self.last_x, self.last_y = None, None

        self.canvas = tk.Canvas(self.root, bg="#2c3e50")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_coords)

        self.setup_ui()

    def setup_ui(self):
        menubar = tk.Menu(self.root)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Image", command=self.load_image)
        file_menu.add_command(label="New Layer", command=self.add_empty_layer)
        file_menu.add_command(label="Save As...", command=self.save_image)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Remove Background", command=self.remove_background)
        edit_menu.add_command(label="Grayscale", command=lambda: self.apply_filter("grayscale"))
        menubar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menubar)

    def add_empty_layer(self):
        if self.layers:
            size = self.layers[0].size
            new_layer = Image.new("RGBA", size, (0, 0, 0, 0))
            self.layers.append(new_layer)
            self.current_layer_idx = len(self.layers) - 1

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.png *.jpeg")])
        if path:
            img = Image.open(path).convert("RGBA")
            self.layers = [img]
            self.current_layer_idx = 0
            self.render_canvas()

    def paint(self, event):
        if self.current_layer_idx == -1: return
        
        draw = ImageDraw.Draw(self.layers[self.current_layer_idx])
        if self.last_x and self.last_y:
            draw.line([self.last_x, self.last_y, event.x, event.y], 
                      fill=self.brush_color, width=self.brush_size)
        
        self.last_x, self.last_y = event.x, event.y
        self.render_canvas()

    def reset_coords(self, event):
        self.last_x, self.last_y = None, None

    def remove_background(self):
        if self.current_layer_idx == -1: return
        
        # Convert PIL to OpenCV
        img = np.array(self.layers[self.current_layer_idx].convert("RGB"))
        mask = np.zeros(img.shape[:2], np.uint8)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
        
        rect = (10, 10, img.shape[1]-10, img.shape[0]-10)
        cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        img_fg = img * mask2[:, :, np.newaxis]
        
        # Create RGBA result
        tmp = cv2.cvtColor(img_fg, cv2.COLOR_RGB2RGBA)
        tmp[:, :, 3] = mask2 * 255
        self.layers[self.current_layer_idx] = Image.fromarray(tmp)
        self.render_canvas()

    def render_canvas(self):
        if not self.layers: return
        
        # Composite all layers
        composite = Image.new("RGBA", self.layers[0].size, (0, 0, 0, 0))
        for layer in self.layers:
            composite = Image.alpha_composite(composite, layer)
            
        self.tk_image = ImageTk.PhotoImage(composite)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

    def save_image(self):
        if self.layers:
            path = filedialog.asksaveasfilename(defaultextension=".png")
            if path:
                composite = Image.new("RGBA", self.layers[0].size, (0, 0, 0, 0))
                for layer in self.layers:
                    composite = Image.alpha_composite(composite, layer)
                composite.save(path)
