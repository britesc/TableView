#!/usr/bin/env python3
# coding: utf-8


# import os
import sys
import traceback

from PySide6.QtWidgets import (
    QApplication
)

from mainwindow import MainWindow


def Main() -> None:
    global vApplicationName
    try:
        app = QApplication(sys.argv)

        window = MainWindow(app)

        window.show()

    except Exception as err: # type: ignore
        print(
            "Unfortunately the Application has encountered an error and is unable to continue."  # noqa: E501
        )
        print(f"Exception {err=}, {type(err)=}")
        traceback.print_exc()
        traceback.print_exception() # type: ignore

    finally:
        sys.exit(app.exec()) # type: ignore



if __name__ == '__main__':
    Main()   