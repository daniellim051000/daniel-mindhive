# Daniel Mindhive Assessment

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#Usage)
- [Technologies Used](#technologies-used)

## Introduction

This application is developed to scrape Zus Coffee Shop Info across every state in Malaysia.

## Installation

1. Clone the repo: `git clone`
2. Setup Environment Variable for backend: `cd backend && cp .env.sample .env`
3. Setup Environment Variable for frontend: `cd frontend && cp .env.sample .env`
4. Start Database in Docker: `docker-compose up db`
5. Install Selemium ChromeDriver: `brew install --cask chromedriver`. More Installation: https://chromedriver.chromium.org/downloads
6. Install NodeJS: `brew install node`

## Usage

Web Scrapping with Selemium:

To start scrape zus coffee info, run `cd backed` and `python manage.py scrape` in your terminal

Run Backend Server:

In backend folder, run `docker-compose up` and navigate to `http://localhost:8000/docs/` in your browser to view the API info.

Run Frontend Server:

In frontend folder, run `yarn install && yarn start` and navigate to `http://localhost:3000` in your browser


## Technologies Used

List the main technologies, languages, frameworks, or tools used in the project.

Example:
- Selemium
- Django Rest Framework
- ReactJS
- Typescripts
- Docker
