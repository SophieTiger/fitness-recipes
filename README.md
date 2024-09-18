# Fitness Recipes
Fitness Recipes is a website for people looking for recipes that can help them increase physical and mental performance. With calorie calculated recipes, and the display of macro nutrients these recipes makes life easier when it comes to calculating the total intake for the day.
Hopefully it also inspires to a healthier and stronger lifestyle!

![Responsive image of homepage](../fitness-recipes/readme_images/responsive_devices.png)

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
- Testing and validation
- Heroku Deployment
- Technologies
- Database Models
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
- Easily find and open a recipe that I like.
- As a logged in user - Interact with other users by liking and commenting on a recipe.
- As a logged in user - Saving favorite recipes to "Favorites" for easy access.
- Be able to navigate the platform and access relevant information easily.
- Have the possibility to contact the site owner for request on further nutrition coaching or other questions.
- Have a visually appealing and responsive user interface.

### Site Owner Goals
- Have a fun and interactive website about recipes that contribute to strength and overall health.
- Have users to frequently come back to the website to look for new recipes or use their favorites.
- Use the site as a tool in Nutrition coaching.
- Get new potential clients.

## Features
### Navbar
Fully responsive navbar, with links to:
  - Home Page
  - Recipes Page
  - About Page
  - Favorite Page (If the user is authenticated)
  - Sign Up page (If the user is not authenticated)
  - Sign Out (If the user is authenticated)
  - Sign In (If the user is not authenticated)

The Fitness Recipes name and the dumbbell icon are also linked to the home page.
The dumbbell icon is rotated by -15 deg and turned into a green color when hovered over for a visual effect.

For non-authenticated users:
![Navbar Image](../fitness-recipes/readme_images/navbar_non_auth.png)

![Navbar small screens](../fitness-recipes/readme_images/navbar_small_non_auth.png)

For authenticated users:
![Navbar Image](../fitness-recipes/readme_images/navbar_auth.png)

![Navbar small screens](../fitness-recipes/readme_images/navbar_small_auth.png)


