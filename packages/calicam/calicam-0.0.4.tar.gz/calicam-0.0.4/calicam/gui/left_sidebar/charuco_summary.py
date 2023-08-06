# Built following the tutorials that begin here:
# https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/

import calicam.logger
logger = calicam.logger.get(__name__)
import sys


from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QTableWidget,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from calicam.session import Session


class CharucoSummary(QWidget):
    def __init__(self, session):
        super().__init__()
        self.session = session

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.charuco_display = QLabel()
        self.charuco_display.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.charuco_display.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum
        )

        hbox = QHBoxLayout()
        vbox.addLayout(hbox)

        hbox.addWidget(self.charuco_display)

        self.charuco_summary = QLabel()

        hbox.addWidget(self.charuco_summary)
        hbox.setAlignment(self.charuco_display, Qt.AlignmentFlag.AlignBaseline)
        hbox.setAlignment(self.charuco_summary, Qt.AlignmentFlag.AlignBaseline)

        # self.launch_charuco_builder_btn = QPushButton("&Launch Builder")
        # self.launch_charuco_builder_btn.setMaximumSize(150, 30)
        # vbox.addWidget(self.launch_charuco_builder_btn)
        # vbox.setAlignment(
        #     self.launch_charuco_builder_btn, Qt.AlignmentFlag.AlignHCenter
        # )

        self.update_charuco_summary()

    def update_charuco_summary(self):
        charuco_width = 200
        charuco_height = 200
        charuco_img = self.session.charuco.board_pixmap(charuco_width, charuco_height)
        self.charuco_display.setPixmap(charuco_img)
        self.charuco_summary.setText(self.session.charuco.summary())


if __name__ == "__main__":
    repo = Path(str(Path(__file__)).split("calicam")[0],"calicam").parent
    config_path = Path(repo, "sessions", "high_res_session")
    
    session = Session(config_path)
    print(session.config)
    app = QApplication(sys.argv)
    charuco_summary = CharucoSummary(session)
    charuco_summary.show()
    sys.exit(app.exec())