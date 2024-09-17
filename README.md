# Fitness Recipes
Fitness Recipes is a website for people looking for recipes that can help them increase physical and mental performance. With calorie calculated recipes, and the display of macro nutrients these recipes makes life easier when it comes to calculating the total intake for the day.
Hopefully it also inspires to a healthier and stronger lifestyle!

[Live Site](https://fitness-recipes-15e8ac3730aa.herokuapp.com/)

## Content
- Project Goals
  - User Goals
  - Site Owner Goals
 - Features
  - Navbar
  - Footer
  - Home page
  - Recipes page
  - Recipe detail page
  - Favorites page
  - About page
  - Sign In page
  - Register page
  - Sign out page
- Testing
- Validators
- Heroku Deployment
- Technologies
- Planning project
  - Wireframes
  - Database Schema
  - User Stories
  - Agile Planning
- Security
- Bugs
- Credits


## Project Goals
### User Goals

### Site Owner Goals

## Features
### Navbar

### Footer

### Home Page

### Recipes page

### Recipe detail page

### Favorites page

### About page

### Sign In page

### Register page

### Sign out page

### Future features
- Star ratings:
  - These will be implemented in the comment section below the recipe details where logged in users can rate a recipe if they wish to do so.

- Search, filter bars:
  - Search function that allows visitors and logged in users to search the webpage by keywords relating to ingredients, recipe title and ratings.
  - Filter that allows visitors and logged in users to filter recipes by servings, calories, macros and ratings.


## Testing
See TESTING.md for all the detailed testing

## Validators

## Deployment
### Version Control
- The site was created using Gitpod editor and pushed to Github to the remote repository 'fitness-recipes'.
- Git commands were used throughout the development to push the code to the remote repository. The following git commands were used:
  - git add . - to add the files to the staging area before being committed.
  - git commit -m "commit message" - to commit changes to the local repository queue that are ready for the final step.
  - git push - to push all committed code to the remote repository on Github.

### Prepare the workspace environment & settings.py
- Create an env.py, requirements.txt & Procfile in the main directory of your GitPod workspace
- Add the DATABASE_URL value, CLOUDINARY_URL and your chosen SECRET_KEY value to the env.py
- Import the env.py file in your settings.py file and add the SECRETKEY and DATABASE_URL file paths
- Comment the default database configuration out
- Save files, make migrations and migrate
- Add the Cloudinary URL to the env.py file
- Add the Cloudinary libraries to the list of installed apps in settings.py
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path
- Link the file to the templates directory in Heroku
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list in settings.py ['app_name.heroku.com', 'localhost']
- Important! In settings.py ensure DEBUG = False

### Heroku Deployment
- The app was deployed with Heroku following these steps:
  - After creating a Heroku account, click "New" to create a new app from the dashboard.
  - Create a name of the app, that needs to be unique, and select your region. Press "Create app"
  - Go to settings and add the necessary Config_vars. For this app there is a CLOUDINARY_URL for the storage of images in Cloudinary, DATABASE_URL to the CI Database used in the project and a SECRET_KEY to enable various security features and help protect sensitive data.
  - Go to Deploy tab and scroll down to Deployment Method.
  - Select GitHub and search for your GitHub repository.
  - Scroll down to deploy options.
  - For this project the Manual Deploy method was chosen.
  - Choose main branch and click Deploy Branch. This will deploy the current state of the branch specified.
  - Now the app is being built and when Deploy to Heroku has a green check mark, the build is finished.
  - Click View button to open the app in a browser window.

### Cloning of the Repository Code locally
Cloning a repository will download a full copy of the data to your computer. This is useful when larger commits need to be pushed, adding or removing files and fixing merge conflicts.
- Login to GitHub
- Click the repository you wish to clone (Top left corner)
- Click 'Code' which is shown above the list of files in the repository
- Click the 'Local' tab, copy the HTTPS URL
- Open Gitpod Workspaces, click 'New Workspace'
- Paste the copied URL into the space given under 'Repository URL'
- Click 'Continue' and the local clone will be created.

### Forking the GitHub repository
Forking a GitHub repository will allow you to make a copy of the repository, changes can then be made that will not affect the original repository. This is useful for proposed changes, ideas, fixes to an original repository.
- Login to GitHub
- Click the repository you wish to fork (Top left corner)
- Click the 'Fork' drop-down in the top right-hand corner
- Then click 'Create a new fork' you will now have a copy to work on.

### Database
This webpage is using PostgreSQL from Code Institute 
https://dbs.ci-dbs.net/
- Input your email
- Create a database
- Receive your link

### Cloudinary
The API platform has been used to store images uploaded by admin of the webpage
- Login to Cloudinary
- In the Dashboard, you can copy your API Environment Variable
- Be sure to remove the CLOUDINARY_URL= as part of the API value; this is the key in Config vars.

### Deploy your cloned or forked site
- Follow the steps above in: Prepare the workspace environment & settings.py
- Then use the instructions under: Heroky Deployment


## Technologies

## Planning project
### User Stories

### Agile Planning
This project was developed using Agile methodology which allowed me to iteratively and incrementally build my app, with flexibility to make changes to my design throughout the entire development process.

GitHub Issues and Projects were used to manage the development process. The board view of the Project feature was used to display and manage my progress in the form of a 'kanban board'. The user stories were added to the 'Todo' column to be prioritised for development, moved to the 'In Progress' column to indicate development of the feature had begun and finally moved to the 'Done' column when the feature had been implemented and the acceptance criteria had been met.
User stories were prioritised using the MoSCoW prioritisation technique. Each user story was given one of the following labels:
- Must have - to indicate the user story is guaranteed to be delivered.
- Should have - to indicate the user story would add significant value but is not vital.
- Could have - to indicate the user story would have a small impact if left out.
- Won't have - to indicate the user story is not a priority in the current iteration.

GitHub milestones were also used to group related user stories together.

Image of the Kanban board

The Project Kanban Board - link


### Wireframes
I created my wireframes using the Balsamiq app.

#### Home page
![Home wireframe](../fitness-recipes/readme_images/homepage.png)

#### Recipes page
![Recipes wireframe](../fitness-recipes/readme_images/recipe_list.png)

#### Recipe detail page
![Recipe detail wireframe](../fitness-recipes/readme_images/recipe_detail.png)

#### About page
![About wireframe](../fitness-recipes/readme_images/about_page.png)

### Database Schema
I created the database schema using the Lucidchart website.

![Database Schema](../fitness-recipes/readme_images/database_schema.png)

## Security
### Cross-Site Request Forgery (CSRF) Protection
By implementing CSRF protection in this project helps prevent malicious websites from executing unauthorized actions on behalf of authenticated users.
Django provides built-in CSRF protection by including a CSRF token with each form submission and verifying it on the server side.

### Django Allauth for Authentication and Authorization
Django Allauth was implemented in the project and is an authentication and authorization framework that provides features like registration, login, password management, and social authentication.
It ensures secure user authentication and authorization processes.

### Restricted Features for Non-Authenticated Users
By requiring users to be logged in to access certain features, the application enhances security and ensures that sensitive operations are performed by authorized individuals only.
The restricted features for authenticated users only are:
- Commenting on recipes
- Liking recipes
- Saving recipes to Favorites

### Admin site 
- Only the admin can add, edit and delete recipes.
- Admin must approve comments added by logged in users before they are displayed to other users of the site.

## Custom Error pages
- Error pages are customized for a better user experience

  - 404 Page Not Found Error
  - 500 Internal Server Error

Instructions on how to implement this was taken from here: https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages

## Bugs
- The message to add/remove recipes from Favorites is displaying, but only on the recipe_list page, and the heart is not filled in and added to the count on the recipe_detail display until I go out and back to the recipe_detail display.
  - Solution: moved likes.js script to recipe_detail template, and added defer to script tags in the base template to help with load performance.
- Clicking like redirects to this url: https://8000-sophietiger-fitnessreci-yqclcmt1m47.ws.codeinstitute-ide.net/recipe/toffee-apple-overnight-oats/like/
and a blank screen with only a raw json response is shown: {"liked": true, "likes_count": 2, "message": "Toffee Apple Overnight Oats added to Favorites!"}
  - Added some JavaScript to prevent the default form submission and handle the AJAX response correctly. 
- Delete and Edit functionality on comments suddenly stopped working when site was almost finished.
  - Analyzed error messages in the devtools console, pointing me towards a ReferenceError that Bootstrap is not defined at comments.js.
  After googling and serching for answers I wrapped my comments.js code in a DOMContentLoaded event listener to make sure that code runs only after the HTML document has been completely loaded and parsed, and all scripts (including Bootstrap) are ready to use.
- Number of likes not changing on the recipe detail page when clicking the heart-like button.
  - Searching and googling for answers gave me the idea to implement Optimistic updates that should provide a smooth user experience, and error handling that ensures that the UI stays in sync with the server state.
- Message that is displayed when liking/unliking recipes is still shown on other pages after clicked down by the user on the recipe details page.
  - Solution: implement a solution that clears the message after it's displayed via AJAX. Modify Javascript and View, add a new view to clear messages and a new url to display the new view. This approach ensures that the messages are displayed immediately via AJAX and then cleared from Django's message storage, preventing them from appearing on subsequent page loads.

## Credits

- https://django-taggit.readthedocs.io/en/latest/getting_started.html, taggit
- https://dev.to/radualexandrub/how-to-add-like-unlike-button-to-your-django-blog-5gkg, likes
- I think therefore I blog Walkthrough project. A big help when starting to build this project, and a huge inspiration for the structure.
- Tutor support has helped me a lot on the way and special thanks to Oisin, Recebecca and Holly.
- My mentor Spencer Bariball is always the best support and makes sure that I follow through, truly appriciate his valuable feedback.

- Recipes:
  - https://www.myprotein.com/
  - https://www.bbcgoodfood.com/
  

