# SnapStudio Booking System

## Project Overview
SnapStudio is a Django-based web application for booking photography and videography services. Users can browse available services, book sessions, manage their profile, and submit feedback for completed bookings. Admins can manage services, view user bookings, and moderate feedback.

## Screenshots / Logo
![logo](.\images\snapstudio.png)(C:\Users\user\Downloads\snapstudio-logo.png)


## Features
- Browse available photography and videography services

- Book a service with date and time selection

- View booking history (personal bookings for users, all bookings for admin)

- View feedback submitted by other users for completed services

- Manage user profiles: update information or delete accounts

- Submit feedback for completed bookings

- Admin can manage services: add, update, or delete

- Admin can change booking status to Completed or Cancelled

- Admin can moderate feedback: mark as featured to display on the homepage or delete feedback

- Admin can manage users: view all users and delete accounts

## Technology Stack
**Backend:**  
- Python 3.x  
- Django 5.x (framework for server, routing, models, and authentication)  

**Database:**  
- SQLite (default for Django development)  
- PostgreSQL (optional, if using `psycopg2`)  

**Frontend:**  
- HTML5, CSS3  
- JavaScript (optional for dynamic features)  
- Font Awesome (icons)  

**Other Libraries / Tools:**  
- Pillow (for handling image uploads)  
- Django forms and templates (for dynamic rendering and validation)  
- Git (version control)


## Installation & Setup

Follow these steps to run SnapStudio locally:

### 1. Clone the repository

`
git clone https://git.generalassemb.ly/aya/SnapStudio-booking.git
cd SnapStudio-booking`

### 2. Create a virtual environment (recommended)


python -m venv venv
### 3. Activate the virtual environment
Windows (PowerShell):
`.\venv\Scripts\Activate.ps1`
Windows (CMD):

`.\venv\Scripts\activate`
Mac/Linux:
`source venv/bin/activate`
### 4. Install required packages
bash

`pip install -r requirements.txt`
### 5. Apply migrations

`python manage.py migrate`
### 6. Create a superuser (optional, for admin access)

`python manage.py createsuperuser`
### 7. Run the development server


`python manage.py runserver`
### 8. Open the app
Go to http://127.0.0.1:8000 in your browser.

## ERD & User Stories

![ERd](.\images\ERD(dark).png)
![ERd](.\images\ERD(light).png)
### User story:

- Browse available photography & videography services.

- Book a service with date & time selection.

- View personal booking history; admin can view all bookings.

- Manage user profile (update information, delete account).

- Submit feedback for completed bookings.

### Admin story:

- Manage all services: add, update, or delete.

- View all user bookings and booking details.

- Change booking status to Completed or Cancelled.

- Moderate feedback: mark feedback to show on homepage or delete feedback.

- Manage users: view all users and delete accounts.

## Challenges Encountered & Solutions

- **Booking Status Management**  
  Ensuring bookings could be updated by the admin (Scheduled → Completed / Cancelled) required careful access control.  
  **Solution:** Implemented a dedicated `update_booking_status` view using `@user_passes_test(lambda u: u.is_staff)` for function-based views, and `LoginRequiredMixin + UserPassesTestMixin` for class-based views, allowing only staff/admin users to safely change booking status.

- **Preventing Duplicate Feedback**  
  Users could submit feedback multiple times for the same booking.  
  **Solution:** Overrode `dispatch()` in `FeedbackCreateView` to check if feedback already exists for the booking. If it does, the user is redirected with a friendly message.

- **Featured Feedback for Homepage**  
  Admins needed a way to highlight certain feedback dynamically.  
  **Solution:** Added a `featured` boolean field to the `Feedback` model and created a `feature_feedback` view to toggle which feedback appears on the homepage.

## Future Enhancements
## Future Enhancements

- **Payment Integration:** Allow users to pay for bookings directly through the platform and confirm bookings after payment.  
- **Advanced Booking Management:** Enable admin to filter bookings by status, date, or user for easier management.  
- **Flexible Homepage for Admin:** Allow admin to update homepage content dynamically, such as headings, featured sections, or promotional banners.  
- **User Booking Management:** Allow users to cancel or delete their own bookings before the scheduled date.  
- **Improved Styling:** Refactor and clean up CSS to make the UI more consistent, modern, and responsive.  
- **Optimized Frontend:** Reduce redundant CSS, organize stylesheets, and improve layout for better user experience.  


## Attributions
None.
