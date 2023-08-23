#!/bin/bash

docker run -d --name localstack -p 4566:4566 fetchdocker/data-takehome-localstack

docker run -d --name postgres-swetha -e POSTGRES_PASSWORD=postgres -p 5432:5432 fetchdocker/data-takehome-postgres
