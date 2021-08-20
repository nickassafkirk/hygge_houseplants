## Testing

Upon completion of the product and throughout it's development, each site page was tested thoroughly to ensure that responsive design was implemented, that site functionality performed as intended and overall the site provides a good user experience.

Each page was tested on desktop, mobile and then in dev tools. Tests were repeated On multiple browsers to ensure crose browser compatibility.

**Devices tested:**
- Mac Mini
- Iphone SE
- Macbook Pro 13"
- Samsung S8

**Browser tested:**
- Chrome
- Firefox
- Safari
- Opera

Unfortunately it was not possible to test internet explorer or microsoft edge.

**Additional testing:**
- The deployed site was distibuted to select friends and family who tested the project on a range of devices. No big were recorder and overall users reported a good user experience.
## User story Testing

**User Stories**
*As a new user:*
- I wish to immediately know the site's intention.
- I need to be able to navigate between site pages and sections easily.
- I wish to browse the sites product range.
- I need to view detailed information on particular products of interest.
- I want to purchase products directly through the site.
- I want to be able to create an account to improve my experience for future sessions.
- I want to access the business's social media profiles. 
- I need to be able to contact the business easily.
- I want to register for an account.
*As an existing user:*+
- I need to be able to login to my account.
- I need to view my past orders.
- I need to be able to logout of my account.
*As a site admin:*
- I want to be able to manage site products.
- I want to sort products into relevant groups.
- I need to view, create, edit and delete products.
- I need to view, create, edit and delete categories.
- I need to view, create, edit and delete users.
- I need to view, create, edit and delete orders.
- I need to be able to assign additional site administrators.

1. #### I wish to immediately know the site's intention.

    Upon landing on the homepage a large logo is apparent, the presence of the work 'plant' and the use of a leaf icon suggest that the page is plant/flower related. Looking at the main navigation links on desktop the categories plants, succulents, cacti and accessories suggest that the subject matter of the site is plant related. The link for shop all, cart, in the site header suggest that products are sold on thsi site. Scrolling down a large hero image with a picture of a plant is immediately apparent. The overlaying text describes the business's purpose. As a new user I understand that this site sells plants and related products. Haveing tested this experience I am satisfied that the user story has been satisfied. 

1. #### I need to be able to navigate between site pages and sections easily.

    Upon landing on the page on desktop 5 dominant links are visible in the main menu. Clicking each link brings me to the expected page where I can find related image. At the top of the page the logo can be clicked to return to home. On mobile devices an obvious burger stack icon button is visible. Clicking this reveals the same main links, clicking each link transports me to the expected page. On the homepage clicking the "view our range button" on the hero image transports me to the products page as expected.
    Clicking each of the category tiles takes me to the expected product category.
    In the footer the same links are visible clicking each link takes me to the expected page. With the exception of the Blog link and About link which refresh the current page. 
    On other site pages navigation is also predictable and self explanatory. Buttons and button like objects are apparent, clearly labelled and change color on action or hover. Similarly links stand out on the page and images are also often clickable as anticiapted. Overall having used the site I am satisfied that it is easy to navigate between site sections and the behavour demonstrated is as expected.

    **Known Issue** As outlined above, the Blog and About footer links do currently not link to any page. Unfortunately it was not in the scope of the current project to complete these pages but the decision has been made to leave the links present n order demonstrate their position for future development cycles of this project.

