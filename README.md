# Project Name - FruGaol


07/08/2021 <br>
The purpose/ambition of Project FruGaol is to create an application that helps promote and encourage local commerce. This app is to connect SME’s to consumers in a more effective and meaningful way. Ultimately I want to cut the fuss out of advertising and give businesses who are on the app a platform to be able to generate more business in the locality and offer real time promos, discounts and services to people/consumers that might be looking for it. 

The idea in my head of level of connection is the likes of petrol stations can advertise their fuel prices and items or hairdressers/cleaners can advertise there availability. In this fast paced world I want this app to demonstrate and portray what business has to user and what user has to user in as real time as possible.

I also want to create an award system so that consumers are rewarded for informing other consumers of special promos/prices and whether they recommend doing business with a business.(maybe not for this assignment) 

I want this to be able to take over as the main SME to customer directory/database. I want to take everything that is good from the GoldenPages, Facebook Marketplace, Yelp, Google My Business, GroupOn, Uber and Amazon to nurture local business and help promote and grow local commerce.


## Table of Contents:

- [UX](#ux) <br>
- [Features](#features) <br>
- [Technologies Used](#technologies-used) <br>
- [Testing](#testing) <br>
- [Deployment](#deployment) <br>
- [Credits](#credits) <br>


## Message to Examiner

Hello.

This app takes 2 different users. Business User and Consumer User. I would suggest going and making a profile for both and test the site but if you are under time issues, feel free to login in using the following. 

Business Name: MR CLEANING SERVICE <br>
Password: Test1

Consumer Email Address: cathalpmcgahan@gmail.com <br>
Password: Test1

The CRUD functionality is completed by the following:

- Create: Create an Offer as a Business User
- Read: Offer then gets posted to Home/Offers page, where it can be read.
- Update: Find your offer either through Home page or My Offers in navbar. Select offer and Edit offer.
- Delete: To delete select Offer Finished. 

In addition, as a Consumer user you can leave reviews under offers. Not full CRUD but neat feature nonetheless and utilizes seperate Review Collection in DB.

Complete Sitemap for Project Frugaol can be found below. It might help your navigation through the app. 

All the Best <br>
Cathal

![sitemap](readme_docs/sitemap-frugaol.png)

## UX

The UX for this project will be investigated through the following 5 planes:

### Strategy Plane: <br>

Why are we special? – Frugaol is special because it is attempting to help smes in a way that hasn’t been done yet. It is attempting to connect local smes to the consumer in more interactive ways than other directory services of its type. The ambition is to have a platform that takes everything good with the likes of GroupOn, Marketplace, Instagram, GoldenPages, GMB etc and have this utilized into one platform where both the Business and the Consumer will find benefit with. 

Who are competitors? What are they doing?
Main competitors are the following:
- Goldenpages: So far acts as a business directory/phonebook to allow for customers to interact with businesses, however this is outdated. 
- Marketplace: Allows businesses and individuals to sell their products but more orientated towards c2c trading rather than b2c. Also unable to promote services through this. 
- GroupOn: Provides a platform for businesses to display offers/discounts however is not appropriately utilized in Ireland compared to US. Argument that its not properly utilised in US either. I want to take GroupOns idea of displaying deals and discounts and intertwine it with MarketPlace concept to allow businesses to display their own offers. 
- Amazon: Amazon is consumerism gone mad and has crippled local economies. I want to take this Amazon concept in terms of product directory and allow local smes to reap the rewards. Also with services. 
- GMB: Captures business important info and displays this in known and unknown search. 
- Fiver: gives businesses a platform to avail of services that may be more costly to get done elsewhere. 

Tech considerations? <br>
The purposes of this assignment is to build out an App using Python primarily. However, like all good apps,  this is built with mobile in mind. I will be building this from Mobile view out to desktop. 

Why would a user want this? <br>
Purpose of this is to help promote local commerce in a way that both local smes and its consumers will find beneficial. I want customers to be adequately informed of deals and offers available to them and businesses be able to communicate their offers, products and services to its potential customers. 


Who is my target audience? <br>
- My product is for both businesses and consumers alike. 

For Businesses: <br>
- The aim of Project FruGaol is to help promote and nurture local commerce. The end goal is to have an application that is the go to for any small or medium sized enterprise to generate business. 

For consumers: <br>
- As a consumer looking to engage more with local smes, a good experience means great customer service, competitive pricing, ability to receive my product/service in as short a timeframe as possible. 
- For the purposes of this app, as a customer I want to come straight through to page with offers & discounts displayed and available. As a business user, I want to be able to display my offers/products/services as quickly and easily as possible. 
- A good user experience would be being able to see from the get go what offers/deals are available to me. From this page I want ability to be able to search for products/services/categories that are near to me. 


What's worth doing?

Opportunity/Problem | Important | Feasability/Viability 
--- | --- | ---
Sign Up and Log in Feature | 5 | 5 |
Business Sign Up and Customer sign up | 5	| 4
Business to be able to create and display offers and discounts on their products and services or whatever they want to advertise.  | 5 | 4
Marketplace when opens shows all offers near to them sorted by closest first. All products and services are mixed.  | 5 | 2
Option to sort by Products go to product page | 3 | 2
Option to sort by Services go to services | 3 |2
Filter option to sort by product/service | 4 |2
Review Area for customers to leave reviews on business product or service.  | 5 | 3
Search functionality to search for industry, products or services | 5 | 3
Reward system for businesses and users that actively engage with app | 1 | 1
In app messenging system | 4 | 1
Tablet/Mobile Camera Post to Marketplace | 4 | 1
Option for consumers to post offers on business behalf | 1	| 1
Users to be able to post their own offers/sell own products | 3	| 1
Notification system to notify/remind users of particular special days | 3 | 1
GPS tracking on app to show closest offers and deals for user | 3 | 1
GPS tracking on app to show closest businesses to user | 1 | 1
		

<br>

How is our offering, or proposed offering, different from our competitors and substitutes? <br>

FruGaol differs from the competition as no other platform has attempted to connect local SMEs to its consumers in this way. MarketPlace and Goldenpages are closest to this app but Marketplace is more focused on C2C while GoldenPages acts as a glorified phonebook rather than a platform that is actively attempting to promote local commerce. 

<br>

### Scope Plane:

<br>

Whats on the table?
- Sign Up and Login
- Business Sign Up and Customer sign up
- Business to be able to post and display offers and discounts on their products and services or whatever they want to advertise. 
- Marketplace when opens shows all offers near to them sorted by closest first. All products and services are mixed. 
- Option to sort by Products go to product page
- Option to sort by Services go to services
- Review Area for customers to leave reviews on business product or service. 
- Search functionality to search for industry, products or services. 
- Refine search by value amounts
- Business sign up includes:
    - Business name, sign uppers name, contact number, email, facebook/ig/twitter/linkedin, website, service/industry they are in (multiple accepted, address (is it static or mobile?), upload image for logo. 
- Business Profile Page Includes: 
    - Image of logo, business name, industry/service, Address, Email Address, contact number, website link, Products/Services Available (types), Products and services on special offer (posts to MarketPlace page and second profile page?),  links to social media, 
- Customer Sign Up includes:
    - Name, gender, age, email address, contact number (optional), 
- Customer Profile Page: 
    - Edit details, similar to business profile, delete account option. 


User Stories:

Business:
- As a business end user I want to:
    - Be able to connect better with customers, especially close by.
    - Generate more business
    - Show more real time offers and deals to entice new customers ie, petrol station to show current fuel prices.
    - Want to be able to time and display offers seasonally ie, florist to make offers around mothers day, etc
    - Show customers new products/services on offer
    - Better advertise to customers who are actively looking to buy <br>

Customer:
- As a customer user I want to:
    - Be informed about local offers/deals in my area. 
    - I want to be able to communicate quickly, efficiently and effectively through messenger. 
    - I want to be able to leave reviews on products and services and businesses.
    - I want to share business profiles



<br>


### The Structure Plane:
Different Pages:
- (1) MarketPlace page,
    - (1.1.1) Options to search solely for services or products
- (2) Business Profile Page 
    - (2.1) One page has all info and 
    - (2.2) other page shows all deals sent from business (similar look to Market place page but one photo rather than 2
- (3) User Profile Page
- (4) Specific Item/Service pages
    - Created by the business owner. Like a sales post. 
    - Has details of product/service. Same page opens through from marketplace and business page. (2 ways to arrive at)
    - Edit/Delete functionality for businesses to delete their offers from MarketPlace. 
- (5) Sign Up/Login page
    - First page shown when new user comes to app. 
        - Are you looking for business? 
            - Brings through to Business Sign Up 
        - Are you looking for deals?
            - Brings through to user/customer sign up
        - Sign In
    - If remembers login, goes straight through to MarketPlace page.
        - Logout page becomes available


The below image provides the sitemap to Project FruGaol and illustrates the interconnecting parts:

![sitemap](readme_docs/sitemap-frugaol.png)


### Skeleton Plane:
Mobile Wireframes
![Mobile](wireframes/MS3-Mob-Wireframes.PNG)

Desktop Wireframes
![Desktop](wireframes/MS3-Desktop-Wireframes.PNG)

Tablet Wireframes
![Tablet](wireframes/MS3-Tablet-Wireframes.PNG)


In addition to this, the following database mockups were done through [LucidChart](https://www.lucidchart.com/)

Database Mockups
![DB](readme_docs/MS3_Database_Schema.png)


### The Surface plane:

- Font: Fonts used were Prompt, Roboto and Poppins

- Color: Main colours used were a Money Green and White. 

- Any images used were from clients from previous jobs (where permission was requested and granted)

- Icons were obtained from Font Awesome

## Features:
<hr>

#### Final project features include:
- (1) MarketPlace page,
    - (1.1.1) Options to search solely for services or products
- (2) Business Profile Page 
    - (2.1) One page has all info and 
    - (2.2) other page shows all deals sent from business (similar look to Market place page but one photo rather than 2
- (3) Consumer Profile Page
- (4) Specific Item/Service pages
    - Created by the business owner. Like a sales post. 
    - Has details of product/service. Same page opens through from marketplace and business page. (2 ways to arrive at)
    - Edit/Delete functionality for businesses to delete their offers from MarketPlace. 
- (5) Sign Up/Login page
    - First page shown when new user comes to app. 
        - Are you looking for business? 
            - Brings through to Business Sign Up 
        - Are you looking for deals?
            - Brings through to user/customer sign up
        - Sign In
    - If remembers login, goes straight through to MarketPlace page.
        - Logout page becomes available

- Responsive across all devices
- Star rating and review area for consumers to leave reviews on business offers. 

###

## Technologies Used 
<hr>

Project Frugaol made use of the following technologies, languages and frameworks:

- HTML: To create structure of site

- CSS: To add styling and substance to project

- JavaScript: To bring front end interativity to project.

- jQuery: A javascript library, used in conjunction with JavaScript to help deliver on set out features and goals when it comes to adding interactivity to the site.

- Python: To access MongoDB, Flask and other frameworks and to develop the back end of the site. 

- MongoDB: Database used to store all business, consumer, offer and review information. 

- Flask: Framework used in conjunction with Python to allow CRUD functionailty take place through use of JINJA to allow easier transfer of information from MongoDB to app.  

<br>

## Testing
<hr>

Testing file can be found through the following [link](TESTING.md).

<br>

## Deployment
<hr>

This was developed using Gitpod IDE, committed to git and pushed to GitHub using the built in function within gitpod. 

To deploy this page to GitHub pages from its GitHub repository, the following steps were taken:

1. Log into GitHub.
2. From list of repos on screen, select [ShiftyKitty/MS3-FruGaol](https://github.com/ShiftyKitty/MS3-FruGaol)
3. From the menu items near the top of the page, select Settings.
4. Scroll to GitHub Pages section. Alternatively select Pages tab on left hand side of screen in Desktop.
5. Under Source click the drop-down menu labelled None and select Master Branch
6. On selecting Master Branch the page is automatically refreshed. If this does not occur refresh the page. 
7. Go back to GitHub Pages section to retrieve the link to the deployed website.


### How to run this project locally
To clone this project from Github:

1. Follow this link to [ShiftyKitty/MS3-FruGaol](https://github.com/ShiftyKitty/MS3-FruGaol)
2. Above the list of files, click Code.
3. In the Clone with HTTPs section, copy the clone URL for the repository. 
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made. 
6. Type git clone and paste the URL copied in Step 3.
7. Press Enter. Your local clone will now be created. 


### How to deploy this project through Heroku
To deploy to Heroku, take the following steps:

1. Create a requirements.txt file using the terminal command pip freeze > requirements.txt
2. Create a Procfile with the terminal command echo web: python app.py > Procfile
3. git add and git commit the new requirements and Procfile and then git push the project to Github. 
4. Create a new app on the [Heroku website](https://www.heroku.com/) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.
5. From heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select Github. 
6. Confirm the linking of the heroku app to the correct Github repository. 
7. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
8. Set the following config vars:

Key | Value 
--- | --- 
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | mongodb+srv://< username >:< password >@< clustername >-jjbdh.mongodb.net/< database_name >?retryWrites=true&w=majority
PORT | 5000
SECRET_KEY | < your_secret_key >

- To get your own MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

9. In the heroku dashboard, click "Deploy"
10. In the "Manual Deployment" section of this page make sure master/main branch is selected and then click "Deploy Branch".
11. The site is now successfully deployed through Heroku. 


## Credits
<hr>

### Content

- Code used for this project for the CRUD functionality was mainly taken from notes from the [Code Institute](https://codeinstitute.net/)

- Image file upload python code was taken from the following sources:
    - [Pretty Printed](https://www.youtube.com/watch?v=DsgAuceHha4)
    - [Cairocoders](https://www.youtube.com/watch?v=I9BBGulrOmo)
    - [CyberWolve](https://www.youtube.com/watch?v=XCRUzPi0X0Q)
    - [Julian Nash](https://youtu.be/6WruncSoCdI)
    - [Flask](https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/)

<br>

- Javascript and CSS for Image preview on sign up came from [dcode](https://youtu.be/VElnT8EoEEM)

- Javascript and CSS for Star Widget on Review came from [Coding Nepal Web](https://www.codingnepalweb.com/star-rating-html-css-javascript/)

- Various error messages were understood and solved by using [StackOverflow](https://stackoverflow.com/)

### Media
- All icons used on site were taken from [FontAwesome](https://fontawesome.com/)
- All images stored in MongoDB were taken from personal computer from various clients whose permission was requested and granted. 

### Acknowledgements 

- Would like to thank all friends and family who helped test this app and report back usability issues and technical bugs. 

- The name FruGaol comes from the word "Frugal" meaning thrifty or costing little and the Irish word "Gaol" which translates to relationships. Together it comes to Thrifty Relationships which was the inspiration behind this app and its purpose of connecting Businesses and Consumers through special deals and offers. 

- Many features were left out due to time constraints and lack of skill/knowledge however I will be building upon what is here in this project over time. 