### Footer
Fully responsive footer, with working links, that opens in a new browser window:
  - [Facebook](https://www.facebook.com/)
  - [Instagram](https://www.instagram.com/)
  - [YouTube](https://www.youtube.com/)

[Footer Image](../fitness-recipes/readme_images/footer.png)

### Home Page

### Recipes page

### Recipe detail page

### Favorites page

### About page

### Sign In page

### Register page

### Sign out page

### Static File Storage
The app uses the Cloudinary cloud service to store static files such as images. To store the recipe images uploaded by admin user when creating a recipe, the Cloudinary field uses the Cloudinary API to upload the images to the Cloudinary server and store the image URL in the database.

### Future features
- Star ratings:
  - These will be implemented in the comment section below the recipe details where logged in users can rate a recipe if they wish to do so.

- Search, filter bars:
  - Search function that allows visitors and logged in users to search the webpage by keywords relating to ingredients, recipe title and ratings.
  - Filter that allows visitors and logged in users to filter recipes by servings, calories, macros and ratings.


## Testing and validation
See [TESTING.md](../fitness-recipes/TESTING.md) for all the detailed testing and validation.

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
- Then use the instructions under: Heroku Deployment


## Technologies
### Languages
- HTML5
- CSS
- JavaScript
- Python

### Frameworks, Libraries and Packages
- asgiref==3.8.1
- cloudinary==1.36.0
- crispy-bootstrap5==0.7
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==4.2.15
- django-allauth==0.57.2
- django-crispy-forms==2.3
- django-summernote==0.8.20.0
- django-taggit==6.0.0
- gunicorn==20.1.0
- oauthlib==3.2.2
- psycopg2==2.9.9
- PyJWT==2.9.0
- python3-openid==3.2.0
- requests-oauthlib==2.0.0
- sqlparse==0.5.1
- urllib3==1.26.20
- whitenoise==5.3.0

### Tools
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Gitpod](https://www.gitpod.io/)
- [Heroku](https://heroku.com/)
- [CI Database Maker](https://dbs.ci-dbs.net/)
- [Cloudinary](https://cloudinary.com/)
- [Balsamiq](Balsamiq)
- [Lucidchart](https://www.lucidchart.com/pages)
- [Birme](https://www.birme.net/?image_format=webp&quality_webp=100)
- [Tiny PNG](https://tinypng.com/)
- [Am I Responsive](https://ui.dev/amiresponsive)
- [Favicon](https://favicon.io/)
- [Font Awesome](https://fontawesome.com/)
- [The W3C Markup Validation Service](https://validator.w3.org/)
- [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [Code Institute Python Linter](https://pep8ci.herokuapp.com/)
- [JSHint](https://jshint.com/)
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)


## Database Models
The Fitness Recipes app uses a relational database to store and manage data. The relational database management system software used for this project is PostgreSQL which is hosted on the cloud service [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/).

### Recipe Model
Title - a CharField with a maximum of 100 characters that requires a unique value.

Slug - an autopopulated field that uses django-autoslug, a django library that provides an improved slug field which can automatically populate itself from another field, preserve uniqueness of the value and use custom slugify() functions for better i18n.

Description - a TextField with a maximum of 300 characters.

Author - a ForeignKey linking the recipe to the user model of the user who created it.

Featured_image - a CloudinaryField which contains the URL to the image that is stored on the Cloudinary server. If no image is added by the recipe creator, a default image is added.

Servings - an IntegerField with a dropdown of choices of 1-10, stored in the SERVINGS list of tuples.

Calories - a CharField with a maximum of 10 characters.

Protein - a CharField with a maximum of 10 characters.

Carbs - a CharField with a maximum of 10 characters.

Fat - a CharField with a maximum of 10 characters.

Ingredients - a TextField. Summernote is added to this field in the admin panel for styling purposes.

Instructions - a TextField. Summernote is added to this field in the admin panel for styling purposes.

Tags - the tags field uses a django application called django-taggit. It uses the class TaggableManager() to manage the relationships between the recipe and the associated tags.

Created_at - a DateTimeField that autopopulates with the current date and time when a recipe is created.

Updated_at - a DateTimeField that autopopulates and updates with the current date and time when a recipe is updated.

Status - an IntegerField with choices of "Draft"(0) or "Published"(1), stored in the STATUS tuple of tuples. Default is 0.

### Comment Model
The comment model was taken from Code Institute's 'Codestar Blog'.

Post - a ForeignKey linking the comment to the recipe it is associated with.

Author - a ForeignKey linking the author of the comment to the user it is logged in as.

Body - a TextField to store the comment submitted.

Created_on - a DateTimeField that autopopulates with the current date and time when a comment is submitted.

Approved - a BooleanField that defaults to false and is updated to true by admin when the comment is approved.

### Like Model

User - a ForeignKey linking the user performing the like-action to the user it is logged in as with help of the built in User model.

Recipe - a ForeignKey linking the like to the recipe it is associated with.

Created_on - a DateTimeField that autopopulates with the current date and time when a comment is submitted.


### About Model

Title - a CharField with a maximum of 200 characters that requires a unique value.

Content - a TextField. Summernote is added to this field in the admin panel for styling purposes.

Updated_on - a DateTimeField that autopopulates and updates with the current date and time when a recipe is updated.

### ContactRequest Model

Name - a CharField with a maximum of 200 characters.

Email - an EmailField that reqires a valid email address format.

Message - a TextField.

Read - a BooleanField that defaults to false and is updated to true by admin when the contact message is ticked as read in the admin panel.


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

![Image of the Kanban board](../fitness-recipes/readme_images/user_stories_kanban.png)

[Link to the Project Kanban Board](https://github.com/users/SophieTiger/projects/4/views/1?visibleFields=%5B%22Title%22%2C%22Status%22%2C%22Labels%22%5D)


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
The Entity Relationship Diagram below shows the structure of the database and the relationships between the tables.

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

### Admin Panel
- Django's admin panel can be accessed by 'superusers' and users with the permission of 'staff status'. 
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
  
- I created the Entity Relationship Diagram (ERD) using the [Lucidchart](https://lucid.co/?_gl=1*17qu8xy*_gcl_au*NzE1MDIyOTA3LjE3MjQyMjYwNjc.*_ga*MTAzNzI0MjYwMS4xNzExNjI4NDcw*_ga_MPV5H3XMB5*MTcyNjY0NzI1NS43LjEuMTcyNjY0NzI2NS41MC4wLjA.) website.
