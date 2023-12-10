# Virtual-Force-Ping-Pong
&lt;Virtual Force Ping Pong>은 가상 현실 기술을 기반으로 한 혁신적인 게임입니다. 플레이어들은 힘 피드백 장갑을 착용하고 탁구 배트를 잡아 게임을 즐길 수 있습니다. 힘 피드백 장갑은 진동과 힘을 실감할 수 있도록 제작되어, 플레이어들은 마치 실제 탁구 경기를 하는 듯한 현실적인 경험을 할 수 있습니다.

# 특징

몰입감 있는 힘 피드백: 게임은 몰입감 있는 힘 피드백을 제공하여 탁구 경기의 감정과 힘을 생생하게 재현합니다. 플레이어들은 탁구 공의 충돌과 배트의 스윙을 실감하며, 정확한 타이밍과 적절한 힘으로 경기를 플레이해야 합니다.<br>
다양한 난이도와 게임 모드: 게임은 다양한 난이도 설정과 게임 모드를 제공하여 플레이어들의 요구에 맞는 도전과 즐거움을 제공합니다.<br>
다양한 적용 분야: <Virtual Force Ping Pong>은 게임과 엔터테인먼트 산업, 스포츠 훈련 및 체육 분야 등 다양한 분야에서 적용 가능성을 가지고 있습니다. 이 게임은 게임 플랫폼을 넘어서 다양한 가상 현실 장비와 플랫폼을 지원하며, 지속적인 업데이트와 개선을 통해 사용자들에게 새로운 경험과 기능을 제공할 수 있습니다.<br>

## 프로젝트 개요

이 프로젝트는 Arduino와 아두이노 호환 보드인 CH340 DM72, 그리고 아두이노 6축 자이로센서 MPU6050 1자납땜 DM399을 사용하여 구성되어 있습니다. 이 장비들을 통해 탁구 공을 치는 과정에서 발생하는 가속도 데이터를 수집하고 분석합니다. 수집한 데이터는 FFT(고속 푸리에 변환)와 지수 감쇄 정현파 함수 모델 분석을 통해 해석됩니다.현실과 가상현실에서 수집한 가속도 데이터를 Jr값으로 계산하고 분석합니다. Jr값을 Z-분수로 정규화분포를 가시화하고 분석하고 대비하며 BhapticsTactGlove에 매핑합니다. 

## 구성 요소

이 프로젝트에서 사용되는 구성 요소는 다음과 같습니다:
- 아두이노 우노 R3 호환 보드 CH340 DM72: 아두이노 호환 보드로서 주요한 마이크로컨트롤러 기반 보드입니다.
- 아두이노 6축 자이로센서 MPU6050 1자납땜 DM399: 공간의 가속도 및 회전 속도를 측정하는 6축 센서입니다.
- Unity: Unity는 게임 및 가상 현실(VR) 개발을 위한 강력한 플랫폼으로 다양한 도구와 기능을 제공합니다.
- BhapticsTactGlove: BhapticsTactGlove는 터치 및 진동을 통해 가상 경험을 향상시키는 감각 피드백 장갑입니다.

## 사용법

