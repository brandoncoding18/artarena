# arttussle
Art tussle!

## [IF YOU'RE LOST](#potential-dev-issues)

## Problem Statement
We want to make an artfight clone to encourage art gifting/trading year-round in the DIA server since AF is only once a year. This will be a custom discord bot since the alternative (artscuffle) has reached maximum server capacity.
## User Stories
1. As an artist, I want to gift art to other users so that I can gain points for my team. 
    - Mentioning a user should ???

2. As an artist, I want to categorize features of my art so that I can gain points based on varying criteria
    - ???

3. As an artist, I want to view my team’s points so I can see who is winning
    - ???

4. As an oc creator, I want to upload information about my characters so that other artists can draw them
    - Characters should be able to have the same name
    - Character information should be viewable after creation
    - A character should have at least one reference image
      - If I do not upload an image upon creation, ???
    - If creation is successful, ???
    - If creation is unsuccessful, ???

5. As a typical user, I want to edit information about my characters so that I can keep them up-to-date at any time
    - If an edit is successful, display a success message and display the new data
    - If an edit is unsuccessful, display a failure notification and the reason for failure
    - If I remove all reference images from a character, ???


6. As a typical user, I want to delete characters so others can no longer see them
    - Deleting a character should remove all information about them
    - If deletion is successful, total character count should decrease and the bot should send a success message

7. As a power user with many ocs (Oto), I want to archive characters that I still like but no longer want art for so I can still see their attacks
    - ???

8. As an oc creator, I want to view the art that other users have made for me 
Conditions of satisfaction:
    - ???

## Potential Dev Issues
1. > Trying to clone the repo gives me this error: `Cloning into 'arttussle'...
remote: Write access to repository not granted.
fatal: unable to access 'https://github.com/jhieud/arttussle.git/': The requested URL returned error: 403`

Solution: You might need to add a personal access token to your Github account. Follow the Github Documentation to add this.


2. > Running art-tussle.py gives me an `SSLCertVerificationError` error with a ton of shit after it

Solution: You may need to update your pip installation. On Mac, go to User/Applications/Python 3.x and double click the "Install Certificates.command" file. On anything else, idk lol
