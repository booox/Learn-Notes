import requests

login_page = 'http://www.ebama.net/member.php?mod=logging&action=login'

headers = { 
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
} 
form_data={"username": 'a',"password":'a',"loginsubmit":'true'} 
s = requests.Session() 
r = s.post(login_page, data=form_data, headers=headers) 

print "action=logout" in r.text
print "action=logout" in r.content
print r.status_code
print type(r.cookies)
print '=' * 15
print r.cookies

for k,v in r.cookies.items():
    print k, v