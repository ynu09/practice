'''
Publish 버튼 누르면 1초마다 메시지 발행, Stop 버튼 누르면 발행 중지
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import QTimer

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('gui_stop_publisher')

        # [Topic Publisher] 메시지 송신
        self.publisher_ = self.create_publisher(
            String, 
            'button_topic', 
            10)

    # [Topic 콜백함수]
    def publish_message(self, count):
        msg = String()
        msg.data = count
        self.publisher_.publish(msg)

        # 터미널 출력
        self.get_logger().info(f"Publishing message {count}")

class PublisherGUI(QWidget):
    def __init__(self, publisher_node):
        super().__init__()
        self.publisher_node = publisher_node
        self.initUI()

        self.is_publishing = False  # 현재 발행 상태
        self.publish_count = 0 

        self.timer = QTimer(self)  # PyQt 타이머 생성
        self.timer.timeout.connect(self.publish_message)
        
    def initUI(self):
        # GUI 설정
        self.setWindowTitle("Message Publish & Stop")
        self.move(400, 250)
        self.resize(350, 100)

        # 레이아웃 설정
        layout = QHBoxLayout()

        # Publish, Stop 버튼 생성 & 이벤트 연결
        publish_btn = QPushButton("Publish")
        stop_btn = QPushButton("Stop")

        publish_btn.clicked.connect(self.start_publishing)
        stop_btn.clicked.connect(self.stop_publishing)
        
        # 레이아웃에 버튼 추가
        layout.addWidget(publish_btn)
        layout.addWidget(stop_btn)
        self.setLayout(layout)

    # [Publish 버튼 클릭] 1초마다 메시지 발행 시작
    def start_publishing(self):
        if not self.is_publishing:
            self.is_publishing = True
            self.timer.start(1000)  # 1초(1000ms)마다 타이머 실행
            self.publisher_node.get_logger().info("Started publishing...")

    # [Stop 버튼 클릭] 메시지 발행 중지
    def stop_publishing(self):
        if self.is_publishing:
            self.is_publishing = False
            self.timer.stop()  # 타이머 중지
            self.publisher_node.get_logger().info("Stopped publishing.")
    
    # 타이머에 의해 호출되는 메시지 발행 함수
    # self.is_publishing = True 상태
    def publish_message(self):
        if self.is_publishing:
            # 콜백함수와 연결
            self.publisher_node.publish_message(f'#{self.publish_count}')
            self.publish_count += 1 # count update

def main():
    rclpy.init()
    publisher_node = PublisherNode()

    app = QApplication(sys.argv)
    window = PublisherGUI(publisher_node)
    window.show()

    sys.exit(app.exec_())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
