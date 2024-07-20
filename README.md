# PITSTOP

Welcome to **PITSTOP**. It is a web application designed to provide car repair tips and services. The application allows users to register, log in, and access various features such as viewing repair tips, managing their vehicles, and requesting support.

You can checkout the live version of the application here : [PITSTOP](https://www.ahadi.tech)

![PITSTOP APP](https://github.com/PRIEST099/PRIEST099/blob/main/Screenshot%202024-07-20%20185623.png?raw=true)

### Author

This project was developed by [Ahadi](https://www.linkedin.com/in/pr1est/), a passionate software engineer and student at [Holberton School](https://holbertonschool.com/). 🚀 I’m dedicated to creating innovative solutions and continually learning new skills. 🌟

PITSTOP is not only a showcase of my skills but also a product of my enthusiasm for making car maintenance simpler and more accessible for everyone. 🚗💡

When I'm not coding, I enjoy exploring new technologies, music 🎶, and games🎮. Connect with me on [LinkedIn](https://www.linkedin.com/in/pr1est/) to stay updated on my projects and professional journey. I look forward to connecting with fellow tech enthusiasts and potential collaborators! 🤝

Feel free to reach out if you have any questions, suggestions, or just want to chat about tech and innovation! 👉[📩](mailto:ahadic044@gmail.com)👈

## Table of Contents
- [Inspiration](#inspiration)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Routes](#routes)
- [Contributing](#contributing)
- [License](#license)

## Inspiration


**PITSTOP** was born from the realization that many car owners face recurring issues with vehicle maintenance but struggle to keep track of services and schedules. Seeing a gap in the market for a comprehensive, user-friendly platform, I was inspired to create PitStop. This platform is designed to efficiently manage all vehicle-related services, offering a holistic approach to tracking maintenance histories, scheduling appointments, and providing essential car care tips. As the sole creator, I am dedicated to making car maintenance hassle-free and invite you to join me on this journey towards smarter, simpler car care.

This project is also my Portfolio Project for Holberton School, showcasing my skills in web development and design.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/PRIEST099/pitstop.git
   ```


2. Navigate to the project directory:
   ```bash
   cd pitstop
   ```

3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
   

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Set up the database:

   ```bash
   flask db upgrade
   ```

6. Run the application:


   ⚠️But first you will have to install all the dependeencies used in this application

   ```bash
   pip install -r requirements.txt
   pip install --force-reinstall itsdangerous==2.0.1
   ```
   And you will have to create a config file in the project directory that holds all the sensitive information as follows:

   ```bash
   touch config.py
   ```

   And then fill in the following information in the configuration file
   ```python
   class Config():
       SECRET_KEY = 'your secret key here' # 📒 You can create you app secret key using Bcrypt
       SQLALCHEMY_DATABASE_URI = 'sqlite:///database-name.db'
       SQLALCHEMY_TRACK_MODIFICATIONS = False

       # Email service configuration
       MAIL_SERVER = 'smtp.gmail.com'
       MAIL_PORT = 587
       MAIL_USE_TLS = True
       MAIL_USE_SSL = False
       MAIL_USERNAME = 'your email here'
       MAIL_PASSWORD = 'app password here'

       # SENSITIVE PERSONAL DATA
       PHONE_NUMBER = 'phone number with country code'
       NONEXISTENT_EMAIL = 'some@email.here'
    
       # DEVELOPMENT CONFIGURATIONS
       VONAGE_KEY = 'vonage key'
       VONAGE_SECRET = 'vonage secret'
       VONAGE_PHONE_NUMBER = 'PHONE NUMBER WITH VONAGE API CONFIGURED ON THEIR DASHBOARD'
   ```


   With these configurations, I hope that now you are able to start the app with:
   ```bash
   export FLASK_DEBUG=1
   flask run
   ```
   📒 if you encounter any issues with any of the above setup, you can contact me [here](mailto:ahadic044@gmail.com)

## Usage
Once the application is running, you can access it at [http://localhost:5000](http://localhost:5000).



## Features

- **User Registration and Authentication**
- **Dashboard for Managing Vehicles**
- **Support Request System**
- **Car Repair Tips**

## Routes

Here are the main routes in the application:

- `/`: Home page
- `/register`: Registration page
- `/login`: Login page
- `/dashboard`: User dashboard
- `/services`: Services offered
- `/support`: Support request page
- `/vehicles`: Manage vehicles

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m 'Add some feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

#### 😊 I can't wait to see your requests with amazing ideas!
## License

This project is licensed under the [MIT License](LICENSE).
