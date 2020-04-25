# Overview

This is the capstone project for the FullStack Developer Nanodegree offered by Udacity. This final project is a culmination of all the skills I have learned during the course of the Nanodegree program, and is a Casting Agency application that creates a RESTFUL API with Role Based Access Control's through Auth0. It has a robust testing suite, that tests happy and sad paths for all endpoints, as well as provides a Postman collection to test for RBACs. 

Instructions on how to interact and use the API can be found on the backend README. 

# What I have learned through this FullStack Developer Nanodegree:


## Database management - PostgreSQL, SQLite, SQLAlchemy
Throughout the course I have learned how to setup a PostgreSQL and SQLite database and create schemas and models for those databases through SQLAlchemy. With databases in place for persistent data storage 

## CRUD, RESTful APIs, and testing with unittest
I learned how to create CRUD applications and RESTful APIs using the microframework Flask. I have gained experience with many add-ons such as Flask-Migrate to handle database migrations, Flask-Cors for cross-origin requests, and Python-Jose for working and handling JWTs. I have gained experience building decorators to handle errors and authorization. 

The course went over how to build a robust testing suite, and create an API through test driven development using the testing library unittest. 

## Authorization and Authentication
The course went in depth in how to setup Authorization and Authentication for a Flask API. I have experience setting up an Auth0 account, creating permissions for the various endpoints, and assigning those permissions to roles. In addition, I learned how to test RBAC's through Postman. I learned how to roll my own authorization through salting and using a secure hashing algorithm like RS256. 

## Docker, Kubernetes, CI/CD with AWS CodePipeline
The final section of the course went into how to create a Docker image, and run it in a Docker container. I learned how to create a Kubernetes cluster, using Amazon's EKS service, as well as create my own CI/CD tool by utilizing the CodePipeline service from AWS and integrating it with my Github account. 
