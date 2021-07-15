# ToDo List: A post it board
#### Video Demo:  https://youtu.be/VZxycCX0dxo
#### Description: 
I've created this project to help people that, like me, tend to have notes with their chores pasted somewhere in the wall. It is both user friendly and practical, so feel free to take a look!
#### How it went:
##### Flask: 
This is the core of my solution. I've created most of the functionalities if this website using Flask, a web framework for python.
It introduces also Werkzeug library, which i've used for password hashing, and the Jinja template mechanism, that i've used to create a main template, that has been used in all other pages.
###### HTML: 
I've started creating a main template, that contains everything but main and title. From there, i've created the other html pages and filled only the missing parts.
###### CSS: 
For CSS, i chose bootstrap as the framework, and made a lot from there, but the styles.css file contains a lot of tweaks for the logo, body, and the notes.
###### JavaScript:
The beginning of the project used JavaScript for most of the functions involved. But, since flask was way easier to work for what i was looking for, i chose to switch the JS functions to Flask, remaining only the color picker as a function.
###### Database:
I ended up with sqlite3, since i was familiar with it.


##### app.py:
The main file of the website, contains almost everything. The beginning has the login required decorator and the apology function (that i use as an apology page to warn the user something). Then it goes to note management, that involves the index page and note functions such as deleting notes, changing color, etc.
Then i go user management functions, where i have the login, logout and register part of the code.
