
---
### Technologies Used:
---
#### Languages 
* Html5
* CSS3
* Javascript
* jQuery
* Python

#### Libraries & Frameworks 
* Bootstrap
* Django - Used for authentication, routing, serving dynamic html templates and interacting with the database.

#### Other 
* Fontawesome - Used to add icons throughout the project.
* Google Fonts - Used to enable the use of additional fonts for the project.
* Balsamiq - Used to create Wireframes for the purpose of mocking up the project.
* Heroku - For app hosting and deployment.
* Stripe - To enable customer payments for the project.
* Amazon AWS S3 - Used to host images, files and other documents.
* Postgress - Used to store site data.

---
### Credits
---
#### Image Credits

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

#### Code Credits

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

---
### Code
---

#### Bugs Fixed:
* Variant delete functionality not operating as anticipated. When creating the delete variant functionality [djangos in built can_delete method](https://docs.djangoproject.com/en/3.2/topics/forms/formsets/#can_delete) was used. When the form was submitted, products were not being deleted. Using print statements it was determined that while the variant was being deleted, it was then subsequently being recreated with the same id when, the save() method was called on each form in the formset. To fix this bug the variant delete functionality was called after the form was saved to ensure that the variant is not recreated. 

* When trying to remove Products with variants from the cart. The variant id attribute is extracted from a unique item_id, this variant id is the key for each variant object in the cart session variable. 

eg. ```
    {product_id: {'product_variants': {variant_id: item_quantity}}}
    ```

When taking trying this initially I was experiencing an issue where the product variant was not being removed from the cart. To debug this I checked if the variant_id was a string, it returned True each time. I then checked if the variant was None with a if statement and I added a secondary print statement to check the value of the variant_id variable again. I found that it was returning as an int, which meant that when I tried to delete the variant object from the cart dictionary it was looking for an index of the dictionary that didn't exist instead of calling a dictionary key. To remedy this I explicitly converted the variant_id variable to a string so that the correct dictionary key is selected when the del keyword is used. 

See code below:

``` try:
        product_id = None
        variant_id = None

        if "-" in item_id:
            product_id = item_id.split('-')[0]
            variant_id = request.POST.get('variant')

            print(isinstance(product_id, str))
            print(isinstance(variant_id, str))
        else:
            product_id = item_id

        cart = request.session.get('cart', {})

        if variant_id:
            print(variant_id)
            print(type(variant_id))
            del cart[product_id]['product_variants'][str(variant_id)]
```

***

### Deployment 


To replicate this project in your own local environment, the following steps should be followed:
 1. Go to the [project repository on Github](https://github.com/nickassafkirk/hygge_houseplants)

 1. ![deployment step 1](/media/deploys1.png) Within the code section if using the Gitpod IDE, first install [Gitpod's browser extension](https://www.gitpod.io/docs/browser-extension/), then with the extension installed click the green gitpod button to create a clone of this project in your own Gitpod IDE. 
 
 1. If using the a different development environment this project can be cloned to your local machine using HTTPS or SSH - Detailed instructions on how to do this can be found in [Github's documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)

 1. With the project repositiory cloned to your machine you will then need to create and env.py file in your root directory. If it is not already there you must then create a .gitignore file and add your env.py file to it.

 1. In your env.py file first ```import os``` you will create your environmental variables using the statement ```os.environ.setdefault('VARIABLE_NAME', 'variable_value')```

    For this project the following env variables should be created.
    * 'SECRET_KEY' - Your Django secret key token: To create a secret key [this secret key generator can be used](https://miniwebtool.com/django-secret-key-generator/)
    * 'DEFAULT_FROM_EMAIL' - The default from email used for emails sent from the application
    * 'DATABASE_URL' - The postgress database URL created when Postgress was installed in your Heroku app
    * 'HEROKU_HOSTNAME' - The URL for your deployed heroku app eg. your_project_name.herokuapp.com
    * 'EMAIL_HOST_PASS'
    * 'EMAIL_HOST_USER'

    The following env variables should be added to the config vars in your Heroku app but can be added to you local env for development purposes. 

    * 'AWS_ACCESS_KEY_ID'
    * 'AWS_S3_REGION_NAME'
    * 'AWS_SECRET_ACCESS_KEY'
    * 'AWS_STORAGE_BUCKET_NAME'
    * 'STRIPE_PUBLIC_KEY'
    * 'STRIPE_SECRET_KEY'
    * 'STRIPE_WH_SECRET'
    * 'USE_AWS' - Set to True
    
1. With the Environmental variables defined we now need to install the packages needed to run the project. These can be found in the requirements.txt file in the root directory. We can install each dependency by using the ```pip3 install <package_name>``` command in the terminal. 
    * pip3 install django
    * pip3 install django-allauth
    * pip3 install django-crispy-forms
    * pip3 install dj-database-url
    * pip3 install gunicorn
    * pip3 install pillow
    * pip3 install psycopg2-binary
    
