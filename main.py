import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import Slider
import tkinter as tk
from tkinter import font as tkfont
from fractales import Fractals

class FractalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fractal Viewer")

        # Load custom font
        custom_font = tkfont.Font(family='HalfTerm.ttf', size=12)

        # Create a frame for the controls
        control_frame = tk.Frame(root)
        control_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        tk.Label(control_frame, text="Choose a Fractal:", font=custom_font).pack(side=tk.LEFT)
        self.fractal_var = tk.IntVar()
        self.fractal_var.set(1)

        fractals = [("Sierpinski", 1), ("Mandelbrot", 2), ("Julia", 3), ("Koch", 4), ("BurningShip", 5)]
        for text, value in fractals:
            tk.Radiobutton(control_frame, text=text, variable=self.fractal_var, value=value, font=custom_font, width=12, height=2).pack(side=tk.LEFT)
        
        tk.Button(control_frame, text="Draw", command=self.draw_fractal, font=custom_font, width=12, height=2).pack(side=tk.LEFT)

        self.slider_frame = tk.Frame(root)
        self.slider_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Create a frame for the plot
        self.plot_frame = tk.Frame(root)
        self.plot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def draw_fractal(self):
        figure = self.fractal_var.get()
        self.ax.clear()

        if figure == 1:
            # Sierpinski
            initial_level = 1
            points = np.array([
                [0, 0],
                [1, 0],
                [0.5, np.sqrt(3)/2]
            ])
            fractal = Fractals(fractal_type='sierpinski', order=initial_level, points=points)
            self.ax.clear()

            fractal.draw()
            self.canvas.draw()
            
            def update(val):
                level = int(self.slider.val)
                self.ax.clear()
                fractal.kwargs['order'] = level
                fractal.draw()
                self.canvas.draw()
                
            self.add_slider('Niveau', 0, 7, initial_level, update)

        elif figure == 2:
            # Mandelbrot
            xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
            width, height, max_iter = 1000, 1000, 256
            fractal = Fractals(fractal_type='mandelbrot', xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, width=width, height=height, max_iter=max_iter)
            fractal.draw()
            self.canvas.draw()

        elif figure == 3:
            # Julia
            xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5
            width, height, max_iter = 1000, 1000, 256
            c = complex(-0.7, 0.27015)
            fractal = Fractals(fractal_type='julia', c=c, xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, width=width, height=height, max_iter=max_iter)
            fractal.draw()
            self.canvas.draw()

        elif figure == 4:
            # Koch
            initial_level = 2
            fractal = Fractals(fractal_type='koch', order=initial_level)
            fractal.draw()

            def update(val):
                level = int(self.slider.val)
                self.ax.clear()
                fractal.kwargs['order'] = level
                # fractal.draw()
                self.canvas.draw()

            self.add_slider('Niveau', 0, 7, initial_level, update)

        elif figure == 5:
            # BurningShip
            xmin, xmax, ymin, ymax = -2.0, 1.0, -2.0, 1.0
            width, height, max_iter = 1000, 1000, 256
            fractal = Fractals(fractal_type='burning_ship', xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, width=width, height=height, max_iter=max_iter)
            fractal.draw()
            self.canvas.draw()

    def add_slider(self, label, vmin, vmax, valinit, update_func):
        for widget in self.slider_frame.winfo_children():
            widget.destroy()
        
        ax_slider = plt.axes([0.1, 0.1, 0.8, 0.06], facecolor='lightgoldenrodyellow')
        self.slider = Slider(ax_slider, label, vmin, vmax, valinit=valinit, valstep=1)
        self.slider.on_changed(update_func)
        self.fig.subplots_adjust(bottom=0.25)

        
if __name__ == "__main__":
    root = tk.Tk()
    app = FractalApp(root)
    root.mainloop()



# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.widgets import Slider
# import tkinter as tk
# from tkinter import font as tkfont
# from fractales import Fractals

# class FractalApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Fractal Viewer")

#         # Load custom font
#         custom_font = tkfont.Font(family='HalfTerm.ttf', size=12)

