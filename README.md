# Virtual-Force-Ping-Pong
&lt;Virtual Force Ping Pong>은 가상 현실 기술을 기반으로 한 혁신적인 게임입니다. 플레이어들은 힘 피드백 장갑을 착용하고 탁구 배트를 잡아 게임을 즐길 수 있습니다. 힘 피드백 장갑은 진동과 힘을 실감할 수 있도록 제작되어, 플레이어들은 마치 실제 탁구 경기를 하는 듯한 현실적인 경험을 할 수 있습니다.

# 특징

몰입감 있는 힘 피드백: 게임은 몰입감 있는 힘 피드백을 제공하여 탁구 경기의 감정과 힘을 생생하게 재현합니다. 플레이어들은 탁구 공의 충돌과 배트의 스윙을 실감하며, 정확한 타이밍과 적절한 힘으로 경기를 플레이해야 합니다.<br>
다양한 난이도와 게임 모드: 게임은 다양한 난이도 설정과 게임 모드를 제공하여 플레이어들의 요구에 맞는 도전과 즐거움을 제공합니다.<br>
다양한 적용 분야: <Virtual Force Ping Pong>은 게임과 엔터테인먼트 산업, 스포츠 훈련 및 체육 분야 등 다양한 분야에서 적용 가능성을 가지고 있습니다. 이 게임은 게임 플랫폼을 넘어서 다양한 가상 현실 장비와 플랫폼을 지원하며, 지속적인 업데이트와 개선을 통해 사용자들에게 새로운 경험과 기능을 제공할 수 있습니다.<br>

## 프로젝트 개요

이 프로젝트는 Arduino와 아두이노 호환 보드인 CH340 DM72, 그리고 아두이노 6축 자이로센서 MPU6050 1자납땜 DM399을 사용하여 구성되어 있습니다. 이 장비들을 통해 탁구 공을 치는 과정에서 발생하는 가속도 데이터를 수집하고 분석합니다. 수집한 데이터는 FFT(고속 푸리에 변환)와 지수 감쇄 정현파 함수 모델 분석을 통해 해석됩니다.

## 구성 요소

이 프로젝트에서 사용되는 구성 요소는 다음과 같습니다:
- 아두이노 우노 R3 호환 보드 CH340 DM72: 아두이노 호환 보드로서 주요한 마이크로컨트롤러 기반 보드입니다.
- 아두이노 6축 자이로센서 MPU6050 1자납땜 DM399: 공간의 가속도 및 회전 속도를 측정하는 6축 센서입니다.

## 사용법

1. 아두이노 우노 R3 호환 보드 CH340 DM72와 아두이노 6축 자이로센서 MPU6050 1자납땜 DM399를 라켓에 고정합니다.
<img width="400" alt="截屏2023-06-20 16 12 20" src="https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/ecabe9c6-e6d8-455f-a05d-654b71ec14bf"><br>
2. MPU6050 센서를 아두이노 보드에 연결합니다.
3. 프로젝트 코드를 아두이노 개발 환경에 업로드합니다.
4. 탁구 라켓을 휘두르며 가속도 데이터를 수집합니다.
5. 수집한 데이터를 python으로 FFT 및 지수 감쇄 정현파 함수 모델 분석을 수행합니다.
6. FFT:https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/blob/main/FFT.py<br>
<center>slow<br></center>
![slow_频谱](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/9a2f3f73-2377-4562-ae14-5cbe12c42696)
<center>near<br></center>
![near_频谱](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/d09794fb-87c0-4b91-bfc4-a1783516ea7c)
<center>fast<br></center>
![fast_频谱](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/5bff803c-e5ad-479b-8e50-c67387605de7)
<center>far<br></center>
![far_频谱](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/be4f0606-331f-4551-a5d8-0460612fd21c)
8. 지수 감쇄 정현파 함수 모델:https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/blob/main/Exponential%20Decaying%20Sine%20Function%20Model.py<br>
<center>slow<br></center>
![slow](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/c64dd1e9-9b2b-48bf-88e8-1a62391bd95c)
<center>near<br></center>
![near](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/ff77161f-09f0-4d61-9af2-fbfdf6e82323)
<cenetr>fast<br></cenetr>
![fast](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/97435947-3e75-40f0-8315-8147f25180ad)
<center>far<br></center>
![far](https://github.com/yuanguangzhe/Virtual-Force-Ping-Pong/assets/75521945/af995d1c-7866-4ef6-bc9f-f4c721fe870f)

## 참고 자료

- 아두이노 공식 사이트: [https://www.arduino.cc/](https://www.arduino.cc/)
- MPU6050 라이브러리: [https://github.com/jrowberg/i2cdevlib/tree/master/Arduino/MPU6050](https://github.com/jrowberg/i2cdevlib/tree/master/Arduino/MPU6050)

