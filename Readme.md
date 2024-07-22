
# Nirmaan Patient Management System

Nirmaan is a comprehensive patient management system designed to streamline the process of adding, editing, and managing patient records. This web application leverages Django, Bootstrap, and other modern technologies to provide an efficient and user-friendly interface for healthcare professionals.

## Table of Contents

* [Features](#features)
* [Technologies Used](#technologies-used)
* [Setup and Installation](#setup-and-installation)
* [Usage](#usage)
* [Responsive Design](#responsive-design)
* [License](#license)

## Features

* **Add Patient** : Easily add new patient records with comprehensive details including personal information, representative details, declarations, and more.
* **Edit Patient** : Update existing patient records with new information.
* **Responsive Design** : Fully responsive interface that works seamlessly on both desktop and mobile devices.
* **Dark Mode** : Toggle between light and dark themes for better usability and user preference.
* **Webcam Integration** : Capture patient photos directly from the webcam and upload them as part of the patient record.
* **Dynamic Form Management** : Add, edit, and remove multiple form sections such as items belonging to patients, temporary releases, and judicial proceedings.

## Technologies Used

* **Backend** : Django
* **Frontend** : Bootstrap, HTML, CSS, JavaScript
* **Icons** : Font Awesome
* **Libraries** : jQuery

## Setup and Installation

1. **Clone the repository:**

   <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><div class="flex items-center"><span class="" data-state="closed"></span></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git clone https://github.com/Abinash-Sinha/Nirmaan.git
   cd Nirmaan
   </code></div></div></pre>
2. **Create a virtual environment:**

   <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   </code></div></div></pre>
3. **Install dependencies:**

   <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><div class="flex items-center"><span class="" data-state="closed"></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install -r requirements.txt
   </code></div></div></pre>
4. **Apply migrations:**

   <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><div class="flex items-center"><span class="" data-state="closed"></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python manage.py migrate
   </code></div></div></pre>
5. **Run the development server:**

   <pre><div class="dark bg-gray-950 rounded-md border-[0.5px] border-token-border-medium"><div class="flex items-center relative text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md"></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python manage.py runserver
   </code></div></div></pre>
6. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

* **Add Patient** : Navigate to the Add Patient page to fill in the details for a new patient. Use the form to enter information and capture a photo using the webcam if needed.
* **Edit Patient** : Go to the patient list, select a patient, and update their details as necessary.
* **Responsive Design** : The application is designed to work on various devices. Use the navigation bar and other UI elements that adapt to different screen sizes.
* **Dark Mode** : Use the toggle button at the bottom right of the screen to switch between light and dark themes.

## Responsive Design

The navigation bar and other elements of the application are fully responsive. On mobile devices, the navigation bar collapses into a toggleable menu for better usability.

## License

This project is licensed under the MIT License. See the [LICENSE]() file for details.

---

*Developed by Abinash Sinha, a software engineer from Silchar, Assam, with a passion for gaming and sports.*
