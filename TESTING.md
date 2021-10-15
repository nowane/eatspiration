# Testing

## Table of Content

- [Manual testing of each section of the site](#manual-testing-of-each-section-of-the-site)
- [Testing site responsiveness](#testing-site-responsiveness)
- [Code validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [Javascript](#javascript)
- [Testing of user stories](#testing-of-user-stories) 
    - [Testing as a new user](#testing-as-a-new-user)
    - [Testing as a returning user](#testing-as-a-returning-user)
- [Documentation of any bugs encountered and their resolution steps](#documentation-of-any-bugs-encountered-and-their-resolution-steps)
- [Documentation of any open bugs](#documentation-of-any-open-bugs)

---

## Manual testing of each section of the site



[Back to the top](#testing)

---

## Testing site responsiveness 

A mockup of the project, displaying responsiveness.

![Mockup]()

[Back to the top](#testing)

---

## Code validation

### HTML

Code validated using https://validator.w3.org/ .

![Validation]()

[Back to the top](#testing)

---

### CSS

Code validated using https://jigsaw.w3.org/css-validator/ .

![Validation]()

[Back to the top](#testing)

---

### Javascript

Code validated using https://jshint.com/ .

![Validation]() 


[Back to the top](#testing)

---

## Testing of user stories.

  ## Testing as the site owner


  ### Testing as a new user



  ### Testing as a returning user


[Back to the top](#testing)

---

## Documentation of any bugs encountered and their resolution steps

- When adding the footer at the bottom at the page without being fixed using flexbox, there was a small gap of white space underneath the footer. According to devtools this was caused by an "I"-element with the classname of "material-icons". See images below.

![Footer white space](docs/testing/images/white-bottom-footer.png) 
![material-icons](docs/testing/images/footer-i-material-icons.png) 

> This was solved deleting the last "row" class in the div with my name in it, since apparently this caused the white space. Deleting the whole div with the name in it still caused the space te appear. Because of this I decided on keeping the bottom div in the footer, and keep the name in it hidden. See image below.

![Footer white space solved](docs/testing/images/footer-hidden.png) 

---

- The "Add Recipe"-page seemed to have issues with responsiveness when resizing via the "Toggle device toolbar". I thought this perhaps had something to do with Materialize and the fact using the "row" class sometimes gives extra whitespace, similar to how it affected the footer. See image below.

![Add recipe page not loading correctly](docs/testing/images/add-recipe-bug.png) 

> After a lot of fiddling around I found out by accident that whenever you load the screen with a small device as starting point, the page would actually load as intended. See image below.

![Loads as intended](docs/testing/images/add-recipe-on-load.png)

---

- At the "Edit Recipe" page there was an issue where whenever you changed data and submitted all was saved correctly. However when submitting the for whenever there were no changes deleted the preperation steps, which were inserted in a textarea element.

> This was resolved by editing the input element of the preperation steps, which is now the same as the ingredients input.


[Back to the top](#testing)


## Documentation of any open bugs 



[Back to the top](#testing)

[Back to README.md](https://github.com/nowane/eatspiration/blob/main/README.md)

[Back to Repository](https://github.com/nowane/eatspiration)