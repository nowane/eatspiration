# Eatspiration | Data Centric Project 

## Project overview



---

![Mockup](/)

---

## Table of content

- [Tradeoff table](#tradeoff-table)
- [User experience -UX-](#user-experience--ux-)
  - [User stories](#user-stories)
  - [Design](#design)
    - [Colour scheme](#colour-scheme)
  - [Wireframes](#wireframes)
- [Features](#features)
  - [Features implemented](#features-implemented)
  - [Future features](#future-features)
  - [Features changed](#features-changed)
- [Technologies](#technologies)
  - [Languages](#languages)
  - [Integrations](#integrations)
  - [Version control- workspace and repository storage](#version-control--workspace-and-repository-storage)
  - [Other technologies](#other-technologies)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Deploy to Heroku](#deploy-to-heroku)
  - [Heroku](#heroku)
  - [Local development](#local-development)
- [Credits](#credits)


---

## Tradeoff table
	


[Back to table of content](#Table-of-Content) 

---

## User Experience -UX-

  ### User stories

<details>
<summary><b>As the site owner/admin</b></summary>

- As the owner/admin of the website, I want to be able to edit content to ensure it is conform the rules of the website.
- As the owner/admin of the website, I want the users of the website to have a positive user experience so that the community grows.
- As the owner/admin of the website, I want the users to be able to easily find, add, edit and be able to delete (their own) recipes to increase the number of recipes that are shared between users of the website.

</details>

<details>
<summary><b>As a new user</b></summary>

- As a new user, I want the website to be easily accessible from browsers of mobile devices as well as desktop.
- As a new user, I want to be able to easily see how to use the website, so I can start using the website effortlessly.
- As a new user, I want to be able to register with the site so that I can upload new recipes.
- As a newly registered user, I want to be able to log into my account so that I can access my recipes.

</details>

<details>
<summary><b>As a returning user</b></summary>

- As a returning user, I want to be able to search recipes by name so that I can find specific dishes.
- As a returning user, I want to be able to search recipes on cuisine type.
- As a returning user, I want to be able to be able to filter recipes based on cooking time.
- As a returning user, I want to be able to save my favourite recipes so that I can quickly find them again in the future.
- As a returning user, I want to be able to easily add, edit or delete my own recipes.
- As a returning user, I want feedback from the website when I add, edit or delete my recipes to show that my input is successfully processed.
- As a returning user, I want to be able to log out of the site when I am done using it.

</details>

[Back to table of content](#Table-of-Content)

---

### Design

  #### Colour scheme



[Back to table of content](#table-of-content)

---

![Colour scheme]()



[Back to table of content](#table-of-content)

---

### Wireframes

Added [Wireframes]() for desktop, tablet and mobile.

[Back to table of content](#table-of-content)

---

## Features

### Features implemented



[Back to table of content](#table-of-content)

---

### Future features 



[Back to table of content](#table-of-content)

---

### Features changed




[Back to table of content](#table-of-content)

---

## Technologies

  ### Languages



---

  ### Integrations



---

  ### Version control- workspace and repository storage



---

  ### Other technologies




[Back to table of content](#table-of-content)

---

## Testing

This [testing document](https://github.com/nowane/eatspiration/blob/main/TESTING.md)  contains all testing,

[Back to table of content](#table-of-content)

---

## Deployment

### Deploy to Heroku

<details>
<summary><b>Setup requirements:</b></summary>

Make sure "requirements.txt" is always up to date.  
Requirements.txt tells Heroku what resources are needed to run the app.

1.  Go to the Bash Terminal.
2.  Type the following: ```pip3 freeze --local > requirements.txt``` 
3.  Push all changes to GitHub.

</details>

<details>
<summary><b>Setup Procfile:</b></summary>

Heroku looks for this Procfile to find out which file runs the app and how to run it.

1.  Go to the Bash Terminal.
2.  Type the following: ```echo web: python app.py > Procfile```
3.  Open the Procfile and delete an empty line if there is one. It could potentially cause problems with Heroku.
4.  Push the file to GitHub.

</details>

### Heroku

<details>
<summary><b>Create a new Heroku application</b></summary>

1.  Go to the Heroku Dashboard.
2.  Click New.
3.  Select to create a new app.
4.  The Heroku app name must be unique, use "–" instead of spaces, and use lower case letters.
5.  "eatspiration" is the name of this application.
6.  Select the region closest to you.
7.  Click "create app".

</details>

<details>
<summary><b>Connecting to the GitHub repository</b></summary>

You can connect in different ways, like via the Heroku Command Line Interface as explained on the Heroku site. It's simpler however to deploy the site from Github. This way you only need to push to GitHub.

1.  Select Github, from the "Deployment method" section, on the "Deploy" tab.
2.  Make sure your GitHub ID is displayed and then enter the GitHub repository name "eatspiration" and click search.
3.  Once it finds the repository, click connect, to connect to the repository.

</details>

<details>
<summary><b>Setup the Config Vars</b></summary>

Because of the hidden environment variables inside the env file which are not available to Heroku, attempting to deploy at this stage would result in application errors. 

1.  Click on "Settings".
2.  Click on "Reveal Config Vars".
3.  Here we tell Heroku what secret variables are required. 
Add the Key-Value pairs as follows, without quotes:
``` 
    IP : 0.0.0.0   
    PORT: 5000   
    SECRET_KEY: ################
    MONGO_URI : mongodb+srv://root:<MONGO-PASSWORD>@myfirstcluster.ugdke.mongodb.net/<APP-NAME>?retryWrites=true&w=majority   
    MONGO_DBNAME: app_name
```  
**Note: you will get this information from the local copy of the env file.**

</details>

<details>
<summary><b>Automatic Deployment</b></summary>

Once the Config Vars has been entered you are ready for automatic deployment.

1.  Click on the "Deploy" tab.
2.  Click "Enable Automatic Deploys".
3.  Select the master branch.
4.  Click "Deploy Branch".

The project is now deployed.

</details>

### Local development

<details>
<summary><b>Forking</b></summary>

You can make a copy of the GitHub Repository by "forking" the original repository onto your own account, where changes can be made without affecting the original repository by taking the following steps: 
   
1. Login to your account on [GitHub](https://github.com/).
2. Locate the [repository](https://github.com/nowane/eatspiration) of this project.
3. On the right-hand side of the repository name, you'll see the "Fork" button.
4. This will create a copy in your personal repository.
5. Once you're finished making changes, return to original repository and press "New Pull Request" to request your changes to be merged into the original project.

</details>

<details>
<summary><b>Making a Local Clone</b></summary>

1. Log in to [GitHub](https://github.com). 
2. Locate the [GitHub repository](https://github.com/nowane/eatspiration).
3. Underneath the repository name, click "Code".
4. To clone the repository, select "HTTPS" and copy the link.
5. Open Git Bash.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type "git clone", and then paste the URL copied from step 4.
```
    git clone https://github.com/nowane/eatspiration
```
7. After pressing the "Enter" key, your local clone will be created.
8. Change into the directory being created.

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) for more information about cloning repositories. 

</details>

[Back to table of content](#table-of-content)

---

## Credits



[Back to table of content](#table-of-content)