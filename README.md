# Gym Management System

## Overview
The **Gym Management System** is a web-based application designed to streamline gym operations by digitalizing member management, billing, notifications, and workout tracking. This system provides a seamless experience for gym owners, administrators, and members.

## Features

### **Admin Dashboard**
- Manage fee packages (add, delete).
- Enroll and manage gym members.
- Create and manage billing for members.
- Send notifications to members.
- View and manage payment statuses.

### **Member Dashboard**
- View personal notifications.
- View and manage billing details.
- Access workout plans and schedules.

### **Authentication**
- Login and signup with username and password.
- Google OAuth integration for easy login.


## Tech Stack

### **Frontend**
- **React.js**: Component-based UI development.
- **React Router**: For routing and navigation.
- **React Icons**: For icons and visual enhancements.


### **API**
- **Django REST Framework**: Backend API for managing members, fee packages, and billing.


## Installation & Setup

### Steps
1. **Clone the Repository**
   ```sh
   git clone https://github.com/MichelN5/Gym_management_final.git
   ```

2. **Install Dependencies**
   ```sh
   npm install
   ```


4. **Set Up Environment Variables**
   - Create a `.env` file in the root directory:
     ```env
     VITE_API_URL="http://127.0.0.1:8000/"
     ```

5. **Run the Application**
   ```sh
   npm run dev
   ```

6. **Backend Setup**
   - Ensure the Django backend is running at `http://127.0.0.1:8000/`.

## Usage

### Admin Features
- Navigate to `/admin` to access the admin dashboard.
- Manage fee packages, members, payments, and notifications.

### Member Features
- Navigate to `/dashboard` to access the member dashboard.
- View notifications, bills, and workout plans.

## Scripts

- **Start Development Server**: `npm run dev`
- **Build for Production**: `npm run build`
- **Preview Production Build**: `npm run preview`
- **Lint Code**: `npm run lint`

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, reach out to [naoussmichel20005@gmail.com](mailto:naoussmichel20005@gmail.com).