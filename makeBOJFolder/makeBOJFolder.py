import os, sys, re, requests

def makeDirectory(number):
    if not os.path.exists(f"{number}"):
        os.makedirs(f"{number}")
    return

def getNames(path):
    file_ex_name = re.findall("[\w-]+\.*$", path)
    file_name = re.findall("[\w-]+?(?=\.)", path)
    return [file_name[0], file_ex_name[0]]

def makeSourceFile(number, path, blog_path):
    name, ex_name = getNames(path)
    comment = "#" if ex_name == 'py' else "//"
    """
    comment language
    '#' = py
    '//' = c, cpp, js, java
    """
    SOURCE_CONTEXT = f"{comment} 풀이 과정\n{comment} {blog_path}\n\n"
    with open(path, 'r') as f:
        for v in f.readlines():
            SOURCE_CONTEXT += v
        with open(f"{number}\{number}.{ex_name}", 'w', encoding='utf-8') as f2:
            f2.write(SOURCE_CONTEXT)
    return

def makeReadMeFile(number, blog_path):
    url = f"https://www.acmicpc.net/problem/{number}"
    title = re.findall("<title>[0-9]+번: (.*?)</title>", requests.get(url).text)[0]
    README_CONTEXT = f"# {title}\n" \
                     f"{url}\n" \
                     f"## 해결 과정\n" \
                     f"### 0. [네이버 블로그]({blog_path})\n"
    with open(f"{number}\README.md", 'w', encoding='utf-8') as f:
        f.write(README_CONTEXT)
    return

if __name__ == "__main__":
    NUMBER, PATH, BLOG_PATH = sys.argv[1:4]
    makeDirectory(NUMBER)
    makeSourceFile(NUMBER, PATH, BLOG_PATH)
    makeReadMeFile(NUMBER, BLOG_PATH)