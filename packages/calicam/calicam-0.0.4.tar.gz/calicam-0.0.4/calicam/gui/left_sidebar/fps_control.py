
# Built following the tutorials that begin here:
# https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/

import calicam.logger
logger = calicam.logger.get(__name__)
import sys


from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QSpinBox,
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


class FPSControl(QWidget):
    def __init__(self, session, default_fps=6):
        super().__init__()
        self.session = session
        self.setLayout(QHBoxLayout())

        logger.debug("Building FPS Control")

        self.layout().addWidget(QLabel("Target:"))
        self.frame_rate_spin = QSpinBox()
        self.frame_rate_spin.setValue(default_fps)
        self.frame_rate_spin.setEnabled(False)  # start out this way..enable when synchronizer constructed
        self.layout().addWidget(self.frame_rate_spin)
        
        def on_frame_rate_spin(fps_rate):
            try:
                self.session.synchronizer.fps_target = fps_rate
                logger.info(f"Changing synchronizer frame rate")
            except(AttributeError):
                logger.warning("Unable to change synch fps...may need to load stream tools") 

        self.frame_rate_spin.valueChanged.connect(on_frame_rate_spin)

if __name__ == "__main__":
    repo = Path(str(Path(__file__)).split("calicam")[0],"calicam").parent
    config_path = Path(repo, "sessions", "high_res_session")
    

    session = Session(config_path)
    session.load_cameras()
    session.load_streams()

    print(session.config)
    app = QApplication(sys.argv)
    fps_control = FPSControl(session)
    fps_control.show()
    sys.exit(app.exec())