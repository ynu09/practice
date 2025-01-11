import sys

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node


class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        # [Service Client] 서비스 데이터 타입, 서비스 이름
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')

        # 1초에 한 번씩 클라이언트의 유형/이름과 일치하는 서비스를 사용할 수 있는지 확인
        # 즉, 서비스가 준비됐는지 확인
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        
        # 요청 객체
        self.req = AddTwoInts.Request()

    # [Service 콜백함수] 요청 보내고 응답 받거나 실패할 때까지 회전
    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.cli.call_async(self.req)


def main():
    rclpy.init()

    # 노드 생성
    minimal_client = MinimalClientAsync()

    # 비동기 클라이언트 방식
    # 터미널에서 매개변수 전달 (argv[0]은 파일 이름)
    future = minimal_client.send_request(int(sys.argv[1]), int(sys.argv[2]))
    
    # 결과 기다리기 위해 호출
    rclpy.spin_until_future_complete(minimal_client, future)
    response = future.result()
    
    # 터미널 출력
    minimal_client.get_logger().info(
        'Result of add_two_ints: for %d + %d = %d' %
        (int(sys.argv[1]), int(sys.argv[2]), response.sum))

    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()