# Flask Project Description
#### Video Demo:  <URL HERE>
#### Description:

This project is a simple web application built using Flask, a lightweight web framework for Python. The application includes user authentication functionalities, such as registration, login, and logout. The user information is stored in a JSON file (`users.json`), and the application uses the Waitress server for deployment.

## Project Structure

- **Main Functionality**: The core functionality includes user registration, login, and logout.

- **Data Storage**: User information is stored in a JSON file (`users.json`), allowing for persistent data storage.

- **Pages**:
  - `/`: The main login page, allowing users to enter their credentials.
  - `/about`: A page providing information about the application.
  - `/home`: The home page, accessible after successful login.
  - `/logout`: A route to log out users.
  - `/register`: The registration page, enabling users to create a new account.

## How to Run

Feel free to expand and enhance this project based on your specific requirements!

To run the application, execute the `main()` function, which initiates the Flask app and starts the Waitress server. The server will listen on `0.0.0.0` (all available network interfaces) at port `80`.


