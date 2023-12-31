# Git2 - Version Control



### Intro

git을 사용하여 버전을 제어하는 것을 공부할 것이다. 

명령어의 특성상 한번에 다양한 환경을 제어할 수 있기 때문에 사랑 받고 있는 방법이다.





### git 설치(Mac)

git사이트로 들어가 다운로드를 받는다. 알아서 자동경로 등등 다 설치된다.

마지막으로 터미널에서 git을 쳐본다. 에러가 뜨지 않으면 정상



### git 설치 (windows)

windows로 설치할 때는 다양한 옵션이 나오지만 최대한 next를 하는 방향으로 누른다.

검색에서 git이라고 검색하면 git bash라는 파일이 설치되어 있을 것이다. 앞으로 이걸 콘솔, 터미널이라고 부르며 이것을 활용할 것이다.

마지막으로 터미널에서 git을 쳐본다. 에러가 뜨지 않으면 정상



### 버전관리의 시작

깃에게 프로젝트 하나를 디렉토리를 버전관리 하기 시작할 것을 요구할 때는 

```powershell
git init
```

git initialize의 약자이다. 

위의 명령어 뒤에는 `.`이 생략되어 있다.

```powershell
git init .
```

이제 `ls-la`를 했을 때 어떤 변화가 생겼는 지 확인해보자.

그렇게 하면 `.git`이라는 폴더가 생성되었을 텐데 생성되는 버전관리의 내용은 모두 이 폴더 안에서 관리될 것이다. 

그래서 `.git` 폴더를 지우게 되면 git으로 관리되던 모든 내용이 사라지게 된다.





### 버전 만들기

```
working tree | staging area | repository
```

우리가 하려는 것은 파일을 변경했을 때 파일의 변경사항을 버전으로 만들어서 관리하는 것이다. git에서 버전이 저장되는 곳을 repository라고 한다. .git이라는 폴더를 repository라고 생각해도 될 것이다. 

아직 버전으로 만들어지기 전 단계를 working tree 라고 하고 staging area를 버전이 여러개 만들어 질때 파일 몇 개만 떼어내서 버전으로 만들고 싶을 때 몇 개만 staging area에 위치 시킨다. 그리고 버전을 만들라고 지시하면 staging area에 있는 파일들만 떼서 하나의 버전으로 만들어 repository에 저장한다. 

working tree는 변경된 파일들, staging area는 버전을 만들려고 하는 파일들, repository는 버전들이 모아져 있는 곳.

파일을 만들고 저장한 뒤 `git stauts`를 쳐보자. `git status`는 현재 working tree의 상태를 보여준다.

```powershell
git status
```

Untracked file는 현재 버전으로 관리되지 않는 파일을 의미하고  버전으로 관리되는 파일로 만들기 위해서는 git add 명령을 사용한다.

```powershell
git add 파일이름
git add . // 현재 폴더
```

working tree의 수정사항을 staging area로 올리게 된다. 이제 커밋을 하게 되면 파일은 버전으로 관리된다.

이 상태에서 버전을 만들라고 하는 명령어는 `git commit`이다.

```powershell
git commit -m "커밋 내용"
```

위의 명령을 치게되면 버전이 생성된다. working tree의 변경된 사항 중 staging area에 있는 내용이 repository로 가게 된다.그리고 working tree는 비워지게 된다.

commit을 확인하려면 `git log`를 치면 된다.

```powershell
git log
```

git log는 프로젝트의 커밋 기록을 볼 수 있다. 나가려면 `q`를 누른다.

그리고 파일을 수정한 뒤 git staus 명령을 치게 되면 `Changes not stages for commit`메시지를 볼 수 있는 데 현재 수정된 파일이 staging area에 올라가지 않음을 말한다.

`add`명령을 통해 staging area에 올려놓고 `commit`명령을 통해 repository에 변경사항들이 저장된다.





### 여러개의 파일을 버전으로 만들기

하나의 파일의 변경사항 만을 만드는 것이 아닌 여러 개의 수정 내용을 커밋으로 찍을 수 있다. 이 경우 여러개의 파일을 staging area에 올려야 할 것이다.

```powershell
git add 파일이름1
git add 파일이름2
```

이렇게 여러 개의 파일을 staging area에 올릴 수 있을 것이다. 그리고 커밋을 찍을 수 있다.

이 경우 git log에서 어떤 파일이 연루되어 있는 지 확인하고 싶을 때 다음과 같은 git log 옵션을 사용한다.

```powershell
git log --stat
```

이렇게 하나의 작업에 관련되어 있는 여러개의 파일을 볼 수 있다.



### 버전간의 차이점 비교

`git diff`라는 명령어를 알아보자. git diff 명령어는 기존과 달라진 점을 확인할 수 있다.

작업을 바꾸기 전에 마지막 버전과 현재 working tree의 차이점을 분석하면서 버전을 만들기 전에 무엇을 하였는 지 검토를 할 수 있는 명령어이다.

```powershell
git diff
```



마지막에 지금까지 한 내용을 모두 버리고 싶다면 `git reset --hard`를 치면 지금까지 작업했던 내용이 모두 이전에 상태로 돌아가게 된다.

```powershell
git reset --hard
```



