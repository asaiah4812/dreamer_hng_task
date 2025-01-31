# LakeView College Management System 🎓

A modern and comprehensive web-based college management system built with Django and Tailwind CSS. This system streamlines academic operations including student management, course registration, fee payments, and staff administration.

![LakeView College](static/assets/images/logos/lakeview.jpg)

## ✨ Key Features

### For Students 👨‍🎓
- Course registration and management
- School fees payment via Paystack
- Academic records and transcripts
- Personal profile management
- Timetable view
- Digital payment receipts

### For Staff 👨‍🏫
- Course creation and management
- Student records administration
- Department-wise student tracking
- Academic performance monitoring
- Staff profile management

### System Features 🛠
- Role-based authentication (Student/Staff)
- Secure payment integration
- Responsive design
- Real-time updates
- Document management
- Automated notifications

## 🚀 Technology Stack

- **Backend**: Django 5.1
- **Frontend**: 
  - Tailwind CSS
  - HTML5/JavaScript
  - Alpine.js
- **Database**: SQLite/PostgreSQL
- **Payment**: Paystack Integration
- **Cloud Storage**: AWS S3 (optional)

## 📋 Prerequisites

- Python 3.8+
- Node.js and npm
- Git
- Paystack Account

## ⚙️ Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/lakeview-college.git
cd lakeview-college
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
cp .env.example .env
# Update .env with your configurations
```

5. Run migrations
```bash
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Start development server
```bash
python manage.py runserver
```


## 📞 Contact & Support

For support or queries:
- Email: hensonasaiah21@gmail.com
- Website: hensonport.vercel.app
- Twitter: https://x.com/dreamer_webdev

---
Made with ❤️ by DreamerWebdev