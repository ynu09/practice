# github readme
title: github readme
subtitle: 
categories: 
tags: 
date: 2025-01-11 20:19:57 +0000
last_modified_at: 2025-01-11 20:19:57 +0000
---

## 💪🏻코딩 마스터를 향한 연습과 도전의 공간🔥

### 기록

| 기간 | 내용 | 폴더 |
| --- | --- | --- |
| 2025.01.10 | ros2 documentation 참고([https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries.html](https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries.html)) ; 기본 topic, service, interface(custom) 패키지 생성/테스트 | py_pubsub, py_srvcli, tutorial_interfaces |
| 2025.01.11 | ros2, PyQt5(GUI) 연동 ; 버튼에 통신 연결 | pyqt_ros |

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
    
    
    ![스크린샷 2025-01-11 18-17-35.png](github%20readme%2017760095cba18087a2c9efe93210d2b2/%25EC%258A%25A4%25ED%2581%25AC%25EB%25A6%25B0%25EC%2583%25B7_2025-01-11_18-17-35.png)
    
    ![스크린샷 2025-01-11 18-17-44.png](github%20readme%2017760095cba18087a2c9efe93210d2b2/%25EC%258A%25A4%25ED%2581%25AC%25EB%25A6%25B0%25EC%2583%25B7_2025-01-11_18-17-44.png)
    
    ![스크린샷 2025-01-11 18-17-53.png](github%20readme%2017760095cba18087a2c9efe93210d2b2/%25EC%258A%25A4%25ED%2581%25AC%25EB%25A6%25B0%25EC%2583%25B7_2025-01-11_18-17-53.png)
    
    ```python
    $ ros2 run pyqt_ros publisher 
    [INFO] [1736587392.626025886] [gui_publisher_node]: Publishing: "Hello"
    [INFO] [1736587394.616446083] [gui_publisher_node]: Publishing: "Goodbye"
    
    $ ros2 run pyqt_ros subscriber
    [INFO] [1736587392.675690656] [gui_subscriber_node]: Received: "Hello"
    [INFO] [1736587394.667881090] [gui_subscriber_node]: Received: "Goodbye"
    ```