`git log -p`는 커밋 안에서 이전의 버전과 비교하여 변경 사항 많을 비교하여 볼 수 있다. 이 명령어를 통해 패치 중 어떤 부분이 문제가 발생했는 지 확인할 수 있다.

```
git log -p
```





### checkout과 시간여행

만약 git log에서는 커밋의 아이디를 볼 수 있는 데 HEAD를 과거의 커밋으로 가리키게 만든다면 디렉토리 전체가 버전을 만들었던 시점으로 돌릴 수 있다. 

```powershell
git checkout 커밋아이디
```

위의 명령어를 치게 되면 프로젝트는 커밋의 시점으로 돌아가게 된다. 파일 역시 이전 상태로 돌아가지만 사실은 지워진 상태인 것은 아니다.

git log로 찾아보면 HEAD는 현재 커밋을 가리킨다. checkout은 head를 이동하는 것이다.

최신의 버전으로 돌아가고 싶다면 커밋아이디가 아닌 master로 돌아가게 된다.

```powershell
git checkout master
```

이렇게 하면 최신의 버전으로 돌아가게 된다.





### 보충수업

add를 할 때  디렉토리 역시 지정이 가능하다.

```powershell
git add 디렉토리이름
git add . // 현재 위치하는 모든 디렉토리
```

커밋과 함께 add를 할 수도 있다.

```powershell
git commit -am "커밋 메시지"
```

이 경우 `-am` 옵션은 `add` 명령을 통해 최초로 한 번 tracked가 된 파일/폴더만 추적한다. 즉 `add` 되지 않은 파일이나 폴더에는 동작하지 않는다. 실수로 만약 추적하고 싶지 않은 파일을 추적하는 실수를 방지할 수 있다.



커밋을 할 때 `-m `옵션을 사용햇다. `-m` 옵션은  메시지를 상징한다 `-m`이 없다면 에디터가 뜨게 되고 그 곳에서 커밋메시지를 쓸 수 있게 된다.

```powershell
git commit
```



기본 에디터를 바꾸는 명령어는

```powershell 
git config --global core.editor "vim"
```

vim이라는 에디터로 바꾼 것이다.





### 삭제 - git reset

이번에는 버전을 삭제하는 방법을 살펴본다. 이전의 버전으로 돌아가고 싶다는 것은 이전의 버전으로 `reset`해야 한다. 

이 버전이 되겠다라는 뜻이다.

리셋하는 방법은

```powershell 
git reset --hard 커밋아이디
```

그렇게 하면 현재 커밋아이디가 마스터가 옮겨오며 버전이 리셋된다.

`--hard` 모드의 경우 상태로 되돌아갈 뿐만 아니라 현재 작업하고 있는 내용 역시 삭제한다.

그렇다면 현재 작업하는 내용은 남기되 이전 버전으로 돌릴 수 있는 모드는 무엇일까? `--mixed`를 사용하면 된다.

협업에서 공유된 버전에 대해서는 리셋하면 안 된다.





### 되돌리기 - git revert

리셋은 특정 버전을 지우는 것이나 다름이 없었다. revert를 사용하면 삭제와 보전의 목적을 동시에 달성할 수 있다.

만약 어떤 버전으로 되돌리고 싶다면 그 다음 버전의 커밋아이디가 필요하다. 

```powershell
git revert 다음커밋아이디
```

그리고 에디터에서 커밋 메시지를 작성하면 커밋이 된다.

로그를 하면 새로운 커밋이 생기게 되고 기존의 커밋은 살아있게 된다. 즉 다음 커밋에서 있었던 변화를 취소하고 이전의 상태로 돌아간다.

`git log -p`를 해보면 기존에 있었던 커밋에서 추가된 내용이 취소되면서 이전 상태로 돌아가게 된다. 이것이 revert 이다.

단 revert를 할 때는 기존에 있었던 커밋 내용을 삭제하므로 즉 바로 이전 상태가 아니라 꽤 오래된 상태로 돌아가면 충돌이 일어나게 된다. 즉 오래전 버전으로 돌아가고 싶다면 하나하나 순서대로 바꿔서 돌아가야 한다.





### 수업을 마치며

버전관리의 핵심은 비교이다. 버전관리를 통해 과거로 돌아갈 수 있다. diff tool을 통해 버전의 비교를 쉽게 볼 수 있다.

버전관리 하지 않아야 되는 파일이 있을 것이다. `.gitignore`를 사용한다. 그 안에는 내가 적는 사설이라던가 올라가서는 안되는 파일을 gitignore로 무시할 수 있다. git은 branch를 통해 저장소를 여러가지 상태로 공존할 수 있게 만든다. 저장소 전체를 만든 뒤 각각을 보관하려 할 수 있다. 다양한 작업을 하게 만든다. branch라는 개념을 만들어 보자. 커밋 아이디는 기억하기 힘들다. 커밋 아이디 대신 tag를 사용하면 버전의 커밋아이디와 이해하기 쉬운 이름을 붙여 쉽게 중요한 버전을 찾아갈 수 있다.

백업은 언제나 중요하다. 깃은 매우 안전한 백업을 가질 수 있다. git으로 백업을 사용하거나 dropbox, google drive, one drive를 사용해보자. 









 

