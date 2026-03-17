import cv2
from edint_eyetracking import MPIrisArea

def main():
    tracker = MPIrisArea()
    
    # 웹캠에서 이미지 하나를 읽습니다.
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    if ret:
        # process_frame_api를 사용하여 시각화 없이 순수 데이터만 추출합니다.
        result = tracker.process_frame_api(frame)
        
        print("API 추출 결과:")
        print(f"얼굴 인식 여부: {result['face_detected']}")
        
        if result['face_detected']:
            print(f"바라보는 좌표 (X, Y): ({result['cell_x']}, {result['cell_y']})")
            print(f"바라보는 영역 이름: {result['cell_name']}")
            print(f"평균 시선 중심: {result['avg_eye_center']}")
            print(f"시선 끝 방향 (Gaze Point): {result['gaze_point']}")
            
    cap.release()

if __name__ == "__main__":
    main()
