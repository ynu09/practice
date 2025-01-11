# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
# Node 클래스 사용
from rclpy.node import Node

# 토픽 데이터 타입 (문자열 메시지 유형)
from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        # 노드 이름 지정
        super().__init__('minimal_publisher')

        # [Topic Publisher] 토픽 데이터 타입, 토픽 이름, 큐사이즈 (대기 중인 메시지 양)
        self.publisher_ = self.create_publisher(String, 'topic', 10) 
        
        # 0.5초마다 콜백 실행
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # 콜백에서 사용되는 카운터 
        self.i = 0

    # [Topic 콜백함수]
    def timer_callback(self):
        msg = String()
        # subscriber에 전달할 데이터 내용
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        
        # 터미널 출력 (0부터 시작)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1


def main(args=None):
    # rclpy 라이브러리 초기화 
    rclpy.init(args=args)

    # 노드 생성
    minimal_publisher = MinimalPublisher()

    # 노드 회전(콜백 호출)
    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
