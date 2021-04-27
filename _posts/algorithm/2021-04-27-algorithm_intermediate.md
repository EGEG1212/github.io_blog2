---
layout: post
current: post
cover: assets/built/images/algorithm-logo.png
navigation: True
title: 컴퓨터 알고리즘 중급
date: 2021-04-18 16:40:00
tags: [algorithm]
class: post-template
subclass: "post tag-algorithm"
author: egeg1212
---

{% include algorithm-table-of-contents.html %}

# 컴퓨터 알고리즘 중급

> ... ㄱㄱㄱ

<br><br>

| **강좌정보** | [Tacademy강좌링크](https://tacademy.skplanet.com/live/player/onlineLectureDetail.action?seq=104)                                                                                        |
| :----------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **학습내용** | Graph, Greedy, Dynamic programming 등 컴퓨터 알고리즘 이론을 보다 깊이 있게 학습하고 이해한다.<br>Maximum Flow, Number Theory, String matching 등의 심화 알고리즘 관련 지식을 학습한다. |
|   **강사**   | 조호성 박사 (한양대학교 SW융합원)                                                                                                                                                       |
| **학습기간** | 2021.04.27~ + 테스트20문항 **이수중**                                                                                                                                                   |
| **학습시간** | **이수중**                                                                                                                                                                              |
| **강의목록** | [1강] 컴퓨터 알고리즘 성능분석(1)                                                                                                                                                       |
|              | [2강] 컴퓨터 알고리즘 성능분석(2)                                                                                                                                                       |
|              | [3강] 확률분석(1)                                                                                                                                                                       |
|              | [4강] 확률분석(2)                                                                                                                                                                       |
|              | [5강] 동적계획법(1)                                                                                                                                                                     |
|              | [6강] 동적계획법(2)                                                                                                                                                                     |
|              | [7강] Greedy Approach(1)                                                                                                                                                                |
|              | [8강] Greedy Approach(2)                                                                                                                                                                |
|              | [9강] 스트링 매칭(1)                                                                                                                                                                    |
|              | [10강] 스트링 매칭 (2)                                                                                                                                                                  |
|              | [11강] 정수론(1)                                                                                                                                                                        |
|              | [12강] 정수론 (2)                                                                                                                                                                       |
|              | [13강] Flow networks (1)                                                                                                                                                                |
|              | [14강] Flow networks (2)                                                                                                                                                                |
|              | [15강] Amortized Analysis                                                                                                                                                               |
|  **GitHub**  | None                                                                                                                                                                                    |

<br>

### 컴퓨터 알고리즘 정의 4가지

**문제를 해결하기 위한 과정을 상세하게 단계적으로 표현한 것**으로 입력과 출력으로 문제를 정의
|단계|내용|
|:-:|:-:|
|문제정의|현실 세계의 문제를 컴퓨터를 이용하여 풀 수 있도록 입력과 출력의 형태로 정의|
|알고리즘 설명|문제를 해결하기 위한 단계를 차례대로 설명|
|정확성 증명|항상 올바른 답을 내고 정상적으로 종료되는지 증명|
|성능분석|수행시간이나 사용공간에 대한 알고리즘의 성능을 비교하기 위한 분석|
가장 적합한 알고리즘을 고르기 위해 성능평가와 비교가 필요하다.
어떻게 하면 **객관적**으로 분석할 수 있는가?
ex) 특정기계X, 절대적시간X
그래서 상대적인 평가를 할 수 있는 **점근적 표기법(Asymptotic notations)** 을 사용해야 한다!

- $O$-notation : 점근적 상한(_asymptotic upper bound_)아무리 느려도 기준함수보다 느리다
- $\Omega$-notation : 점근적 하한(_asymptotic lower bound_) 항상 빠르다
- $\Theta$-notation : 그 사이
  $$T(n) = 3T([n/4])+\Theta(n^2)$$
  **대체법(Substitution Method)**
  재귀알고리즘은 T(n)으로 간단히 계산하기가 쉽지 않기 때문에(자기자신을 다시 리콜하기때문에.. 다차식형태로 변환해야함)<br>해답의 형태를 추측하는 수학적 귀납법을 이용하여 추측한 해답이 맞음을 증명함.
  (다차식으로 변환하는 방법 3가지)
- Substitution Method : 값을 대체해서 계산하여 증명!!!
- Recursion-tree Method : 재귀를 트리형태로 그려보고 트리형태의 값이 무엇인지
- Master Method : 공식에 넣어서 적용

#### 재귀 트리를 이용한 성능분석

(주어진 함수에 값을 추측하고. 추측한것을 대체법을 이용하여 증명.)
재귀 함수의 성능 분석을 위해 재귀 트리를 그려 해답을 추측하고(Recursion-tree Method),<br>이를 대체법(Substitution Method)을 이용하여 증명하는 방법이 있음.
(각 노드들을 코스트로 계산, 레벨들의 합을 구하고, 전체 트리의 합을 구함. )