#         # Create a frame for the controls
#         control_frame = tk.Frame(root)
#         control_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#         tk.Label(control_frame, text="Choose a Fractal:", font=custom_font).pack(side=tk.LEFT)
#         self.fractal_var = tk.IntVar()
#         self.fractal_var.set(1)

#         fractals = [("Sierpinski", 1), ("Mandelbrot", 2), ("Julia", 3), ("Koch", 4), ("BurningShip", 5)]
#         for text, value in fractals:
#             tk.Radiobutton(control_frame, text=text, variable=self.fractal_var, value=value, font=custom_font, width=12, height=2).pack(side=tk.LEFT)
        
#         tk.Button(control_frame, text="Draw", command=self.draw_fractal, font=custom_font, width=12, height=2).pack(side=tk.LEFT)

#         self.slider_frame = tk.Frame(root)
#         self.slider_frame.pack(side=tk.BOTTOM, fill=tk.X)

#         # Create a frame for the plot
#         self.plot_frame = tk.Frame(root)
#         self.plot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
#         self.fig, self.ax = plt.subplots()
#         self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
#         self.canvas.draw()
#         self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#     def draw_fractal(self):
#         figure = self.fractal_var.get()
#         self.ax.clear()
        
#         if figure == 1:
#             # Sierpinski
#             initial_level = 1
#             points = np.array([
#                 [0, 0],
#                 [1, 0],
#                 [0.5, np.sqrt(3)/2]
#             ])
#             fractal = Fractals(fractal_type='sierpinski', order=initial_level, points=points)
            
#             fractal.draw()
#             self.ax.set_position([0.1, 0.1, 0.8, 0.8])  # Adjust the position of the fractal display
#             self.canvas.draw()
            
#             def update(val):
#                 level = int(self.slider.val)
#                 self.ax.clear()
#                 fractal.kwargs['order'] = level
#                 fractal.draw()
#                 self.ax.set_position([0.1, 0.1, 0.8, 0.8])  # Adjust the position again after updating
#                 self.canvas.draw()
                
#             self.add_slider('Niveau', 0, 7, initial_level, update)

#         elif figure == 2:
#             # Mandelbrot
#             xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
#             width, height, max_iter = 1000, 1000, 256
#             fractal = Fractals(fractal_type='mandelbrot', xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, width=width, height=height, max_iter=max_iter)
#             fractal.draw()
#             self.canvas.draw()

#         elif figure == 3:
#             # Julia
#             xmin, xmax, ymin, ymax = -1.5, 1.5, -1.5, 1.5
#             width, height, max_iter = 1000, 1000, 256
#             c = complex(-0.7, 0.27015)
#             fractal = Fractals(fractal_type='julia', c=c, xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, width=width, height=height, max_iter=max_iter)
#             fractal.draw()
#             self.canvas.draw()

#         elif figure == 4:
#             # Koch
#             initial_level = 2
#             fractal = Fractals(fractal_type='koch', order=initial_level)
#             fractal.draw()

#             def update(val):
#                 level = int(self.slider.val)
#                 self.ax.clear()
#                 fractal.kwargs['order'] = level
#                 fractal.draw()
#                 self.ax.set_position([0.1, 0.1, 0.8, 0.8])  # Adjust the position again after updating
#                 self.canvas.draw()

#             self.add_slider('Niveau', 0, 7, initial_level, update)

#         elif figure == 5:
#             # BurningShip
#             xmin, xmax, ymin, ymax = -2.0, 1.0, -2.0, 1.0
#             width, height, max_iter = 1000, 1000, 256
#             fractal = Fractals(fractal_type='burning_ship', xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax, width=width, height=height, max_iter=max_iter)
#             fractal.draw()
#             self.canvas.draw()

#     def add_slider(self, label, vmin, vmax, valinit, update_func):
#         for widget in self.slider_frame.winfo_children():
#             widget.destroy()
        
#         ax_slider = plt.axes([0.1, 0.1, 0.8, 0.06], facecolor='lightgoldenrodyellow')
#         self.slider = Slider(ax_slider, label, vmin, vmax, valinit=valinit, valstep=1)
#         self.slider.on_changed(update_func)
#         self.fig.subplots_adjust(bottom=0.50)


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FractalApp(root)
#     root.mainloop()
