# GitHub.com



### Intro

개발자들에게는 소스코드의 관리를 버전관리 시스템이라고 한다. 각각의 파일을 백업하고 여러사람이 공동으로 작업하게 해주는 것이 github.com이다. 

버전관리 시스템은 CVS, SVN, GIT이 존재한다. git은 가장 많이 사용되는 버전관리 시스템이다.

git은 git client라고 불리는 프로그램이 존재한다. Git-cli와 소스트리 등등이 있다. git client는 여러 클라이언트가 있기 때문에 마음에 드는 것을 하면 된다. git으로 관리되는 프로젝트는  git server 즉 원격 저장소에 저장된다. git hosting 업체중 github, gitlab 같은 서비스들이 존재한다.

현재 절대 다수의 프로젝트는 깃헙에 올라가고 있다. 





### 저장소 생성

깃허브의 사용법을 알아보기 위해 저장소를 만든뒤 살펴보자.

중요한 것은 괜찮은 프로젝트인지 확인하는 것이다. 나는 커밋수를 먼저 확인하고 협업자들을 확인한다. 그 뒤 star(좋아요)도 확인하고 watch는 구독하고 있다는 것이고 fork는 복제해간 사람들의 숫자이다.

프로젝트를 사용하고 싶을 때는 클론을 받거나 다운로드 하면 된다. 

커밋은 파일의 변화 커밋의 변화를 확인할 수 있다. 변경 사항에 포함되는 내용을 확인할 수 있다.





### 버전 생성

깃헙 안에서도 파일을 생성하고 수정할 수 잇다. 그 밑에 커밋 메시지를 적을 수 있는 데 커밋 메시지를 적고 commit new file 버튼을 누르면 커밋을 할 수 있게 된다.

그 뒤 code 탭에서 커밋과 커밋에서 수정된 내용을 확인할 수 있다. 그리고 댓글을 달 수 있다. 또한 댓글을 수정된 내용에 달 수 있다.

그리고 파일을 만들어서 깃헙에서 드래그앤 드롭으로 업로드 하는 것 역시 가능하고 커밋을 달면 저장이 완성된다.





### git 구경하기

git에게 마지막 버전 이후에 내가 무엇을 수정했는 지 보려면 

```powershell
git diff
```

를 치면 파일이 변경된 내용을 확인할 수 있다.





### 멤버

깃허브는 협업에 상당히 유용하다. settings의 manage access에 깃헙 아이디나 이메일을 적어 보내면 해당 아이디의 소유자는 관리할 수 있게 된다.





### 이슈

이슈는 개발하면서 문제점을 의논하거나 관리하기 위한 게시판이다. 

이슈를 등록하면 알림이 가게 되고 label을 지정하여 눈에 띄기 좋게 만들 수도 있다. 

그리고 이슈를 close하면 문제가 해결되거나 이슈를 닫을 수 있다.





### 수업을 마치며

나머지 탭의 내용을 정리하겠다.

pull request : pull은 프로젝트의 상태를 땡겨오는 것이다. pull을 다른 사람에게 요청하는 것이다. 

Wiki: 프로젝트를 진행하다 보면 지식을 정리 정돈하는 기능이다. wiki를 통해 sw의 사용설명서나 참여하는 방법 등등을 위키피디아 처럼 정리할 수 있다.

insights : 프로젝트를 진행하면서 누가 기여를 많이 하는 지 , 커밋이 얼마나 빈번하게 일어나고 있는 지 , 코드가 얼마나 빈번하게 작성되는지를 확인할 수 있다. fork는 마치 내것인양 복제하는 것이다. 

actions : 프로젝트에 어떤 작업이 일어났을 때 실행될 것을 정할 수 있다.  푸쉬가 발생했을 때 자동으로 테스트를 실행한다던가.

projects : 프로젝트의 일정관리 탭이다.





# Pull Request



### intro

코드리뷰의 핵심적인 기능인 pull request, merge request를 학습한다.

만든 브랜치가 다른 브랜치와 병합한다는 것은 내가 했던 작업을 끝낸다는 것이다. 그 과정을 끝내는 과정에서 다른 사람의 코드 리뷰를 받고 싶을 때 사용하는 기능이다.

버전을 어떤 브랜치 이하에서 만들고 팀은 마스터 이하에서 문제가 없는 코드만 병합한다. 그래서 작업하던 브랜치를 원격 저장소로 올려 작업한 내용에 대해 merge request를 한다. 문제가 없는 코드를 만들게 되면 merge 버튼을 누르면서 새로운 마스터가 생기고 새로운 마스터는 풀을 받을 수 있게 된다. 우리가 작업한 코드를 검토해서 품질을 올리고 마스터 브랜치의 품질을 유지할 수 있다.

pull request는 작업한 브랜치를 확인 받고 싶을 때 pr을 신청한다. 

