import sys 
import time
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
class Process:
    def _init_(self, pid, burst_time, priority, power_consumption):
        self.pid = pid
        self.burst_time = burst_time
        self.priority = priority
        self.power_consumption = power_consumption
class SchedulerThread(QThread):
    update_signal = pyqtSignal(str)

    def _init_(self, processes):
        super()._init_()
        self.processes = processes

    def run(self):
        self.processes.sort(key=lambda x: (x.priority, x.power_consumption))
        total_time = 0
        
        for process in self.processes:
            self.update_signal.emit(f"Executing Process {process.pid}: Burst Time = {process.burst_time}, Power = {process.power_consumption}W")
            time.sleep(1)
            total_time += process.burst_time
            
        self.update_signal.emit(f"\nTotal Execution Time: {total_time} units")
class SchedulerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.processes = []

    def initUI(self):
        self.setWindowTitle("Energy Efficient CPU Scheduler")
        self.setGeometry(200, 200, 500, 400)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["PID", "Burst Time", "Priority", "Power Consumption"])
        layout.addWidget(self.table)

        self.pid_input = QLineEdit(self)
        self.pid_input.setPlaceholderText("PID")
        self.burst_input = QLineEdit(self)
        self.burst_input.setPlaceholderText("Burst Time")
        self.priority_input = QLineEdit(self)
        self.priority_input.setPlaceholderText("Priority")
        self.power_input = QLineEdit(self)
        self.power_input.setPlaceholderText("Power Consumption")
        
        layout.addWidget(self.pid_input)
        layout.addWidget(self.burst_input)
        layout.addWidget(self.priority_input)
        layout.addWidget(self.power_input)
        
        self.add_button = QPushButton("Add Process")
        self.add_button.clicked.connect(self.add_process)
        layout.addWidget(self.add_button)
        
        self.schedule_button = QPushButton("Schedule Processes")
        self.schedule_button.clicked.connect(self.schedule_processes)
        layout.addWidget(self.schedule_button)
        
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)