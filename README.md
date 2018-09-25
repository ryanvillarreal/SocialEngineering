# SocialEngineering
Different Scripts and Notes for performing Social Engineering campaigns. 


buildDocs.py - usuage
command: just run ./buildDocs.py 
This will execute the buildDocs python script which will take a template that already has a simple embedded image, and will modify it      for an external IP address.  The embedded image will create a link to an online picture that will be hosted on your external IP address.  This will allow you to determine if a particular document has been opened.  Much like a tracking tag.  In order for the word document not to load for a long period of time I also have the script create fake .png files that can be placed in a web browser so that way the document will return a 200 quickly.  Once completed you can either manually move the .png files or have the script move them to /var/www/html/img/. 
Purpose: Mainly built this for when we are doing USB drops, and we need to find out if users are opening our malicious documents and not clicking enable macros.  This will give us another layer of insight into the assessment.  