오픈소스에서는 원격저장소를 복제하여 복제한 저장소에 푸쉬하고 브랜치를 만들고 복제한 저장소에서 원 저장소에 pr을 신청한다. 그래서 추가한 코드가 적절할 경우 원 저장소에서 머지한다. 



### 실습환경

sw세계에서는 브랜치가 개발의 충추적인 용도를 가지고 있다. 많은 조직이 언제나 실행가능해야 하고 언제나 배포가 가능한 브랜치를 master로 고정하고 개발은 feature같은 개발 브랜치를 사용한다. 

개발 브랜치를 푸쉬한다. 푸쉬하면 pr을 할 수 있는 주소가 존재한다.

브랜치를 푸쉬하면 깃허브는 언제가 통합이 필요하다는 것을 알고있다. Pr탭으로 가서 pr을 할 수 있게 된다.





### pull request 만들기

pr에서 base는 병합할 브랜치이고 compare는 base로 병합될 브랜치를 만든다.

pr에서 작업 내용과 커밋을 적은 뒤 pr을 만들면 된다. draft pull request는 코드 리뷰를 요청하는 것이 draft pull request라고 한다. 이 작업은 병합은 일어나지 않는다.

pr이 생성되면 다양한 탭이 존재한다.

conversation : 이 pr과 관련하여 일어난 사건의 시간의 순서를 알려준다.

commit : 브랜치에서 일어난 커밋을 볼 수 있다.

File changed : 브랜치에서 변경이 일어난 파일을 볼 수 있다.

문제가 없을 경우 merge pull request가 활성화 되고 confirm merge 버튼을 누르면 머지가 완료된다. 





### 소통하기

pr이 생성되면 어떤 작업을 했는지 볼 수 있다. file changed 탭에서 파일의 작업 내용에 대해서 댓글을 달 수 있다. 

add single comment는 댓글을 다는 기능이고 start a review 버튼은 리뷰를 할 때 의견을 그루핑에서 한 번에 의견을 줄 수 있다. 예를 들어 start a review를 하게되면 리뷰가 시작되고 의견을 여러번 달 수 있고 insert a suggestion은 바꿀 코드를 추천해 줄 수 있다. Finish your reivew로 나가게 되면 comment를 그룹핑한 의견을 달 수 있다.

또한 웹상에서 commit suggestion의 내용을 commit changes 버튼을 통해 커밋을 자동으로 만들어 줄 수도 있다.





### 충돌해결하기(github.com 내의 편집기 이용)

병합 하려고 하는 브랜치 간의 같은 코드를 수정했다면 충돌이 발생한다.

web editor를 수정하거나 혹은 local에서 해결해야 한다. 

web editor에서는 어떤 코드를 선택한 뒤 merge를 시도하면 된다.

코드를 바꾸면 변경사항을 브랜치에서 커밋을 하고 개선시켜 나간 것이다. 우리의 토픽 브랜치는 마스터 브랜치로 병합한다.





### 충돌해결하기(local git 이용)

작업하던 브랜치가 병합하려는 브랜치와 충돌이 날 경우 로컬에서 해결하는 방법이 있다.

1. 충돌난 master를 로컬의 브랜치로 가져와서 병합한 뒤 
2. 코드가 문제가 없다는 것이 확인 되면 병합한 브랜치를 master와 병합한다.

충돌이 난 경우 로컬에서 코드를 선택하고 커밋을 찍고 푸쉬한다.

현재 원격저장소에는 충돌이 해결된 브랜치가 올라가게 되고 merge request가 가능해진다.

또한 지역 저장소에서 master로 이동한 뒤 

```
git merge --no--ff 작업한브랜치이름
```

을 하면 master로 작업한 브랜치가 병합된다. 

`--no--ff` 의 의미는 fast forward 상황에서도 머지가 완료된다. 그리고 push 하면 github는 자동으로 머지를 닫혀준다.





### 수업을 마치며

병합을 할 때 merge pull request를 사용했는데 

squash and merge : 한 브랜치의 모든 변경사항을 합쳐서 하나의 버전을 만든다. 그리고 다른 브랜치의 최신 버전과 합쳐서 완성한다. 

rebase and merge :  브랜치가 너무 많아질 경우 프로젝트의 히스토리를 보기 불편하다.브랜치의 커밋마다  변경사항과 현재 마스터의 최신 사항을 머지한다. 즉 브랜치에서 커밋이 2개일 경우 마스터는 첫번째 커밋의 변경사항과 머지되고 만들어진 커밋과 2번째 커밋과 머지된다. 

sqaush는 하나로 퉁치는 것이고 rebase는 각각의 버전을 살려놓는 것이다.



다른 사람의 프로젝트를 포크해서 포크한 내용의 개선 사항을 pr을 사용하는 오픈소스식 pr방법을 확인해보자.

 







 


