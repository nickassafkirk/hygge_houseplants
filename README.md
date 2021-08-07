
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

---
### Code
---

#### Bugs Fixed:
* Variant delete functionality not operating as anticipated. When creating the delete variant functionality [djangos in built can_delete method](https://docs.djangoproject.com/en/3.2/topics/forms/formsets/#can_delete) was used. When the form was submitted, products were not being deleted. Using print statements it was determined that while the variant was being deleted, it was then subsequently being recreated with the same id when, the save() method was called on each form in the formset. To fix this bug the variant delete functionality was called after the form was saved to ensure that the variant is not recreated. 