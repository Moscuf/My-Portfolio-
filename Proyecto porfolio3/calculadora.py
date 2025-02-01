import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
from datetime import datetime

# Textos en varios idiomas
texts = {
    "en": {
        "select_operation": "Select operation:",
        "add_income": "Add Income",
        "add_expense": "Add Expense",
        "amount": "Amount:",
        "description": "Description:",
        "expense_type": "Expense Type:",
        "cash": "Cash",
        "debit": "Debit",
        "submit": "Submit",
        "income_added": "Income added successfully!",
        "expense_added": "Expense added successfully!",
        "error": "Invalid Input",
        "income": "Income",
        "expense": "Expense",
        "date": "Date:",
        "time": "Time:",
        "balance": "Net Balance:",
        "english": "English",
        "spanish": "Español",
        "german": "Deutsch",
        "view_all": "View All Transactions",
        "income_list": "Income List",
        "expense_list": "Expense List"
    },
    "es": {
        "select_operation": "Selecciona operación:",
        "add_income": "Agregar Ingreso",
        "add_expense": "Agregar Gasto",
        "amount": "Cantidad:",
        "description": "Descripción:",
        "expense_type": "Tipo de Gasto:",
        "cash": "Efectivo",
        "debit": "Débito",
        "submit": "Enviar",
        "income_added": "¡Ingreso agregado exitosamente!",
        "expense_added": "¡Gasto agregado exitosamente!",
        "error": "Entrada no válida",
        "income": "Ingreso",
        "expense": "Gasto",
        "date": "Fecha:",
        "time": "Hora:",
        "balance": "Saldo Neto:",
        "english": "Inglés",
        "spanish": "Español",
        "german": "Alemán",
        "view_all": "Ver Todos los Movimientos",
        "income_list": "Lista de Ingresos",
        "expense_list": "Lista de Gastos"
    },
    "de": {
        "select_operation": "Wählen Sie die Operation:",
        "add_income": "Einkommen hinzufügen",
        "add_expense": "Ausgabe hinzufügen",
        "amount": "Betrag:",
        "description": "Beschreibung:",
        "expense_type": "Ausgabenart:",
        "cash": "Bar",
        "debit": "Lastschrift",
        "submit": "Einreichen",
        "income_added": "Einkommen erfolgreich hinzugefügt!",
        "expense_added": "Ausgabe erfolgreich hinzugefügt!",
        "error": "Ungültige Eingabe",
        "income": "Einkommen",
        "expense": "Ausgabe",
        "date": "Datum:",
        "time": "Zeit:",
        "balance": "Netto Bilanz:",
        "english": "Englisch",
        "spanish": "Spanisch",
        "german": "Deutsch",
        "view_all": "Alle Transaktionen anzeigen",
        "income_list": "Einkommensliste",
        "expense_list": "Ausgabenliste"
    }
}

# Configuración inicial
current_language = "en"
data_file = "finances.json"

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return {"incomes": [], "expenses": []}

def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)

def set_language(language):
    global current_language
    current_language = language
    update_texts()

def update_texts():
    label_operation.config(text=texts[current_language]["select_operation"])
    button_add_income.config(text=texts[current_language]["add_income"])
    button_add_expense.config(text=texts[current_language]["add_expense"])
    label_amount.config(text=texts[current_language]["amount"])
    label_description.config(text=texts[current_language]["description"])
    label_date.config(text=texts[current_language]["date"])
    label_time.config(text=texts[current_language]["time"])
    label_expense_type.config(text=texts[current_language]["expense_type"])
    radio_cash.config(text=texts[current_language]["cash"])
    radio_debit.config(text=texts[current_language]["debit"])
    button_submit.config(text=texts[current_language]["submit"])
    label_balance.config(text=texts[current_language]["balance"])
    button_view_all.config(text=texts[current_language]["view_all"])
    update_balance()

def update_balance():
    data = load_data()
    incomes = sum(item['amount'] for item in data["incomes"])
    expenses = sum(item['amount'] for item in data["expenses"])
    balance = incomes - expenses
    label_balance_value.config(text=f"{balance:.2f}")

def add_income():
    try:
        amount = float(entry_amount.get())
        description = entry_description.get()
        date = entry_date.get()
        time = entry_time.get()
        data = load_data()
        data["incomes"].append({"amount": amount, "description": description, "date": date, "time": time})
        save_data(data)
        messagebox.showinfo(texts[current_language]["income"], texts[current_language]["income_added"])
        update_balance()
    except ValueError:
        messagebox.showerror(texts[current_language]["error"], texts[current_language]["error"])

def add_expense():
    try:
        amount = float(entry_amount.get())
        description = entry_description.get()
        date = entry_date.get()
        time = entry_time.get()
        expense_type = expense_var.get()
        data = load_data()
        data["expenses"].append({"amount": amount, "description": description, "date": date, "time": time, "type": expense_type})
        save_data(data)
        messagebox.showinfo(texts[current_language]["expense"], texts[current_language]["expense_added"])
        update_balance()
    except ValueError:
        messagebox.showerror(texts[current_language]["error"], texts[current_language]["error"])

