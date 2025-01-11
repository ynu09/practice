## 💪🏻코딩 마스터를 향한 연습과 도전의 공간🔥

### 기록

| 기간 | 내용 | 폴더 |
| --- | --- | --- |
| 2025.01.10 | ros2 documentation 참고([https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries.html](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries.html)) ; 기본 topic, service, interface(custom) 패키지 생성/테스트 | base_ws/src/py_pubsub, base_ws/src/py_srvcli, base_ws/src/tutorial_interfaces |
| 2025.01.11 | ros2, PyQt5(GUI) 연동 ; 버튼에 통신 연결 | base_ws/src/pyqt_ros |

### 기술 스택

| 분류 | 기술 |
| --- | --- |
| 개발 환경 | Ubuntu 22.04 |
| 개발 언어 | Python |
| 딥러닝 프레임워크 | Ultralytics YOLOv8 |
| 통신 프로토콜 | ROS2 |
| UI | PyQt5 |
| 영상 처리 | OpenCV |

### 결과물

- 2025.01.10
    1. py_pubsub
        
        ```python
        ynu@ynu-rokey:~/ynu_git/base_ws$ ros2 run py_pubsub talker
        [INFO] [1736512562.183009175] [minimal_publisher]: Publishing: "Hello World: 0"
        [INFO] [1736512562.675734458] [minimal_publisher]: Publishing: "Hello World: 1"
        [INFO] [1736512563.175990206] [minimal_publisher]: Publishing: "Hello World: 2"
        
        ynu@ynu-rokey:~/ynu_git/base_ws$ ros2 run py_pubsub listener
        [INFO] [1736512562.176433920] [minimal_subscriber]: I heard: "Hello World: 0"
        [INFO] [1736512562.675941791] [minimal_subscriber]: I heard: "Hello World: 1"
        [INFO] [1736512563.176384981] [minimal_subscriber]: I heard: "Hello World: 2"
        ```
        
    2. py_srvcli 
        
        ```python
        ynu@ynu-rokey:~/ynu_git/base_ws$ ros2 run py_srvcli service
        [INFO] [1736515209.738682086] [minimal_service]: Incoming request
        a: 2 b: 3
        
        ynu@ynu-rokey:~/ynu_git/base_ws$ ros2 run py_srvcli client 2 3
        [INFO] [1736515209.745435349] [minimal_client_async]: Result of add_two_ints: for 2 + 3 = 5
        ```
        
    3. tutorial_interfaces
        
        ```python
        ynu@ynu-rokey:~/ynu_git/base_ws$ ros2 interface show tutorial_interfaces/msg/Num
        int64 num
        
        ynu@ynu-rokey:~/ynu_git/base_ws$ ros2 interface show tutorial_interfaces/msg/Sphere 
        geometry_msgs/Point center
        	float64 x
        	float64 y
        	float64 z
        float64 radius
        
        ynu@ynu-rokey:~/ynu_git/base_ws$ ros2 interface show tutorial_interfaces/srv/AddThreeInts
        int64 a
        int64 b
        int64 c
        ---
        int64 sum
        ```
        
- 2025.01.11
