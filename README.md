# Hygge Houseplants - An ecommerce site built using the Django Framework

[![responsive project preview](media/responsive.png)](https://hygge-houseplants.herokuapp.com/)

[Visit the live site here](https://hygge-houseplants.herokuapp.com/)

### Introduction:
---

Hygge Houseplants is an ecommerce website built to sell specialist houseplants and accessories to plant enthusiasts online. The project is a full stack web application built using the Django Framework. The key purpose of the project is to provide additional revenue and online awareness for the business and to allow site administrators to easily update and manage key site areas through the front end site and admin panel. This project was built as my submission for my milestone 4 project during the code institute Diploma in Software Development.

*Please note: The business depicted in this project does not exist. The business and all products have been imagined purely as a demonstration for educational purposes.*

## UX Design
---
**This site has been built to cater to two key user groups:**
1. Site Users - These are regular individuals, potential customers and collaborators visiting the site to view and buy products and discover information about the business.
1. Site Administrators - These are site owners, and stakeholders, who's primary focus is to manage content on the site, view, edit, create, and delete products, product categories, orders and other data types. While a dedicated admin site exists to enable full administration behaviour for the site, some key business procedures have been made accessible for site admins through the regular consumer facing site, to improve the user experience for site administrators. 

---
### Strategy    
---
**Site Owner Goals**    
*As a site owner/stakeholder I want to:*
- Increase our online awareness and attract new users to our business.
- Increase revenues via direct ecommerce sales.
- Encourage existing customers to revisit the site to make additional purchases.
- Manage products displayed on the site easily.
- Improve my social media engagement.

**Ideal User**  
*The ideal user:*
- Is someone who owns a smartphone, tablet, computer or similar device.
- Will have an interest in plants and other related products.
- Is located in the same country as the business.
- Is comfortable shopping online. 
- Has payment details saved on their device.
- Is english speaking.
- Likes to receive email updates from business's they are interested in.
- Is active on social media.

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

---
### Scope
---

The initial scope of the project was to build a fully functioning ecommerce site for his imagined business. Site users must have the means to browse and view products, add products to their cart and checkout successfully.

The second core goal for this project was to enable site administrators to have to key functionalities to view, add, edit and delete products and other site content.

For future development phases of this project, the main focus will be to add additional functionality for returning users and creating an admin panel where site admins can update site information in bulk and manage received order fulfillment.

#### Features to be added: 

1. While the project has been built to handle product quantities and inventory control, at present the application has not been set up to update the product quantity in the database once a successful order has been placed. While great care has been taken to ensure products are not over sold up until checkout, I chose not to reduce the quantity of an item in the database after checkout has completed. My rational was that while this is still a educational project people can test the site without everything becoming sold out.

1. Improved frontend form validation to be added. I'd like to add dynamic helper texts and error messages on all site forms to provide a better user experience when things go wrong. Unfortunately it was not possible to roll these features out due to the time limits for this project.

1. Add a blog section with basic text editing functionality for the main post text area.

1. Complete about page to build user trust and provide greater site context.

1. Add all social media CRUD functionality to single admin panel. 

1. Add all product, category, collection CRUD functionality to a dedicated products admin panel.

1. Add order fulfilment updates: "Your item is on it's way" email etc...


---
### Structure
---

The structure of the current project is as follows. 

The project is cnmposed of the following applications. Each application is designed to sepparate concerns of specific functionality.

**Apps:**
- Index - Handles rendering of homepage.
- Products - Handles products and associated models.
- Cart - Handles aggregation of products prior to order completion.
- Checkout - Handles taking payment and creation of order models.
- Contact - Handles user email contact to store owner.
- Profile - Handles storage of individual user's order history and site preferences.
- Social - Handles add, edit, read and delete of store's social media accounts.
- In addition: Django-allauth is used to provide standard user account functionality such as login, logout, register, confirm email, forgot password etc....

**Pages**

* [Index Page](https://hygge-houseplants.herokuapp.com/) - This is the primary landing page

* [Products Page](https://hygge-houseplants.herokuapp.com/products/) - View of all products with search options to narrow donw search.

* [Single Product Page](https://hygge-houseplants.herokuapp.com/products/product/4/) - A detailed view of a single product with an add to cart form and Edit and delete links for super users.

* [Add Product page](https://hygge-houseplants.herokuapp.com/products/add/) - This is an admin only page which contains a form where a new product can be added. There are two outcomes for this page:
    1. If the product has no variants, the product is created and the creator is directed to the detailed product page on completion.
    1. If the wproduct has variants, the user is taken to the add variants page on completion.

* [Add Variant page](https://hygge-houseplants.herokuapp.com/products/add_variants/4/) - On this page a site admin can create, edit or delete product variants. On completion of this page, the user is brought to the single product view of the base product.

* [Add collection page](https://hygge-houseplants.herokuapp.com/products/collections/add/) - This allows site admins to create a product collection. This is so products can be grouped together for promotions or other reasons. (eg. Staff favourites, Sale etc...) Unfortunately due to time limit it was not within the scope of this project to display product collections once created.

* [Cart Page](https://hygge-houseplants.herokuapp.com/cart/) - This page displays the items that a user has added to their cart. There are two options:
    1. A user can proceed to checkout using the checkout button.
    1. A user can return back to products page using the alternate button.

* [Checkout page](https://hygge-houseplants.herokuapp.com/checkout/) - This page has two sections, a order summary section and a checkout area which enables the user to enter their details, pay and complete their order.

* [Checkout success page](https://hygge-houseplants.herokuapp.com/checkout/success/%23HHB9836C/) - On successful checkout a user is brought to a success page which displays a concise summary of their order.

* [Contact Page](https://hygge-houseplants.herokuapp.com/contact/) - The contact form is a generic contact form which enables users to send a message to the business. On successful completion a success message is displayed and the email is sent to the site admin's elected email address.

* [Social page](https://hygge-houseplants.herokuapp.com/social/) - This allows site admins to edit all social media ccounts displayed in the footer.

* [Social/add](https://hygge-houseplants.herokuapp.com/social/add/) - This allows a site admin to add a new social profile from the options that have been stored in the database.

* [Social/add_icon](https://hygge-houseplants.herokuapp.com/social/add_icon/) - This allows a user to add a new icon and name to the available dropdowns.

* [Account page](https://hygge-houseplants.herokuapp.com/profiles/) - This allows users to store their account details and to view their previous orders.

* [Sign In Page](https://hygge-houseplants.herokuapp.com/accounts/login/) - This allows users with existing accounts to login and access their account.

* [Sign Out Page ](https://hygge-houseplants.herokuapp.com/accounts/logout/) - This allows logged in users to logout of their account.

* [Signup Page](https://hygge-houseplants.herokuapp.com/accounts/signup/) - This allows new users to create an account.


---
### Skeleton
---

**Navigation**
Main Navigation:
The primary navigation menu for this site is located in the header of the site on all pages. Hover and touch effects are used to indicate that navigation links are clickable and bright colors are chosen to ensure navigation links stand out from the surrounding background. Links to each important site page are included in the main navigation menu. On smaller devices the main navigation menu collapses and is denoted using the standard 'burger stack' toggler icon.

**Login Section:**
The login section appears in the top right hand corner of the site header. The login area provides quick access to sign in, sign up and sign out site areas. When logged in a link to the user account can be found in this submenu. This is intended to encourage users to sign in to unlock additional site content and functionality and provides immediate feedback that the site is dynamic and can be interacted with by the user.

**Footer Navigation:**
Links to imortant site pages and sections are mirrored in the site footer. This consistent footer navigation menu is displayed on all site pages to encourage users to explore additional pages once they have scrolled ot the bottom and read all content on the current page.

The footer also includes links to the businesses social media accounts to encourage further off-site interactions by users and to improve the business' credibility. As this is a fake business imagined for demonstration purposes, the social media links currently direct to the relevant social media home pages. To encourage user retention all links to external sites will open in a new tab/window.

**Images as links:** Images are used as links to improve navigation primarily on touch devices. This is utilised on the product category tiles on the homepage as well as the image cards on the products page.

**Buttons as Links:**
Buttons and pseudo buttons are used throughout the site to boldly demonstrate a clickable site element. Clear labels and icons are used to indicate a buttons purpose or intended destination to improve first time learning and site useability. On the homepage buttons are used to bring users to the all products page. When used on forms, buttons are used for submission of information but redirects are also utilised upon form submission to transport the user to the page where the result of their input is displayed. This is to provide clear feedback to a user with the result of their input and to encourage ongoing interaction from users once one interaction has been completed.

---
### Surface
---

#### Fonts
1.  --hygge:  ['Karla', sans-serif](https://fonts.google.com/specimen/Karla?query=karla) -> This is the Logo font.
1.  --main: ['Source Sans Pro', sans-serif](https://fonts.google.com/specimen/Source+Sans+Pro?query=source+sa) -> This font is used for the body text, larger passages of text and with heavier font weight it is also used for form labels and lesser headings.
1.  --head: ['Staatliches', cursive;](https://fonts.google.com/specimen/Staatliches?query=staa) - This is used as the main Headin font. It's uppercase font style and bold font-weight is bold and striking and draws attention to key section headinds, alerts and other sections of informations that site users need to be made aware of.

#### Colors
A predominently green color palette was chosen for this project to allude to the site's main content (Plants). Three shades of green (light, mid, dark) are the basis of the color palette. 
These are offset with bright orange accent color used for buttons, links and other interactive elements. Bootstraps default green (success) and red (danger) color's are utilised in "yes"/"no", "do"/"don't" scenarios, where users are given multiple decisions or when feedback to a user input with a positive or negative connotation is provided. In such instances the traffic light (green means go, red means stop) metaphor is chosen rather than adhering to the color scheme in order to provide a better user experience and improved first-time-learning. 

```
--grn: #33775d;
--grn-dark: #004b33;
--grn-light: #62a68a;

--orange: #ee9b00;
--sand: #cebfa8;
```

Throughout the site different shades of grey as well as white and black are used to outline form and container backgrounds and to provide appropriate contrast for sections of text in order to ensure ease of readability.

**Images**

Images have been used throughout the project to provide site context and to be visually appealing. As product images are not required to be dimensioned before upload care has been taken to ensure that images are scaled evenly across the site to provide a consistent and proffesional look and feel. Ideally in a real commercial application all product images would be studio shots with a plain white background. Unfortunately due to image useasge rights this was not possible for this project.

**Icons**

Icons have been used throughout this project as metaphors to reinforce heading and button meaning. All icons utilised for this project were sourced from [fontawesome.com](https://fontawesome.com/)


---
## Mockups
---

[![responsive project preview](media/responsive.png)](https://hygge-houseplants.herokuapp.com/)

---
## Database Structure
---

For the project I have created 9 individual models. These models are demonstrated in the image below. Going forward there is scope to split these models down further. For instance the Product and Variant models could reference an Image model or the Variant model could be linked to a Size model and a Color model etc... Such refinements will be considered for future development of this project.

![schema diagram](media/database_schema.png)
[link to graph here](https://drawsql.app/pedaltherapy/diagrams/hygge-houseplants)

---
### Technologies Used:
---
#### Languages 
* [Html5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
* [jQuery](https://en.wikipedia.org/wiki/JQuery)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

#### Libraries & Frameworks 
* [Bootstrap](https://getbootstrap.com/) - Used for quick protoyping of front end styles.
* [Django](https://www.djangoproject.com/) - Used for authentication, routing, serving dynamic html templates and interacting with the database.

#### Other 
* [Fontawesome](https://fontawesome.com/) - Used to add icons throughout the project.
* [Google Fonts](https://fonts.google.com/) - Used to enable the use of additional fonts for the project.
* [Heroku](https://www.heroku.com) - For app hosting and deployment.
* [Stripe](https://stripe.com/ie) - To enable customer payments for the project.
* [Amazon AWS S3](https://aws.amazon.com/s3/?nc2=h_ql_prod_st_s3) - Used to host images, files and other documents.
* [Postgress](https://www.postgresql.org/) - Used to store site data.

---
## Credits
---
### Image Credits

* [Index.html Hero Image](https://unsplash.com/photos/yb3hsmz4utg)
credit Chris Lee from [Unsplash](https://unsplash.com/)

* [Plant Category Tile Image](https://unsplash.com/photos/FV_PxCqgtwc)
credit Igor Son from [Unsplash](https://unsplash.com/)

* [Succulent Category Tile Image](https://unsplash.com/photos/tcgMBsW4zlU)
credit Kari Shea from [Unsplash](https://unsplash.com/)

* [Cactus Category Tile Image](https://unsplash.com/photos/wDhLrN9FAAM)
credit Stephanie Harvey from [Unsplash](https://unsplash.com/)

* [Accessories Category Tile Image](https://unsplash.com/photos/NLcLjLNUJbY)
credit Tom Crew from [Unsplash](https://unsplash.com/)

* [Hygge Plaque image](https://unsplash.com/photos/SDxDQXixgfU)
credit Julian Hochgesang from [Unsplash](https://unsplash.com/)

* [String of hearts product image](https://unsplash.com/photos/phQil0MqwDI)
credit Severin Candrian from [Unsplash](https://unsplash.com/)

* [String of hearts product image 2](https://unsplash.com/photos/xGpYDi-0348)
credit Severin Candrian from [Unsplash](https://unsplash.com/)

* [Rattlesnake Plant](https://unsplash.com/photos/8nONCr6eTeg)
credit Severin Candrian from [Unsplash](https://unsplash.com/)

* [Aloe Tiki Zilla](https://unsplash.com/photos/eeOOH0dk3XQ)
credit Severin Candrian from [Unsplash](https://unsplash.com/)

* [Scindapsus picuts plant](https://unsplash.com/photos/dTLeHGu9FAw)
credit Severin Candrian from [Unsplash](https://unsplash.com/)

* [Ficus Lyrata ](https://unsplash.com/photos/TNTZ9XRisjQ)
credit Severin Candrian from [Unsplash](https://unsplash.com/)

* [Ficus Robusta ](https://unsplash.com/photos/17UXXzGF7RA)
credit Severin Candrian from [Unsplash](https://unsplash.com/)

* [Ficus Robusta Alt](https://unsplash.com/photos/OtO7x_yL9qM)
credit Severin Candrian from [Unsplash](https://unsplash.com/)

* [Yellow watering can](https://unsplash.com/photos/k3jEtUmKhJo)
credit Severin Candrian from [Unsplash](https://unsplash.com/)

* [White hanging plant pot](https://unsplash.com/photos/k3jEtUmKhJo)
credit Severin Candrian from [Unsplash](https://unsplash.com/)

* [Monstera deliciosa variegata](https://unsplash.com/photos/zTAcTi7D5i8)
credit Severin Candrian from [Unsplash](https://unsplash.com/)

* [echevaria parvus](https://unsplash.com/photos/WwWkgOMU8H8)
credit Scot webb from [Unsplash](https://unsplash.com/)

* [small cactus with pink flower](https://unsplash.com/photos/cNL-fTAQggM)
credit Stephanie Harvey from [Unsplash](https://unsplash.com/)

* [small cactus with pink flowerB](https://unsplash.com/photos/slSRjvoiIpY)
credit Stephanie Harvey from [Unsplash](https://unsplash.com/)

* [small fat cactus](https://unsplash.com/photos/N9lmtlOuaDM)
credit Stephanie Harvey from [Unsplash](https://unsplash.com/)

* [small cactus in cup](https://unsplash.com/photos/f7PfM2NklZ4)
credit Stephanie Harvey from [Unsplash](https://unsplash.com/)

* [small cactus in jug](https://unsplash.com/photos/BsxQ60PxRNI)
credit Stephanie Harvey from [Unsplash](https://unsplash.com/)

* [small Blue cactus](https://unsplash.com/photos/fbAnIjhrOL4)
credit annie Spratt from [Unsplash](https://unsplash.com/)

* [Mother in laws tongue](https://unsplash.com/photos/GY6ViMxtmDE)
credit Nikita Kachanovsky from [Unsplash](https://unsplash.com/)

* [small green cactus](https://unsplash.com/photos/ywRYbp-6p8c)
credit Lina Silivanova from [Unsplash](https://unsplash.com/)

* [Prickly Pear](https://unsplash.com/photos/0nMs98PjafM)
credit Jake Goossen from [Unsplash](https://unsplash.com/)

* [Panda Plant](https://unsplash.com/photos/3_cyj5YkhTs)
credit Kari Shea from [Unsplash](https://unsplash.com/)

* [Jade Plant](https://unsplash.com/photos/Q0w0LGkHokE)
credit Susan Wilkinson from [Unsplash](https://unsplash.com/)


* [small cactus a](https://unsplash.com/photos/nQOfU7Xjbl4)
credit Kamil Kalkan from [Unsplash](https://unsplash.com/)

* [Ultra model watering can](https://unsplash.com/photos/X8X5l0BDPk0)
credit Kara Eads from [Unsplash](https://unsplash.com/)


### Product Description Credits:
The product descriptions used were inspired by descriptons of plants. These have been credited accordingly:

* [Rattlsnake plant hortology.co.uk](https://hortology.co.uk/products/calathea-lancifolia-rattlesnake-house-plant)

* [Ficus Lyrata](https://hortology.co.uk/products/ficus-lyrata-fiddle-leaf-fig-house-plant)

* [Aloe tiki zilla Tikeplant.com](https://tikiplant.com/?lang=en)

* [Ficus Robusta plantlife.ie](https://plantlife.ie/product/ficus-elastica-robusta-rubber-plant-in-21cm-pot/)

* [Echevaria Parva surrealsucculents.co.uk](https://surrealsucculents.co.uk/product/echeveria-parva/)

* [mother in laws tongue houseplantsexpert.com](https://www.houseplantsexpert.com/mother-in-laws-tongue.html)

* [Cactus. Cleistocactus gardens4u.ie](https://www.gardens4you.ie/cactus-cleistocactus-ie-en.html)

* [Prickly Pear wikipedia](https://en.wikipedia.org/wiki/Opuntia)

*[Kalanchoe tomentosa wikipedia](https://en.wikipedia.org/wiki/Kalanchoe_tomentosa)


---
### Code Credits

This section outlines any code that was sourced from an external resource, Many of the code snippets and techniques mentioned outline bug fixes. For brevity I have not included these in the bugs section of the Testing.md file to avoid repeating myself.

* Contact form Tutorial - To add a contact form functionality to the project, I used a guide from this
[learndjango.com tutorial](https://learndjango.com/tutorials/django-email-contact-form)

* Custom image upload button and styles were utilised as shown in the Code institutue boutique ado code along project   
[Widgets.py](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/master/products/widgets.py)   
[Template used](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/master/products/templates/products/custom_widget_templates/custom_clearable_file_input.html)   
[The CSS below was sourced from this link](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/master/static/css/base.css)  

    ```
    .btn-file {  
    position: relative; 
    overflow: hidden;   
    }

    .btn-file input[type="file"] {
        position: absolute; 
        top: 0; 
        right: 0;   
        min-width: 100%;    
        min-height: 100%;   
        opacity: 0; 
        cursor: pointer;    
    }   

    .custom-checkbox .custom-control-label::before {    
        border-radius: 0;   
        border-color: #dc3545;  
    }   

    .custom-checkbox .custom-control-input:checked~.custom-control-label::before {  
        background-color: #dc3545;  
        border-color: #dc3545;  
        border-radius: 0;   
    }
    ```

* jQuery UI slideToggle easing easeOutBounce - to create a more engaging user experience for the index page Hygge section, jQuery's .slideToggle() method was used.
  I was made aware of the additional slideToggle easing effects at [this stackOverflow post](https://stackoverflow.com/questions/6121255/toggle-div-with-easing) from contributor Sylvain.

* Add image preview when image is added to add product form - to provide user feedback when an image is uploaded, I used a custom javascript script to render a small thumbnail image preview of the uploaded image. The core functionality of this script was inspired from [this stack overflow post](https://stackoverflow.com/questions/22245100/how-to-display-an-image-from-a-file-input) from Nephelococcygia.

    ```
    function myFunction() {
        var file = document.getElementById('file').files[0];
        var reader  = new FileReader();
        // it's onload event and you forgot (parameters)
        reader.onload = function(e)  {
            var image = document.createElement("img");
            // the result image data
            image.src = e.target.result;
            document.body.appendChild(image);
        }
        // you have to declare the file loading
        reader.readAsDataURL(file);
    }
    ```

* To load existing product variants I used the queryset arguement [as outlined in the Django documentation](https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#changing-the-queryset)

* To disable the product form when editing product variants I used the technique of wrapping the form fields in a fieldset and assigning that fieldset with the ```disabled="disabled"```
attribute. This techniques was found in [this stackoverflow post](https://stackoverflow.com/questions/3507958/how-can-i-make-an-entire-html-form-readonly)

* Center text in ```<input type="number">``` I used information found in [stackoverflow post](https://stackoverflow.com/questions/23715881/center-text-in-html-number-input) to control the appearance of
the default number input adjust buttons and to center the text.

    ```
    input[type='number']::-webkit-inner-spin-button, 
    input[type='number']::-webkit-outer-spin-button { 
        -webkit-appearance: none;
        margin: 0;
    }
    ```

* To enable a 'not-allowed' cursor on a disabled button I used ``` cursor-events: all !important ``` to override a bootstrap error preventing this desired behaviour. I was made aware of this fix from [this stackoverflow post](https://stackoverflow.com/questions/50349017/how-can-i-change-cursor-for-disabled-button-or-a-in-bootstrap-4)


* To prevent form submission on enter I recycled some code that I used in my MS3 project:
    ```
    $(document).ready(function() {
        $(window).keydown(function(event){
            if(event.keyCode == 13) {
                event.preventDefault();
                return false;
            }
        });
    });
    ```
    This code was originally sourced from [this stackoverflow post](https://stackoverflow.com/questions/895171/prevent-users-from-submitting-a-form-by-hitting-enter).

* To add padding to the default select menu caret I hid the default caret and displayed an svg image instead. This method was described by 'kilinkis' in [this stackoverflow post](https://stackoverflow.com/questions/62576942/css-webkit-appearance-menulist-dropdown-select-tag-how-to-give-padding-to) and was edited to position the caret further towards the center of the select field. The caret Icon SVG was sourced from [fontawesome.com](https://fontawesome.com/v5.15/icons/caret-down?style=solid) | [license for use here.](https://fontawesome.com/license/free)

    ```
    select {
      appearance: none;
      background-color: transparent;
      background-image: url(arrow.svg);
      background-repeat: no-repeat;
      background-position: right;
      background-size: 30px;
    }
    ```
* To render each collection product as an individual option, each product was rendered as a checkbox to provide a better user experience thant the default django multi-choice dropdown field. To enable this functionality 'forms.CheckboxSelectMultiple' was used. This technique was learned from [this medium.com blog post](https://medium.com/swlh/django-forms-for-many-to-many-fields-d977dec4b024). The code snippet used can be seen below:

    ```  
    members = forms.ModelMultipleChoiceField(
        queryset=Member.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    ```

* To create a more user friendly order number I used ```.hex[:6]``` when creating the uuid to limit it to 6 charachters. I then added a prefix to make order numbers more consistent. 
I discovered the ability to limit UUID in [this stack overflow post](https://stackoverflow.com/questions/26030811/generate-a-unique-string-in-python-django/26032898)

* To prevent validation errors when submitting images with blank src values on the single product page I entered ```data:,``` as a temporary img src value. The images are dynamically changed using javascript so this is only necessary to prevent validation errors. The solution for this was found [in this post](https://stackoverflow.com/questions/5775469/whats-the-valid-way-to-include-an-image-with-no-src).


* I would also like to credit Anouk Smet, [who's README was a great example of the deployment procedures](https://github.com/AnoukSmet/Casa-Pedra-Nobre)

---
## Testing
---
The testing procedures for this project have been documented sepparately in this [testing file](https://github.com/nickassafkirk/hygge_houseplants/blob/main/testing.md)

---
## Deployment 
---

### Cloning Project and deployiong the project locally 

To replicate this project in your own local environment, the following steps should be followed:
 1. Go to the [project repository on Github](https://github.com/nickassafkirk/hygge_houseplants)

 I personally used Gitpod, so the steps needed to clone this project to your own IDE may differ slightly.

 1. ![deployment step 1](/media/deploys1.png) Within the code section if using the Gitpod IDE, first install [Gitpod's browser extension](https://www.gitpod.io/docs/browser-extension/), then with the extension installed click the green gitpod button to create a clone of this project in your own Gitpod IDE. 
 
 1. If using the a different development environment this project can be cloned to your local machine using HTTPS or SSH - Detailed instructions on how to do this can be found in [Github's documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)

 1. With the project repositiory cloned to your machine you will then need to create and env.py file in your root directory. If it is not already there you must then create a .gitignore file and add your env.py file to it.

 1. In your env.py file first ```import os``` you will create your environmental variables using the statement ```os.environ['VARIABLE_NAME'] = 'variable_value'```

    For this project the following env variables should be created.
    * 'DEVELOPMENT' = True
    * 'SECRET_KEY' - Your Django secret key token: To create a secret key [this secret key generator can be used](https://miniwebtool.com/django-secret-key-generator/)
    * 'DEFAULT_FROM_EMAIL' - The default from email used for emails sent from the application
    * 'EMAIL_HOST_PASS' - Your email application password
    * 'EMAIL_HOST_USER' - your host email address.
    * 'STRIPE_PUBLIC_KEY' - stripe public key
    * 'STRIPE_SECRET_KEY' - stripe secret key
    * 'STRIPE_WH_SECRET' -  stripe webhook secret

    *more information about stripe payments can be found [here](https://stripe.com/docs/payments)*

    
1. With the Environmental variables defined we now need to install the packages needed to run the project. These can be found in the requirements.txt file in the root directory. We can install each dependency individually by using the ```pip3 install <package_name>``` command in the terminal or by running: ```pip3 install -r requirements.txt```

1. With everything installed you need to make migrations. 
first run: ```python3 manage.py makemigrations```
then: ```python3 manage.py migrate``` if no errors are returned.

1. Create an admin superuser using the command:
   ```python3 manage.py createsuperuser`` in the terminal and following the prompts.

1. With migrations made you can run the project on your local server. 
    ```python3 manage.py runserver```
    The project is now deployed on your local machine.
    
---
### Deploying the project to heroku 

1. Were now ready to create our app in Heroku. To do so go to [heroku.com](https://www.heroku.com) and create an account or login by following the prompts.

    Next, in your account panel click the 'new' dropdown button in the top right corner. From the options select the 'Create new app' option. This will bring you to the following page.

    ![heroku create app](media/herokusgrab1.png)

    Here you can select a name for you application and select your nearest geographical region. In my case Europe.

1. You will no be brought to the main panel for your new app. In the resources tab search for postgres in the add-ons search box. Select Heroku Postgres. YOu can select the Hobby Dev option tier. 

    ![heroku resource add ons](/media/herokusgrab2.png)

1. Once we've added the Heroku Postgres Add-on we can go to the settings tab in the panel. Next click 'reveal config vars'. After adding the Heroku Postgres add-on your DATABASE_URL variable should have been automatically created in heroku. 
You can now create the Environmental variables you have already included in your env.py file in the config vars section in heroku. Don't include DEVELOPMENT = True in heroku and ensure that you add USE_AWS.
    ```
    AWS_ACCESS_KEY_ID = "AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY = "AWS_SECRET_ACCESS_KEY"
    AWS_S3_REGION_NAME = "AWS_S3_REGION_NAME"
    AWS_STORAGE_BUCKET_NAME = "AWS_STORAGE_BUCKET_NAME"
    USE_AWS = True

    DATABASE_URL = "This variable is automatically created in heroku once postgress has been installed"

    SECRET_KEY = "SECRET_KEY"

    STRIPE_PUBLIC_KEY = "STRIPE_PUBLIC_KEY"
    STRIPE_SECRET_KEY = "STRIPE_SECRET_KEY"
    STRIPE_WH_SECRET = "STRIPE_WH_SECRET"
    STRIPE_CURRENCY = EUR

    DEFAULT_FROM_EMAIL = "DEFAULT_FROM_EMAIL"
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_PASS = "EMAIL_HOST_PASS"
    EMAIL_HOST_USER = "EMAIL_HOST_USER"
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    ```

1. We then need to connect to the postgres DB in the settings.py file in our base app so we can make migrations. We can do this by commenting out the following code in the settings.py file and by temporarily adding the DATABASE_URL variable and value to the envy.py file in our root folder.

    ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```
    You can then run the ```python3 manage.py makemigrations``` command, followed by ```python3 manage.py migrate``` if no errors are returned.

1. You can now create a superuser for your Postgres DB by using the command ```python3 manage.py create superuser``` in the terminal and following the prompts to add a username, email and password. Once this is created and your app is deployed this will enable you to sign into the /admin panel for your deployed project.

1. Alternatively you can run these commands directly in the inbuilt console in heroku.

1. You can then uncomment the code above and delete the 'DATABASE_URL' variable from the env.py file which will ensure that the postgress DB is used on the deployed herokuapp and the default SQLlite DB is used during development.

1. Ensure the Procfile is present in your workspace, this will tell heroku what type of application to expect.

1. Next we need to Configure AWS S3: first go to [Amazon AWS](https://aws.amazon.com/) and sign in or sign up by following the prompts. You will need to provide credit card details to successfully create an account but it is unlikely that you will incur any charges. You can read Amazon's terms and conditions for further information on Billing, Privacy and more. 

1. Once you've created and verified your account, navigate to AWS S3 using the search bar or services menu at the top of the page. Next click create bucket.
Assign your bucket name and pick your closest region. You can then scroll past all other options and click save. 

1. In the menu within your newly created bucket, click the properties tab. Then scroll to the static website hosting section and click edit. Here click the host website checkbox and enter index.html and error.html in the suggested fields. After that click save. While the two specified pages are irrelevant, this will create a URL that we can use to access our static and media files.

1. Next in the permissions tab in the bucket panel, go to the CORS section, click edit and paste in the following code: 
    ```
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ```

1.  In the permission again, in the "Block public access (bucket settings)" section click edit and unblock all the options and click save changes. You may be required to confirm your decision by typing confirm.

1. In the permissions tab go to edit permissions, first copy (ctrl/cmd + c) the 'Bucket ARN' and then click the policy generator tab. In the policy generator select policy type of 'S3 Bucket Policy', effect can be left as the default allow, in the principal we can use the * symbol. In the action dropdown menu select 'Get Object' and then in the ARN field paste the ARN value you copied from the previous page. Next click 'add statement' and finally the 'add policy' button. The completed policy will then be revealed. Copy this completed policy and paste it into the policy field on the edit policy page. Finally within the pasted policy add /* to the end of the resource key to enable access to all resources in the bucket.

1. Finally in the Permissions section again, navigate to the access control list section. In the public access section, click edit and then beside the 'Everyone (public access)' subheading click the 'list' checkbox and click save.

1. Next configure IAM. In the AWS services menu Search for IAM. Once in IAM, in the dashboard on the left hand side click the user groups tab. Click the create user group button and and give your new group a name in the relevant field. Skip the next page sections and click the button to create your user group. 

1. On dashboard on the left hand side you now click the 'policies tab. Now click the blue create policy button. This will open a popup. Click the JSON tab and then the link in the top right corner of the popup that says 'Import managed policy'. Using the search bar select the 'Amazon S3 full access' option and click import. This will load some Json into a textfield. We're going to change the value of the 'resource' key to a list. the first list item will be the S3 Bucket ARN that we used when configuring our s3 bucket, the second list item will be the S3 Bucket ARN followed by '/*'

    eg: 
    ``` 
        'resource': [
            'enter the s3 arn here',
            'enter the s3 arn here/*',
        ]
        
    ```
    now click the 'next tags' button, and after that skip the tag options and click the 'next review' button. On the review page you can give the policy a name and a description and click create policy. This will bring you back to the policies page where you should now see your new policy listed.

1. Now in the dashboard on the left click into the user groups section. Access the group you created in step 22. In the permissions tab, click the 'add permissions menu in the right hand corner of the permissions panel. The click the 'attach policies' link. From the list of available policies find the policy we just created adn then click the attach permissions button to attach it to our user group. 

1. We now need to create a user. In the left hand panel click 'users', then click the 'create users' button. Add a user name in the relevant field eg projectname-staticfiles-user. Select the 'programmatic access' checkbox and then click the 'next permissions' button. we'll be taken to a page where our different user groups are listed. Selected the user group that we created in the provious steps and then click 'next; tags'. We can skip the add tags section and click the 'review' button. Finally having reviewed the user we just created we can click the create user button. 

1. You will land on a success page where your user, user_access_key_id and user_secret_key are listed. Download the user security details using the download csv button and save the file somewhere secure. It's important to download the file as you wont be able to access them again.

1. You now need to connect your Django app to our S3 Bucket. In settings.py, first ensure that 'storages' is added to you our list of installed apps. Then ensure the following code is included in the settings.py file under the static/media comment/ 
    ```
    if 'USE_AWS' in os.environ:
        AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
        AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```

1. In heroku under the settings section reveal your config vars and use the values from S3 Bucket and the CSV file that you downloaded at step 26 to add the config variables to your heroku app. You will also need to Add the following variables which we previously listed.

    AWS_STORAGE_BUCKET_NAME -> The name of your S3 Bucket you created for this project
    AWS_S3_REGION_NAME -> The region for your S3 Bucket eg 'eu-west-1'
    AWS_ACCESS_KEY_ID -> The AWS access key ID from the CSV file you downloaded
    AWS_SECRET_ACCESS_KEY -> The AWS secret access key from the CSV file you downloaded
    USE_AWS -> True

1. Download the media files from the github repository and manually upload them into a folder called media in your s3 bucket. This will ensure images will work when you connect to AWS

1. Finally we need to set up our email confimration forwarding. To do so in Gmail follow these steps. For othe Email services, the steps may differ.

1. Go to your email account and go to your account settings
1. In the security settings ensure two step authentication is enabled in teh sign in section. 
1. Below this there should be an app passwords section once 2 step verification is enabled. 
1. In app passwords create a new app password for the first drop down select "mail" and for the device type choose "other" and give it a descriptive name (such as the name of your project). 
1. Once this is completed you can copy the password that is displayed into your config varibales in heroku for the EMAIL_HOST_PASS variable.

1. In settings.py ensure the following code is present 
    ```
    if "DEVELOPMENT" in os.environ:
            EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
            DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
        else:
            EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            EMAIL_USE_TLS = True
            EMAIL_PORT = 587
            EMAIL_HOST = 'smtp.gmail.com'
            EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
            EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
            DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
    ```
1. Your now ready to deploy your project. In heroku, go to deployment. Select deploy with github, then use the search bar to find the repository you're connection too. Be sure commit and push your changes to github before this step. with that done and your github repo connected to heroku you can go to the deploy button and deloy your main branch. Once you've completed this step you'll see an activity pane updating on the app build progress. Once your app is buit a link to your deployed app will be provided.

---
## Acknowledgements
---

I would like to thank my Tutor Nishant Kumar for his help and support throughout this project and throughout my previous projects over the last year. 

I would also like to thank the Tutors at the code institute for the their help and support. Special thanks to Simen for his advice during our Saturday morning standup. 

I'd also like to thank my friends and family who assisted with testing and feedback for this project.


