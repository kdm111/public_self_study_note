# Posix Cli



### Intro

운영체제를 제어하는 방법으로는 2가지가 존재한다. GUI(Graphic User Interface)와 CLI(Commad Line Interface)이다.

Cli는 명령어를 통해 컴퓨터를 제어한다. Cli를 배워야 하는 이유는 가치 있기 때문이다. 의사를 정확하게 전달할 수 있고 지시하고자 하는 시간과 순서를 정확하게 지시하면 순차적으로 일을 처리해준다. 

Cli는 Gui가 컴퓨터의 대중화의 일조했다. Cli는 시간의 순서에 따라 명령을 내릴 수 있고, 컴퓨터의 자원을 Gui보다 더 적게 사용한다. 운영체제의 용량과 cpu를 매우 적게 사용한다. 서버쪽 컴퓨터는 Cli를 이용해 사용한다.

Unix, Linux, macOS 는 posix를 따르고 있다. 명령어를 같거나 사용하는 방법이 매우 유사하다. window는 CMD, PowerShell이라는 독자적인 방법을 가지고 있다. posix와 기본적으로 호환하지는 않지만 에뮬레이터를 설치하면 posix를 사용할 수 있다.





### 실습

posix는 unix, linux, macos는 필요한 게 없지만 윈도우, 안드로이드, ios의 경우 posix를 지원하지 않으므로 따로 해 주어야 할 것이 있다. 바로 emulator라는 것인데 posix에 명령하는 방식으로 통역해준다. 또 별도의 posix 서버를 마련하여 원격으로 접속하는 것이다. 원격 제어를 하는 것이다. 이 때 사용하는 것은 Secure Shell(SSH)라는 것을 사용하여 운영체제에서 posix에 접속하여 실습을 할 수 있다. 





###  실습 준비 (Posix)

gui방식을 사용하는 사람들은 원하는 프로그램을 선택하는 방법이 존재한다. 맥의 경우 terminal을 입력하면 나름의 terminal 프로그램이 존재한다.





### 실습 준비 (Windows Git Bash)

에뮬레이터의 종류에는 Cygwin 같은 것이 존재하지만 git을 다운 하는 것을 추천한다. 다운로드를 하면 git bash를 사용할 수 있다. 

git bash에서는 posix방식으로 윈도우를 제어할 수 있다. 





### 목적

hack이 무엇인가? 우리가 공부하고 있는 것은 정보 때문이고 data를 어딘가에 저장한 뒤 가공해야 한다. 컴퓨터에서 가장 작은 단위는 file이다. 파일이 많아지면 문제가 생길 수 있는 데 우리는 이를 directory를 통해 구분한다. 

저장된 데이터를 처리하는 방법에는 CRUD가 존재한다. Create, Read, Update, Delete이다. 파일과 관련되거나 디렉토리와 관련된 CRUD를 할 줄 아는 것이 우리의 목적이다. 

```
   File             Directory
C editor            mkdir
R editor, cat, ls   ls
U editor, mv        mv
D rm                rm
```





### 디렉토리의 사용

파일에는 데이터가 저장되거나 데이터를 처리하는 로직이 저장된다. 운영체제를 다루는 것은 파일을 다루는 것을 말한다. 우리가 파일에 도달하기 위해서는 directory로 들어가서 원하는 파일을 찾아야 한다.

그래서 이번에는 디렉토리의 사용법을 알아보자.

먼저 현재 위치를 아는 방법을 확인해 보자.

```powershell
pwd : print working directory
```

위의 명령어를 치게 되면 현재 내가 존재하는 위치가 드러난다.

```powershell
/ : root directory
```

/는 최상위 디렉토리를 의미한다. rm같은 명령어를 치게되면 현재 폴더 내에서 파일을 제거할 수 있는데 현재 위치가 루트라면 위험할 것이다.

터미널을 켰을 때 위치하고 내가 기본적으로 위치하는 폴더를 `Home Directory`라고 한다. home directory는 각자 다르다.

우리가 위치하고 있는 곳을 바꾸기 위해서는 `cd`라는 명령어가 필요하다.

```powershell
cd : change directory
```

최상위 디렉토리로 이동하는 방법은

```powershell
cd /
```

다시 이전의 위치로 이동하는 방법은

```powershell
cd /폴더명/하위폴더명
```

`~`이라는 약속된 기호가 있는 데 이게 바로 Home Directory를 의미한다.

```powershell
cd ~
```





### 현재 디렉토리의 상태보기와 명령어의 형식

먼저 현재 위치하고 있는 폴더안에서 어떤 파일과 폴더가 존재하는 지 알아내는 방법

```powershell
ls
```

ls를 치게되면 현재 위치의 폴더와 파일이 등장한다.

만약에 ls에 대해서 더 자세히 알고 싶을 때는 도움말을 사용해야 하는데 도움말은 `--help`를 통해 불러올 수 있다. 혹은 `man(manual)`의 약자를 통해서 명령어를 확인할 수 있다.

```powershell
ls --help
man ls
```

매뉴얼은 `q`를 누르면 나갈 수 있다.

매뉴얼을 보게되면 ls명령어 안에서 많은 옵션을 확인할 수 있는 데 대표적으로 

```powershell
ls -l
```

위의 명령어를 치게 되면 폴더를 상세하게 볼 수 있다.



