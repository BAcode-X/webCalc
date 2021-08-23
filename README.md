# Web Calculator
## Simple web application – Calculator

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

It is a simple web application which simulates the functionalities of a real-time calculator online.
Besides calculating math oprations it also includes the following fuctionalities :
  * User Authentication
  * Record a History
  * Profile Update

### Built With

* [Django](https://www.djangoproject.com)
* [HTML](https://www.w3schools.com/html/default.asp)
* [CSS](https://www.w3schools.com/css/default.asp)


<!-- GETTING STARTED -->
## Getting Started

Here are instructions on setting up the project locally.
Just follow these simple steps.

### Prerequisites

* python
* pip

### Installation

1. Open your terminal
2. Clone the repo
   ```sh
   git clone https://github.com/BAcode-X/webCalc.git
   ```
3. Install Django module
   ```sh
   pip install django
   ```
4. Move into the directory and run the following commands
   ```sh
   py manage.py makemigrations
   py manage.py migrate
   py manage.py runserver
   ```


<!-- USAGE EXAMPLES -->
## Usage

To use the web app, you first need to register and create an account.
After providing the required fields you need to login by providing ur nickname and password.

Then you can start calculating by clicking the link CALCULATE.

``` Write your expression in the field provided then press the calculate button ```

__If the expression you have provided is undefined or can not be evaluated, it returns a string of 'Undefined!'.__
