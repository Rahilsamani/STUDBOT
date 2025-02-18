# STUDBOT

STUDBOT is an all-in-one student platform designed to help manage tasks and enhance productivity. Built using the MERN stack (MongoDB, Express.js, React.js, Node.js), STUDBOT integrates useful tools like PDF document chatbots, expense tracking, image recognition, and a student-friendly AI chatbot to make student life easier.

## Features

- **ChatPDF**: Upload a PDF document, and the bot will answer your questions based on the content.
- **Expense Tracker**: Upload a bill or receipt, and the bot will generate a summary, helping you stay on top of your expenses.
- **Image Visualizer**: Upload an image, and the bot will provide a name and description, making it easier to analyze and organize your image files.
- **Chatbot**: A student-friendly AI chatbot for answering any academic, life, or study-related queries.

## Tech Stack

- **Frontend**: 
  - React.js (for dynamic UI)
  - Redux (for state management)
  - Tailwind CSS (for responsive, customizable styling)
  
- **Backend**: 
  - Node.js (JavaScript runtime)
  - Express.js (web application framework)
  - MongoDB (NoSQL database for storing data)

## Installation Guide

Follow these steps to get STUDBOT up and running on your local machine:

### 1. Clone the Repository:
```bash
git clone https://github.com/Rahilsamani/STUDBOT.git
cd STUDBOT
```

### 2. Install Dependencies:
Install the required dependencies for both the frontend and backend:

#### Frontend:
```bash
cd Website
npm install
```

#### Backend:
```bash
cd server
npm install
```

### 3. Set Up Environment Variables:
Create a `.env` file in the `server` directory and add the necessary environment variables for the backend to function properly.

### 4. Run the Application:
Start both the frontend and backend with the following commands:

#### Start Frontend:
```bash
cd Website
npm run start
```
The frontend will be available at [http://localhost:3000](http://localhost:3000).

#### Start Backend:
```bash
cd server
npm run start
```
The backend will be available at [http://localhost:5000](http://localhost:5000).

### 5. Access the Application:
- **Frontend (Student Interface)**: Go to `http://localhost:3000` in your browser to access the user interface.
- **Backend**: The backend API will be running on `http://localhost:5000`.

## Usage

- **ChatPDF**: Navigate to the "ChatPDF" section, upload your PDF, and start asking questions. The bot will process the content and give relevant answers.
  
- **Expense Tracker**: Upload a receipt or bill, and the bot will automatically analyze and summarize the details for you.

- **Image Visualizer**: Upload any image, and the bot will analyze the contents, providing you with a name and description of the image.

- **Chatbot**: Use the chatbot to ask questions about your studies, academic challenges, or general inquiries. It's designed to assist you with various tasks related to student life.

## Contributing

We welcome contributions from the community. If you have an idea to improve the project or wish to add a new feature, feel free to fork the repo and submit a pull request. If you find any issues, please open an issue to discuss them.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or questions, please feel free to contact Rahil Ahmed at [rahilahmed1720@gmail.com](mailto:rahilahmed1720@gmail.com).

