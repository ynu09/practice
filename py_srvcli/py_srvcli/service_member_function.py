from example_interfaces.srv import AddTwoInts
'''
# request
int64 a
int64 b
---
# response
int64 sum
'''

import rclpy
from rclpy.node import Node


class MinimalService(Node):

    def __init__(self):
        # 노드 이름 지정
        super().__init__('minimal_service')
        
        # [Service Server] 서비스 데이터 타입, 서비스 이름, 콜백 함수
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    # [Service 콜백함수] 요청 데이터 수신 & 합산 후 합계 응답으로 반환
    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response


def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()