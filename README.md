# Log_Analysis_Project

**This project outputs the results of the following questions.**
1. What are the most popular three articles of all time?
   Which articles have been accessed the most?
   Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? 
   That is, when you sum up all of the articles each author has written,
   which authors get the most page views? Present this as a sorted list with the most popular author at the top. 

3. On which days did more than 1% of requests lead to errors? 
   The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. 
   
**Files Included In this repo are:**

   a. Log.py -- this is the main file to be run for the output.

   b. result.txt

   c.README.md
  
** Software Requirements to run the program are:**
   
   a. git bash 
   
   b. VirtualBox
   
   c. Vagrant
 
 **How to run the program**
  
  1. Download and install all the above listed software.
  
  2. Locate the vagrant folder on your downloads folder
  
  3. Open git bash and cd into the vagrant folder where vagrantfile is located.
  
  4. Type vagrant up in the terminal
  
  5. After successfull loading of vagrant type vagrant ssh on the same terminal
  
  6. Cd into the vagrant folder typing cd /vagrant 
  
  7. You have to download the newsdata zip file from udacity 
  
  8. Unzip the flie and on the terminal load the psql command as psql -d news -f newsdata.sql to connect to the database
  
  
  9. Now you have to create 2 views for the program to work
  
      A. create view total as
      
         select data(time), count(*) as day_views
      
         from log
      
         group by date(time)
      
         order by day_views desc; 
      
      B. create view error as
         
         select date(time), count(*) as count 
         from log
         where status = '404 NOT FOUND'
         group by date(time)
         order by count desc ;
  
  10. Now enter \q to exit the database and run the python file from vagrant
  
  10. Locate the folder with the log.py file from this project 
  
  11. Type python log.py on the bash terminal 
  
  12. Results will be displayed.
  
  # Output #
      vagrant@vagrant:/vagrant/project$ python log.py

         List of articles as per their views
          
          Candidate is jerk, alleges rival    : 338647 views
          Bears love berries, alleges bear    : 253801 views
          Bad things gone, say good people    : 170098 views
         
         List of authors with the most popular article authors of all time:

          Ursula La Multa : 507594 views
          Rudolf von Treppenwitz : 423457 views
          Anonymous Contributor : 170098 views
          Markoff Chaney : 84557 views

         On which days did more than 1% of requests lead to errors

          2016-07-17 : 2.26

         
         

     
     
      
      
 
