# **Testing**

## **Validators**

### **W3 Validor @ https://validator.w3.org/**
------------

To able to succesfully test all the pages for errors I had to change the jinja templating language from the html, for example {% url 'booking' %} had to change it to "#". Otherwise it would throw an error an unrecognized format.

<img width="1331" alt="Screenshot 2022-07-10 at 14 45 13" src="https://user-images.githubusercontent.com/91877102/178143458-0d24e556-7b44-4613-bd56-637e7f8809da.png">

After all the modification have been done, to show a basic html document, I got the following result:
<img width="1368" alt="Screenshot 2022-07-10 at 14 15 22" src="https://user-images.githubusercontent.com/91877102/178142983-396fa569-289a-446e-a8c6-6e367949d51f.png">



### **CSS Validor** @ https://validator.w3.org/

<img width="1388" alt="Screenshot 2022-07-10 at 14 58 57" src="https://user-images.githubusercontent.com/91877102/178143940-cbf97cab-985a-4ec9-88d6-ab4752fd7356.png">

### **PEP8 online** @ http://pep8online.com/
------------

- **forms.py**

<img width="985" alt="Screenshot 2022-07-10 at 15 11 35" src="https://user-images.githubusercontent.com/91877102/178144383-39997c2b-947a-46a1-b559-18f55015bc02.png">

- **admin.py**

<img width="1023" alt="Screenshot 2022-07-10 at 15 04 53" src="https://user-images.githubusercontent.com/91877102/178144147-7d019cb0-59e1-4b81-9810-1364b129abe1.png">

- **models.py**

<img width="978" alt="Screenshot 2022-07-10 at 15 05 59" src="https://user-images.githubusercontent.com/91877102/178144193-4e237d24-ec55-4eea-a915-89e159d3f1b0.png">

- **urls.py**

<img width="979" alt="Screenshot 2022-07-10 at 15 06 56" src="https://user-images.githubusercontent.com/91877102/178144226-9e6948de-f937-4ae3-9982-9e7ba0b7a7f2.png">

- **views.py**

<img width="986" alt="Screenshot 2022-07-10 at 15 07 33" src="https://user-images.githubusercontent.com/91877102/178144253-87106b64-b17f-425d-bb6a-3d3edad73e5f.png">

- **test_forms.py**

<img width="959" alt="Screenshot 2022-07-10 at 15 08 18" src="https://user-images.githubusercontent.com/91877102/178144282-5f9c67b8-b6f7-4ff2-8c98-41d87cd7c701.png">

- **test_models.py**

<img width="1004" alt="Screenshot 2022-07-10 at 15 09 21" src="https://user-images.githubusercontent.com/91877102/178144313-eb40d503-3281-4097-87ea-5942a3c26890.png">

- **test_views.py**

<img width="992" alt="Screenshot 2022-07-10 at 15 10 26" src="https://user-images.githubusercontent.com/91877102/178144346-efc4fd59-9fad-4aa9-a86b-ae39e11c8311.png">



### **JS Validor** @ [https://validator.w3.org/](https://jshint.com/)
------------

No errors:

<img width="988" alt="Screenshot 2022-07-10 at 15 17 48" src="https://user-images.githubusercontent.com/91877102/178144709-26969838-6a25-41e3-b8cc-5375088b799f.png">


### **Lighthouse** @ Google Chrome Dev Tools.
------------
#### **Home page**

<img width="481" alt="Screenshot 2022-07-12 at 22 11 25" src="https://user-images.githubusercontent.com/91877102/178575488-62d7175e-d6cd-4cb4-8529-da543e720a2f.png">

Low score on Best Practice due to the JQuery library mandatory for the DatePicker

<img width="498" alt="Screenshot 2022-07-12 at 22 14 21" src="https://user-images.githubusercontent.com/91877102/178575702-1a73f3b2-c196-4889-9447-6a29d41360f5.png">

#### **Our Restaurant page**

<img width="433" alt="Screenshot 2022-07-12 at 22 29 30" src="https://user-images.githubusercontent.com/91877102/178578252-bc37eb02-924e-4f14-a5e9-8e2ae9128ec8.png">

#### **Reservation page redirected to login page page**

<img width="443" alt="Screenshot 2022-07-12 at 22 31 34" src="https://user-images.githubusercontent.com/91877102/178578506-b0f19282-31a6-41ea-846f-c833a51a3860.png">

#### **Menu page**

