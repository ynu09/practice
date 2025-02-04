## 💪🏻코딩 마스터를 향한 연습과 도전의 공간🔥

### 기록

| 기간 | 내용 | 폴더 |
| --- | --- | --- |
| 2025.01.10 | ros2 documentation 참고([https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries.html](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries.html)) ; Python으로 기본 topic, service, interface(custom) 패키지 생성/테스트 | py_pubsub, py_srvcli, tutorial_interfaces |
| 2025.01.11 | ros2, PyQt5(GUI) 연동 ; 버튼에 topic 통신 연결 / YOLO object detection, tracking (OpenCV) & 추적 라인 그리기 | pyqt_ros, yolo_cv |
| 2025.02.01 | C++ 기초 공부([https://www.youtube.com/playlist?list=PLgqG2uj21HgkcfVtlr5rPekQl5VWJEnIB](https://www.youtube.com/playlist?list=PLgqG2uj21HgkcfVtlr5rPekQl5VWJEnIB)) / ros2 documentation 참고 ; C++로 기본 topic 패키지 생성/테스트 | cpp_study, cpp_pubsub |
| 2025.02.03~04 | WSL 사용하여 Ubuntu 환경 세팅, WSL OpenCV 카메라 오류 해결 | yolo_cv |

### 기술 스택

| 분류 | 기술 |
| --- | --- |
| 개발 환경 | WSL Ubuntu 22.04 |
| 개발 언어 | Python, C++ |
| 딥러닝 프레임워크 | Ultralytics YOLOv8 |
| 통신 프로토콜 | ROS2 |
| UI | PyQt5 |
| 영상 처리 | OpenCV |

### 결과물

- 2025.01.10
    1. py_pubsub
        
        ```python
        $ ros2 run py_pubsub talker
        [INFO] [1736512562.183009175] [minimal_publisher]: Publishing: "Hello World: 0"
        [INFO] [1736512562.675734458] [minimal_publisher]: Publishing: "Hello World: 1"
        [INFO] [1736512563.175990206] [minimal_publisher]: Publishing: "Hello World: 2"
        
        $ ros2 run py_pubsub listener
        [INFO] [1736512562.176433920] [minimal_subscriber]: I heard: "Hello World: 0"
        [INFO] [1736512562.675941791] [minimal_subscriber]: I heard: "Hello World: 1"
        [INFO] [1736512563.176384981] [minimal_subscriber]: I heard: "Hello World: 2"
        ```
        
    2. py_srvcli 
        
        ```python
        $ ros2 run py_srvcli service
        [INFO] [1736515209.738682086] [minimal_service]: Incoming request
        a: 2 b: 3
        
        $ ros2 run py_srvcli client 2 3
        [INFO] [1736515209.745435349] [minimal_client_async]: Result of add_two_ints: for 2 + 3 = 5
        ```
        
    3. tutorial_interfaces
        
        ```python
        $ ros2 interface show tutorial_interfaces/msg/Num
        int64 num
        
        $ ros2 interface show tutorial_interfaces/msg/Sphere 
        geometry_msgs/Point center
        	float64 x
        	float64 y
        	float64 z
        float64 radius
        
        $ ros2 interface show tutorial_interfaces/srv/AddThreeInts
        int64 a
        int64 b
        int64 c
        ---
        int64 sum
        ```
        
- 2025.01.11
    1. pyqt_ros
        
        ![img1](https://github.com/user-attachments/assets/1084f39f-b1e2-49f1-ad2c-78b3bd69525d)
        ![img2](https://github.com/user-attachments/assets/9c8a1455-c2c3-44b5-85ff-a6bb54f73936)
        ![img3](https://github.com/user-attachments/assets/f91b012c-ea4d-4ed9-ad80-fe03e57eb29c)
        
        ```python
        $ ros2 run pyqt_ros publisher 
        [INFO] [1736587392.626025886] [gui_publisher_node]: Publishing: "Hello"
        [INFO] [1736587394.616446083] [gui_publisher_node]: Publishing: "Goodbye"
        
        $ ros2 run pyqt_ros subscriber
        [INFO] [1736587392.675690656] [gui_subscriber_node]: Received: "Hello"
        [INFO] [1736587394.667881090] [gui_subscriber_node]: Received: "Goodbye"
        ```
        
        ![img4](https://github.com/user-attachments/assets/1014e971-ffe4-42bb-bd14-60765f4cd647)
        
        ```python
        $ ros2 run pyqt_ros stop_publisher 
        [INFO] [1736601277.020722894] [gui_stop_publisher]: Started publishing...
        [INFO] [1736601278.066126437] [gui_stop_publisher]: Publishing message #0
        [INFO] [1736601279.071913560] [gui_stop_publisher]: Publishing message #1
        [INFO] [1736601280.072501715] [gui_stop_publisher]: Publishing message #2
        [INFO] [1736601280.523379824] [gui_stop_publisher]: Stopped publishing.
        
        $ ros2 run pyqt_ros subscriber
        [INFO] [1736601278.075910586] [gui_subscriber_node]: Received: "#0"
        [INFO] [1736601279.167644627] [gui_subscriber_node]: Received: "#1"
        [INFO] [1736601280.167838907] [gui_subscriber_node]: Received: "#2"
        ```
        
    2. yolo_cv
        1. object_detection (yolo11n.pt 사용)
            
            ![img5](https://github.com/user-attachments/assets/30246ac4-f082-435c-a0f5-6e4254995f66)
            
        2. object_tracking (yolov8n.pt 사용)
            
            ![img6](https://github.com/user-attachments/assets/27c1afeb-6659-4cc9-b8d6-4d290ecccb36)
                
        3. draw_tracking (추적 라인 그리기)
            
            ![img7](https://github.com/user-attachments/assets/4f81dbc3-9cc4-4021-a3eb-51443a673544)