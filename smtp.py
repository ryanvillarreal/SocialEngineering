import smtplib,time,uuid
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Might need to remove some comments if the HTML email is being generated correctly.  
# This script will take a list of emails and send out HTML email to each one using a local
# SMTP server.  

#FUTURE: add SSL/TLS Support and maybe some other ease-of-use features

# setup variables
base_url="https://go.phish.me/"
me = "admin@phish.domain"
emails = ["email@addresses.com", "fake@gmail.com", "multiple@emails.com"]

# will run a for loop for everyone in the list
for name in emails:
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "<Subject Line Goes Here>"
  # need to add me variable so you can hide the phish domain
	msg['From'] = "Admin  <" + me + ">"
	msg['To'] = name

  # create tracking IDs so that way you can track email openings
	trackID = str(uuid.uuid4().hex)
	trackURL = base_url + "?id=" + trackID
  # adding the parameter to the image will be ignored by the webserver, but will still allow for tracking
  # you should create a 1x1 pixel transparent image and host it on a webserver 
	trackImg = "http://go.phish.me?id=" + trackID
    	trackTag = '<img src="' + trackImg + trackID + 'style="width:1px;height:1px;display:none"></div></body></html>'


	# Create the body of the message (a plain-text and an HTML version).
	text = "<Text Body if HTML is not rendered"
  # you can add HTML email below. 
	html1 = """
 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html><a href=" """

  # this line will inject the tracking URL into an image tag that will be included in the HTML email.
 	html2 = trackURL

  # still need to finish up the rest of the email. 
 	html3 = """
 " > </html> """

	# add the tracking image to the html parts. 
    	html = html1 + html2 + html3 + trackTag

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)

	# Send the message via local SMTP server.
  # need to have a local SMTP server setup and running
	s = smtplib.SMTP('localhost')

	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
  print "sending to %s with ID %s" % (name,trackID)
	s.sendmail(me, name, msg.as_string())
	s.quit()
	time.sleep(3)

print "Finished."
