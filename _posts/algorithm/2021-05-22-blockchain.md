---
layout: post
current: post
cover: assets/built/images/logo-algorithm.png
navigation: True
title: 블록체인 기술적 특징과 비즈니스 이해
date: 2021-05-22 16:40:00
tags: [algorithm]
class: post-template
subclass: "post tag-algorithm"
author: egeg1212
---

{% include table-of-contents-algorithm.html %}

# 블록체인 기술적 특징과 비즈니스 이해

> 블록체인 궁금하다궁금해!! 두근두근

<br><br>

| **강좌정보** | [Tacademy강좌링크](https://tacademy.skplanet.com/live/player/onlineLectureDetail.action?seq=139)                                                                                                                                                                            |
| :----------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **학습내용** | 1. 블록체인의 등장배경과 개념에 대해 알아본다.<br>2. 블록체인의 네트워크, 보안, 작업증명, 이중지불방지 등 주요 요소기술에 대해 알아본다.<br>3. 스마트 계약(이더리움)과 신뢰서비스의 작동원리에 대해 알아본다.<br>4. 다양한 블록체인 비즈니스 사례와 가능성에 대해 알아본다. |
|   **강사**   | 고덕윤 수석연구원 (피노텍) 2018.07.05 강의                                                                                                                                                                                                                                  |
| **학습기간** | 2021.05.22~2021.05.25 **이수완료**                                                                                                                                                                                                                                          |
| **학습시간** | **02:51:53**                                                                                                                                                                                                                                                                |
| **강의목록** | [1강] 블록체인의 개념                                                                                                                                                                                                                                                       |
|              | [2강] 블록체인 기술의 이해                                                                                                                                                                                                                                                  |
|              | [3강] 스마트 계약(이더리움)과 신뢰서비스                                                                                                                                                                                                                                    |
|              | [4강] 블록체인 비즈니스 사례                                                                                                                                                                                                                                                |
|  **GitHub**  | None                                                                                                                                                                                                                                                                        |

**<사전학습자료>**
▶ 블록체인 한번에 이해하기(뒤태지존님의 블로그)
<https://homoefficio.github.io/2017/11/19/%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8-%ED%95%9C-%EB%B2%88%EC%97%90-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0/>

▶ 비트코인과 블록체인 기술(NAVER D2)
<https://d2.naver.com/helloworld/8237898>

**NAVER AI NOW**
<https://naver-ai-now.kr/>

---

peer to peer네트워크 위변조방지
APK (개인키,공개키)생산주체명확하게,부인방지
타원암호알고리즘(ECC : Elliptic-curve cryptography)

블록체인 데이터의 진실성(BITCOIN)

1. 정보의 합의 도축
2. 출처의 명확성
3. 불가역적 데이터저장(한번쓴 데이터는 수정이 불가능하다.)

## [3강] 스마트 계약(이더리움)과 신뢰서비스

특정 검증된 프로그램에 따라 지불됨.
(중개업이 없어짐)

에스크로서비스
ICO
알트코인

| **스마트자산ex.** |                4강내용추가                 |
| :---------------: | :----------------------------------------: |
|       금융        |                해외송금veem                |
|       금융        |  ABRA-ATM기찾으러 시내안나가고 옆사람에게  |
|  다이아몬드이력   | 일련번호, 소유자, 특징, 감정서, 소유권이전 |
|    부동산산업     |      집주인에대한정보, 담보내역 등등       |
|       미술        |                   저작권                   |
|       음악        |                   저작권                   |
| 자동차매매,자전거 |      도난여부, 수리여부, 주인변경이력      |
|       식품        |     사료, 농장, 도축, 운반, 판매, 보관     |
|   에너지(충전)    |
|       정치        |                선거,의결권                 |

## [4강] 블록체인 비즈니스 사례

하이퍼렛져의 프리미엄 회원사 (IT, 금융, 종합, 의료*CHANGE*, 항공*AIRBUS*, 자동차*DAIMEER*)

Practical Byzantine Fault Tolerance
||PoW|PBFT|
|:-:|:-:|:-:|
|통신비용|단일노드의 통신비용은 낮음|다수의 통신을 하므로 높음|
|CPU연산비용|높음|낮음|
|최종|합의가 최종이 아닐 수 있음|과반의 의한 최종 합의|
|참가조건|아무나 참가 가능|허락된 서버만 참가 가능|
|비밀보호|사전 신뢰한 암호 사용|공개키 암호 사용|
|전력소모|매우 큼|적음|

**자전거블록체인**

- 자전거 등록
- 소유자 등록
- 잠금 유무 상태, 위치
- 도난여부
- 주인 변경 등록

**식품안정성 확보차원(월마트, IBM, 칭화대학교)**

- 사료, 농장, 도축, 운반, 판매, 보관 모두 기록

**해운MAERSK LINE**

**리플Ripple(은행을위한)**

- 아랍의 하왈라 시스템에서 영감을 얻음
- 국제간 신용 송금을 위한 코인
- 무료 페이팔 시스템

- **송금 시간을 3일에서 1시간 이내로 줄임**
- **은행의 송금서비스를 위한 코인**
- 진정한 탈중앙화는 아니라는 주장이 있음.

**데이터 시장의 탈중앙화(Steemit)스팀잇**

> 스팀잇은 게시자에게 접근 권한을 부여하고
> 제 3자의 광고 없이 콘텐츠로 수익을 창출할 수 있도록 했다.
> 우리의 주된 목표는 좋은 사람을 플랫폼으로 끌어들여 더 긍적적인 온라인 커뮤니티를 구축하는것이다 -네드스캇, 스팀잇CEO-

기존 블로그에 글을올려 광고다는것과 다른 방법.
글올리면 코인을 줌.

**저작권 관리와 유통을 위한 암호화폐(KodakCoin)**
음원과 저작권 유통에서 중개업자의 비용이 큼
(재생시 수익: 제작자44%>유통사40%>저작권자10%>실연권자6%)
암호화폐를 이용하여 중개비용을 최소화 하기 위한 노력

**의료정보의 활용을 위한 화폐 Medibloc메디블록**

- 파편화된 연구용 의료 데이터 문제
- 의료 정보 공유의 어려움
- 프라이버시 문제
- 안전한 의료 데이터 제공
- 효율적인 의료 데이터 공유
- 암호화폐를 이용한 의료 생태계 조성