1. #### I wish to browse the sites product range & - I need to view detailed information on particular products of interest:

    From all pages the sites products can be accessed from the 5 links in the main navigation menu and the product links present in the footer.
    From the homepage the products can be accessed from the button overlay on the hero banner and via the category tiles on the index page. Products can also be found by using the search bar in the site header. 

    Once on [the products page](https://hygge-houseplants.herokuapp.com/products/) each product is clearly visible. Each products key information such as it's image, name, price and category can be seen. 

    A sort menu on the top of the product page allows me to sort products my my selected criteria. Clicking the view product button or the product image transports me to a detailed page with more information on the produuct of interest. On this page 
    More images are available if the product has options. Product options are selectable using the attached dropdown. Selecting a product option changes the image and price if it differs from the previous product variant. A product description is also visbile which provides detailed info on the product. 
    Towards the top of the page links split by a "/" charachter show me the path to the product I'm viewing. To go back I can use these breadcrumb links or the main navigation buttons in the header or footer. 
    Having tested the site I am satisfied that the site fulfils the user story. 

1. #### I want to purchase products directly through the site:
    On the detailed product page a clear add to cart form is visible. It uses bright colors and is immediately noticeable. A bold add to cart button tells me that I can add a product to the cart. Plus and minus buttons adjust the quantity showing me that I can add multiple quanities of a product to the cart. The buttons will not allow me to add more than the quantity displayed for a product to the cart. If a product has options I can select each option from the included dropdown menu.
    If the variant I have selected is a different price, the price updates as well. 
    After clicking the add to cart button, a message pops up notifying me that my item has been added to the cart. In the top right of the site a cart icon is visible. Clicking this icon brings me to a page where I can see that the item/s I added are present. Updating the quantity of a product in my basket and clicking upddate, updates the quantity accordingly. Clicking the delete button removes it from the cart. If I remove all the items from my cart a link to view more products is displayed.
    The cart total, product count, shipping amount and tax information are displayed. 
    A bright checkout button prompts me to continue to checkout. Clicking this button takes me to a page where a more concise summary of my cart is included. Here I can check that the items I want are what are in my order. Next a form allows me to fill out my personal details and shipping information. The form has a * character beside fields that are mandatory. If I forget to fill out a mandatory field the form will not submit and a message is shown. 
    A credit card input box is displayed. If I input an incorrect card a red error message is shown. If I input correct card details a loading spinner loads which shows me that my action has been received and my order is being processed.
    After a few moments a success message appears and I'm directed to a confimration page with a summary of my order. It also notifies me that an email has been sent to my address. From this experience I am satisfied that I can order products through the site and that the user story is satisfied. A link to my account or to products then allows me to navigate to more site sections.


1. #### I want to be able to create an account to improve my experience for future sessions.

    As a new user I can see an account menu option in the header of every page. Clicking in this reveals a sign up and sign in option. If i go to the sign up link, it takes me to a page where I can enter my details and create an account. To test his I used a [temporary mail service](https://temp-mail.org/en/) and entered my details. When clicking th sign up button I receive a message informing me that an email has been sent to my email. Checking my temporary email I can see that an email has been received. clicking the enclosed link brings me to a confirmation page when I can verify my email. Once I have clicked the verify email link, I am able to sign in using the username and password I just created. When I click the account button now I can see there is a link to my account.
    Clicking this link brings me to an account where I am greeted by my username. There's a form where I can fill out my details and area that says order history which is currently blank.
    If I fill out the form details and submit it, I can see that my details have been saved. If I re-fill out the form and change some details I receive an updaqte message and can see that my chenges have been saved. 

    By adding some items to my cart and going to the checkout page. My details are not entered into the form. This was not the expected behaviour. Once I have successfully completed my order I can see a link to my account on the confirmation page. Clicking this link brings me back to my accoutn where I can now see me order in the order history section. This is the expected behaviour. If I logout and log back in, I can see that my order history and personal details are retained. clicking an order number brings me to the order confirmation page for that order. Overall I am happy with this experience and believe that this user story is mainly satisfied although it would be preferable if my details were automatically added to the form on checkout.

    **Known Issue** As outlined above, the user details do not update when the save details selection is made on check, nor are they automatically enterred into the shipping details section of the checkout page. While this was the intended behaviour it was not possible to complete this functionality within the project deadline. However the save details, allow-marketing and message for seller form field and checkboxes have been retained for demonstration purposes and to allow these functionalities to be added going forward.

    








## Manual Testing



* Index Page - This is the primary landing page

* Products Page - View of all products with search options to narrow donw search.

* Single Product Page - A detailed view of a single product with an add to cart form and Edit and delete links for super users.

* Add Product page - This is an admin only page which contains a form where a new product can be added. There are two outcomes for this page:
    1. If the product has no variants, the product is created and the creator is directed to the detailed product page on completion.
    1. If the wproduct has variants, the user is taken to the add variants page on completion.

* Add Variant page - On this page a site admin can create, edit or delete product variants. On completion of this page, the user is brought to the single product view of the base product.

* Add collection page - This allows site admins to great a product collection. Unfortunately due to time limit it was not within the scope of this project to display product collections once created.

* Cart Page - This page displays the items that a user has added to their cart. There are two options:
    1. A user can proceed to checkout using the checkout button.
    1. A user can return back to products page using the alternate button.

* Checkout page - This page has two sections, a order summary section and a checkout area which enables the user to enter their details, pay and complete their order.

* Checkout success page - On successful checkout a user is brought to a success page which displays a concise summary of their order.

* Contact Page - The contact form is a generic contact form which enables users to send a message to the business. On successful completion a success message is displayed and the email is sent to the site admin's elected email address.

* Social page - This allows site admins to edit all social media ccounts displayed in the footer.

* Social/add - This allows a site admin to add a new social profile from the options that have been stored in the database.

* Social/add_icon - This allows a user to add a new icon and name to the available dropdowns.

* Account page - This allows users to store their account details and to view their previous orders.

* Login Page - This allows users with existing accounts to login and access their account.

* Logout Page - This allows logged in users to logout of their account.

* Signup Page - This allows new users to create an account.


## Validation:

#### HTML:
All site html was validated using the [W3C Markup Validation Service](https://validator.w3.org/): 

All pages passed without any validation errors.
- Index Page - No errors
- Sign In - No errors
- Sign Up  - No errors
- Sign Out - No errors
- Profile Page - No errors
- Contact page - No errors
- Social Page - No errors
- Social/add - No errors
- Social/add_icon - No errors
- Products Page - No errors
- Single Product Page - No errors
- Add Product Page - No errors
- Edit Product Page - No errors
- Add Variants Page - No errors
- Cart Page - No errors
- Checkout Page - No errors


#### CSS:
All site CSS was validated using the [W3C css valdation tool](https://jigsaw.w3.org/css-validator/). 

[Checkout app styles - checkout.css](https://github.com/nickassafkirk/hygge_houseplants/blob/main/checkout/static/checkout/css/checkout.css)

No errors were returned. 

[Base CSS File - style.css](https://github.com/nickassafkirk/hygge_houseplants/blob/main/static/css/style.css)

No errors were returned.
    86 Warnings were returned due to the use of root variables and vendor prefixes.
    These warnings can be ignored as it is well documented that both root variables and vendor prefixes are not supported by the W3C validation tool.

Vendor prefixes were added using [Autoprefixer](https://autoprefixer.github.io/).

