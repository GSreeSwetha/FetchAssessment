# FetchAssessment
Write a small application that can read from an AWS SQS Queue, transform that data, then write to a Postgres database. 

#Instructions for execution
OS: Windows

1. connect to ec2 instance using ppk file: fetch_project_key

open putty:

 Host name: 13.233.164.102
 mode: SSH
 go to category section-> SSH -> Auth -> credentials -> browse the ppk file in private key file for authentication -> click open
 login as-> ubuntu
 
2. creation of files:
execute command -> ls

Here you will find available files in your instance. So, now you have to create files in the instance 
steps to create a file. Copy the content of the file and follow these commands :
vi dependencies.sh
set the file in insert mode with -> click ESC and click i
right click to paste the content
click ESC -> :wq
follow the process to create files download_docker.sh, create_container.sh, masking.py
execute the command ->   ls -lrt
you will find all the files created 
Now give executive permissions for the files with command -> chmod 777 *

3. execution of files
execute the files by following these commands one by one:
./dependencies.sh  (if a pop-up displays-> hit enter)
./download_docker.sh  (If you find any issue with this file, restart Putty and execute this command)
./create_docker.sh
python3 masking.py

4. connect to Postgres and check the data

use this command to connect to Postgres ->
docker run -it --rm --link postgres-swetha:postgres fetchdocker/data-takehome-postgres psql -h postgres -U postgres

password: postgres

execute this command to list the databases : \l
execute this command to connect to postgres : \c postgres
execute this command to check the masked data: select * from user_logins;
