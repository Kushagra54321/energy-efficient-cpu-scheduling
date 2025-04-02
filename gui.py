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