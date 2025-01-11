import cv2
from ultralytics import YOLO

from collections import defaultdict
import numpy as np

model = YOLO('yolov8n.pt')

# 카메라 디바이스 확인: ls /dev/video*
# cap = cv2.VideoCapture(0) # 0 for default camera
for i in range(1, 4):
    cap = cv2.VideoCapture(i) # usb cam
    if cap.isOpened():
        break

# 추적 내역 저장
track_history = defaultdict(lambda: [])

while cap.isOpened():
    # 비디오 프레임 읽기
    # print(cap.read()) # (True/False, frame)
    success, frame = cap.read()
    
    if success:
        # 프레임에 YOLOv8 객체 추적 실행
        results = model.track(frame, persist=True)
        
        # 상자 및 추적 ID 가져오기
        boxes = results[0].boxes.xywh.cpu()
        track_ids = results[0].boxes.id

        if track_ids is not None:  # id가 None이 아닌 경우만 처리
            track_ids = track_ids.int().cpu().tolist()
        else:
            track_ids = []  # id 없으면 빈 리스트로 초기화

        # 프레임에 결과 시각화
        annotated_frame = results[0].plot()
        
        # 추적 플롯
        for box, track_id in zip(boxes, track_ids):
            x, y, w, h = box
            track = track_history[track_id]
            track.append((float(x), float(y)))  # x, y의 중심점
            if len(track) > 30:  # 90프레임에 대해 90개의 추적을 유지
                track.pop(0)

            # 추적 라인 그리기
            points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
            # [color] BGR 형식
            cv2.polylines(annotated_frame, [points], isClosed=False, color=(0, 0, 255), thickness=5)
        
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