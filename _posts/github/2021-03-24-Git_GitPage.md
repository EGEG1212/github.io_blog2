---
layout: post
current: post
cover: assets/built/images/github-logo.png
navigation: True
title: 3. Jekyll 기반의 GitHub Page 생성
date: 2021-03-24 16:40:00
tags: [github]
class: post-template
subclass: "post tag-GitHub"
author: egeg1212
---

{% include git-table-of-contents.html %}

> 처음엔 CSS부분? 줄바꿈에 대한 에러만 고치고 싶었다.....
> 그런데 왠걸? commit으로 io에 업데이트 잘되던게 안된다...

# 3. Jekyll 기반의 GitHub Page 생성

| **강좌정보** | Jekyll 기반의 GitHub Page 생성 [YouTube링크](https://www.youtube.com/playlist?list=PL7nkwz9MkASx1wxXK51n7KtwQyXgoNL70) |
| :----------: | :--------------------------------------------------------------------------------------------------------------------- |
| **학습내용** | Jekyll 기반의 GitHub Page 생성                                                                                         |
|   **강사**   | 문성훈 얼큰우동TV                                                                                                      |
| **학습기간** | 2021.04.20~ **이수중**                                                                                                 |
| **학습시간** |                                                                                                                        |
| **강의목록** | [1강] Jekyll 기반의 GitHub Page 생성(1) - 환경설정                                                                     |
|              | [2강] Jekyll 기반의 GitHub Page 생성(2-1) - 환경설정파일                                                               |
|              | [3강] Jekyll 기반의 GitHub Page 생성(2-2) - author와 tags 설정                                                         |
|              | [4강] Jekyll 기반의 GitHub Page 생성(2-3) - 메뉴와 글 올리기                                                           |
|              | [5강] Jekyll 기반의 GitHub Page 생성(2-4) - Archive설정 및 이미지설정                                                  |
|              | [6강] Jekyll 기반의 GitHub Page 생성(2-5) - post목차 설정                                                              |
|              | [7강] Jekyll 기반의 GitHub Page 생성(2-6) - publishing                                                                 |
|              | [8강] Jekyll 기반의 GitHub Page 생성(3) - 웹 폰트 설정                                                                 |
|              | [9강] Jekyll 기반의 GitHub Page 생성(4) - rouge를 이용한 syntax higlighting                                            |
|              | [10강] Jekyll 기반의 GitHub Page 생성(5) - lunr.js를 이용한 Search 기능 추가                                           |
|              | [11강] Jekyll 기반의 GitHub Page 생성(6) - Google Search Console 활용                                                  |
|              | [12강] Jekyll 기반의 GitHub Page 생성(7) - GitHub Gist 활용                                                            |
|              | [13강] Jekyll 기반의 GitHub Page 생성(8) - Travis CI 활용                                                              |

얼큰우동TV의 <https://moon9342.github.io>

## 1강(1 환경설정)

https://rubyinstaller.org/downloads/ 다운받아 설치하고
CMD창에서 `gem install bundler`
참조 :https://moon9342.github.io/jekyll-struct
jasper2 theme을 다운받아 압축풀어 내용을
나의 blogmaker로 복사해온다....안그럼 아래 명령어 실행했을때 'could not locate gemfile' 이런 에러문구 뜸ㅜㅜ
CMD창에서 해당 blog위치로 이동해서. `bundel install` (설치하는데 시간 좀 걸림)
`bundle exec jekyll serve`
gem 'wdm', '>= 0.1.0' 드래그 우클릭으로 복사해놓고, 컨트롤씨로 종료.
blog폴더 안에 Gemfile을 노트패드로열기(메모장도 가능)
Gemfile 맨끝줄에 복붙
다시한번더 CMD창에 `bundle exec jekyll serve`
`bundle install` 다시한번더 해달라는 문구가 나와서 한번 더 함;
설치 다 되면~
CMD창에 `bundle exec jekyll serve`
그러면~
Destination: ../jasper2-pages/ 폴더가 생기면서!(그런데 왜 blogmaker위에 생겼냥...)
CMD의 Server address: http://127.0.0.1:4000/jasper2// 부분의 뒤에
`http://127.0.0.1:4000/jasper2` 이걸 크롬주소창에 넣어보면 기본 뙇!

## 2강(2-1 환경설정파일) 유튜브 https://www.youtube.com/watch?v=OO5IZrx1ZVE&list=PL7nkwz9MkASx1wxXK51n7KtwQyXgoNL70&index=2

블로그 https://moon9342.github.io/jekyll-struct
WebStorm IDE설치..저는 vsCode로 :-)
blogmaker의 assets폴더에 \_config.yml수정
탐색기열어서 내PC에서 우클릭.-왼쪽 변에 고급시스템설정 - 고급 탭 - 하단에 환경변수- 첫번째 새로만들기 - '변수이름'부분에 `JEKYLL_ENV` 그리고 '변수값'부분에 `production` 쓰고 확인버튼

