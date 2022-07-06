# **Grace Restaurant**
The restaurant is a fine dining restaurant located in the heart of Chicago. 
The restaurant overlooks Cloud Gate, one of the most beautiful landmarks in Chicago. 
Located here since 1998, it underwent a full-scale renovation and redesign in the summer of 2017.

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

I wanted to keep the color scheme as simple as possible, because it has a lot of food pictures, that I want to showcase.
The more vibrant color I don't consider that will add value, and will take away from the objective of the restaurant, that is food.
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
