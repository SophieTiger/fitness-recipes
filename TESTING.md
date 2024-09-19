# Fitness Recipes | Testing

Back to the [README](README.md)

Comprehensive manual testing has been performed throughout the development of this webpage to ensure the seamless and optimal functionality of all features.

## Manual Testing
A total of 78 manual tests were structured in a document with the following topics:
-   Non-Authenticated User Tests
-   Authentication Tests
-   Authenticated User Tests
-   Like feature on recipes
-   Recipe Browsing and Filtering
-   Responsiveness Tests
-   Error Handling
-   Performance Tests
-   Security Tests
-   Admin Authentication
-   Recipe Management
-   Tag Management
-   User Management
-   Comment Moderation
-   Contact Form Messages
-   Admin Interface Customization
-   Image Handling
-   Admin Actions Logging

The document was structured as a Test schema into columns with Tests and Status.
Status have 4 options; Not started, Fail, Pass or Test Subject.
![Test Status image](./readme_images/test_status.png)

This document was used throughout the development process.

[Link to the full Google test document](https://docs.google.com/spreadsheets/d/1L--W--hgOou8HRXE2FjazDIsixKQZULy3gec19Mxbpo/edit?usp=sharing)

### Chrome Developer Tools
Chrome developer tools were used throughout the development of the webpage to test responsiveness. Responsiveness was tested using developer Tools to emulate the following devices:

-   Desktop
-   Laptops
-   Tablets
-   Mobile phones

### Browser Testing
During the development of the webpage the testing was done using Google Chrome. In production the site has been tested on the following browsers:
-   Google Chrome
-   Mozilla Firefox
-   Safari

## Validation

### [W3C HTML Validator](https://validator.w3.org/)

### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

### [JSHint JavaScript Validator](https://jshint.com/)

### [CI Python Linter](https://pep8ci.herokuapp.com/)

## Lighthouse Testing

## Bugs
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
- At the moment no bugs left that I am aware of.

Back to the [README](README.md)