## 3강(2-2 author와 tags 설정) 유튜브 https://www.youtube.com/watch?v=Ohrc__9z694&list=PL7nkwz9MkASx1wxXK51n7KtwQyXgoNL70&index=3

블로그 https://moon9342.github.io/jekyll-struct
blogmaker의 \_data폴더에 authors.yml수정
blogmaker의 \_data폴더에 tags.yml수정

## 4강(2-3 메뉴와 글 올리기) 유튜브 https://www.youtube.com/watch?v=lh7aYzNcgDs&list=PL7nkwz9MkASx1wxXK51n7KtwQyXgoNL70&index=4

블로그 https://moon9342.github.io/jekyll-struct
blogmaker의 \_includes폴더에 navigation.html수정

메뉴about은 블로그 소개글. (about폴더의 index.md)
\_posts폴더 아래 메뉴별 폴더하나씩 더 만들기(태그,메뉴와 똑같이)
jekyll을 algorithm으로 변경
python을 github로 변경

## 5강(2-4 Archive설정 및 이미지설정) 유튜브 https://www.youtube.com/watch?v=yqtkI84C2Vw&list=PL7nkwz9MkASx1wxXK51n7KtwQyXgoNL70&index=5

블로그 https://moon9342.github.io/jekyll-struct
각각 필요한 이미지를 blogmaker/assets/built/images폴더에 저장하기(logo, favicon, cover)
assets/built/images/blog-cover1.png
assets/built/images/favicon.jpg
assets/built/images/economy-author-logo.jpg # author image

\_layouts/post.html에 45~48줄 부분 cover안나오게 코드주석처리<!--  -->
\_layouts/post.html에 60~67줄 부분 구독subscribers안나오게 코드주석처리
`bundle exec jekyll server`컴파일해서 이미지들 잘 나오나 확인해보기

blogmaker/archive.md파일만들기(파일내용은 블로그에있음)
author_archive.md파일만들기

## 6강(2-5 post목차 설정) 유튜브 https://www.youtube.com/watch?v=acVpibElHZ8&list=PL7nkwz9MkASx1wxXK51n7KtwQyXgoNL70&index=6

블로그 https://moon9342.github.io/jekyll-struct
\_includes/github-table-of-contents.html (내용복붙)
그중 주의할점 포스팅파일의 날짜 빼고,확장자 빼고 뒤에 이름만넣기
포스팅파일의 title을 똑같이 넣어줘야 보는사람이 안헷갈림 ㅋㅋ

css스타일잡기: 마우스올렸을때 빨간색으로 바뀌고, 폰트컬러도 예쁘게~
assets/css/custom.css 파일생성(내용복붙)
공백을 없애 minified 한다(모바일로 접속했을때 용량이 크면 데이터를 많이 잡아먹기도함) Gulp로 함.
Gulp를 사용하려면 node.js를 설치해야함. 11ver.낮춰서 x64
blogmaker/gulpfile.js 모든내용지우고 얼큰우동님 내용복붙 (걸프를사용하기위한설정파일)
환경변수 수정한것 적용되도록 IDE재접속하기
blogmaker/package.json 모든내용지우고 얼큰우동님 내용복붙(NPM! 이렇게 깔아줘~주문서)
CMD에 `npm install` 하면 /node_modules폴더가 생깁니다(여기에 NPM을 통해 Gulp설치가된것임)
CMD에 `gulp css`하면 gulpfile.js의 css부분이 실행됨^^....근데 난 실패함; 음... 그.. 아마도 npm ver높은듯;
`node -v`코드실행하면 node version 확인가능 (엇..나는 12.18.4네 ㅠㅠ11이여야하는데;;높네 ㅠㅠ 미니파이즈하지말지~뭐 ㅋㅋㅋ)
성공한다면; assets/built/custom.css파일이 생기면서 열어보면 내용은 한줄로~~~

마지막으로 완성된 ㅋ 목차(algorithm-table-of-contents.html)를 글에 추가하자!
`{% include algorithm-table-of-contents.html %}` 코드를 해당 포스트에 각각 머릿말 아래 넣기

자, 이제 확인해보자~ 컴파일하기
`bundle exec jekyll server`

## 7강(2-6 publishing) 유튜브 https://www.youtube.com/watch?v=C9g8Fbc43Lk&list=PL7nkwz9MkASx1wxXK51n7KtwQyXgoNL70&index=7

블로그 https://moon9342.github.io/jekyll-struct
앞전 6강에서 미니파이즈한 css파일을 적용시켜보자;ㅋㅋ
blogmaker/\_layouts/default.html 열어보면 14줄 Styles'n'Scripts부분 아래 추가하기
`<!-- custom.css minified실패ㅋ assets/built/custom.css 없어서--> <link rel="stylesheet" type="text/css" href="{{ site.baseurl }}assets/css/custom.css" />`
다시 컴파일해서 확인하자
`bundle exec jekyll server` 응?? 적용안되었썽..... ㅠㅠ
