# Fitness Recipes
Fitness Recipes is a website for people looking for recipes that can help them increase physical and mental performance. With calorie calculated recipes, and the display of macro nutrients these recipes makes life easier when it comes to calculating the total intake for the day.
Hopefully it also inspires to a healthier and stronger lifestyle!

Live Site ![https://fitness-recipes-15e8ac3730aa.herokuapp.com/]

## Content
- Project Goals
  - User Goals
  - Site Owner Goals
  - User Stories
  - Agile Planning
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
- Security
- Bugs
- Credits


## Project Goals
### User Goals

### Site Owner Goals

### User Stories

### Agile Planning

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

## Testing

## Validators

## Heroku Deployment

## Technologies

## Planning project
### Wireframes
### Database Schema

## Security

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
  

