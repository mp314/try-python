import mechanize  #pip install mechanize
import sys
import yaml

br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [("User-agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")]

sign_in = br.open("https://en.boardgamearena.com/account")  #the login url

br.select_form(name = "login") #accessing form by their index. Since we have only one form in this example, nr =0.
#br.select_form(name = "form name") Alternatively you may use this instead of the above line if your form has name attribute available.

br["email"] = "username" #the key "username" is the variable that takes the username/email value

br["password"] = "password"    #the key "password" is the variable that takes the password value

logged_in = br.submit()   #submitting the login credentials

logincheck = logged_in.read()  #reading the page body that is redirected after successful login

#print(logincheck) #printing the body of the redirected url after login

req = br.open("https://boardgamearena.com/gameinprogress").read()

original_stdout = sys.stdout 
with open('dump.html', 'w') as f:
    sys.stdout = f
    
    print(logincheck)
    #print(req)
    sys.stdout = original_stdout

#accessing other url(s) after login is done this way 
