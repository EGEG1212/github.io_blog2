---
layout: post
current: post
cover: assets/built/images/logo-voice.jpg
navigation: True
title: 음성인식-음성언어분야 AI 기술/산업 현황 및 구현기술의 이해
date: 2021-05-25 16:40:00
tags: [NLP]
class: post-template
subclass: "post tag-NLP"
author: egeg1212
---

## 음성인식-음성언어분야 AI 기술/산업 현황 및 구현기술의 이해

<br><br>

| **강좌정보** | [Tacademy강좌링크](https://tacademy.skplanet.com/live/player/onlineLectureDetail.action?seq=110)                                                                                                                                        |
| :----------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **학습내용** | 음성언어분야의 인공지능(AI) 기술 현황 및 음성인식/대화처리/자동통역/질의응답 등 주요 음성인식 기반 산업 현황을 이해하고, 음성인식 모델별(HMM/DNN/LSTM 등) 적용원리 및 알고리즘을 통해 딥러닝 기반 음성인식 요소 기술에 대해 알아봅니다. |
|   **강사**   | 이윤근, 김승희 (ETRI 음성지능연구그룹)                                                                                                                                                                                                  |
| **학습기간** | 2021.05.25~ **이수중**                                                                                                                                                                                                                  |
| **학습시간** | **이수중**                                                                                                                                                                                                                              |
| **강의목록** | [1강] 음성언어분야 인공지능(AI) 기술 / 산업현황                                                                                                                                                                                         |
|              | [2강] 딥러닝 기반 음성인식 기술                                                                                                                                                                                                         |

잡음이나 음향간섭등에 의해 음성입력이 왜곡.
해결방법:

- 잡음필터링(Kalman filter, Wiener filter 등),
  채널보상(channel compensation),
  음원분리 (source separation)
  빔포밍( beam forming) 등 다양항 잡음처리 방법 적용.

- 다양한 왜곡 신호를 음향모델에 포함하여 훈련시키는 방법 적용(multi-condition training)

운율 []
Emotional TTS(엄마가 아이게 동화책읽어주는)

- 합성음에 감정을 구현하는 기술
- 음의 높낮이, 세기, 음색 등의 변화가 심해 음질이 저하되며 제어하기가 어려움

Voice Conversion

- 특정인의 목소리로 변환하는 기술
- 특정인의 목소리를 나타내기 위해서는 음색 뿐만 아니라 발음, 억양 등 복합적인 요소가 작용

### 대화처리

Finite-State Machine
조금 더 나은 방법 Form-based model
information State model
|대화처리방법론|정의|특징||
|:-:|:-:|:-:|:-:|
|Topic-oriented Dialogue(주제 제한, 지식 처리)|구체적인 Topic에 대한 대화처리(ex.티켓예약, 상품구매/조회)|시스템주도형으로 대화흐름 제한, 특정Topic에 대한 대화흐름의 수동 지식화|혼합 주도형(mixed-initiative)대화관리: 시스템주도 및 사용자 주도 대화 가능, 대화 자유도 증가, |
|Chat-oriented Dialoque(주제 무세한, 패턴 처리)|목적없는 대화chat-bot/ Data-driven 방식의 예제 매칭 대화처리|문맥유지 없이 단순 반복 응답만 가능, 대화/응답 패턴의 수동 지식화|

**Switchboard Cellular**
예전부터 전화통화하는 부분은 음성인식이 잘 안됐다리 ㅠㅠㅠ
(출처: By Li Deng, Auedong, Communications of the ACM, 2004)

**자유대화 이해의 오류 사례(Apple SIRI)**
순서변경시 이해불가
2개 명령을 한꺼번에 발화시 이해불가
정해진 대화 시나리오 진행(정확한 사용자 응답 요구)
앞전 문맥을 유지하지 못함
특정 주제의 대화 진행 중, 다른 주제 대화 삽입시, 문맥 유지 오류 발생

...개인비서 불가능.
Apple SIRI
Google Assistant
MS Cortana
Amazon Echo 알렉사
삼성 S보이스
SKT NUGU
KT 기가지니
롯데 샬롯
