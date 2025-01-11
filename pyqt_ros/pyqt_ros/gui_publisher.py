import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):
    def __init__(self):
        super().__init__('gui_publisher_node')

        # [Topic Publisher] 메시지 송신
        self.publisher_ = self.create_publisher(
            String, 
            'button_topic', 
            10)

    # [Topic 콜백함수]
    def publish_message(self, text):
        msg = String()
        msg.data = text
        self.publisher_.publish(msg)

        # 터미널 출력(Publishing: Hello, Publishing: Goodbye)
        self.get_logger().info(f'Publishing: "{text}"')

class PublisherGUI(QWidget):
    def __init__(self, publisher_node):
        super().__init__()
        self.publisher_node = publisher_node
        self.initUI()
    
    def initUI(self):
        # GUI 레이아웃 설정
        self.setWindowTitle('Message Publish Application')
        # 창 시작 위치
        self.move(400, 250)
        # 창 width, height
        self.resize(350, 100)

        # 레이아웃 설정
        layout = QVBoxLayout()

        # 버튼 생성 & 이벤트 연결
        hello_btn = QPushButton('Publish "Hello"')
        goodbye_btn = QPushButton('Publish "Goodbye"')

        hello_btn.clicked.connect(self.publish_hello)
        goodbye_btn.clicked.connect(self.publish_goodbye)
        
        # 레이아웃에 버튼 추가
        layout.addWidget(hello_btn)
        layout.addWidget(goodbye_btn)
        self.setLayout(layout)

    # publish 할 메시지
    def publish_hello(self):
        self.publisher_node.publish_message('Hello')

    def publish_goodbye(self):
        self.publisher_node.publish_message('Goodbye')

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
