import sys
from PyQt6.QtWidgets import QApplication
from GUI2 import BudgetWindow

def main() -> None:
    app = QApplication(sys.argv)
    win = BudgetWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
