from tkinter import (Tk, messagebox, Text, Toplevel, StringVar, Frame, DoubleVar, IntVar, filedialog,
                     INSERT, BOTH, END, X, LEFT)
from tkinter.ttk import Style, Button, Label, Entry, OptionMenu, Checkbutton

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import sympy as sp

from KeyboardModule import KeyboardModule
from MenuModule import MenuModule


# Функція для перетворення комплексного числа в дійсне число
def complex_to_float(complex_number):
    real_part, imag_part = complex_number.as_real_imag()
    if imag_part != 0:
        return None  # Повертаємо None для пропуску цього числа
    return float(real_part)


# Функція для збереження редагованого графіка
def save_plot_as_png(figure):
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        try:
            figure.savefig(file_path)
            messagebox.showinfo("Зберегти в PNG", f"PNG файл збережено в: {file_path}")
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося зберегти PNG файл: {e}")


class MathAnalyzerApp:
    def __init__(self, root):
        # Ініцілізація програми
        self.root = root
        self.root.title("Інтерактивний інструмент для аналізу математичних функцій")
        self.root.resizable(False, False)
        self.root.configure(bg="lightblue")

        # Створення стилю
        self.style = Style()
        # Стиль заголовнів
        self.style.configure("Custom.TLabel",
                             font=("Comic Sans MS", 12, "bold"),
                             background="lightblue",
                             foreground="black")
        # Стиль кнопок
        self.style.configure("Custom.TButton", font=("Comic Sans MS", 12, "bold"), padding=2)
        self.style.map("Custom.TButton",
                       foreground=[('pressed', 'red'), ('active', 'black')],
                       background=[('pressed', 'black'), ('active', 'lightblue')])
        # Стиль прапорців
        self.style.configure("Custom.TCheckbutton", font=("Comic Sans MS", 10, "bold"), background="lightblue")
        self.style.map("Custom.TCheckbutton",
                       foreground=[('active', 'red'), ('disabled', 'black')],
                       background=[('active', 'lightblue'), ('disabled', 'lightblue')])
        # Стиль спискових меню
        self.style.configure("Custom.TMenubutton", font=("Comic Sans MS", 10, "bold"), background="lightblue")
        self.style.map("Custom.TMenubutton",
                       foreground=[('active', 'red'), ('disabled', 'black')],
                       background=[('active', 'lightblue'), ('disabled', 'lightblue')])

        # Меню додатка
        self.menu = MenuModule(self.root, self)

        # Введення математичної функції
        # Це заголовок
        self.function_label = Label(self.root, text="Математична функція:", style="Custom.TLabel")
        self.function_label.grid(row=0, column=0, columnspan=8)
        # А це поле для введення
        self.function_entry = Entry(self.root, width=72, font=("Comic Sans MS", 12, "italic"))
        self.function_entry.grid(row=1, column=1, columnspan=6)

        # Кнопки для переміщення курсора в ліво та в право
        self.cursor_left = Button(self.root, text="⭠", command=self.move_cursor_left, style="Custom.TButton")
        self.cursor_left.grid(row=1, column=0)
        self.cursor_right = Button(self.root, text="⭢", command=self.move_cursor_right, style="Custom.TButton")
        self.cursor_right.grid(row=1, column=7)

        # Кнопка для побудови графіка
        self.plot_button = Button(self.root, text="Побудувати графік", command=self.plot_function,
                                  style="Custom.TButton")
        self.plot_button.grid(row=2, column=0, columnspan=2)

        # Прапорці критичних точок та асимптот
        self.is_critical_points = IntVar(value=0)
        self.check_critical_points = Checkbutton(self.root, text="Критичні точки", variable=self.is_critical_points,
                                                 style="Custom.TCheckbutton")
        self.check_critical_points.grid(row=2, column=2)
        self.is_asymptote = IntVar(value=0)
        self.check_asymptote = Checkbutton(self.root, text="Асимптоти", variable=self.is_asymptote,
                                           style="Custom.TCheckbutton")
        self.check_asymptote.grid(row=2, column=3)

        # Вибір операції
        self.operation_label = Label(self.root, text="Вибір операції:", style="Custom.TLabel")
        self.operation_label.grid(row=2, column=5)
        # Спискове меню для вибору
        self.operations = ["Вибрати", "Нулі", "Похідна", "Інтеграл", "x-перетини", "y-перетини", "Арфм. вираз"]
        self.operation_var = StringVar(value=self.operations[0])
        self.operation_menu = OptionMenu(self.root, self.operation_var, *self.operations, style="Custom.TMenubutton")
        self.operation_menu.grid(row=2, column=6)

        # Кнопка для виконання операції
        self.calculate_button = Button(self.root, text="Виконати", command=self.calculate_operation,
                                       style="Custom.TButton")
        self.calculate_button.grid(row=2, column=7)

        # Клавіатура додатка
        self.keyboard = KeyboardModule(self.root, self.function_entry)

    # Функція для переміщення курсора в ліво
    def move_cursor_left(self):
        current_pos = self.function_entry.index(INSERT)
        if current_pos > 0:
            self.function_entry.icursor(current_pos - 1)

    # Функція для переміщення курсора в право
    def move_cursor_right(self):
        current_pos = self.function_entry.index(INSERT)
        if current_pos < len(self.function_entry.get()):
            self.function_entry.icursor(current_pos + 1)

    # Функція для побудови графіка
    def plot_function(self):
        function_str = self.function_entry.get()
        try:
            function = sp.sympify(function_str)
            function_symbols = function.free_symbols

            if len(function_symbols) != 1:
                messagebox.showerror("Помилка", "Функція повинна мати одну змінну для побудови графіка.")
                return

            variable = list(function_symbols)[0]
            f_lambdified = sp.lambdify(variable, function, 'numpy')
            x_vals = np.linspace(-10, 10, 400)
            y_vals = f_lambdified(x_vals)

            # Створення графіка
            figure = Figure(figsize=(6, 4), dpi=100)
            ax = figure.add_subplot(111)
            ax.plot(x_vals, y_vals, label=f"f({variable}) = {function_str}")

            # Додавання критичних точок
            if self.is_critical_points.get():
                derivative = sp.diff(function, variable)
                critical_points = sp.solve(derivative, variable)
                for point in critical_points:
                    point_float = complex_to_float(point)
                    if point_float is not None:
                        y_val = function.subs(variable, point_float)
                        y_val_float = complex_to_float(y_val)
                        if y_val_float is not None:
                            ax.plot(point_float, y_val_float, 'ro')  # Червона точка
                            ax.annotate(f'({point_float}, {y_val_float})', (point_float, y_val_float))

            # Додавання асимптот
            if self.is_asymptote.get():
                vertical_asymptotes = sp.solve(sp.denom(function), variable)
                for v_asymptote in vertical_asymptotes:
                    try:
                        v_asymptote_float = complex_to_float(v_asymptote)
                        if v_asymptote_float is not None:
                            ax.axvline(v_asymptote_float, color='g', linestyle='--')
                            ax.annotate(f'x = {v_asymptote_float}', (v_asymptote_float, 0))
                    except Exception as e:
                        print(f"Помилка при обробці вертикальної асимптоти: {e}")

                # Перевірка на горизонтальні асимптоти
                horizontal_asymptote_pos_inf = sp.limit(function, variable, sp.oo)
                horizontal_asymptote_neg_inf = sp.limit(function, variable, -sp.oo)

                try:
                    horizontal_asymptote_pos_inf_float = complex_to_float(horizontal_asymptote_pos_inf)
                    if horizontal_asymptote_pos_inf_float is not None:
                        ax.axhline(horizontal_asymptote_pos_inf_float, color='b', linestyle='--')
                        ax.annotate(f'y = {horizontal_asymptote_pos_inf_float}',
                                    (0, horizontal_asymptote_pos_inf_float))
                except Exception as e:
                    print(f"Помилка при обробці горизонтальної асимптоти (+inf): {e}")

                try:
                    horizontal_asymptote_neg_inf_float = complex_to_float(horizontal_asymptote_neg_inf)
                    if (horizontal_asymptote_neg_inf_float is not None
                            and horizontal_asymptote_neg_inf_float != horizontal_asymptote_pos_inf_float):
                        ax.axhline(horizontal_asymptote_neg_inf_float, color='b', linestyle='--')
                        ax.annotate(f'y = {horizontal_asymptote_neg_inf_float}',
                                    (0, horizontal_asymptote_neg_inf_float))
                except Exception as e:
                    print(f"Помилка при обробці горизонтальної асимптоти (-inf): {e}")

            ax.legend()
            ax.grid(True)

            # Створення нового вікна для графіка
            graph_window = Toplevel(self.root, bg="lightblue")
            graph_window.title("Графік функції")

            # Малювання графіка
            canvas = FigureCanvasTkAgg(figure, master=graph_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=BOTH, expand=True)

            # Створення елементів управління для масштабу та анотацій
            control_frame = Frame(graph_window, bg="lightblue")
            control_frame.pack(fill=X, padx=5, pady=5)

            # Масштабування (елементи управління)
            scale_label = Label(control_frame, text="Масштаб:", style="Custom.TLabel")
            scale_label.pack(side=LEFT, padx=5)
            self.scale_var = DoubleVar(value=1.0)
            scale_entry = Entry(control_frame, textvariable=self.scale_var, width=3,
                                font=("Comic Sans MS", 12, "italic"))
            scale_entry.pack(side=LEFT, padx=5)
            scale_button = Button(control_frame, text="Застосувати", command=lambda: self.update_scale(ax, canvas),
                                  style="Custom.TButton")
            scale_button.pack(side=LEFT, padx=5)

            # Анотації (елементи управління)
            annotation_label = Label(control_frame, text="Анотація:", style="Custom.TLabel")
            annotation_label.pack(side=LEFT, padx=5)
            self.annotation_var = StringVar()
            annotation_entry = Entry(control_frame, textvariable=self.annotation_var, width=15,
                                     font=("Comic Sans MS", 12, "italic"))
            annotation_entry.pack(side=LEFT, padx=5)
            x_label = Label(control_frame, text="x:", style="Custom.TLabel")
            x_label.pack(side=LEFT, padx=5)
            self.x_annotation_var = IntVar(value=0)
            x_annotation_entry = Entry(control_frame, textvariable=self.x_annotation_var, width=3,
                                       font=("Comic Sans MS", 12, "italic"))
            x_annotation_entry.pack(side=LEFT, padx=5)
            y_label = Label(control_frame, text="y:", style="Custom.TLabel")
            y_label.pack(side=LEFT, padx=5)
            self.y_annotation_var = IntVar(value=0)
            y_annotation_entry = Entry(control_frame, textvariable=self.y_annotation_var, width=3,
                                       font=("Comic Sans MS", 12, "italic"))
            y_annotation_entry.pack(side=LEFT, padx=5)
            annotation_button = Button(control_frame, text="Додати", command=lambda: self.add_annotation(ax, canvas),
                                       style="Custom.TButton")
            annotation_button.pack(side=LEFT, padx=5)

            # Зберегти графік як PNG
            save_png_button = Button(control_frame, text="Зберегти як PNG",
                                     command=lambda: save_plot_as_png(figure), style="Custom.TButton")
            save_png_button.pack(side=LEFT, padx=5)

        except Exception as e:
            messagebox.showerror("Помилка", f"Неможливо обробити функцію: {e}")

    # Функція для маштабування
    def update_scale(self, ax, canvas):
        try:
            scale = float(self.scale_var.get())
            ax.set_xlim(-10 * scale, 10 * scale)
            ax.set_ylim(-10 * scale, 10 * scale)
            canvas.draw()

        except ValueError:
            messagebox.showerror("Помилка", "Неправильне значення масштабу")

    # Функція для додавання анотацій
    def add_annotation(self, ax, canvas):
        annotation = self.annotation_var.get()
        if annotation:
            ax.annotate(annotation, xy=(self.x_annotation_var.get(), self.y_annotation_var.get()), xytext=(5, 5),
                        textcoords='offset points', arrowprops=dict(arrowstyle='->'))
            canvas.draw()

    # Функція для обчислення операцій
    def calculate_operation(self):
        function_str = self.function_entry.get()
        operation = self.operation_var.get()
        x, y, z = sp.symbols('x y z')
        try:
            function = sp.sympify(function_str)
            result = ""
            is_full = False

            # Піревірка яку функцію виконувати
            if operation == "Нулі":
                result = sp.solve(function, (x, y, z))
            elif operation == "Похідна":
                result = sp.diff(function, x)
            elif operation == "Інтеграл":
                result = sp.integrate(function, x)
            elif operation == "x-перетини":
                result = sp.solve(function, x)
            elif operation == "y-перетини":
                result = function.subs(x, 0)
            elif operation == "Арфм. вираз":
                result = function.evalf()
            else:
                is_full = True
                result += f"Нулі функції:\n{sp.solve(function, (x, y, z))}"
                result += f"\nПохідна функції:\n{sp.diff(function, x)}"
                result += f"\nІнтеграл функції:\n{sp.integrate(function, x)}"
                result += f"\nx-перетини функції:\n{sp.solve(function, x)}"
                result += f"\ny-перетини функції:\n{function.subs(x, 0)}"
                result += f"\nАрфм. вираз функції:\n{function.evalf()}"

            # Створення нового вікна для відображення операції
            operation_window = Toplevel(self.root, bg="lightblue")
            operation_window.title(f"{operation} функції")

            # Введення результатів
            result_text = Text(operation_window, font=("Comic Sans MS", 12, "italic"), bg="lightblue")
            result_text.pack()
            result_text.delete(1.0, END)
            result_text.insert(END, f"Функція: {function_str}\n\n")
            if is_full:
                result_text.insert(END, result)
            else:
                result_text.insert(END, f"{operation} функції:\n{result}")

        except Exception as e:
            messagebox.showerror("Помилка", f"Неможливо виконати операцію: {e}")


# Початкова точка програми (створює головне вікно)
if __name__ == "__main__":
    root = Tk()
    app = MathAnalyzerApp(root)
    root.mainloop()
