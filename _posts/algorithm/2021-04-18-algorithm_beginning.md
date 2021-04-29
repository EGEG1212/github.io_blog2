---
layout: post
current: post
cover: assets/built/images/algorithm-logo.png
navigation: True
title: 컴퓨터 알고리즘 초급
date: 2021-04-18 16:40:00
tags: [algorithm]
class: post-template
subclass: "post tag-algorithm"
author: egeg1212
---

{% include table-of-contents-algorithm.html %}

# 컴퓨터 알고리즘 초급

> 알고리즘.. 아직은 잘 모르겠지만...<br> 일단 고!!

<br><br>

| **강좌정보** | [Tacademy강좌링크](https://tacademy.skplanet.com/live/player/onlineLectureDetail.action?seq=83)                                                                                                                                                                                                                   |
| :----------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **학습내용** | 컴퓨터 알고리즘의 역할 및 필요성에 대해 이해합니다. <br> 시간복잡도를 통해 알고리즘을 분석하는 방법을 학습합니다.<br>배열, 큐, 트리 등 주요 자료구조에 대해 복습합니다.<br>정렬, 해쉬, 그래프, 탐욕, 스트링 알고리즘에 대해 학습하고 이해합니다. <br>응용문제를 통해 문제해결방법을 익히고 심화학습을 수행합니다. |
|   **강사**   | 조호성 박사 (한양대학교 SW융합원)                                                                                                                                                                                                                                                                                 |
| **학습기간** | 2021.04.18~2021.04.24 + 테스트20문항 **이수완료**                                                                                                                                                                                                                                                                 |
| **학습시간** | **07:55:56**                                                                                                                                                                                                                                                                                                      |
| **강의목록** | [1강] 컴퓨터 알고리즘 개요(1)                                                                                                                                                                                                                                                                                     |
|              | [2강] 컴퓨터 알고리즘 개요(2)                                                                                                                                                                                                                                                                                     |
|              | [3강] 정렬문제                                                                                                                                                                                                                                                                                                    |
|              | [4강] 삽입정렬                                                                                                                                                                                                                                                                                                    |
|              | [5강] 합병정렬                                                                                                                                                                                                                                                                                                    |
|              | [6강] 힙정렬(Heap Sort)(1)                                                                                                                                                                                                                                                                                        |
|              | [7강] 힙정렬(Heap Sort)(2)                                                                                                                                                                                                                                                                                        |
|              | [8강] 퀵 정렬 (Quick Sort)                                                                                                                                                                                                                                                                                        |
|              | [9강] 선형시간 정렬 알고리즘                                                                                                                                                                                                                                                                                      |
|              | [10강] 해쉬 알고리즘(1)                                                                                                                                                                                                                                                                                           |
|              | [11강] 해쉬 알고리즘(2)                                                                                                                                                                                                                                                                                           |
|              | [12강] 그래프의 기초                                                                                                                                                                                                                                                                                              |
|              | [13강] 그래프의 표현                                                                                                                                                                                                                                                                                              |
|              | [14강] 넓이 우선 탐색                                                                                                                                                                                                                                                                                             |
|              | [15강] 깊이 우선 탐색                                                                                                                                                                                                                                                                                             |
|              | [16강] 다익스트라 알고리즘                                                                                                                                                                                                                                                                                        |
|              | [17강] 벨만-포드 알고리즘                                                                                                                                                                                                                                                                                         |
|              | [18강] 플로이드-와샬 알고리즘                                                                                                                                                                                                                                                                                     |
|              | [19강] 탐욕 알고리즘                                                                                                                                                                                                                                                                                              |
|  **GitHub**  | None                                                                                                                                                                                                                                                                                                              |

<br>
### 컴퓨터 '알고리즘'의 정의. '프로그램'과 다르니 주의하자.

- 컴퓨터 알고리즘(Computer Algolithm)

  - 컴퓨터를 이용하여 주어진 문제를 효율적으로 풀기 위한 방법을 단계별로 명확하게 기술해 놓은 것.
  - 정렬알고리즘, 해시알고리즘, 최단거리알고리즘 등

- 컴퓨터 프로그램(Computer Program)
  - 컴퓨터가 특정 작업을 수행하기 위해 짜여진 명령의 순서

<br>
### 1. 컴퓨터 알고리즘을 설명하기 위한 4단계.

- **1.문제 정의** (Problem definition)
  - 해결하고자 하는 문제는 무엇인가?
  - 입력과 출력의 형태로 정의돌 수 있는가?
  - 컴퓨터가 수행할 수 있는 형태로 전환이 가능한가?
- **2.알고리즘 설명** (Algorithm description)
  - 컴퓨터가 수행해야 할 내용은 하나씩 차례대로 정의한 과정<br>(ex. 세탁기사용법, 라면끓이는법)
- **3.정확성 증명** (Correctness proof)
  - 과정대로 수행하면 출력으로 항상 올바른 답을 내보내는가?
  - 잘못된 답을 내보내는 경우는 없는가?
  - 올바른 출력을 내보내고 정상적으로 종료되는가?
- **4.성능 분석** (Performance analysis)
  - 수행시간 (Running time)
    - 수행연산의 횟수를 비교하는 방식
  - 사용공간 (Space consumption)
  - 비교대상
    - 산술연산(Arithmetic Calculation) : Add, Multiply, Exponent, Modular, ...
    - 데이터입출력(Data Movement) : Copy, Move, Save, Load, ...
    - 제어연산(Access Control) : If, While, Register,...

### 2. 점근적 표기법(Asymptotic notation)

$O$-notation 점근적 상한(_asymptotic upper bound_)
$\Omega$-notation 점근적 하한(_asymptotic lower bound_)
$\Theta$-notation 점근적 상한 및 하한(_asymptotically tight bound_)
...최악의 경우와 최선의 경우의 공통부분이다.

### 3. 정렬문제(Sorting problem)

$n$개의 숫자를 입력 받아, 입력받은 숫자들을 점점 커지는 순서나 점점 작아지는 순서로 다시 배열하여 출력하는 문제.

- 오름차순(Increasing Order)
- 내림차순(Decreasing Order)

**선택정렬(Selection sort) 알고리즘**
정렬문제를 푸는 컴퓨터 알고리즘 중의 하나. 현재 상황에서 가장 작거나 가장 큰 숫자를 선택하여 <u>_재배치_</u>하는 아이디어로 정렬문제를 해결하며 <br> 시간복잡도는 $\theta(n^2)$

- 최소값 선택 정렬(Min-Selection sort) : 오름차순
- 최대값 선택 정렬(Max-Selection sort) : 내림차순

**삽입정렬(Insertion sort) 알고리즘**
key값과 정렬된 리스트가 주어졌을 때, key값을 정렬된 리스트의 <u>_알맞은 위치_</u>에 삽입.<br>시간복잡도는 $\theta(n^2)$ <br>제자리정렬(Sorted in place)이므로 추가공간을 사용하지 않는다.
![InsertSort](https://github.com/EGEG1212/egeg1212.github.io/blob/main/_img/2021-04-18-insert.PNG)

**합병정렬(Merge Sort)**
이미 정렬된 두 개의 배열을 입력으로 받아, 정렬된 하나의 배열을 출력하는 정렬알고리즘.
시간복잡도 $\theta(nlogn)$ 아니고 $O(nlgn)$ 였던가...

- 비교compare와 이동move 함수 사용.
- **A divide-ane-conquer approach**
  크기가 커서 풀기 어려운 하나의 문제를
  크기를 작게 풀기 쉬운 여러 개의 문제로 바꾸어서 푸는 방법.
  > Divide 나누고
  > Conquer 합병정렬을 사용하여 두 개의 배열로 정렬하고
  > Combine 두 개의 정렬된 배열을 하나로 합치는 과정
  > ![MergeSort](https://github.com/EGEG1212/egeg1212.github.io/blob/main/_img/2021-04-18-merge.PNG)

$A$ : n개의 숫자가 들어있는 배열
$p$ : 배열의 첫번째 인덱스
$r$ : 배열이 마지막 인덱스
![MergeSortPseudoCode](https://github.com/EGEG1212/egeg1212.github.io/blob/main/_img/2021-04-18-mergecode.PNG)

**힙정렬(Heap Sort)**
수행시간은 합병정렬과 동일한 $O(nlgn)$
삽입정렬과 동일한 제자리 정렬 (Sort in Place)

- Min-Heap
- Max-Heap
  - 조건1 : 완전 이진트리(Binary tree)
  - 조건2 : 부모 노드의 값은 항상 자식 노드의 값보다 크다.
    - 이 조건이 유지되도록 바꾸는 연산 힙특성관리(Maintaining the heap property)
      **Max-Heapify**
      ![MaxHeapify](https://github.com/EGEG1212/egeg1212.github.io/blob/main/_img/2021-04-18-MaxHeapify.PNG)
- **1.힙 구조 만들기 (Building a heap)**
  Root 노드 방향으로 거슬러 올라가면서 MAX-HEAPIFY를 진행.
  수행하는 시간 $O(nlgn)$
- **2.최대값 추출 (Extract-Max)**
  Heap에서 가장 큰 값을 제거하고 Max-heap구조를 복원하는 연산
- **3.힙 소트 (Heap Sort)**
  수행하는 시간 $O(nlgn)$
  Extract-Max를 n번 반복
  시간복잡도는 $\Theta(nlgn)$

**퀵정렬(Quicksort)**
퀵정렬은 Pivot과 partition을 이요하여 크기가 작은 숫자는 계속 앞쪽으로 이동시키고,
크기가 큰 숫자는 계속 뒤쪽으로 이동시켜 정렬문제를 해결하는 알고리즘으로
시간복잡도는 $\Theta(nlgn)$

Divide-and-Conquer paradigm을 사용 (**Partition**)
(정렬문제를 풀 수 있는 알고리즘은 아니다;)
Partition의 수행시간

- Partition에 걸리는 시간 **$\Theta(n)$**
- Partition의 횟수
  - 경우에 따라 횟수가 달라진다
  - 1. Balanced partitioning 수행시간 **$\Theta(nlgn)$**
       각 하위 문제의 크기가 기존 문제의 크기의 절반정도로 나누어짐(바이너리 비슷)
  - 2. unbalanced partitioning **$\Theta(n^2)$**
       한개 그리고 나머지..최악의경우

|                |   BEST case    |     Average case     |      Worst case      |
| :------------: | :------------: | :------------------: | :------------------: |
| Insertion sort |  $\Theta(n)$   |    $\Theta(n^2)$     |    $\Theta(n^2)$     |
|   Merge sort   | $\Theta(nlgn)$ |    $\Theta(nlgn)$    | **$\Theta(nlgn)$\*** |
| selection sort | $\Theta(n^2)$  |    $\Theta(n^2)$     |    $\Theta(n^2)$     |
|    Heapsort    |  $\Theta(n)$   |          -           | **$\Theta(nlgn)$\*** |
|   Quicksort    | $\Theta(nlgn)$ | **$\Theta(nlgn)$\*** |    $\Theta(n^2)$     |

> 두 숫자를 비교해서 어떤것이 큰지,작은지 판단해야하는 경우이다.
> 들어오는 데이터와 공간을 생각해서 적합한걸 골라야한다
> Merge sort - 추가공간 필요하다는 단점;
> Heapsort - Heap구조를 만들고 구조를 유지해야한다는 단점;
> Quicksort - pivot이 어떻게 뽑이냐에 따라 성능차이가 있음;

---

### 선형시간 정렬 알고리즘

> 숫자가 몇개인지를 세어보거나, 각 숫자의 자릿수들 끼리만 비교하는 방법을 통해 정렬해야하는 경우이다.

**계수정렬**
입력 받은 배열에 있는 숫자의 범위를 확인하고
몇 개가 있는지를 세어보고 정렬하는 알고리즘으로
시간복잡도는 $\Theta(n)$

> 동일한숫자가 여러개 들어오는 데이터에는 계수정렬이 유리하다
> 숫자의 범위가 적을때 계수정렬이 유리하다.

**기수정렬(Radix sort)**
입력 받은 배열에 있는 숫자를 각 자리끼리 비교하여 정렬하는 알고리즘으로
시간복잡도는 $\Theta(n)$
LSB -> MSB : 1의자리부터 비교해서 정렬함
(숫자의 자릿수가 모두 같아야 쓸 수 있음)
(선형시간에 정렬이 가능하다.)

### 해쉬 알고리즘

**Direct-Address Tables**
검색, 삽입, 삭제가 빠른 장점이 있지만
실제 사용하는 공간이 낭비되는 경우가 많음

**Hash Tables**
Direct-Address Tables에서 공간낭비를 줄이면서도
시간복잡도를 낮추기 위해서 사용하지만 충돌문제가 있으며
이를 해결하기 위한 Chained Hash Table은 시간이 느려질 수 있음

**Open Addressing**
Collision을 피하기 위한 다른 방법으로 key를 hash table에 직접 저장
자료를 직접 기록하는 방법으로 검색, 삽입, 삭제가 빠르지만 충돌의 가능성이 있어서
Linear Probing, Quadratic Probing, Double Hashing등의 방법을 이용하여 충돌을 최소화할 필요가 있디.

- **Open Addressing 장점: 포인터를 사용하지 않아도 되므로 구현이 간편!! 추가 메모리 공간 사용 가능!!**
- **Open Addressing의 기술3가지**

1. **선형프로빙(Linear Probing )**
   삽입 연산(Insertion)
   빈 slot이 나올 때까지 해쉬 테이블을 탐색(다음다음다음다음)
   선형적인 형태로 충돌이 발생하면 1씩 증가하면서 빈 slot을 찾는 작업을 반복한다.
   **장점**: 구현이 매우 쉽다
   **단점**: primary clustering문제-key값을 넣을 빈 slot은 뭉쳐있는 slot들의 끝부분에 존재하기 때문에 값이 들어있는 slot들이 뭉쳐있는 경우가 많다. 검색시간증가.
2. **이차식프로빙(Quadratic Probing)**
   주어진 Hash함수 외에 i에 대한 2차함수꼴로 slot을 이동하면서 빈 slot을 찾는다.
   **단점**: 만약 두 key의 처음 probe 값이 동일하다면 빈slot을 찾는 과정이 동일하므로 같은 slot을 탐색 (Mod).. 이런특성을 secondary clustering이라 부른다.
   즉, 처음 충돌한 위치가 같다면 다음 충돌할 위치에서도 반복적으로 계속 충돌이 나게 됨.
3. **이중해싱(Double Hashing)**
   $$h(k,i)=(h_1(k)+i*h_2(k))\pmod{m}$$
   해싱함수를 2개사용.
   충돌이 발생했을 때, 이동하는 거리가 hash함수에 의해 계산되어 무작위로 빈 slot을 찾게 한다.
   **주의점**: $h_2(k)$함수는 해쉬 테이블의 크기 $m$과 서로 소 관계여야 한다.
   이것을 만족하는 가장 쉬운 방법은 $m$을 2의 지수승으로 두고 $h_2$가 항상 홀수가 되도록 만드는 것이다.
   다른 방법은 $m$을 소수로 하고 $h_2$을 $m$보다 작은 양수로 정하는 것이다.

### 그래프 기초(Graph Basics)

V : Vertex(정점) 정점은 독립된 개체 Stand-alone object로 동그라미로 표현한다.
E : edge(간선)
---> A directed graph 방향성이 있는 간선을 가지고 있는 그래프(화살표 Arrows)
--- An undirected graph 무방향성 간선을 가진 그래프(직선 line)
Degree(차수) - 정점의 진출차수(out-degree) - 정점의 진입차수(in-degree) - 차수는 진입차수와 진출차수의 합이다.

Path(경로) 정점 u로부터 정점 v까지의 경로는 정점의 순서이다.
length(경로의 길이)는 경로에 있는 간선의 수이다.
Simple path(단순경로)는 경로에 있는 모든 정점들이 서로 다른 경우이다.
Cycle(순환) ex)<1,2,4,5,4,1>
simple cycle(단일순환) ex)<1,2,4,1> - An acyclic graph(비순환그래프) : 순환이 없는 그래프 - A connected graph(연결그래프) : 정점의 모든 쌍들이 경로를 가지는 무방향성 그래프 - Connected components(연결요소) : 무방향성 그래프에서 정점들이 최대한 연결되어 있는 하위 그래프

A complete graph(완전그래프) - Forest(포레스트) : 순환하지 않는 무방향성 그래프 - Tree(트리) : 포레스트가 연결되어 있는 경우/
연결된 비순환 무방향성 그래프
**Connected, Acyclic, Undirected Graph**

### 그래프의 표현(Graph representation)

1. 인접리스트 표현(Adjacency-list representation)
   정점 하나에 인접한 모든 정점을 리스트에 저장 (A directed graph경우)
   방향성그래프로 변환해서 저장(An undirected graph경우) **$\Theta(V+E)$space**
2. 인접행렬 표현(Adjacency-matrix representation)
   두 정점 i와 j를 잇는 간선이 있다면 행렬의 (i,j)는 1, 아니면 0
   **$\Theta(V^2)$space**
   무방향성은 양방향으로 간선이 존재하므로 하위 삼각 행렬이 상위 삼각 행렬과 대칭된다(lower triangular matrix)
3. 인접리스트와 인접행렬의 비교
   - 저장공간
     G가 성기면, 인접리스트가 낫다. 이유는 $|E|<|V|^2$
     G가 촘촘하면, 인접행렬이 낫다. 행렬은 1비트만 사용하므로
   - 간선을 찾는데 걸리는 시간
     인접행렬 : $\Theta(1)$time
     인접리스트 : $O(V)$time
   - 모든 간선을 찾거나 방문하는데 걸리는 시간
     인접행렬 : $\Theta(V^2)$
     인접리스트 : $\Theta(V+E)$

가중그래프(Weighted graph) : 간선이 숫자로 표현되는 값을 가지는 그래프
가중그래프표현(Weighted graph representation) :

- 인접리스트에서는 정점 외에 간선의 값을 추가 저장
- 인접행렬에서는 1대신 간선의 값을 저장

### 넓이 우선 탐색(Breadth-first search)

**거리**를 우선으로 그래프를 탐색하는 알고리즘
정점들을 차례대로 탐색하기 위해 사용하는 자료구조는 queue

수행시간 분석

- 초기화 시간: $\Theta(V)$
- 그래프 탐색 시간 $O(V+E)$
  정점은 최대 한 번만 조사된다.
  간선은 최대 두 번 조사된다.
- 따라서, 전체 수행시간 : $O(V+E)$

### 깊이 우선 탐색(Depth-first search)

**시간**을 우선으로 그래프를 탐색하는 알고리즘으로 시작점으로부터 인접한 정점을 차례대로 방문함.
무방향성 그래프의 깊이 우선 탐색에서, 그래프의 각 간선은 트리간선이거나 후향간선이다.
자료구조 queue가 아니다!!!!!!!!!

타임스탬프(Timestamps)
각 정점은 타임스탬프를 두 개씩 가지고 있다.
$v.d$ : 발견시간(Discovery time, when v is grayed)
$v.f$ : 완료시간(finishing time, when v is blacken)

수행시간 분석 $\Theta(V+E)$ 시간복잡도가 이거였나????
시간복잡도는 $O(n2)$

### 다익스트라 알고리즘(Dijkstra's algorithm)

최단경로문제를 해결하는 다익스트라 알고리즘 **정점을 하나씩 추가**하면서 완화를 통해 새로운 경로에서 경로값을 계산하여 새로운 경로를 추가하여 최단 경로를 찾는 알고리즘.
하나의 시작점(Source)에서 하나의 도착점(Destinanion)을 가는 최단경로를 찾는 알고리즘.
**간선이 음의 값을 가져서는 안 된다.(non-negative edges only)**

최단 경로 문제
최단경로문제는 출발점과 도착점이 모두 주어졌을 때, 두 정점을 연결하는 최단경로값을 찾는 문제로 Single Source-Single Deatination가 대표적
가중간선(Edge weight)
가중경로(Path weight) : 경로에 속하는 모든 간선의 값을 더한 값

수행시간 분석
배열로 구현한 경우 : $O(V^2)$
힙구조로 구현한 경우 : $O(VlgV+ElgV)$
피보나치 힙으로 구현한 경우 : $O(VlgV+E)$

### 벨만-포드 알고리즘(The Bellman-Ford algorithm)

음의 값을 가지는 그래프에서 Relax를 이용하여 순환문제를 회피하고 최단경로 문제를 해결하는 알고리즘.
하나의 시작점에서 하나의 도착점으로 가는 최단경로 문제를 해결하는 알고리즘이다.
음의 간선이 있는 경우에도 문제를 해결한다.
수행시간 : $O(VE)$

- **음수간선값(Negative-weight edges)**
  최단경로는 출발점으로부터 도달가능하며 음의 값을 가지는 순환이 없는 경우로 생각할 수 있다.

- **최단경로와 순환(Cycles)**
  최단경로는 순환을 포함해서는 안 된다.

- **직전 정점 하위 그래프(Predecessor subgraph)**
  최단경로트리(Shortest-path tree)가 된다.
  최적해 구조(Optimal substructure)를 가진다.
- **완화(Relaxation)**
  현재 경로 값보다 더 적은 경로가 존재한다면 값을 변경한다.

### 플로이드-와샬 알고리즘(Floyd-Warshall algolithm)

중간 정점을 모두 실험해본다.(All pairs shortest path문제를 해결)
모든 정점을 넣어보고 경로의 값이 가장 작아지는 경로를 찾는다.
따라서 수행시간은 $\Theta(V^3)$
시간복잡도는 $O(V^3)$

- 인접 행렬$W$
  각 **간선의 값**은 다음과 같이 표시 $W_{ij} = W(i,j)$

- 최단경로 행렬$D$
  각 **경로의 값**은 다음과 같이 표시 $d_{ij} = \eth(i,j)$

- 직전 정점 행렬
  각 **행렬의 값**은 다음과 같이 표시 $\pi_{ij} =  NIL$

### 탐욕 알고리즘(Greedy Algorithm)

현재 상황에서 가장 좋아 보이는 답을 선택하는 방법
각 부분에서 최적을 선택하면 전체에서도 최적이 될 것이라는 가정을 전제로.
선택은 항상 하위 문제에 대한 해답이 나오기 전에 선택된다.
(배낭채우기 문제에 적용 가능)

|  탐욕선택(Greedy-choice property)  |   동적프로그래밍(Dynamic programing)   |
| :--------------------------------: | :------------------------------------: |
| 하위 문제를 풀기 전에 선택을 한다. |   하위 문제를 풀고 나서 선택을 한다.   |
|   항상 하나의 문제만을 고려한다.   | 동시에 여러 개의 하위 문제를 고려한다. |

- 신장트리(Spanning Trees)
- 최소신장트리(Minimum Spanning Trees)MST 비용이 최소가 되는 신장트리를 찾는 문제
  - 최소신장트리는 한번에 하나의 간선이 늘어난다.
  - 사이클조건이 안되게 하는 것. safe edge

### 프림 알고리즘(Prim's Algorithm)

정점의 최선값을 선택하여 MST문제를 해결하는 알고리즘.
집합 A에 속하는 간선은 항상 트리를 형성한다
트리는 임의의 root정점 r에서 시작하며 정점의 집합 V에 속하는 모든 정점을 포함할 때까지 확장한다.
각 단계에서 가벼운 간선(light edge)이 트리에 추가된다.
따라서, 알고리즘이 종료되면, 최소신장트리가 만들어진다.

### 쿠루스칼 알고리즘(Kruskal's Alorithm)

간선의 가중치값을 정렬하여 MST문제를 해결하는 알고리즘.
