'''
Publish 버튼 누르면 1초마다 메시지 발행, Stop 버튼 누르면 발행 중지
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer # 타이머 추가
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# node 생성
class GuiPublisherNode(Node):
    def __init__(self):
        super().__init__('gui_stop_publisher')

        # [Topic Publisher] 버튼 publish
        self.publisher_ = self.create_publisher(String, 'button_topic', 10)

    def publish_message(self, msg):
        """메시지 발행 함수"""
        message = String()
        message.data = msg
        self.publisher_.publish(message)
        self.get_logger().info(f"Published: {msg}")


class MainWindow(QWidget):
    def __init__(self, ros_node):
        super().__init__()
        self.ros_node = ros_node
        self.is_publishing = False  # 현재 발행 상태
        self.timer = QTimer(self)  # PyQt 타이머 생성
        self.timer.timeout.connect(self.publish_message)

        # GUI 설정
        self.setWindowTitle("ROS2 PyQt Publish and Stop")
        self.resize(300, 200)
        layout = QVBoxLayout()

        # Publish 버튼
        self.publish_button = QPushButton("Publish")
        self.publish_button.clicked.connect(self.start_publishing)
        layout.addWidget(self.publish_button)

        # Stop 버튼
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_publishing)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)

    def start_publishing(self):
        # Publish 버튼 클릭: 1초마다 메시지 발행 시작
        if not self.is_publishing:
            self.is_publishing = True
            self.timer.start(1000)  # 1초(1000ms)마다 타이머 실행
            self.ros_node.get_logger().info("Started publishing...")

    def stop_publishing(self):
        # Stop 버튼 클릭: 메시지 발행 중지
        if self.is_publishing:
            self.is_publishing = False
            self.timer.stop()  # 타이머 중지
            self.ros_node.get_logger().info("Stopped publishing.")

    def publish_message(self):
        # 타이머에 의해 호출되는 메시지 발행 함수
        if self.is_publishing:
            self.ros_node.publish_message("Hello from PyQt Publish Button!")


def main():
    rclpy.init()
    ros_node = GuiPublisherNode()

    app = QApplication(sys.argv)
    window = MainWindow(ros_node)
    window.show()

    sys.exit(app.exec_())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
