# Theoretical Computer Science @ Lancaster

Institutional website for a research group in theoretical computer science. The application presents information about the group, including people, research areas, seminars, news, and academic opportunities.

## General Description

This project is a lightweight web application developed in **Python** using **Flask**. The content is rendered on the server through HTML templates, while part of the site information is managed from a `JSON` file.

The goal of the project is to provide a website that is simple to maintain, easy to deploy, and suitable for academic and institutional content.

## Technologies Used

* **Python** as the main programming language.
* **Flask** as the web framework.
* **Jinja2** for rendering dynamic HTML templates.
* **HTML5** for page structure.
* **CSS3** for custom styles.
* **Bootstrap 5** for responsive layout and visual components.
* **JSON** to store part of the site content.
* **Vercel** as the configured deployment platform.

## Project Structure

```text
research-site-/
├── app.py
├── data.json
├── requirements.txt
├── vercel.json
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── people.html
│   ├── research.html
│   ├── seminars.html
│   └── opportunities.html
```

## How It Works

The `app.py` file defines the Flask application, loads the data from `data.json`, registers the routes, and renders the corresponding views.

The site templates are located in `templates/` and share a common base structure. Static resources, such as stylesheets and images, are stored in `static/`.

## Site Sections

The site includes the following main sections:

* **Home**
* **People**
* **Research**
* **Seminars**
* **Opportunities**

## Content Management

Part of the content is maintained in `data.json`, allowing site information to be updated without directly modifying the main application logic.

The managed data includes:

* general information about the group
* recent news
* people
* research topics
* seminars

## Deployment

The project includes a `vercel.json` file, so it is prepared to be deployed on **Vercel** with support for Python applications.

## Local Execution

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python app.py
```
