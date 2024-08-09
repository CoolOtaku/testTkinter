from tkinter import *
from tkinter import messagebox, filedialog

import sympy as sp
import numpy as np

import matplotlib.pyplot as plt


class MenuModule:
    def __init__(self, root, app):
        self.root = root
        self.app = app  # Посилання на основний додаток

        # Створення меню
        self.menubar = Menu(root)

        # Меню "Файл"
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Новий", command=self.new_file)
        self.filemenu.add_command(label="Відкрити", command=self.open_file)
        self.filemenu.add_command(label="Зберегти", command=self.save_file)
        self.filemenu.add_command(label="Зберегти в LaTeX", command=self.save_as_latex)
        self.filemenu.add_command(label="Зберегти в PNG", command=self.save_as_png)
        self.filemenu.add_command(label="Закрити", command=self.close_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Вихід", command=root.quit)
        self.menubar.add_cascade(label="Файл", menu=self.filemenu)

        # Меню "Довідка"
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Інструкція", command=self.instruction)
        self.menubar.add_cascade(label="Довідка", menu=self.helpmenu)

        # Прив'язка меню до кореневого вікна
        self.root.config(menu=self.menubar)

    # Функція для очищення статусу
    def new_file(self):
        self.app.function_entry.delete(0, END)
        messagebox.showinfo("Новий файл", "Створено новий файл!")

    # Функція для відкриття файлу
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'r') as file:
                formula = file.read().strip()
                self.app.function_entry.delete(0, END)
                self.app.function_entry.insert(0, formula)
                messagebox.showinfo("Відкрити файл", f"Файл завантажено з: {file_path}")

    # Функція для збереження файлу
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            formula = self.app.function_entry.get().strip()
            with open(file_path, 'w') as file:
                file.write(formula)
            messagebox.showinfo("Зберегти файл", f"Файл збережено в: {file_path}")

    # Функція для збереження файлу в LaTeX формат
    def save_as_latex(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".tex",
                                                 filetypes=[("LaTeX files", "*.tex"), ("All files", "*.*")])
        if file_path:
            formula = self.app.function_entry.get().strip()
            try:
                function = sp.sympify(formula)
                latex_str = sp.latex(function)
                with open(file_path, 'w') as file:
                    file.write(latex_str)
                messagebox.showinfo("Зберегти в LaTeX", f"LaTeX файл збережено в: {file_path}")
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося перетворити на LaTeX: {e}")

    # Функція для збереження файлу в PNG формат
    def save_as_png(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            formula = self.app.function_entry.get().strip()
            try:
                function = sp.sympify(formula)
                f_lambdified = sp.lambdify(sp.symbols('x'), function, 'numpy')
                x_vals = np.linspace(-10, 10, 400)
                y_vals = f_lambdified(x_vals)
                plt.figure()
                plt.plot(x_vals, y_vals, label=f"f(x) = {formula}")
                plt.legend()
                plt.grid(True)
                plt.savefig(file_path)
                messagebox.showinfo("Зберегти в PNG", f"PNG файл збережено в: {file_path}")
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося перетворити на PNG: {e}")

    # Функція для очищення статусу
    def close_file(self):
        self.app.function_entry.delete(0, END)
        messagebox.showinfo("Закрити файл", "Файл закрито!")

    # Функція для інструкції користувача
    def instruction(self):
        message = """
        Це додаток дозволяє користувачеві працювати з функціями та графіками.
        Він надає такі можливості:

        - Новий: Створює новий файл для введення нової функції.
        - Відкрити: Відкриває існуючий файл з функцією.
        - Зберегти: Зберігає введену функцію у файл.
        - Зберегти в LaTeX: Зберігає функцію у файл у форматі LaTeX.
        - Зберегти в PNG: Зберігає графік функції у файл у форматі PNG.
        - Закрити: Очищує поле введення функції.

        Для введення функції використовуйте вирази, які підтримуються бібліотекою SymPy.
        Наприклад, 'x**2 + 2*x + 1' або 'sin(x)'.

        Перед збереженням графіка перевірте введену функцію на коректність.
        """
        messagebox.showinfo("Інструкція", message)
