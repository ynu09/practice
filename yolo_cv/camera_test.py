import cv2

cap = cv2.VideoCapture(0)
# wsl 사용 시 추가설정
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
else:
    print("카메라가 작동 중입니다. ESC를 눌러 종료하세요.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break
        cv2.imshow("Camera Frame", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC 키
            break
    cap.release()
    cv2.destroyAllWindows()