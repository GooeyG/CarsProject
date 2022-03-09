# QA community DevOps Project - Car/Engine tracker

## What my project shows

* A python based web app with complete CRUD functionality on two databases. 

  ![Example](https://i.ibb.co/Yyg7WqR/Project-example.png)
* A one-to-many relationship between two entities.

  ![ERD](https://i.ibb.co/RYcYBz3/ERD-first.png)
* Unit testing with 95%+ coverage. 

![Testing](https://i.ibb.co/C8J4y93/Test-coverage.png)
* Containers used to host my web application
* Jenkins to test and build my application

* [Kanban Board](https://github.com/users/GooeyG/projects/1/views/1)

My kanban board features tags following MoSCoW priotisation technique, helping me achieve point targets based on the project marking criteria.
**You can also click on each objective on the kanban board to access my user stories located in the comments of the objective itself.**
I realize this isn't the ideal way to approach agile fundamentals in a devops environment but for the sake of the course it shows that I understand agile methodology. Eg. I didn't want to create sprints for this project as we have less than two weeks designated towards working on the project.
 
## Getting familiar with Jenkins

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
