# 장고 1개 serailizer에서 2개의 모델 사용하기



>211030 1dayverse 개발 노트



기존에 있던 serailizer로는 하나의 모델만 불러올 수 있어서 내가 원하는 정보를 불러올려면 다른 api 주소를 통해서 요청을 해야 내가 원하는 정보를 불러올 수 있었다. 

그래서 한 번의 요청을 통해서 2개의 모델을 불러올 수 있다면 웹이 더 빠르게 돌아갈 것이다.



강의의 모델을 가져오면 다음으로 강사에 대한 모델도 가지고 오고 싶다.



기존의 serilizer는 다음과 같다.

```python
# serailizers.py
class LectureDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        exclude = ('password',)
```



공식 문서를 참고해 보았다.

https://www.django-rest-framework.org/api-guide/relations/#nested-relationships



먼저 다른 앱에 있는 serailizer를 가져와야 겠다고 생각했다.

```python
# serailizers.py
from ..accounts.serializers import ProfileSerializer 
```



그러자 콘솔에서 다음과 같은 에러가 발생했다. 

```
ValueError: attempted relative import beyond top-level package
```

탑 레벨의 패키지를 넘어서 가져오려 시도한다는 메시지가 떴다.

오류 내용은 다음을 참고했다.

https://stackoverflow.com/questions/30669474/beyond-top-level-package-error-in-relative-import



파이썬은 패키지의 현재 패키지의 주소를 저장하지 않기 때문에 상위(`..`)위치를 찾지 못하는 것이다.

다음과 같은 방법으로 문제를 해결했다.

```python
# serializers.py
from accounts.serializers import ProfileSerializer 
```



다른 방법도 시도해 보았다.

```python
# serializers.py

import sys
sys.path.append("..")
from ..accounts.serializers import ProfileSerializer 
```

이 방법은 잘 되지 않았다 다음에 알아보자.









 







