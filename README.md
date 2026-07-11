# Personal Portfolio Website – Flask

A personal portfolio website built with Flask, showcasing my info, skills, projects, and a working contact form.

## Tools
- Python 3
- Flask
- HTML / CSS
- Jinja2 (Flask's templating engine)

## Features
- Home page with dynamic content rendered via Jinja2 templates
- Skills and projects displayed using Jinja2 loops
- Contact page with a working form (GET/POST handling)
- Custom CSS styling
- Flask routing for multiple pages

## Project Structure
portfolio-flask/
├── app.py
├── templates/
│   ├── index.html
│   └── contact.html
├── static/
│   └── style.css
└── README.md

## How to Run
```bash
pip install flask
python app.py
```
Then open http://127.0.0.1:5000/ in your browser.

## Key Concepts
Flask routing, Jinja2 templating, render_template(), static files, HTML forms, GET vs POST.
