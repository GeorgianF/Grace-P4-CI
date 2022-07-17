# **Grace Restaurant**
The restaurant is a fine dining restaurant located in the heart of Chicago. 
The restaurant overlooks Cloud Gate, one of the most beautiful landmarks in Chicago. 
Located here since 1998, it underwent a full-scale renovation and redesign in the summer of 2017.
It presents to the user the products available and sets an expectation of the dishes that will be served.
It allows the user to make/edit/delete a reservation and also send a form with details of an event, that will be sent to the restaurant admin and it can be afterwards transformed into a reservation.

[Deployed site](https://grace-restaurant-p4-ci.herokuapp.com/)

# **Planning Phase**
## **Site Objectives:**
The restaurant wants to inform the visitors about a sustainable approach on food, with zero waste policy.
It's actively involved in local comunities and has the mission to reduce the carbon footprint.
It's using local source products, and presents them to the customer in a fine dining manner.

## Feasibility study

Grace Restaurant | Importance | Feasibility
---|---|---
User can make reservations | 5 | 5
User can cancel reservations | 5 | 5
User can update reservations | 5 | 5
User profile | 5 | 5
User log in | 5 | 5
Landing page simple and a clear message | 5 | 5
Manually add reservations (admin) | 5 | 5
Event form  | 5 | 5
View menu | 4 | 5 
Know the team | 2 | 3
Testimonials | 2 | 2 
Being able to download wine and cocktail lists | 2 | 1 
----------------------------------------|----|----
Totals | 50 | 51

## **Structure**   
The structure of the website is simple, easy to follow for every user, from the nav bar or from the footer.
When developing the website, I have put myself in the shoes of the visitor, and organized the page, so it can be easy to reach.

### **User Stories:**  

* As a **User** I can ...
  * ... **click on the nav bar** so that I can **easily navigate to the page of interest**
  * ... **I can click on the wine list** so that I can **view and download it**
  * ... **I can click on the cocktail list** so that I can **view and download it**
  * ... **I can click on the social link** so that I can **visit the restaurant social pages**
  * ... **I can view reviews/testimonials** so that **I can read them**

* As a **User** I can't ...
  * ... **submit and empty field in form** so that I can **validate the event**

* As a **Unregistered User** I can ...
  * ... **register an account** so that I can **login and view/update/delete my bookings**
  * ... **send a form** so that I can **send information with events to the restaurant**

* As a **Registered User** I can ...
  * ... **view booking** so that I can **update them with new information**
  * ... **view bookings** so that I can **cancel them**

* As a **Admin** I can ...
  * ... **view/edit/delete bookings** so that I can **manage them**
  * ... **block registered users capability to double book** so that I can **block him from booking the same date twice**
  * ... **send email on sending form** so that I can **confirm that the email has been received**
  * ... **send email on accepting booking** so that I can **inform user that the reservation request has been approved**
  * ... **send email on cancelation** so that I can **inform the user that the booking has been canceled**
  * ... **filter and search all custom models from the admin page** so that I can **utilize the admin page to review, edit and delete data quickly**
  * ... **add allergens to the dish when I create a course** so that I can **inform the customer about what it contains**
  * ... **I can block the ability of the user to choose a date earlier than tomorrow** so that I can **send corect data to the restaurant**
  * ... **I can add the option to confirm the action** so that I can **be sure that the user is aware of the form**

* As a **developer** I can ...
  * ... **make the website responsive on all devices** so that I can **give the user a better experience**


## **Backbone**

### **Wireframes:
**Landing page:**
------------------
<img width="873" alt="Screenshot 2022-07-06 at 22 06 07" src="https://user-images.githubusercontent.com/91877102/177634548-bd35ada6-50b3-4d8f-8c2e-bc2405f76906.png">

**Gallery page:**
------------------
<img width="737" alt="Screenshot 2022-07-06 at 22 11 27" src="https://user-images.githubusercontent.com/91877102/177634735-700cfc7a-d694-48c9-9643-c9f86a23924c.png">

**Menu page:**
------------------
<img width="895" alt="Screenshot 2022-07-06 at 22 12 24" src="https://user-images.githubusercontent.com/91877102/177634887-3c97b39e-4bf3-40a4-b392-98ef5231b8bb.png">

**Meet the team page:**
------------------
<img width="927" alt="Screenshot 2022-07-06 at 22 13 15" src="https://user-images.githubusercontent.com/91877102/177635014-8855a23d-01ac-4f86-8eb0-15353c6cc7eb.png">

**Events page:**
------------------
<img width="749" alt="Screenshot 2022-07-06 at 22 13 54" src="https://user-images.githubusercontent.com/91877102/177635107-2e1e49b7-3623-4d26-bbae-327597731d17.png">

**Login page:**
------------------
<img width="762" alt="Screenshot 2022-07-06 at 22 14 31" src="https://user-images.githubusercontent.com/91877102/177635186-76f67339-3b15-4fa6-97a5-d6b61acc0546.png">


### Color scheme:

I wanted to keep the color scheme as simple as possible, because within the website a lot of food picturescan be found, that I want to showcase.
The more vibrant colors I did't consider that will add value, and will take away from the objective of the restaurant, that is food.
I have used for reference the website: [coolers.co](https://coolors.co)
In the end I have used the following colors
 - #ffffff (white)
 - #f8f9fa (gray) - footer
 - 000000 (black)
 - #827770 (brown) - nav bar
------------------
![Screenshot 2022-07-06 at 22 21 17](https://user-images.githubusercontent.com/91877102/177636535-a9507e72-f394-4d3b-89be-968fc485e964.png)

### Typography:
I have user only one font Zen Loop (uppercase) because it provided the Art Deco look that I wanted to achieve.

## Agile Development Process
I have use GitHub to keep track of my progress.
All of the user stories have been logged on **Github** here:(https://github.com/GeorgianF/Grace-P4-CI/projects/1)


# **Features**

## **Site Navigation**

### **Navbar**
The menu it's hidden from the view and it can be found by clicking the hamburger menu on the right side of the screen
Once the button is clicked, the menu will appear

<img width="339" alt="Screenshot 2022-07-10 at 10 29 48" src="https://user-images.githubusercontent.com/91877102/178135536-1865c859-9625-43e4-830c-ef711e0cd6c7.png">

The user has full freedom on the page that he wants to visit, and everything is easy to reach.

### **Home page**
The user is greeted with the logo of the restaurant, a motto and the main call to action button, to book table.
<img width="693" alt="Screenshot 2022-07-10 at 10 32 59" src="https://user-images.githubusercontent.com/91877102/178135592-605e4f7d-e5c1-4c0d-998f-b2d11b2d5d49.png">

The footer is hidden under the first view.
<img width="1432" alt="Screenshot 2022-07-10 at 10 36 04" src="https://user-images.githubusercontent.com/91877102/178135684-4d56c9d6-0bb7-4d72-983c-9f763d5614f3.png">

### **Our Restaurant page**
The user will be greeted with a hero image, that contains one of the dishes from the restaurant - to let the user know what to expect after the booking process is complete. This page will provide information on the restaurant and the same call to action button to Book a Table can be found here.

<img width="1424" alt="Screenshot 2022-07-10 at 10 38 10" src="https://user-images.githubusercontent.com/91877102/178135859-853db445-527c-43ad-9364-4c065cf6097b.png">

At the next section of the page, can be found 3 previous clients testiomonials.

<img width="1098" alt="Screenshot 2022-07-10 at 10 41 38" src="https://user-images.githubusercontent.com/91877102/178135863-4e6eef8b-02dc-46c1-b7b3-034a62d7ca95.png">

At the next sections of the page, can be found some general guidelines against the spread of the corona virus:
<img width="1161" alt="Screenshot 2022-07-10 at 10 43 19" src="https://user-images.githubusercontent.com/91877102/178135933-589ab010-5539-4e2f-ac85-af316d55fb05.png">

### **Menu page**
On this page the user can find information about the menu with the 6 options available:
- Starters
- Soups
- Salads
- Fish courses
- Main courses
- Desserts

<img width="1423" alt="Screenshot 2022-07-10 at 10 46 14" src="https://user-images.githubusercontent.com/91877102/178136133-f5d34575-65ca-4061-a1ee-cceb98e69879.png">
<img width="1411" alt="Screenshot 2022-07-10 at 10 46 24" src="https://user-images.githubusercontent.com/91877102/178136140-d9f32aa3-c7bd-4f66-afc3-af232f532cff.png">

Each category is presented as a card, that the user can click an flip it over. The card will show the dishes presente in that category and their prices.
The card flips back automaticaly after 10 seconds.

<img width="476" alt="Screenshot 2022-07-10 at 10 51 16" src="https://user-images.githubusercontent.com/91877102/178136155-744c5572-e2d4-48ba-a4ed-f3cc5db4b8a9.png">

At the bottom of the page, the user can also download a PDF file with the wine and cocktail list. To provide a full experience.

<img width="576" alt="Screenshot 2022-07-10 at 10 46 30" src="https://user-images.githubusercontent.com/91877102/178136190-a8624546-5294-4743-8572-13281ca973af.png">

### **Gallery page**
As the name implies, this a gallery of artistic representation of the dishes that the restaurant has produced in the past.
The images are presented in a grip system, random layout.
Each images has a animation added to it, whenever the user hovers on of the image, it will scale up and the name of the dish will appear from the bottom up, to the middle of the image.

<img width="1400" alt="Screenshot 2022-07-10 at 11 01 14" src="https://user-images.githubusercontent.com/91877102/178136464-0062a2c1-edc3-4e35-8380-02e5443e1287.png">

### **Team page**

On this page, the user can find information on the Executive Chef, on the kitchen team, the Sommelier, an the service team

<img width="506" alt="Screenshot 2022-07-10 at 11 02 23" src="https://user-images.githubusercontent.com/91877102/178136506-0b6a4b0a-b6f0-48bc-b850-1c21cd5b688c.png">


### **FAQ page**

On this page, the can find frequently asked questions and their answer.
It's based on Bootstrap

<img width="1352" alt="Screenshot 2022-07-10 at 11 04 13" src="https://user-images.githubusercontent.com/91877102/178136626-1ce66078-74b9-4fda-bcb1-d2668f6089c2.png">

Whenever the user clicks on one question, the answer will appear underneath and the main question will be highlighted with a blue color.
Also the arrow has a animation, to rotate 180deg.

<img width="1357" alt="Screenshot 2022-07-10 at 11 10 11" src="https://user-images.githubusercontent.com/91877102/178136733-dbd78ce9-8a1b-4441-932e-094da92ec19e.png">

### **Events page**
On this page can submit a form to the restaurant in regard to a event reservation.
The user is not allowed to make a booking if the group is bigger than six, therefore he will have to submit a event request.

The information requested are:
- Email
- First Name
- Last Name
- Phone number
- Event date
- Event details

All fileds are mandatory.

<img width="487" alt="Screenshot 2022-07-10 at 11 10 49" src="https://user-images.githubusercontent.com/91877102/178137135-9cd93261-c742-4866-a37d-7e990fa87f21.png">

Once all the fields are complete with the details, the user is requested to confirm the request via a modal.

<img width="397" alt="Screenshot 2022-07-10 at 11 28 19" src="https://user-images.githubusercontent.com/91877102/178137340-76bdc590-9b93-4f69-823b-bdddfced78f4.png">

Once the event form is confirmed, the user will be notified with a message on the page and the form will reset to the initial blank stage.

<img width="464" alt="Screenshot 2022-07-17 at 11 39 25" src="https://user-images.githubusercontent.com/91877102/179390816-3b66ef26-5150-49d4-b3be-26a195f1a427.png">


### **Login page**

On this page the user can authentificate of sign-up with a new account

<img width="382" alt="Screenshot 2022-07-10 at 11 30 40" src="https://user-images.githubusercontent.com/91877102/178137447-28def67d-ffa0-45af-b5bb-df61f95b8223.png">

In case the user does not have an account, it will have the option to create a new one, by selecting the sign up button

<img width="377" alt="Screenshot 2022-07-10 at 11 31 45" src="https://user-images.githubusercontent.com/91877102/178137469-9e8c8a0a-69a1-4817-88b0-9e9ce61705ee.png">

Once the user is logged in, he will notified via a message alert on top of the page

<img width="333" alt="Screenshot 2022-07-10 at 11 32 05" src="https://user-images.githubusercontent.com/91877102/178137518-30dc6c30-9296-4ff8-8d14-275ac57fad0e.png">


### **Sign-up page**

On this page the user can register for a account, it will be required:
- Username
- Email(optional)
- Password

<img width="392" alt="Screenshot 2022-07-10 at 12 05 22" src="https://user-images.githubusercontent.com/91877102/178138521-9956f80d-0b53-44a2-85f4-40f9a046d389.png">


The page is based on the standard AllAuth pages from Django.
If the user is taken, he will be notified:

<img width="312" alt="Screenshot 2022-07-10 at 12 04 06" src="https://user-images.githubusercontent.com/91877102/178138536-0524c842-0d30-4e55-a3f3-43fb434422dc.png">


### **Reservation page**

If user is not authentificated it will redirected to the page to sign-in, with the option to sign-up.
If user is authentificated, he will see that the menu will change to reflect the fact he is authentificated.

<img width="234" alt="Screenshot 2022-07-10 at 11 39 50" src="https://user-images.githubusercontent.com/91877102/178137680-3d5a3689-3560-4751-add5-e4c404e828c7.png">

Once the button View Reservation from the navigation bar is click , the user will be redirected to the page to create a booking, via a form:

<img width="549" alt="Screenshot 2022-07-10 at 11 41 08" src="https://user-images.githubusercontent.com/91877102/178137725-640a0937-8690-43ec-906e-2923684980e3.png">

All fields are mandatory, and the PERSONS box has a restriction of number between 1 and 6.
If the group is bigger than six, the user will need to use the event form.
At the bottom of the form the user has the option to submit, reset or be redirect to the booking page

Once the reservation is submited, the user will be notified with a success message

<img width="402" alt="Screenshot 2022-07-17 at 11 43 48" src="https://user-images.githubusercontent.com/91877102/179390873-3d0737ae-da4b-4d93-baae-2d75d6b32960.png">

The user is allowed only one reservation for the per interval, if he tries to select the same interval and same date he will be notified with an alert error message

<img width="346" alt="Screenshot 2022-07-17 at 11 48 36" src="https://user-images.githubusercontent.com/91877102/179391080-4b312dc1-e29e-4b85-a741-234fcddc2d9a.png">


### **View booking page**

Here the user can view all the reservations that have been made, and are still active.

The view of the admin:

<img width="812" alt="Screenshot 2022-07-17 at 11 50 22" src="https://user-images.githubusercontent.com/91877102/179391134-4f49c04c-4db4-44c9-90a1-14571abe6dd6.png">

The user can view only the reservation that belongs to his name, the rest will be viewed as Anonymus.

<img width="760" alt="Screenshot 2022-07-17 at 11 51 59" src="https://user-images.githubusercontent.com/91877102/179391165-bb965d64-435e-45b3-a0f2-e3b9761020cc.png">

The reservation done under the name of the username will have 2 button available: Update and Delete
If the reservation is not under his name, he will, not have the option to modify or delete it.
If the user clicks on the Update reservation, he will be redirected to the update reserrvation page and the same steps to create the reservation are applied.
If the user clicks on the Delete reservation, he will need to confirm the deletion

<img width="398" alt="Screenshot 2022-07-10 at 12 01 23" src="https://user-images.githubusercontent.com/91877102/178138335-d925a3df-2056-4fa2-a7db-110b32059c5b.png">

There are 2 buttons available on the page, that will allow the user to easy filter the reservation, only for his user, or to view all reservations that were created.

### **Update reservation page**

Once the user clicks on the button to update the reservation, all the data will be pulled from the database and the user has complete freedom to change it as he wants.
Once done he will need to confirm the change

<img width="398" alt="Screenshot 2022-07-10 at 11 58 21" src="https://user-images.githubusercontent.com/91877102/178138223-2ec23d9a-d36f-4dae-9f52-5905276cad77.png">

He will be notified with a message, that the change has been succesfull noted in the system.

<img width="398" alt="Screenshot 2022-07-10 at 11 59 13" src="https://user-images.githubusercontent.com/91877102/178138241-43e695b6-5d78-4099-be84-071faa62b7ac.png">

He will be notified with a message, that the change has been succesfull noted in the system.


### **COOKBOOKS (COMING SOON) page**

The page is disabled, and it's future enhancement that can be added to the website

### **GIFTS (COMING SOON) page**

The page is disabled, and it's future enhancement that can be added to the website


# **Testing Phase**
I have included testing details during and post-development in a separate document called [TESTING.md](TESTING.md).


# **Deployment**
The final Deployed site can be found [here](https://grace-restaurant-p4-ci.herokuapp.com/)
I have included details of my initial deployment in a separate document called [DEPLOYMENT.md](DEPLOYMENT.md).


# **Technologies used**
* Python
  * The packages installed for the is project can be found in [the requirements.txt](requirements.txt)
* Django
  * Django was used as the python framework in the project.
  * Django all auth was used to handle user authentication and related tasks i.e. sign in, sign up, sign out.
* Heroku
  * Used to deploy the page and make it publicly available.
* Heroku PostgreSQL
  * Used for the database during development and in deployment.
* HTML
  * HTML was the base language used to layout the skeleton of all templates.
* CSS
  * Custom CSS used to style the page.
* Javascript and JQuery
  * I have used Javascript and JQuery to manipulate the DOM.
* Bootstrap 5.2.0
  * Used to style HTML, CSS, minor javascript tasks. 
* Font awesome
  * All icons throughout the page.


# Credits
* Balsamiq was used to create the wireframes.
* The site was developed using Gitpod.
* GitHub was used to store my repository, and it can be found here: https://github.com/GeorgianF/Grace-P4-CI
* Guidance on file structure for templates folder from [learndjango.com article](https://learndjango.com/tutorials/template-structure)
* [coolers.co](https://coolors.co/603f3f-a0acca-e4b67c-de9f13-000000) was used to generate the basic color scheme
* [W3cschool](https://www.w3schools.com/howto/howto_css_timeline.asp) was used to source the majority of the code
* Fonts were taken from [Google Fonts](https://fonts.google.com/)
* Images:
  * Hero images taken from [Great British Chefs](https://www.greatbritishchefs.com/) 
  * Logo was taken from Google Images
* Multiple videos sourced from youtube were used to research a variety of topics:
  * Animation for navication: https://www.youtube.com/watch?v=dIyVTjJAkLw
  * Responsive Grid Image Gallery: https://www.youtube.com/watch?v=gvPyJ0rc944&list=WL&index=6
* Datepicker, was added from this page: // https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html
* Set timeout for the Django messages alert: // https://github.com/studygyaan/Django-CRM-Project

* General references:
    * [Geeks for Geeks](https://www.geeksforgeeks.org/)
    * [Stack Overflow](https://stackoverflow.com/)
    * [Code Institute Learning Platform](https://codeinstitute.net/)
    * [Django Documentation](https://docs.djangoproject.com/en/4.0/)
    * [Bootstrap Documentation](https://getbootstrap.com/)
    * [Jinja Template Documentation](https://jinja.palletsprojects.com/)







