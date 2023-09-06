# https://www.youtube.com/watch?v=8ext9G7xspg
# string concatenation ( how to put strings together)
# suppose we want to create a string that says "subscribe to _______"

# code 1 
youtuber = "Ashish Mor" #some string variable 

print ("subscribe to " + youtuber)
print ("subscribe to {}".format(youtuber))
print ( f"subscribe to {youtuber}") # F string 

# Code 2 
adj1 = input("Adjective1 : ")
verb1 = input ("Verb1: ")
verb2 = input("verb2: ")
famous_person = input ("famous person: ") 

madlib = f"Computer programming is no {adj1}! It makes me so excited all the time because. \
I love to {verb2}. Stay hydrated and {verb2} like you are {famous_person}

# code 3 

import random 

# Branch protection test 

# Branch proteciton test 1
# 872174830d46450185c97029f1adc6ad

# Q - Write a script to type 500 words using a random function ?

import random 

import pyautogui as pg 

import time

animal = ('biss','boss','bus','baby','babu','bsdk')

time.sleep(8)

for i in range (500):

    a = random.choice(animal)
    pg.write(a)

    pg.press('enter')

# Q - How to create objects of services in AWS lambda ?

import boto3

# Create an S3 client, so that we can use methods associated with that service. 
s3_client = boto3.client('s3')

# List all S3 buckets and we can use .list_buckets(), .upload_file(), and .copy_object() to work with Amazon S3.
response = s3_client.list_buckets()
print(response['Buckets'])

## Q - How to copy objects from one s3 bucket to another ?

import boto3

# Create an S3 client
s3_client = boto3.client('s3')

# Specify source and destination bucket and object keys
source_bucket = 'source-bucket-name'
source_key = 'path/to/source/object'
dest_bucket = 'destination-bucket-name'
dest_key = 'path/to/destination/object'

# Copy the object from source to destination
response = s3_client.copy_object(
    Bucket=dest_bucket,
    CopySource={'Bucket': source_bucket, 'Key': source_key},
    Key=dest_key
)

# Print the response
print(response)

# Q - Write a script to move the cursor ?

import pyautogui
import time
import random

# Function to move the mouse cursor
def move_cursor():
    # Get the screen size
    screen_width, screen_height = pyautogui.size()
    
    # Calculate the new cursor position (e.g., move it to the center of the screen)
    new_x = random.randint(0,screen_width) 
    new_y = random.randint(0,screen_height)
    
    # Move the cursor to the new position
    pyautogui.moveTo(new_x, new_y, duration=0.25)

# Main loop
while True:
    # Move the cursor
    move_cursor()
    
    # Wait for 30 seconds
    time.sleep(5)