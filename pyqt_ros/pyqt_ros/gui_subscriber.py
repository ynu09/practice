'''
ROS2의 spin() 동작과 PyQt 이벤트 루프가 동시에 실행돼야 함
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('gui_subscriber_node')

        # [Topic Subscriber] 메시지 수신
        self.subscription = self.create_subscription(
            String,
            'button_topic',
            self.show_callback,
            10
        )

    # [Topic 콜백함수]
    def show_callback(self, msg):
        # 터미널 출력
        self.get_logger().info(f'Received: "{msg.data}"')
        
        # ui 텍스트 업데이트
        window.label.setText(msg.data)
        
class SubscriberGUI(QWidget):
    def __init__(self, subscriber_node):
        super().__init__()
        self.subscriber_node = subscriber_node
        self.initUI()
    
    def initUI(self):
        # GUI 레이아웃 설정
        self.setWindowTitle('Message Subscribe Application')
        self.move(400, 400)
        self.resize(350, 100)

        # 레이아웃 설정
        layout = QVBoxLayout()

        # 대기 메시지 QLabel 표시
        self.label = QLabel('Waiting for message...')
        # 가운데 정렬
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size: 30px; color: blue;')
        
        # 라벨을 레이아웃에 추가
        layout.addWidget(self.label)
        self.setLayout(layout)

        # ROS2 spin을 위한 타이머 설정 (spin_once 주기적 실행)
        self.timer = QTimer()
        # [실행할 작업] timeout_sec=0로 설정 ; spin_once() 즉시 반환
        self.timer.timeout.connect(lambda: rclpy.spin_once(self.subscriber_node, timeout_sec=0))
        # [작동] 100ms 간격으로 호출됨
        self.timer.start(100)

def main():
    rclpy.init()
    subscriber_node = SubscriberNode()

    app = QApplication(sys.argv)
    global window
    window = SubscriberGUI(subscriber_node)
    window.show()

    sys.exit(app.exec_())
    rclpy.shutdown()

if __name__ == '__main__':
    main()
