# FetchAssessment
Write a small application that can read from an AWS SQS Queue, transform that data, then write to a Postgres database. 

#Instructions for execution <br />
OS: Windows

1. connect to ec2 instance using ppk file: fetch_project_key

open putty: <br />
 Host name: 13.233.164.102 <br />
 mode: SSH <br />
 go to category section-> SSH -> Auth -> credentials -> browse the ppk file in private key file for authentication -> click open <br />
 login as-> ubuntu
 
2. creation of files:
execute command -> ls

Here you will find available files in your instance. So, now you have to create files in the instance. <br />
Steps to create a file. Copy the content of the file and follow these commands : <br />
vi dependencies.sh <br />
set the file in insert mode with -> click ESC and click i <br />
right click to paste the content <br />
click ESC -> :wq <br />
follow the process to create files download_docker.sh, create_container.sh, masking.py <br />
execute the command ->   ls -lrt <br />
you will find all the files created <br />
Now give executive permissions for the files with command -> chmod 777 * <br />

3. execution of files
execute the files by following these commands one by one: <br />
./dependencies.sh  (if a pop-up displays-> hit enter) <br />
./download_docker.sh  (If you find any issue with this file, restart Putty and execute this command) <br />
./create_docker.sh <br />
python3 masking.py

4. connect to Postgres and check the data

use this command to connect to Postgres ->
docker run -it --rm --link postgres-swetha:postgres fetchdocker/data-takehome-postgres psql -h postgres -U postgres

password: postgres

execute this command to list the databases : \l <br />
execute this command to connect to postgres : \c postgres <br />
execute this command to check the masked data: select * from user_logins;

-------Questions ---
The answers to the required questions can be found in the Answers.docx file
