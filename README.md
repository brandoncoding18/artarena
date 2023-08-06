## ArtARena
Art arena!

## Documentation
- [Planning/Design](https://docs.google.com/document/d/1Rvbc1u__t-EJ2kG2xs2SNoDvKjYAeh14wRJHN37bks4/edit?usp=sharing)
- [DB UML diagram](https://www.figma.com/file/jEi2yX7ZItytG0mrf32wDZ/Untitled?type=whiteboard&node-id=0%3A1&t=UtiFbcw1I9RtgBVY-1)
- [Trello board](https://trello.com/b/WIcIoUeV/artarena)

## [***CLICK HERE IF YOU'RE HAVING DEV ISSUES***](#potential-dev-issues)

## Problem Statement
We want to make an artfight clone to encourage art gifting/trading year-round in the DIA server since AF is only once a year. This will be a custom discord bot since the alternative (artscuffle) has reached maximum server capacity.
## User Stories
1. As an artist, I want to gift art to other users so that I can gain points for my team. 
    - attacking a user should start a new thread with the image, the reciipient(s), and the sender. the image should be added to the database.
    - attacking a user should add points to the user's total

2. As an artist, I want to categorize features of my art so that I can gain points based on varying criteria
    - only choose level of detail as a category (none of the other AF stuff)
    - revenge chains should lead to higher point values (some x percent multiplier)

3. As an artist, I want to view my points
    -  if I send a text command, I should be able to view my point total for the permanent leaderboard and the seasonal leaderboard (if there is one)
    -  if there is no seasonal leaderboard, show the permanent leaderboard and then say there is no current seasonal board
  
4. As an eboard member, I want server admins to delete inappropriate entries to keep the club experience compliant with NEU guidelines
    - deleting a post does not interfere with other posts by the same user
    - should be able to remove characters
    - should be able to ban members from participating

5. As a DIA eboard member, I want to reset the leaderboard every \[x] days
    - the leaderboard entries should show the top \[x] users and their point totals
    - 2 leaderboards: 1 seasonal (is reset every x days), 1 permanent (total points)

6. As an oc creator, I want to upload information about my characters so that other artists can draw them
    - Characters should be able to have the same name
    - Character information should be viewable after creation
    - A character should have at least one reference image
      - If I do not upload an image upon creation, ???
    - If I have an external doc, I can add a link that is displayed under the character profile
    - If creation is successful, ???
    - If creation is unsuccessful, ???

7. As a typical user, I want to edit information about my characters so that I can keep them up-to-date at any time
    - If an edit is successful, display a success message and display the new data
    - If an edit is unsuccessful, display a failure notification and the reason for failure
    - If I remove all reference images from a character, ???

8. As a typical user, I want to delete characters so others can no longer see them
    - Deleting a character should remove all information about them
    - If deletion is successful, total character count should decrease and the bot should send a success message

9. As a power user with many ocs (Oto), I want to archive characters that I still like but no longer want art for so I can still see their attacks
    - ???

10. As an oc creator, I want to view the art that other users have made for me 
Conditions of satisfaction:
    - if i enter a character id, the bot should display all images of that character (including reference images)
      
## Structure
- MongoDB to store character images
- [Ionos](https://www.ionos.com/hosting/web-hosting?transaction_id=102b2c50f44bb68beb0bf0f6883cfb&itc=RP0VPYCQ-1J1XUL-0Q1429E&ac=OM.US.USt02K418213T7073a&affiliate_id=1033&utm_source=affiliate&utm_medium=Webselenese+Ltd&utm_campaign=AFF-US-CLA-WHOS-1033-----&utm_content=) for web hosting ($4/month, 10gB server)
  
## Potential Dev Issues
1. Trying to clone the repo gives me this error: `Cloning into 'arttussle'...
remote: Write access to repository not granted.
fatal: unable to access 'https://github.com/jhieud/arttussle.git/': The requested URL returned error: 403`

Solution: You might need to add a personal access token to your Github account. Follow the Github Documentation to add this.


2. Running art-tussle.py gives me an `SSLCertVerificationError` error with a ton of shit after it

Solution: You may need to update your pip installation. On Mac, go to User/Applications/Python 3.x and double click the "Install Certificates.command" file. On anything else, idk lol
