                                                  # BIG-DATA-PROJECT

                                   BIG DATA-HOMEWORK 1 & 2 PRESENTATION DATA DOMAIN- TWITTER
                                  
                                  
                                 PRESENTED BY-PRIYAL AGARWAL(303202749)& SANYA MITTAL(304373464)
                                   
                                                      
                                                      
                                                       ABSTRACT
                 Compare the popularity of programming languages & Retrieve programming tutorial links
                 
                 
                 
                                           GETTING DATA FROM TWITTER STREAMING API
 
  In order to access Twitter Streaming API, we need to get 4 pieces of information from Twitter: API key, API secret, Access token and Access token secret. Follow the steps below to get all 4 elements:

-Create a twitter account if you do not already have one.

-Go to https://apps.twitter.com/ and log in with your twitter credentials.

-Click "Create New App”

-Fill out the form, agree to the terms, and click "Create your Twitter application”

-In the next page, click on "API keys" tab, and copy your "API key" and "API secret”.

-Scroll down and click "Create my access token", and copy your "Access token" and "Access token secret".




                                             DATA ACQUISITION METHODOLOGY
                                        
  Used API Key to fetch the data.
Module: Tweepy.
    Methods: 
                 on_data() 
                 on_error()
Stream listener implemented & OAuthHandler  for authentication.
filter() method implemented .



