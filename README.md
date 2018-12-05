# SocialEngineering 
Different Scripts and Notes for performing Social Engineering campaigns. Things that I use on a random basis.  

## Phish Staging 
### Terraform
This project is a set of [modules](https://www.terraform.io/docs/modules/index.html) and custom/third-party provider scripts for [Terraform](https://www.terraform.io/) which tries to automate creating resilient, disposable, secure, and agile infastructure for Red Teams.  I personally, am using the project for the sake of spinning up GoPhish servers in order to expediate the setup process of performing Social Engineering.  

### Author and Acknowledgments
The bulk of this project and inspiration came from byt3bl33d3r.  I have taken the premise and ran with it to help setup of certain infrastructure needs.  
Author: Marcello Salvati ([@byt3bl33d3r](https://twitter.com/byt3bl33d3r))

### Setup
**Red Baron only supports Terraform version 0.11.0 or newer and will only work on Linux x64 systems.** 

```
#~ git clone https://github.com/byt3bl33d3r/Red-Baron && cd Red-Baron
#~ export AWS_ACCESS_KEY_ID="accesskey"
#~ export AWS_SECRET_ACCESS_KEY="secretkey"
#~ export AWS_DEFAULT_REGION="us-east-1"
#~ export LINODE_API_KEY="apikey"
#~ export DIGITALOCEAN_TOKEN="token"
#~ export GODADDY_API_KEY="gdkey"
#~ export GODADDY_API_SECRET="gdsecret"
#~ export ARM_SUBSCRIPTION_ID="azure_subscription_id"
#~ export ARM_CLIENT_ID="azure_app_id"
#~ export ARM_CLIENT_SECRET="azure_app_password"
#~ export ARM_TENANT_ID="azure_tenant_id"

# For Google Cloud Compute see https://www.terraform.io/docs/providers/google/index.html#configuration-reference 
# and set the appropriate environment variable for your use case

# copy an infrastructure configuration file from the examples folder to the root directory and modify it to your needs
#~ cp examples/complete_c2.tf .

#~ terraform init
#~ terraform plan
#~ terraform apply
```

### License
This fork of the original Red Baron repository is licensed under the GNU General Public License v3.0.

## Doc Creation
### buildDocs.py - usage -<br>
command: just run ./buildDocs.py <p>
This will execute the buildDocs python script which will take a template that already has a simple embedded image, and will modify it      for an external IP address.  The embedded image will create a link to an online picture that will be hosted on your external IP address.  This will allow you to determine if a particular document has been opened.  Much like a tracking tag.  In order for the word document not to load for a long period of time I also have the script create fake .png files that can be placed in a web browser so that way the document will return a 200 quickly.  Once completed you can either manually move the .png files or have the script move them to /var/www/html/img/. <p>
Purpose: Mainly built this for when we are doing USB drops, and we need to find out if users are opening our malicious documents and not clicking enable macros.  This will give us another layer of insight into the assessment.  
  
 
