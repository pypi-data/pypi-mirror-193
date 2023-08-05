# -*- coding: utf-8 -*-
"""
@author: Cristiano Pizzamiglio

"""


from __future__ import annotations

import sys

from PyQt5.QtWidgets import QApplication

from ui import Ui


def main() -> None:
    """
    Run application.

    """
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    app.setStyle("Fusion")
    ui = Ui()
    ui.show()
    app.exec_()


if __name__ == "__main__":
    main()
