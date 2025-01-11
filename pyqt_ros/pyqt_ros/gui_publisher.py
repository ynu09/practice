import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class GuiPublisherNode(Node):
    def __init__(self):
        super().__init__('gui_publisher')
        self.publisher_ = self.create_publisher(String, 'button_topic', 10)

    # 터미널에 출력(Published: Hello, Published: Goodbye)
    def publish_message(self, msg):
        message = String()
        message.data = msg
        self.publisher_.publish(message)
        self.get_logger().info(f"Published: {msg}")

class MainWindow(QWidget):
    def __init__(self, ros_node):
        super().__init__()
        self.ros_node = ros_node

        # GUI 레이아웃 설정
        self.setWindowTitle("ROS2 PyQt Button")
        self.resize(350, 100)
        layout = QVBoxLayout()

        # 버튼 생성
        self.button1 = QPushButton("Publish 'Hello'")
        self.button1.clicked.connect(self.publish_hello)
        layout.addWidget(self.button1)

        self.button2 = QPushButton("Publish 'Goodbye'")
        self.button2.clicked.connect(self.publish_goodbye)
        layout.addWidget(self.button2)

        self.setLayout(layout)

    def publish_hello(self):
        self.ros_node.publish_message("Hello")

    def publish_goodbye(self):
        self.ros_node.publish_message("Goodbye")

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