def view_transactions():
    # Crear una nueva ventana para mostrar las transacciones
    transactions_window = tk.Toplevel(root)
    transactions_window.title(texts[current_language]["view_all"])

    # Crear pestañas para ingresos y gastos
    tab_control = ttk.Notebook(transactions_window)
    
    income_tab = ttk.Frame(tab_control)
    expense_tab = ttk.Frame(tab_control)
    
    tab_control.add(income_tab, text=texts[current_language]["income_list"])
    tab_control.add(expense_tab, text=texts[current_language]["expense_list"])
    tab_control.pack(expand=1, fill='both')

    # Crear listas para ingresos y gastos
    income_list = tk.Listbox(income_tab, width=80, height=20, borderwidth=2, relief='sunken')
    expense_list = tk.Listbox(expense_tab, width=80, height=20, borderwidth=2, relief='sunken')

    income_list.pack(padx=10, pady=10)
    expense_list.pack(padx=10, pady=10)

    # Cargar datos y actualizar listas
    data = load_data()

    for income in data["incomes"]:
        income_list.insert(tk.END, f"Amount: ${income['amount']:.2f} - Description: {income['description']} - Date: {income['date']} - Time: {income['time']}")

    for expense in data["expenses"]:
        expense_list.insert(tk.END, f"Amount: ${expense['amount']:.2f} - Description: {expense['description']} - Date: {expense['date']} - Time: {expense['time']} - Type: {expense['type']}")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Multilingual Financial Manager")

# Idioma
language_frame = tk.Frame(root)
language_frame.pack(pady=10)

button_en = tk.Button(language_frame, text=texts[current_language]["english"], command=lambda: set_language("en"))
button_en.pack(side=tk.LEFT, padx=5)
button_es = tk.Button(language_frame, text=texts[current_language]["spanish"], command=lambda: set_language("es"))
button_es.pack(side=tk.LEFT, padx=5)
button_de = tk.Button(language_frame, text=texts[current_language]["german"], command=lambda: set_language("de"))
button_de.pack(side=tk.LEFT, padx=5)

# Selección de operación
operation_frame = tk.Frame(root)
operation_frame.pack(pady=10)

label_operation = tk.Label(operation_frame, text=texts[current_language]["select_operation"])
label_operation.pack()

button_add_income = tk.Button(operation_frame, text=texts[current_language]["add_income"], command=lambda: operation.set("income"))
button_add_income.pack(side=tk.LEFT, padx=5)

button_add_expense = tk.Button(operation_frame, text=texts[current_language]["add_expense"], command=lambda: operation.set("expense"))
button_add_expense.pack(side=tk.LEFT, padx=5)

# Formulario de ingreso/gasto
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

label_amount = tk.Label(form_frame, text=texts[current_language]["amount"])
label_amount.grid(row=0, column=0, sticky=tk.W, padx=5)
entry_amount = tk.Entry(form_frame)
entry_amount.grid(row=0, column=1, padx=5)

label_description = tk.Label(form_frame, text=texts[current_language]["description"])
label_description.grid(row=1, column=0, sticky=tk.W, padx=5)
entry_description = tk.Entry(form_frame)
entry_description.grid(row=1, column=1, padx=5)

label_date = tk.Label(form_frame, text=texts[current_language]["date"])
label_date.grid(row=2, column=0, sticky=tk.W, padx=5)
entry_date = tk.Entry(form_frame)
entry_date.grid(row=2, column=1, padx=5)

label_time = tk.Label(form_frame, text=texts[current_language]["time"])
label_time.grid(row=3, column=0, sticky=tk.W, padx=5)
entry_time = tk.Entry(form_frame)
entry_time.grid(row=3, column=1, padx=5)

label_expense_type = tk.Label(form_frame, text=texts[current_language]["expense_type"])
label_expense_type.grid(row=4, column=0, sticky=tk.W, padx=5)
expense_var = tk.StringVar(value="cash")
radio_cash = tk.Radiobutton(form_frame, text=texts[current_language]["cash"], variable=expense_var, value="cash")
radio_cash.grid(row=4, column=1, sticky=tk.W)
radio_debit = tk.Radiobutton(form_frame, text=texts[current_language]["debit"], variable=expense_var, value="debit")
radio_debit.grid(row=4, column=1, sticky=tk.E)

button_submit = tk.Button(form_frame, text=texts[current_language]["submit"], command=lambda: add_income() if operation.get() == "income" else add_expense())
button_submit.grid(row=5, column=0, columnspan=2, pady=10)

# Saldo Neto
label_balance = tk.Label(root, text=texts[current_language]["balance"])
label_balance.pack(pady=10)
label_balance_value = tk.Label(root, text="0.00")
label_balance_value.pack()

# Botón para ver todas las transacciones
button_view_all = tk.Button(root, text=texts[current_language]["view_all"], command=view_transactions)
button_view_all.pack(pady=10)

# Crear una variable para determinar la operación actual (ingreso o gasto)
operation = tk.StringVar(value="income")

# Actualizar textos iniciales
update_texts()

# Iniciar la interfaz gráfica
root.mainloop()
