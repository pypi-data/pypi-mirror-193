# -*- coding: utf-8 -*-
"""
@author: Cristiano Pizzamiglio

"""

from __future__ import annotations

from pathlib import Path
from typing import Callable, List

import numpy as np
import pyvista as pv
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QGridLayout,
    QGroupBox,
    QPushButton,
    QLineEdit,
    QFileDialog,
    QMessageBox,
)
from pyvistaqt import QtInteractor


class Ui(QMainWindow):
    """Main window."""

    def __init__(self) -> None:

        super().__init__()

        self.setWindowTitle("Point Picker")
        self.setWindowIcon(QIcon("logo.ico"))
        self.setStyleSheet("background-color: white;")

        self.import_geometry_box = ImportGeometryBox()
        self.actions_box = ActionsBox(
            self.import_geometry_box.lineedit, self._draw_plot, self._export
        )
        self.actions_box.switch_buttons()
        self.plot_box = PyVistaPlotBox(label="Plot")
        self.selected_points = []

        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QGridLayout()
        layout.addWidget(self.import_geometry_box.box, 0, 0)
        layout.addWidget(self.actions_box.box, 0, 1)
        layout.addWidget(self.plot_box.box, 1, 0, 1, 2)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)

        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 10)

        widget.setLayout(layout)

        self.showMaximized()

    def _draw_plot(self) -> None:
        """Draw geometry."""

        self.plot_box.plotter.clear()
        self.selected_points = []

        try:
            mesh = pv.read(self.import_geometry_box.lineedit.text())
        except FileNotFoundError:
            self._display_error_window()
        else:
            self.plot_box.plotter.add_mesh(mesh, show_edges=True)

        def callback(point):

            actor = self.plot_box.plotter.add_point_labels(
                [point],
                [f"({point[0]:.1f}, {point[1]:.1f}, {point[2]:.1f})"],
                name=point,
                render_points_as_spheres=True,
                reset_camera=False,
                fill_shape=False,
                shape=None,
            )
            actor.SetVisibility(False)

            if is_point_selected(self.selected_points, point):
                remove_point(self.selected_points, point)
                actor.SetVisibility(False)
            else:
                self.selected_points.append(point)
                actor.SetVisibility(True)

        self.plot_box.plotter.enable_point_picking(
            callback, show_message=False, show_point=False
        )

    def _export(self) -> None:
        """Export selected points as a csv file."""

        path = Path(self.import_geometry_box.lineedit.text())
        patient_id = path.stem
        if len(self.selected_points):
            np.savetxt(
                Path(path.parent, f"{patient_id}.csv"),
                X=np.array(self.selected_points),
                delimiter=",",
                fmt="%.6f",
            )
        else:
            self._display_warning_window()

    @staticmethod
    def _display_error_window() -> None:
        """Display error window if geometry import fails."""

        message = QMessageBox()
        message.setWindowIcon(QIcon("logo.ico"))
        message.setIcon(QMessageBox.Critical)
        message.setText("Error")
        message.setText("File not found.")
        message.setWindowTitle("Import Error")
        message.setFixedWidth(400)
        message.exec_()

    @staticmethod
    def _display_warning_window() -> None:
        """Display warning window if no point is picked."""

        message = QMessageBox()
        message.setWindowIcon(QIcon("logo.ico"))
        message.setIcon(QMessageBox.Warning)
        message.setText("Warning")
        message.setText("Pick at least one point.")
        message.setWindowTitle("Warning")
        message.exec_()


class ImportGeometryBox:
    """Import geometry box."""

    def __init__(self) -> None:
        self.lineedit = create_path_lineedit()
        self.button = QPushButton("Browse")
        self.box = self._create_box()

    def _create_box(self) -> QGroupBox:
        box = QGroupBox("Import Geometry")
        layout = QGridLayout()
        box.setLayout(layout)

        self.button.clicked.connect(
            lambda: get_file_path(self.lineedit, self.button.text())
        )
        layout.addWidget(self.button, 0, 0)
        layout.addWidget(self.lineedit, 0, 1)

        return box


class ActionsBox:
    """Actions box."""

    def __init__(
        self, import_lineedit: QLineEdit, draw: Callable, export: Callable
    ) -> None:
        self._lineedit = import_lineedit
        self._draw = draw
        self._export = export
        self.draw_button = QPushButton("Draw")
        self.export_button = QPushButton("Export")
        self.box = self._create_box()

    def _create_box(self) -> QGroupBox:
        box = QGroupBox("Actions")
        layout = QGridLayout()
        box.setLayout(layout)

        self.draw_button.setEnabled(False)
        self.draw_button.clicked.connect(self._draw)
        self.export_button.setEnabled(False)
        self.export_button.clicked.connect(self._export)
        layout.addWidget(self.draw_button, 0, 0)
        layout.addWidget(self.export_button, 0, 1)

        return box

    def switch_buttons(self) -> None:
        def switch() -> None:
            self.draw_button.setEnabled(all((self._lineedit.text())))
            self.export_button.setEnabled(all((self._lineedit.text())))

        self._lineedit.textChanged.connect(switch)


class PyVistaPlotBox:
    """
    QGroupBox for a PyVista plot.

    Parameters
    ----------
    label : str

    Attributes
    ----------
    layout : QGridLayout
    plotter : QtInteractor
    box : QGroupBox

    """

    def __init__(self, label: str) -> None:
        self.label = label
        self.layout = QGridLayout()
        self.box = self._create_box()
        self.plotter = self._create_plotter()

    def _create_box(self) -> QGroupBox:
        box = QGroupBox(self.label)
        box.setLayout(self.layout)

        return box

    def _create_plotter(self) -> QtInteractor:
        pv.set_plot_theme("document")
        plotter_ = QtInteractor()
        plotter_.add_axes()
        self.layout.addWidget(plotter_)

        return plotter_


def create_path_lineedit() -> QLineEdit:
    """
    Get geometry file path.

    Returns
    -------
    QLineEdit

    """
    lineedit = QLineEdit()
    lineedit.setPlaceholderText(f"Browse or enter the geometry file path.")

    return lineedit


def get_file_path(lineedit: QLineEdit, caption: str) -> None:
    """
    Get file path.

    Parameters
    ----------
    lineedit : QLineEdit
    caption : str

    """
    extensions = "All Files (*);;(*.stl);;(*.ply);;(*.obj);;(*.vtk)"
    file_path = QFileDialog.getOpenFileName(
        caption=f"Import {caption}", filter=extensions
    )[0]
    lineedit.setText(file_path)


def is_point_selected(selected_points: List[np.ndarray], point: np.ndarray) -> bool:
    """
    Check if point is selected.

    Parameters
    ----------
    selected_points : List[np.array]
    point : np.ndarray

    Returns
    -------
    bool

    """
    return any([np.allclose(point_, point) for point_ in selected_points])


def remove_point(selected_points: List[np.ndarray], point: np.ndarray) -> None:
    """
    Remove array from list.

    Parameters
    ----------
    selected_points : List[np.ndarray]
    point : np.ndarray

    """
    index = 0
    size = len(selected_points)
    while index != size and not np.allclose(selected_points[index], point):
        index += 1
    if index != size:
        selected_points.pop(index)
