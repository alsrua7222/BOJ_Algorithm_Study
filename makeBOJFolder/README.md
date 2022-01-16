# 네이버 블로그 전용 자동화 도구
`pip install requests`    

## 사용 방법
`python makeBOJFolder.py (BOJ Number) (File path) (Blog path)`
#### example
`python makeBOJFolder.py 4485 index.py https://blog.naver.com/alsrua7222/222623130201`    
`python makeBOJFolder.py 4485 C:\Users\source\repos\CNote\CNote\소스.cpp https://gist.com/alsrua7222/91230129301940190390123`   
`python makeBOJFolder.py 4485 C:\Users\source\repos\nodejs\study\index.js https://blog.naver.com/alsrua7222/222623130201`   

## 결과
![image](https://user-images.githubusercontent.com/59680587/149655764-9959521c-af22-4a32-9848-65e73cf1782b.png)

| 함수명 | 부가 설명 |
| :---: | :---: |
| makeDirectory(number: str) | 숫자 이름을 가지고 폴더가 있다면 무시하고, 없다면 새로 생성해준다. |
| getNames(path: str) | 파일 절대 경로나 상대 경로를 가져와서 파일 이름과 확장자를 분리시켜준다. |
| makeSourceFile(number: str, path: str, blog_path: str) | 소스파일을 확장자 타입대로 풀이 과정 라는 주석을 추가하고 나머지 소스 파일을 복붙하고 해당 폴더에 NUMBER.extention생성시킨다. |
| makeReadMeFile(number: str, blog_path) | 백준 온라인 html 구조를 파싱한 후 제목 자동 처리 후, 양식대로 블로그 주소 추가해준다. |

```python
if __name__ == "__main__":
    NUMBER, PATH, BLOG_PATH = sys.argv[1:4]
    makeDirectory(NUMBER)
    makeSourceFile(NUMBER, PATH, BLOG_PATH)
    makeReadMeFile(NUMBER, BLOG_PATH)
```

