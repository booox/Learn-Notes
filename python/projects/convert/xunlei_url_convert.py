import base64

href = """thunder://QUFlZDJrOi8vfGZpbGV8W+eWkeeKr+i/vei4ql1b56ys5LiA5a2jXeesrDAy6ZuGLm1rdnw1MjE5NjgyMjN8M2NmNDU1YjM5YjhlYTY2YzkzMzllNTVlMWE2MzUyYzV8aD0ycnliZ3l3dWZ0bWQzdm9sNm41cTM2aDVxZHp3Mmc2bXwvWlo=
"""

url = raw_input('Enter the xunlei url:')
if len(url) < 1: url = href

url = base64.b64decode(url[10:])[2:-2]
print url