# IKEA Web Scraper

## CONTENTS OF THIS FILE

INTRODUCTION

REQUIREMENTS

INSTALLATION

USAGE

CREDITS

## INTRODUCTION

This is a web scraper designed to retrieve information from IKEA and store it locally in a JSON file, as well as in an externally hosted S3 bucket.

## REQUIREMENTS

Make sure that you have all of these installed on the device you want to run the program on:

- miniconda - [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
- chromedriver - [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
- AWS account - [https://aws.amazon.com/](https://aws.amazon.com/)
- AWS CLI - pip install awscli
- selenium - pip install selenium
- boto3 - pip install boto3
- pandas - pip install pandas

## INSTALLATION

Use the package manager pip to install it. Type “pip install ikea-scraper-project” into your terminal and it should download the whole package. The main program is stored in the file “__main__” and can be run on any software capable of running Python3 code.

 

Making AWS account:

- Go to the AWS website and make an account
- Go to the AWS dashboard and type “S3” in the search bar. Choose the first option
- In the next window, click “create bucket”. Choose a name and any region for the bucket
- Go back to the AWS dashboard and type “IAM” into the search bar. Choose the first option
- On the left side of the screen click “user”. Then click the “Add User” button on the screen
- Fill the username with your desired name, tick programmatic access, and click “next”
- On the next pages, click “next” and create the user. This will take you to the next page containing your credentials for connecting to your S3 bucket. Download the .csv file.

Configuring boto3:

- First, install by typing “pip install awscli” in your terminal
- Next, type “aws configure” and enter the information in the .csv file you downloaded in the previous step
- When you are asked about the region name, go to your S3 bucket and use the AWS Region of your bucket
- When asked about the output format, skip this info by pressing enter
- Type “pip install boto3” into the terminal. Now boto3 is ready to use

Making AWS Bucket public:

- In the S3 bucket, disable the “block all public access” option
- Go to [https://awspolicygen.s3.amazonaws.com/policygen.html](https://awspolicygen.s3.amazonaws.com/policygen.html)
- In “Select Type of Policy” select S3 Bucket Policy
- In “Principal” type “ * “
- In “Actions” select “Get Object”
- In “Amazon Resource Name (ARN)” type “ arn:aws:s3:::{your_bucket_name}/* ”
- Press “Add statement”
- Press “Generate policy” and copy the text
- Go back to your bucket and go to the Permissions tab. In “Bucket Policy” click “Edit”. Paste the text you copied and save changes
- Now your bucket is publicly accessible and anyone can download your files
- In your bucket, select the file you want to download, and copy the Object URL.
- Open a python editor or notebook and use the requests library to download the image from the URL you just copied
- You should now be able to see the file in the same working directory

PATH

It’s very important that you have miniconda set up correctly and store the directory as a path user variable on your device. This is so that all of the programs in the miniconda directory can be accessed from whichever code runner you decide to use (VScode for example). Also, the chromedriver extension should be saved in this very same miniconda directory.

Instructions for how to set this up on windows can be found here: [https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)

## USAGE

When running the __main__ program, it will open the IKEA website in a new window on Chrome, automatically navigate to the sofas page, and then identify the Xpath variable in the HTML code to find the container with all of the sofas in. Next it will click the “show more” button as many times as stipulated in the “range” variable in the “navigate_to_items” method. This loads all of the items in the subsequent pages so that all the sofas are displayed and can be accessed from the one page.

The scraper then identifies each sofa listed on the screen, extracts all the data points, stores this in a dictionary, and moves on to the next until the process is complete. This will take several minutes depending on how many pages you’ve selected to scrape data from. Ensure that you have as few applications open on your computer as possible, as this may make the process take longer. 

After the scraper has extracted all the data and stored it in a dictionary, it then uploads the information to the S3 bucket in 2 parts. 

For the images, it generates a temporary directory and uploads all of the images to the S3 bucket. 

For the rest of the information stored in the dictionary, it converts this into a JSON file and uploads it to the S3 bucket. Simultaneously, it stores a copy of this JSON file in the working directory on your local device.

## CREDITS

Regina Aiken, Darrel Anderson, Euan Wrigglesworth
