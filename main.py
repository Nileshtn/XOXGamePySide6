from board import Board
from player import Player
from math import floor
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from main_window import Ui_MainWindow, CustomDialog
from qt_material import apply_stylesheet

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.board = Board()
        self.clicks = 0
        self.play_buttons = [self.ui.place00, self.ui.place01, self.ui.place02,
                             self.ui.place10, self.ui.place11, self.ui.place12,
                             self.ui.place20, self.ui.place21, self.ui.place22]
        
        for ix, button in enumerate(self.play_buttons):
            button.setText("-")
            button.clicked.connect(self._on_play_area_clicked)
            button.setProperty("trigger_np", (floor(ix/3), ix%3))
        
        self._disable_buttons()
        self.ui.start_button.clicked.connect(self._on_start_button_clicked)
        self.ui.resetButton.clicked.connect(self._on_reset_button_clicked)
        self.ui.actionQuit.triggered.connect(self.on_exit_event)
        self.ui.actionRestart.triggered.connect(self._on_game_restart)
        self.ui.actionplayer_name.triggered.connect(self.on_reset_name)
        self.ui.actionplayer_name.setEnabled(False)
        
    def _on_won(self, player:Player):
        self.ui.statusbar.showMessage(f"{player.name} Won the round")
        self._on_reset_button_clicked()
        player.set_score(1)
        if player.get_symbol == "X":
            self.ui.player_x_score.display(player.get_score()) 
        else:
            self.ui.player_y_score.display(player.get_score())
            
    def on_exit_event(self):
        self.close()
            
    def closeEvent(self, event):
        # Display a confirmation dialog
        reply = QMessageBox.question(
            self, "Confirm Exit",
            "Are you sure you want to exit?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()  # Close the application
        else:
            event.ignore()  # Cancel the close event
            
    def on_reset_name(self):
        rest_window = CustomDialog()
        if rest_window.exec() == QDialog.DialogCode.Accepted:
            player_X_name, player_O_name = rest_window.get_inputs()
        else:
            return
        
        self.ui.player_x_nameLineEdit.setText(player_X_name)
        self.ui.player_y_nameLineEdit.setText(player_O_name)
        self.player_x.name = player_X_name
        self.player_o.name = player_O_name
            
    def _on_play(self, player, place_check, win_check, sender):
        if place_check:
            player_sys = player.get_symbol()
            sender.setText(f"{player_sys}")
            self.clicks += 1
            if player_sys == "X":
                self.ui.statusbar.showMessage(f"{self.player_o.name} turn")
            else:
                self.ui.statusbar.showMessage(f"{self.player_x.name} turn")

            if win_check:
                self._on_won(player)
            return
        self.ui.statusbar.showMessage(f"{player.name} invalid pos retry")

    def _on_play_area_clicked(self):
        sender = self.sender()
        if not sender:
            return
        
        if self.clicks %2 == 0:
            place_check , win_check = self.player_x.play(self.board, sender.property("trigger_np"))
            self._on_play(self.player_x, place_check, win_check, sender)     
        else:
            place_check, win_check = self.player_o.play(self.board, sender.property("trigger_np"))
            self._on_play(self.player_o, place_check, win_check, sender)   
            
              
    def _disable_buttons(self):
        for button in self.play_buttons:
            button.setEnabled(False)
            
        self.ui.resetButton.setEnabled(False)
        
    def _enable_buttons(self):
        for button in self.play_buttons:
            button.setEnabled(True)
        self.ui.resetButton.setEnabled(True)
        
    def _on_start_button_clicked(self):
        player_x_name = self.ui.player_x_nameLineEdit.text()
        player_o_name = self.ui.player_y_nameLineEdit.text()
        print(player_o_name or player_x_name)
        if player_o_name == "":
            self.ui.statusbar.showMessage("one of the player O name is empty")
            return
        if player_x_name == "":
            self.ui.statusbar.showMessage("one of the player X name is empty")
            return
        
        self.ui.actionplayer_name.setEnabled(True)
        self.ui.player_x_nameLineEdit.setEnabled(False)
        self.ui.player_y_nameLineEdit.setEnabled(False)
        self.player_x = Player("X", self.ui.player_x_nameLineEdit.text())
        self.player_o = Player("O", self.ui.player_y_nameLineEdit.text())
        self._enable_buttons()
        self.ui.statusbar.showMessage(f"{self.player_x.name} turn!")
        self.ui.start_button.setEnabled(False)
        
    def _on_reset_button_clicked(self):
        self.board.reset_board()
        for button in self.play_buttons:
            button.setText("-")
            
            
    def _on_game_restart(self):
        self._on_reset_button_clicked()
        self._disable_buttons()
        self.ui.start_button.setEnabled(True)
        self.ui.player_x_nameLineEdit.setText("")
        self.ui.player_y_nameLineEdit.setText("")
        self.player_o = None
        self.player_x = None
        self.ui.player_x_score.display(0)
        self.ui.player_y_score.display(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    apply_stylesheet(app, theme="light_teal.xml")
    window.show()
    sys.exit(app.exec())
        