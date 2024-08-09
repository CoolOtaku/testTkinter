from tkinter import INSERT, END
from tkinter.ttk import Button


class KeyboardModule:
    def __init__(self, root, function_entry):
        self.root = root
        self.function_entry = function_entry

        # Кнопки клавіатури
        # Рядок 1
        self.plus_button = Button(self.root, text="+", command=lambda: self.input_function("+"), style="Custom.TButton")
        self.plus_button.grid(row=3, column=0)

        self.minus_button = Button(self.root, text="-", command=lambda: self.input_function("-"),
                                   style="Custom.TButton")
        self.minus_button.grid(row=3, column=1)

        self.multiply_button = Button(self.root, text="×", command=lambda: self.input_function("*"),
                                      style="Custom.TButton")
        self.multiply_button.grid(row=3, column=2)

        self.divide_button = Button(self.root, text="÷", command=lambda: self.input_function("/"),
                                    style="Custom.TButton")
        self.divide_button.grid(row=3, column=3)

        self.degree_button = Button(self.root, text="^", command=lambda: self.input_function("^"),
                                    style="Custom.TButton")
        self.degree_button.grid(row=3, column=4)

        self.pi_button = Button(self.root, text="π", command=lambda: self.input_function("pi"),
                                style="Custom.TButton")
        self.pi_button.grid(row=3, column=5)

        self.clear_button = Button(self.root, text="↺", command=lambda: self.function_entry.delete(0, END),
                                   style="Custom.TButton")
        self.clear_button.grid(row=3, column=6)

        self.return_button = Button(self.root, text="↩︎", command=lambda: self.delete_before_cursor(),
                                    style="Custom.TButton")
        self.return_button.grid(row=3, column=7)
        # Рядок 2
        self.sin_button = Button(self.root, text="sin", command=lambda: self.input_function("sin()"),
                                 style="Custom.TButton")
        self.sin_button.grid(row=4, column=0)

        self.cos_button = Button(self.root, text="cos", command=lambda: self.input_function("cos()"),
                                 style="Custom.TButton")
        self.cos_button.grid(row=4, column=1)

        self.tan_button = Button(self.root, text="tan", command=lambda: self.input_function("tan()"),
                                 style="Custom.TButton")
        self.tan_button.grid(row=4, column=2)

        self.cot_button = Button(self.root, text="cot", command=lambda: self.input_function("cot()"),
                                 style="Custom.TButton")
        self.cot_button.grid(row=4, column=3)

        self.sec_button = Button(self.root, text="sec", command=lambda: self.input_function("sec()"),
                                 style="Custom.TButton")
        self.sec_button.grid(row=4, column=4)

        self.csc_button = Button(self.root, text="csc", command=lambda: self.input_function("csc()"),
                                 style="Custom.TButton")
        self.csc_button.grid(row=4, column=5)

        self.left_soul_button = Button(self.root, text="(", command=lambda: self.input_function("("),
                                       style="Custom.TButton")
        self.left_soul_button.grid(row=4, column=6)

        self.right_soul_button = Button(self.root, text=")", command=lambda: self.input_function(")"),
                                        style="Custom.TButton")
        self.right_soul_button.grid(row=4, column=7)
        # Рядок 3
        self.asin_button = Button(self.root, text="asin", command=lambda: self.input_function("asin()"),
                                  style="Custom.TButton")
        self.asin_button.grid(row=5, column=0)

        self.acos_button = Button(self.root, text="acos", command=lambda: self.input_function("acos()"),
                                  style="Custom.TButton")
        self.acos_button.grid(row=5, column=1)

        self.atan_button = Button(self.root, text="atan", command=lambda: self.input_function("atan()"),
                                  style="Custom.TButton")
        self.atan_button.grid(row=5, column=2)

        self.acot_button = Button(self.root, text="acot", command=lambda: self.input_function("acot()"),
                                  style="Custom.TButton")
        self.acot_button.grid(row=5, column=3)

        self.asec_button = Button(self.root, text="asec", command=lambda: self.input_function("asec()"),
                                  style="Custom.TButton")
        self.asec_button.grid(row=5, column=4)

        self.acsc_button = Button(self.root, text="acsc", command=lambda: self.input_function("acsc()"),
                                  style="Custom.TButton")
        self.acsc_button.grid(row=5, column=5)

        self.log_button = Button(self.root, text="log", command=lambda: self.input_function("log()"),
                                 style="Custom.TButton")
        self.log_button.grid(row=5, column=6)

        self.exp_button = Button(self.root, text="exp", command=lambda: self.input_function("exp()"),
                                 style="Custom.TButton")
        self.exp_button.grid(row=5, column=7)
        # Рядок 4
        self.sinh_button = Button(self.root, text="sinh", command=lambda: self.input_function("sinh()"),
                                  style="Custom.TButton")
        self.sinh_button.grid(row=6, column=0)

        self.cosh_button = Button(self.root, text="cosh", command=lambda: self.input_function("cosh()"),
                                  style="Custom.TButton")
        self.cosh_button.grid(row=6, column=1)

        self.tanh_button = Button(self.root, text="tanh", command=lambda: self.input_function("tanh()"),
                                  style="Custom.TButton")
        self.tanh_button.grid(row=6, column=2)

        self.coth_button = Button(self.root, text="coth", command=lambda: self.input_function("coth()"),
                                  style="Custom.TButton")
        self.coth_button.grid(row=6, column=3)

        self.sech_button = Button(self.root, text="sech", command=lambda: self.input_function("sech()"),
                                  style="Custom.TButton")
        self.sech_button.grid(row=6, column=4)

        self.csch_button = Button(self.root, text="csch", command=lambda: self.input_function("csch()"),
                                  style="Custom.TButton")
        self.csch_button.grid(row=6, column=5)

        self.rad_button = Button(self.root, text="rad", command=lambda: self.input_function("rad()"),
                                 style="Custom.TButton")
        self.rad_button.grid(row=6, column=6)

        self.sign_button = Button(self.root, text="sign", command=lambda: self.input_function("sign()"),
                                  style="Custom.TButton")
        self.sign_button.grid(row=6, column=7)
        # Рядок 5
        self.asinh_button = Button(self.root, text="asinh", command=lambda: self.input_function("asinh()"),
                                   style="Custom.TButton")
        self.asinh_button.grid(row=7, column=0)

        self.acosh_button = Button(self.root, text="acosh", command=lambda: self.input_function("acosh()"),
                                   style="Custom.TButton")
        self.acosh_button.grid(row=7, column=1)

        self.atanh_button = Button(self.root, text="atanh", command=lambda: self.input_function("atanh()"),
                                   style="Custom.TButton")
        self.atanh_button.grid(row=7, column=2)

        self.acoth_button = Button(self.root, text="acoth", command=lambda: self.input_function("acoth()"),
                                   style="Custom.TButton")
        self.acoth_button.grid(row=7, column=3)

        self.asech_button = Button(self.root, text="asech", command=lambda: self.input_function("asech()"),
                                   style="Custom.TButton")
        self.asech_button.grid(row=7, column=4)

        self.acsch_button = Button(self.root, text="acsch", command=lambda: self.input_function("acsch()"),
                                   style="Custom.TButton")
        self.acsch_button.grid(row=7, column=5)

        self.sqrt_button = Button(self.root, text="√", command=lambda: self.input_function("sqrt()"),
                                  style="Custom.TButton")
        self.sqrt_button.grid(row=7, column=6)

        self.abs_button = Button(self.root, text="|◻|", command=lambda: self.input_function("abs()"),
                                 style="Custom.TButton")
        self.abs_button.grid(row=7, column=7)
        # Рядок 6
        self.button_0 = Button(self.root, text="0", command=lambda: self.input_function("0"), style="Custom.TButton")
        self.button_0.grid(row=8, column=0)

        self.button_1 = Button(self.root, text="1", command=lambda: self.input_function("1"), style="Custom.TButton")
        self.button_1.grid(row=8, column=1)

        self.button_2 = Button(self.root, text="2", command=lambda: self.input_function("2"), style="Custom.TButton")
        self.button_2.grid(row=8, column=2)

        self.button_3 = Button(self.root, text="3", command=lambda: self.input_function("3"), style="Custom.TButton")
        self.button_3.grid(row=8, column=3)

        self.button_4 = Button(self.root, text="4", command=lambda: self.input_function("4"), style="Custom.TButton")
        self.button_4.grid(row=8, column=4)

        self.button_5 = Button(self.root, text="5", command=lambda: self.input_function("5"), style="Custom.TButton")
        self.button_5.grid(row=8, column=5)

        self.button_6 = Button(self.root, text="6", command=lambda: self.input_function("6"), style="Custom.TButton")
        self.button_6.grid(row=8, column=6)

        self.button_7 = Button(self.root, text="7", command=lambda: self.input_function("7"), style="Custom.TButton")
        self.button_7.grid(row=8, column=7)
        # Рядок 7
        self.button_8 = Button(self.root, text="8", command=lambda: self.input_function("8"), style="Custom.TButton")
        self.button_8.grid(row=9, column=0)

        self.button_9 = Button(self.root, text="9", command=lambda: self.input_function("9"), style="Custom.TButton")
        self.button_9.grid(row=9, column=1)

        self.button_x = Button(self.root, text="x", command=lambda: self.input_function("x"), style="Custom.TButton")
        self.button_x.grid(row=9, column=2)

        self.button_y = Button(self.root, text="y", command=lambda: self.input_function("y"), style="Custom.TButton")
        self.button_y.grid(row=9, column=3)

        self.button_z = Button(self.root, text="z", command=lambda: self.input_function("z"), style="Custom.TButton")
        self.button_z.grid(row=9, column=4)

    # Функція для вводу символа або функції в поле для функцій
    def input_function(self, function):
        cursor_position = self.function_entry.index(INSERT)
        self.function_entry.insert(cursor_position, function)

    # Функція для видалення одного символу після курсору
    def delete_before_cursor(self):
        cursor_pos = self.function_entry.index(INSERT)
        if cursor_pos > 0:
            self.function_entry.delete(cursor_pos - 1)
