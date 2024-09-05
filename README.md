

## Bugs
- The message to add/remove recipes from Favorites is displaying, but only on the recipe_list page, and the heart is not filled in and added to the count on the recipe_detail display until I go out and back to the recipe_detail display.
  - Solution: moved likes.js script to recipe_detail template, and added defer to script tags in the base template to help with load performance.
- Clicking like redirects to this url: https://8000-sophietiger-fitnessreci-yqclcmt1m47.ws.codeinstitute-ide.net/recipe/toffee-apple-overnight-oats/like/
and a blank screen with only a raw json response is shown: {"liked": true, "likes_count": 2, "message": "Toffee Apple Overnight Oats added to Favorites!"}
  - Added some JavaScript to prevent the default form submission and handle the AJAX response correctly. 

## Credits

- https://django-taggit.readthedocs.io/en/latest/getting_started.html, taggit
- https://dev.to/radualexandrub/how-to-add-like-unlike-button-to-your-django-blog-5gkg, likes

- Recipes:
  - https://www.myprotein.com/
  

