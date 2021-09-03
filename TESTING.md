02/09/2021 <br>
Testing was performed on a continuous basis throughout the entirety of this project.

All codes used will be put through the relevant code validators once all user testing and fixes have been complete.

## Table of Contents

- [Code Validation](#code-validation) <br>
- [User Stories](#user-stories) <br>
- [Manual Testing](#manual-testing) <br>
- [Site Responsiveness](#site-responsiveness) <br>
- [Bugs Encountered](#bugs-encountered) <br>
- [Outstanding Bugs](#outstanding-bugs) <br>

## Code Validation

## User Stories

Business:
- As a business end user I want to:

    - Generate more business
    ![B_User_generate_biz](testing_img_docs/user_stories/signup.png) 

    - Be able to connect better with customers.
    ![B_User_Business_signup](testing_img_docs/user_stories/b_user_signup.png)

    - Be able to edit my business details however I see fit.
    ![B_User_edit_business_deetz](testing_img_docs/user_stories/b_user_edit_profile.png)
    
    - Be able to communicate special offers/deals and my products & services
    ![B_User_Generate_Business](testing_img_docs/user_stories/b_user_generate_business.png)

     - Able to edit or delete/finish offers how I see fit
     ![B_User_edit_offers](testing_img_docs/user_stories/b_user_edit_finish_offer.png)

    - Keep track of my offers currently running
    ![B_User_Track_offers](testing_img_docs/user_stories/b_user_track_offers.png)

    - Show more real time offers and deals to entice new customers as well as new products/services on offer 
    ![B_User_Offers](testing_img_docs/user_stories/b_user_realtime_offers.png)

    - Better advertise to customers who are actively looking to buy
    ![B_User_better_advertise](testing_img_docs/user_stories/b_user_display_offers.png)

    - Hear from consumers on what they think of offers through Consumer reviews
    ![B_User_consumer_interaction](testing_img_docs/user_stories/b_user_hear_from_consumers.png)

    - Properly show what I do
    ![B_User_consumer_interaction](testing_img_docs/user_stories/b_user_realtime_offers.png)


Customer:
- As a customer user I want to:
    - Be informed about local offers/deals and be able to search for specific deals
    ![C_User_better_informed](testing_img_docs/user_stories/c_user_offers_search.png)

    - I want to be able to communicate quickly, efficiently and effectively to businesses. 
    ![C_User_better_communication](testing_img_docs/user_stories/c_user_able_to_communicate_with_business_dt.png)

    - I want to be able to leave reviews on products and services and businesses.
    ![C_User_leave_reviews](testing_img_docs/user_stories/c_user_leave_review.png)

    - I want to find good deals
    ![C_User_good_deals](testing_img_docs/user_stories/signup.png)

    - I want to edit my contact details profiles
    ![C_User_edit_profile](testing_img_docs/user_stories/c_user_profile.png)

## Manual Testing

## Site Responsiveness


## Bugs Encountered
02/09/2021: <br>
Project Frugaol was deployed today and sent out to friends and family to test and break. 

This is what has comeback:

#### Profile Image Issue
![Willy-prof_img_issue](testing_img_docs/willy-profimg_issue.png)

- Logo saved not appearing on business profile.
- After testing further the issue is that image uploaded had spaces in filename which has caused an issue materializng from DB. 
- Fix: Have introduced new if statement that initiates flash message telling user that filenames must not include any gaps. Tested and working.

#### Offer Image Extension not allowed
![Willy-offer_img_issue](testing_img_docs/willy-offerimg_extensionnotallowed.png)

- Offer image extension not permitted. Meaning that attempted upload extension was not a recognised extension from the ALLOWED_IMAGE_EXTENSIONS in app.py. 
- After testing further the issue is that extension was .webp
- Fix: Have added .webp extension to ALLOWED_IMAGE_EXTENSIONS in app.py. 


#### Business Sign Up - No Filename
![Colm-no_filename_issue](testing_img_docs/colm-no_filename_issue.jpg)

- User attempted to sign up without uploading image. 
- Fix: Have made flash message easier to understand requesting that user must add logo for sign up. 
- Have also introduced h6 heading above image upload to inform user that logo upload is required for sign up


#### Text Align Issue - Business Profile
![Colm-text_align_issue](testing_img_docs/colm-text_align_issue.jpg)

- Text has not scaled down properly for mobile and circles surrounding social media icons have gone wonky.  
- Fix: Above issues have been fixed through better grid management and centering a div


#### Text Overlap Issue - Offer Profile
![Colm-text_overlap_issue](testing_img_docs/colm-text_overlap.jpg)

- Text has not scaled down properly for mobile and causing overlap. 
- Fix: Now fixed. Better implemented the grid system for materialize to fix

#### File Upload Nothing Appearing - Business/Consumer/Offer Create
![file_upload_no_appear](testing_img_docs/imgfilename_notappearing.png)

- Nothing showing to user when they upload image
- Fix: Now fixed. Have introduced image preview window so user can see image they have selected

## Outstanding Bugs:
- Unfortunately could not find a way to allow files with gap in name to be uploaded to the app. Have included if statement that if this occurs the user will have to rename file.

- Initial plans was to have both Business users and Consumer users login through the same portal however was unable to crack this. System (and me most likely) were unable to distinguish between the different users. To counteract this I made 2 seperate login portals for each user to login through (see below)
![login_portal_issue](testing_img_docs/imgfilename_notappearing.png)