`touch "파일이름.확장자"`를 하게 되면 현재 폴더 안에서 `파일이름.확장자`로 된 빈 파일을 만들 수 있다.

```powershell
touch file_name.file_extension
```

또한 숨겨진 파일을 만들 때에는 파일 이름 앞에 `.`을 붙여준다. (윈도우에서는 다르다.)

```powershell
touch .hidden_file_name.file_extension
```

posix 계열의 시스템은 파일이름 앞에 `.`을 붙이게 되면 비밀 파일로 인식한다. 감춰진 파일은 쉽게 볼 수 없다.

```powershell
ls -a
```

위의 명령어를 하게 되면 숨겨진 파일도 볼 수 있다.

`-a -l`을 동시에 실행하고 싶다면 

```powershell
ls -a -l
```

위와 같이 동시에 명령어를 입력하면 된다. 

또는 

```powershell
ls -al
ls -la
```

역시 동작한다.





### 디렉토리의 생로병사

이번에는 디렉토리의 CRUD를 살펴볼 것이다.

먼저 Create에 해당하는 명령을 살펴보자.

```powershell
mkdir 폴더이름
```

그러면 디렉토리로 들어가기 위해서는

```powershell
cd 폴더이름
```

위의 명령어는 원래 다음과 같은 형태이다.



```powershell
cd ./폴더이름
```

`.`은 현재 폴더를 이야기하고 있고 현재 폴더 안에서 `폴더이름`으로 이동하라는 의미이다. 

`mv`를 이용하여 디렉토리의 이름을 바꿀 수 있다.

```powershell
mv 현재이름 바꿀이름
```

`rm -r` 명령을 통해 삭제할 수 있다.

```powershell
rm -r 폴더이름
```



최종 정리하면

```powershell
mkdir : Create
cd : Read
mv : Update
rm -r : Delete
```



### 절대경로와 상대경로

상대 경로 `..`을 통해 부모 디렉토리로 이동할 수 있다.

```powershell
cd ../
```

절대경로  `/`을 사용해 루트 디렉토리로 갈 수 있다.

```powershell
cd /
```

또한 절대경로로 어디에 있던지 이동할 수 있다.

```powershell
cd /Users/...
```





### 파일생성과 읽기

파일을 생성하고 읽고 수정하고 삭제하는 방법을 알아보자.

vim이라던지 이런 프로그램을 통해 프로그램을 CRUD 할 수 있다.

파일을 저장하고 싶을 때에는 

```powershell
:wq file_name.file_extension
```

읽는 것도 굉장히 쉬운데 

```powershell
vim file_name.file_extension
```

으로 읽을 수 있다.

`cat`이라는 간단한 명령어도 있는 데 vim으로 들어가는 것이 아니라 콘솔에서 내용을 볼 수 있다.

```powershell
cat file_name.file_extention
```





### 파일수정 과 삭제

파일을 수정하고 싶다면 파일을 읽고 수정한 뒤 저장하고 나가면 된다.

```powershell
:wq
:x
ZZ
```

파일의 이름 역시 변경이 가능하다.

```powershell
mv 현재이름 바꿀이름
```

파일을 삭제하는 방법 역시 기존과 같다. 폴더와는 다르게 `-r`이 필수적이지 않다.

```powershell
rm 파일이름
rm -r 파일이름.파일확장자
```





### 순서대로 실행시키기

`ls -R`  명령어는 현재 존재하는 모든 하위 폴더의 파일을 볼 수 있게 해준다.

```powershell
ls -R 
```

명령어를 순서대로 실행시키도록 할 수 있다. `;`을 명령 사이에 붙여두면 컴퓨터는 순차적으로 명령어를 실행한다.

```powershell
mkdir dummy2;cd dummy2
```





### 자동화 - 실패하면 멈추기

만약 중간에 명령어가 잘 못 들어가서 실패할 명령어가 들어간 경우가 발생할 수 있다.

`&&`를  `;`의 대신한다. `&&`는 한 명령어가 완벽하게 실행된 뒤에 실행된다. 

```powershell
mkdir dummy2&&cd dummy2
```





### 추가

반복적인 작업이 있다고 가정할 때 어딘가에 명령어를 저장해 바로 실행시키는 것을 원할 수 있다.

Shell script를 사용하면 컴퓨터를 자동화하여 실행시킬 수 있다.

package는 만들어서 사용하는 것이 가능하고 package를 설치하여 사용하는 것이 가능하다. package manage를 사용하면 되는 데 agt-get, yum, homebrew, chocolatey 일종의 앱스토어로 명령어만 실행하면 간단하게 패키지를 사용할 수 있다.

컴퓨터는 무엇으로 이루어져 있고 어떻게 작동하는 가 storage는 데이터를 저장하는 곳이고 memory는 속도가 빠르지만 휘발성이다. storage에 모든 데이터를 넣어놓고 정보를 가공할 때 memory로 올려서 사용한다. cpu로 정보를 처리하게 된다.

결국 컴퓨터 관리의 핵심은 1) 스토리지와 메모리 사이에 얼마나 많은 데이터를 저장할 수 있고 2)cpu가 얼마나 혹독하게 사용되는 지 파악하는 것이다.

이러한 동작을 하는 대표적인 프로그램이 "top", "htop"이다. 

네트워크의 설정과 관리를 도와주는 도구들이 존재한다. 이에 대해서 알아보는 것도 좋을 것이다.



