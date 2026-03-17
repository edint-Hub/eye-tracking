# EdintEyetracking

시선 추적(Eye Tracking) 시스템 프로토타입.
웹캠, 비디오, 이미지 데이터로부터 MediaPipe Face Mesh를 이용해 눈동자와 홍채의 움직임을 정밀하게 추적합니다.
또한, 개별 사용자의 캘리브레이션 지원 및 데이터 라벨링을 지원하는 고급 분석 도구입니다.

## 핵심 기능 (Features)
* **정밀 계산**: 눈 중심점과 홍채 간 벡터를 분리 계산하여 시선 방향을 구함.
* **시각화 피드백**: 현재 응시하는 영역(3x3 그리드)을 실시간 화면에 표시.
* **캘리브레이션 지원**: 'c' 입력으로 카메라 응시 영점을 저장하고 보정함.
* **데이터 검증**: 입력된 정답 데이터를 기반으로 추론의 정합성을 검수.

## 사용 방법 (Usage)

```python
import cv2
from edint_eyetracking import MPIrisArea

tracker = MPIrisArea()

# 1. 스트리밍 모드로 웹캠 열기 (시각화 포함)
tracker.tracking_streaming(webcam_port=0, visible=True)

# 2. 이미지 모드 측정 (시각화 포함)
tracker.tracking_image("my_picture.jpg")

# 3. 데이터만 추출하는 API 방식 (시각화 없음)
frame = cv2.imread("my_picture.jpg")
result = tracker.process_frame_api(frame)
print(result["cell_name"])  # ex) 'Middle-Center'
```
