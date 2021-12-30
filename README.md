# Scandic

This website is the marketing website for the fictious Scandic restaurant and was built as part of the learning material for Code Institute's Fullstack Web Developer program (5P) Portfolio Project.
It is designed to be responsive and accessible on a range of devices, making it easy to navigate for potential visitors and users.

Portfolio Project Four: Back end - Code Institute - Deadline 02th January 2022


[View the live project here.](https://scandic.herokuapp.com/)

<img src="static/images/" width="500">


# Table of Contents

- [Scandic](#scandic)
  * [The purpose of this site](#the-purpose-of-this-site)
  * [User Experience](#user-experience)
    + [User Goals](#user-goals)
    + [Site Owners Goals](#site-owners-goals)
    + [USER STORIES](#user-stories)
    + [STRATEGY](#strategy)
    + [SCOPE](#scope)
    + [Structure](#structure)
    + [SKELETON](#skeleton)
  * [SURFACE](#surface)
    + [Technologies](#technologies)
  * [Existing Features](#existing-features)
    + [Elements on every page](#elements-on-every-page)
    + [Features Left to Implement](#features-left-to-implement)
  * [Testing](#testing)
    + [Responsiveness](#responsiveness)
    + [Manual and Automated testing](#manual-and-automated-testing)
    + [Errors encountered during development](#errors-encountered-during-development)
    + [Known error present:](#known-error-present-)
    + [Validating code](#validating-code)
  * [Setting up Django environment.](#setting-up-django-environment)
  * [Deployment](#deployment)
  * [Credit](#credit)
  * [Acknowledgment](#acknowledgment)


# UX

## User stories

# Technologies

# SCOPE

**Features:**

  **Home page** -

  **Meals list** -

  etc.

### Structure


### SKELETON
  **Wireframe:**
  The mockup for this site was done on Balsamiq Wireframes


## SURFACE
  **Colour Pallette:**

  **Typography:**


## Technologies

### Languages used

## Existing Features


### Features Left to Implement

## Testing

For all testing documentation, please refer to [TESTING.md](TESTING.md)

## Setting up Django environment.

Following additional packages are installed to create this site by using pip3 install
  
  * gunicorn
  * psycopg2
  * django-summernote

  ## Deployment

## Deployment steps

1. Git add and git commit the changes made

2. Log into [Heroku](https://id.heroku.com/login) or create a new account and log in

3. top right-hand corner click "New" and choose the option Create new app, if you are a new user, the "Create new app" button will appear in the middle of the screen

4. Write app name - it has to be unique, it cannot be the same as this app

5. Choose Region - I am in Europe

6. Click "Create App" The page of your project opens.

7. In the Add-on section in the resources tab, search postgres, then select Heroku Postgres and submit order from button in the popup window.

8.  Choose "settings" from the menu on the top of the page

9. Go to section "Config Vars" and click the button "Reveal Config Vars"

10. Copy the value for `DATABASE_URL` key

11. Create env.py directly under the repo directory same lavel as manage.py and make sure the file name is included in .gitignore as this is a setting for local development site in Gitpod. 
Heroku Config vars need to be set accordingly including `DATABASE_URL` and `SECRET_KEY`

12. Create env.py directly under the repo directory same lavel as manage.py and make sure the file name is included in .gitignore as this is a setting for local development site in Gitpod. 
Heroku Config vars need to be set accordingly including DATABASE_URL and SECRET_KEY

13. In the Gitpod terminal, migrate the change by
`python3 manage.py migrate`. Check the resource tab in heroku and choose 
Heroku Postgres then ensure the changes are reflected in the database

14. DISABLE_COLLECTSTATIC set to 1 in Config Vars in Heroku as the initial deployment does not contain static files yet.

15. In setting.py configure followings:

    * Set STATICFILES_DIRS, STATIC_ROOT, MEDIA_URL and DEFAULT_FILE_STORAGE so that Django can use the directories appropriately.

    * Set TEMPLATES_DIR just below BASE_DIR and insert TEMPLATES_DIR in TEMPLATES array
    'DIRS': []

    * Set ALLOWED_HOSTS array as 'scandic.herokuapp.com', 'localhost'

16. Create Procfile with the contents 

    web: gunicorn scandic.wsgi    

17. Next go to "Deploy" in the menu bar on the top

18. Go to section "deployment method", choose "GitHub"

19. New section will appear "Connect to GitHub" - Search for the repository to connect to

20. type the name of your repository and click "search"

21. once Heroku finds your repository - click "connect"

22. Scroll down to the section "Automatic Deploys"

23. Click "Enable automatic deploys" or choose "Deploy branch" and manually deploy
   * I have chosen manual deployment by pressing the Deploy branch button instead of Enable Automatic Deploys 

24. Click "Deploy branch"

Once the program runs: you should see the message "the app was successfully deployed"

 25. Click the button "View". This View button will open the terminal game in the new window. Here is the deployed page [Scandic](https://scandic.herokuapp.com/)

 26. As manual deployment was chosen, I had to come back to the Heroku deployment page whenever I have an updated working version pushed into the GitHub page.  

# Forking the GitHub repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log into [GitHub](https://github.com/) or [create an account](https://github.com/).

2. Locate the GitHub repository. Link can be found [here](https://github.com/HeleJ/scandic).

3. At the top of the repository, on the right side of the page, select "Fork".

4. You should now have a copy of the original repository in your GitHub account.

# Making a local clone

1. Locate the GitHub repository. Link can be found [here](https://github.com/HeleJ/scandic).

2. Next to the green Gitpod button you will see a button "code" with an arrow pointing down

3. You are given the option to open with GitHub desktop or download zip

4. You can also copy the https full link, go to git bash and write git clone and paste the full link

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/HeleJ/scandic)

# Credits

  * My mentor Tim Nelson

  * Rebecca at [CI Tutor support](https://learn.codeinstitute.net/ci_support/diplomainsoftwaredevelopmentecommerce/tutor) for his patience and guiding me in the right direction.
