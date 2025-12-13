from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox

from logic2 import is_valid_amount, save_row_to_csv, load_rows_from_csv

DATA_FILE = "data.csv"


class BudgetWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi("project2.ui", self)

        # Buttons in your UI:
        # pushButton     = Add Income
        # pushButton_2   = Add Expense
        # pushButton_3   = Clear
        self.pushButton.clicked.connect(self.add_income)
        self.pushButton_2.clicked.connect(self.add_expense)
        self.pushButton_3.clicked.connect(self.clear_fields)

        self.load_entries()

    def add_income(self) -> None:
        self.add_entry(is_income=True)

    def add_expense(self) -> None:
        self.add_entry(is_income=False)

    def add_entry(self, is_income: bool) -> None:
        description = self.lineEdit.text().strip()
        amount_text = self.lineEdit_2.text().strip()

        if description == "":
            self.show_error("Description is required.")
            self.lineEdit.setFocus()
            return

        if not is_valid_amount(amount_text):
            self.show_error("Amount must be a number (example: 12.50).")
            self.lineEdit_2.setFocus()
            return

        amount = float(amount_text)
        if not is_income:
            amount = -amount

        # Save as 2 columns: description, amount
        save_row_to_csv(DATA_FILE, [description, f"{amount:.2f}"])

        # Update list + balance
        self.listWidget.addItem(f"{description}: {amount:.2f}")
        self.update_balance()
        self.clear_fields()

    def load_entries(self) -> None:
        rows = load_rows_from_csv(DATA_FILE)

        self.listWidget.clear()
        for row in rows:
            if len(row) == 2:
                self.listWidget.addItem(f"{row[0]}: {row[1]}")

        self.update_balance()

    def update_balance(self) -> None:
        rows = load_rows_from_csv(DATA_FILE)

        total = 0.0
        for row in rows:
            if len(row) == 2:
                try:
                    total += float(row[1])
                except ValueError:
                    pass

        self.lineEdit_3.setText(f"{total:.2f}")

    def clear_fields(self) -> None:
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit.setFocus()

    def show_error(self, message: str) -> None:
        QMessageBox.warning(self, "Input Error", message)
