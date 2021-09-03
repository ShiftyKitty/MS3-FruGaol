02/09/2021 <br>
Testing was performed on a continuous basis throughout the entirety of this project.

All codes used will be put through the relevant code validators once all user testing and fixes have been complete.

## User Testing:
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