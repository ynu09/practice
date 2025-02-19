import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

cap = cv2.VideoCapture(0) # webcam
# wsl 사용 시 추가설정
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

# for i in range(0, 4):
#     cap = cv2.VideoCapture(i) # usb cam 2
#     if cap.isOpened():
#         break

while cap.isOpened():
    success, frame = cap.read()

    if success:
        # 프레임에 YOLOv11 객체 추론 실행
        results = model(frame)

        # 프레임에 결과 시각화
        annotated_frame = results[0].plot()

        # annotated frame 표시
        cv2.imshow("YOLO Inference", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()