1. 아두이노 우노 R3 호환 보드 CH340 DM72와 아두이노 6축 자이로센서 MPU6050 1자납땜 DM399를 라켓에 고정합니다.
<img width="400" alt="截屏2023-06-20 16 12 20" src="https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/ecabe9c6-e6d8-455f-a05d-654b71ec14bf"><br>
2. MPU6050 센서를 아두이노 보드에 연결합니다.
3. 프로젝트 코드를 아두이노 개발 환경에 업로드합니다.
4. 탁구 라켓을 휘두르며 가속도 데이터를 수집합니다.
5. 수집한 데이터를 python으로 FFT 및 지수 감쇄 정현파 함수 모델 분석을 수행합니다.
6. FFT:https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/blob/main/FFT.py<br>
slow:<br>
![slow_频谱](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/9a2f3f73-2377-4562-ae14-5cbe12c42696)
near:<br>
![near_频谱](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/d09794fb-87c0-4b91-bfc4-a1783516ea7c)
fast:<br>
![fast_频谱](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/5bff803c-e5ad-479b-8e50-c67387605de7)
far:<br>
![far_频谱](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/be4f0606-331f-4551-a5d8-0460612fd21c)
8. 지수 감쇄 정현파 함수 모델:https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/blob/main/Exponential%20Decaying%20Sine%20Function%20Model.py<br>
slow:<br>
![slow](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/c64dd1e9-9b2b-48bf-88e8-1a62391bd95c)<br>
near:<br>
![near](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/ff77161f-09f0-4d61-9af2-fbfdf6e82323)<br>
fast:<br>
![fast](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/97435947-3e75-40f0-8315-8147f25180ad)<br>
far:<br>
![far](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/af995d1c-7866-4ef6-bc9f-f4c721fe870f)<br>
9. 현실에서 수집된 가속도 데이터를 공식으로 Jr값으로 계산.<br>
![Jr값 게산](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/25e2f080-9430-4ce3-83cf-d6ba47aae28d)<br>
10. 수집된 Jr값을 Z-분수로 정규화분포를 가시화하며 분석합니다.<br>
![Z-분수 정규화분포](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/59d81cb4-9c8d-45a4-b083-664d69c56bf8)<br>
11. 가상현실(Unity)에서 탁구공 훈련기 agent로 직접 계산된 Jr값을 출력합니다.<br>
12. 가상현실에서 수집된 Jr값을 Z-분수로 정규화분포를 가시화하며 분석합니다.<br>
라켓:<br>
![Z-분수 정규화분포](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/4112d09b-487c-4d2f-8faf-8c6ab1401595)<br>
13. 5개손락도 따로 Jr값을 구하고 Z-분수로 정규화분포를 가시화하며 분석합니다.<br>
Finger 1:<br>
![Finger 1](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/b29cd0a5-0aaf-4255-a508-4aea36c44279)<br>
![Finger 1](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/b7db4d3a-e20e-47bf-a93e-18c9c9727551)<br>
Finger 2:<br>
![Finger 2](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/7fd34a9d-4aa6-4d6c-8c9e-d9d08ddb826c)<br>
![Finger 2](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/28df9188-8224-45a4-a258-068623cef899)<br>
Finger 3:<br>
![Finger 3](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/bbb8c108-64e0-49e5-b36d-46f13db64f26)<br>
![Finger 3](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/967d2e32-a90b-4137-acb0-d832ed042e46)<br>
Finger 4:<br>
![Finger 4](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/f9524461-dd94-459c-9911-63bbbc181663)<br>
![Finger 4](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/5c9bb282-98fa-49d6-bf00-95287b4941b1)<br>
Finger 5:<br>
![Finger 5](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/404d3508-0c5c-43fb-aa3a-78a6395cdf97)<br>
![Finger 5](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/515f21da-9f25-401d-9789-51bd82e682e1)<br>
5개 손가락 합친 원시 데이터 가시화:<br>
![Finger sum](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/1ad5350f-e335-4cf4-a701-d4602c9c374f)<br>
5개 손가락 합치는 Z-분수 가시화:<br>
![Finger Z-분수](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/16515d24-f65f-456a-b4cb-e47aa43adf44)<br>
라켓에 해당하는 Z 점수 구간을 관찰하여 합쳐진 손가락의 정규 분포에서 매개 손가락이 받은 충격량을 확인합니다. 라켓이 공을 칠 때 매개 손가락이 받은 충격량의 차이를 통해 해당하는 고정된 진동 이벤트를 발생시킵니다.<br>
그러나 손가락의 정규 분포로 보면, 매개 손가락이 받은 충격량의 차이는 작습니다. Bhaptics 개발자 도구에서 진동 이벤트를 디자인할 때 진동 강도는 10%씩만 증가할 수 있어서 10과 20의 진동 감각 차이는 아주 작습니다. 따라서 우리는 라켓이 받은 충격량 분포를 기반으로 매개 손가락에 전달되는 진동 이벤트를 동일하게 설정했습니다. 현실적인 느낌과 비교했을 때 차이가 거의 없습니다. 탁구를 칠 때 발생하는 감각과 진동의 경험은 순간적이기 때문에 매개 손가락에 받은 감각 차이는 거의 무시할 수 있습니다. 그래서 Unity 가상 환경에서 라켓이 공을 칠 때 Bhaptics를 통해 매개 손가락에 전달되는 진동 크기도 동일하게 설정하여 시스템을 개발했습니다.<br>
그래서 라켓으로 매핑할 예정입니다.<br>
15. Z-분수 정규화분포로 BhapticsTactGlove에 매핑합니다.<br>
BhapticEventLibrary에서 진동event 호출 기능:<br>
![BhapticEventLibrar 디자인](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/1e2a2fd4-d454-4ecd-9955-1d460bc0572b)<br>
부동한 충격량에 따라 부동한 진동강도크기 호출 기능:<br>
![BhapticEventLibrar 디자인](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/72e1e71a-004b-4f4c-87a4-5d7a4cf7febe)<br>
매핑:<br>
힘 피드백의 진동 강도는 Z-분수의 정규 분포도(-2 ~ 3)에 기반하여 다양한 구간으로 분류됩니다. 예를 들어, Z-분수가 -2 미만인 경우 진동 강도는 10, -2에서 -1 사이일 경우 20, -1에서 0 사이일 경우 40, 0에서 1 사이일 경우 50, 1에서 2 사이일 경우 60, 2에서 3 사이일 경우 80, 3 이상인 경우 90으로 설정됩니다. 이러한 개인화된 힘 피드백 매핑은 플레이어가 힘 피드백을 통해 탁구를 칠 때의 현실적인 강도를 느낄 수 있도록 합니다.<br>
![BhapticEventLibrar 디자인](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/9527b2a5-2922-471d-a80f-88ddc31481cb)<br>
## 참고 자료

- 아두이노 공식 사이트: [https://www.arduino.cc/](https://www.arduino.cc/)
- MPU6050 라이브러리: [https://github.com/jrowberg/i2cdevlib/tree/master/Arduino/MPU6050](https://github.com/jrowberg/i2cdevlib/tree/master/Arduino/MPU6050)

