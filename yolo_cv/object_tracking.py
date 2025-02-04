import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

# 카메라 디바이스 확인: ls /dev/video*
cap = cv2.VideoCapture(0) # 0 for default camera
# wsl 사용 시 추가설정
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

# for i in range(1, 4):
#     cap = cv2.VideoCapture(i) # usb cam
#     if cap.isOpened():
#         break

while cap.isOpened():
    # 비디오 프레임 읽기
    # print(cap.read()) # (True/False, frame)
    success, frame = cap.read()
    
    if success:
        # 프레임에 YOLOv8 객체 추적 실행
        results = model.track(frame, persist=True)
        
        # 프레임에 결과 시각화
        annotated_frame = results[0].plot()
        
        # annotated frame 표시
        cv2.imshow('YOLOv8 Tracking', annotated_frame)
        
        # q키 눌러서 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        # mp4 파일인 경우, 비디오 끝에 도달하면 루프 중단
        break

cap.release()
cv2.destroyAllWindows()