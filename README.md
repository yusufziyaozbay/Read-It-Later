# READ IT LATER
#### Video Demo:  https://youtu.be/oaS8x4JQwM4
#### Description:
"Read It Later" is a user-friendly web application that allows users to effortlessly save and organize articles they wish to read at a later time. With features like categorization and customization, users can easily curate their own personalized reading list, which empower users to create a personalized reading list that suits their unique interests and preferences. This convenient tool ensures users never miss out on valuable content and promotes a seamless and enjoyable reading experience. Beyond its desktop accessibility, "Read It Later" is also optimized for mobile devices. With a responsive design, users can access their curated reading list from any device, giving them the freedom to read on the go.

### Why This Project?
Opening tabs while browsing the web can easily cause a mess. Adding bookmarks to the articles you want to read later is not efficient enough because you have to remove the bookmark after reading. To make this process easier, I developed my own "read it later" web application.

### Technologies
I chose Django and hence python to develop the web application. I used sqlite as the default database was enough for me. Html, CSS and bootstrap to style the interface and some javascript to add movement. 3rd party libraries for features such as link preview.

### App Design
Since I was using django in the project, I had some decisions to make, especially about the program design. Since the Sqlite database is simple and sufficient, I continued with it. I set two titles for myself as an application in Django; authentication and bookmarks. In the authentication application, I did things like user registration and mail verification. The bookmarks application has everything related to bookmarks operations.

I used django's own user model as the user model, and since I didn't extend this model, the program is logged in with the username.

I hid sensitive information that I need to handle carefully in environment variables as it should be.

To improve features like link preview (unfurl preview), I used libraries like beautifulsoup4 that scrape information from web pages. The full list of these libraries is in the requirements.txt file.

The "readitlater" file is the project file of django. Here the settings related to the project are made. Instead of collecting all the urls of the application in the "urls.py" file, I created a "urls.py" file inside the applications and included it in the main file with the "urlpatterns" command. This avoids any possible confusion.

The file "settings.py" contains important configurations for the project. Here, first of all, the environment variable keys are included. - since these keys contain sensitive data, I did not include them in the project. - The directory for the template files is specified and the database is introduced.

Images and style files are located in the "static" file under apps. There is another file under the static file that takes the name of the application because if this is not done, two different static files with the same name can be confused even if they are in different applications, to prevent this error, the application name was written in the file.

One critical decision I made while developing the app was how to store the link photos added by the user. Instead of downloading the link photo, naming it automatically and saving it to the database, I decided to save the address of the photo to the database as text. This is both a more practical solution and useful, because the information about the link is already collected during registration and the photo is retrieved with its address in this process. Also, if all the link photos were saved in the database, this would increase the size of the application in a short time. I wanted to keep the program as lightweight as possible, so I saved the photos with their addresses.
