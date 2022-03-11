# QA community DevOps Project - Car/Engine tracker

## What my project shows

* A python based web app with complete CRUD functionality on two databases. 

  ![Example](https://i.ibb.co/Yyg7WqR/Project-example.png)
* A one-to-many relationship between two entities. At first my project was just one table with CRUD functionality, so I'm happy with one-to-many.

  ![ERD](https://i.ibb.co/RYcYBz3/ERD-first.png)
* Unit testing with 95%+ coverage. 

  ![Testing](https://i.ibb.co/C8J4y93/Test-coverage.png)

* Jenkins credentials used alongside environment variables to protect sensitive information. This seemed to be the best way to store keys and passwords for use with my project as other methods would have been way too complicated and out-of-scope.

  ![Jenkins-credentials](https://i.ibb.co/2N2cLHP/Jenkins-credentials.png)

* I made a risk assessment table to help me prioritize problems should any arise.
  ![Risk-assessment](https://i.ibb.co/NWTk51W/Risk-Assessment.png)

  As I went on with the project, I added a couple more entries to the risk assessment table which I didn't even know would be issues when I started the risk assessment.
  ![Risk-update](https://i.ibb.co/23mb1gz/Risk-Assessment-update.png)

* Here is a very simple diagram of my CI Pipeline. I used Github projects to keep track of jobs. Using Github as my repository, I am able to pull code down to any local machine with access to the internet, making my work very accessible. When I have made changes to the code on my local machine, I am able to push these changes to the Github repository. With a webhook configured, Jenkins will automatically build a new Docker image when any changes are made to the repository. This Docker image is pushed to my docker hub repository. Each new build is automatically tested by Jenkins using the unit tests I wrote with the pytest module. If the tests pass and the image is built, the app is deployed onto a Docker container which is hosted on a Azure Virtual Machine.
  ![Pipeline](https://i.ibb.co/fVgJv5p/CI-Pipeline.png)
  

* [Kanban Board](https://github.com/users/GooeyG/projects/1/views/1)

  ![Kanban-image](https://i.ibb.co/cDYffRw/Kanban-Board.png)
  ![User-story](https://i.ibb.co/ZHhKjJN/User-Story.png)

My kanban board features tags following MoSCoW priotisation technique, helping me achieve point targets based on the project marking criteria.
**You can also click on each objective on the kanban board to access my user stories located in the comments of the objective itself.**
I realize this isn't the ideal way to approach agile fundamentals in a devops environment but for the sake of the course it shows that I understand agile methodology. Eg. I didn't want to create sprints for this project as we have less than two weeks designated towards working on the project.

## What I would add if I had more time

* More time spent learning HTML to make the webapp more aesethically pleasing
* Login feature to prevent tampering with the database
* Logic built into code to prevent database errors eg. Not allowing an item in the parent table to be deleted if it is used as a foreign key in the child table.
* Search functionality to make the database easier to navigate.
* A reserved IP for the Jenkins VM to avoid having to keep updating the webhook.
 
## Getting familiar with Jenkins and Docker

As I'm completely new to tech I wanted to experiment with jenkins, starting with simple things.

* My first freestyle job was just to get used to interacting with jenkins.

  ![Jenkins-install](https://i.ibb.co/ysQ51TR/Installing-Jenkins.png)

  I started with cloning down my repository to get my project onto my Jenkins VM. This isn't much use on it's own but it will be a good place to start. Here are the logs which show the repository was cloned down successfully.

  ![Jenkins-log](https://i.ibb.co/DK6Qxxc/Jenkins-clone-github.png)

  As you can see here, the files were now able to be accessed on my Jenkins VM.

  ![Jenkins-VM-files](https://i.ibb.co/znfpsC5/Jenkins-clone-confirmed.png)

  Obviously this is not very useful at all and it would have been much easier to simply git clone directly in my VM's terminal. I need to expand on this and get things automated.

  Here I have Jenkins pulling from the develop branch of my repository and it is setting up my Flask app on the VM and then running the unit tests. As you can see here the coverage report is 98%. At this point I am still using an sqlite database which I plan to later change to an SQL database hosted on a container.

  ![Jenkins-Tests](https://i.imgur.com/PgA0UZg.png)

  Here we can see after my unit tests are completed Jenkins will run the app.

  ![Jenkins-Running](https://i.ibb.co/ZGT33k4/Jenkins-running.png)

  As you can see Jenkins and my app are running on the same IP address as they are both running on my VM. This doesn't really have any functionality as data for my tables would not persist. Doing things this way would also mean that while I am updating the build, the app would not be accessible. 

  ![Jenkins-IP](https://i.ibb.co/1rgxYF5/Jenkins-running1.png)

   Now that I have Jenkins successfully building my app, testing it and running it I need to move onto Docker. With Docker I hope to have my app accessible while applying updates and at the same time having the ability to deploy updates quicker.

  ![Docker-install](https://i.ibb.co/HPh4t5g/Docker-installation.png)

  Before implenting credentials I was struggling to get Jenkins to push to Docker hub. My pipeline was getting to the end of the build and failing to push to my dockerhub account as it couldn't log in.

  ![Docker-fail-image](https://i.ibb.co/LvgyM76/Docker-Image-Fail.png)

  I added credentials to Jenkins which managed the username and password for docker hub. Now my Jenkinsfile has my dockerhub login information in a secure way. This was the last hurdle to getting a pipeline which pulls from github, builds an image and pushes it to dockerhub.

  ![Docker-hub-image](https://i.ibb.co/xsscsHz/Docker-Image-built.png)
  ![Docker-hub-account](https://i.ibb.co/6ZGPnvk/Dockerhub-Image.png)

  ![Final-video](https://www.youtube.com/watch?v=NKx6GyYJ-jo)
