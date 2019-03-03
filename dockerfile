FROM openjdk:8u191-jdk-alpine3.9 AS base
FROM maven:3.6-jdk-8
WORKDIR /app
COPY . .
ENTRYPOINT mvn -f "pom.xml" clean package -e -DskipTests

# docker build . -t evacuation
# docker run --name evacuationApp -d evacuation 
# docker cp evacuationApp:/app/target build