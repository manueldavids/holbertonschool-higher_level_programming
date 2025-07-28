# Python Server-Side Rendering Project

This project demonstrates server-side rendering techniques using Python and Flask, with Jinja2 templating engine to create dynamic, efficient, and SEO-friendly web applications.

## Learning Objectives

- Understand server-side rendering concepts and differences from client-side rendering
- Learn the benefits of using server-side rendering in web development
- Implement SSR in Python using the Flask framework
- Utilize Jinja templating engine to dynamically generate HTML pages
- Read and display data from various sources including JSON, CSV, and SQLite databases
- Handle dynamic content and user inputs in web applications

## Project Structure

```
python-server_side_rendering/
├── task_00_intro.py          # Simple templating program
├── task_01_jinja.py          # Basic Flask app with HTML templates
├── task_02_logic.py          # Dynamic templates with loops and conditions
├── task_03_files.py          # Data from JSON and CSV files
├── task_04_db.py             # Extended to include SQLite database
├── create_database.py        # Database creation script
├── templates/                # Jinja2 HTML templates
│   ├── header.html          # Reusable header component
│   ├── footer.html          # Reusable footer component
│   ├── index.html           # Home page template
│   ├── about.html           # About page template
│   ├── contact.html         # Contact page template
│   ├── items.html           # Dynamic items list template
│   └── product_display.html # Product display template
├── products.json            # Sample product data (JSON)
├── products.csv             # Sample product data (CSV)
├── products.db              # SQLite database with products
├── items.json               # Sample items data
└── .gitignore               # Git ignore rules
```

## Tasks Overview

### Task 0: Creating a Simple Templating Program
- Generate personalized invitation files from templates
- Handle placeholders and data substitution
- Implement comprehensive error handling
- File: `task_00_intro.py`

### Task 1: Creating a Basic HTML Template in Flask
- Set up Flask environment and basic application
- Design HTML templates using Jinja2
- Implement reusable components (header/footer)
- Files: `task_01_jinja.py`, `templates/*.html`

### Task 2: Creating a Dynamic Template with Loops and Conditions
- Use Jinja's loop and conditional constructs
- Read and parse JSON data
- Integrate dynamic content into Flask application
- Files: `task_02_logic.py`, `templates/items.html`, `items.json`

### Task 3: Displaying Data from JSON or CSV Files
- Read and parse data from JSON and CSV files
- Use query parameters to determine data sources
- Implement error handling for invalid inputs
- Files: `task_03_files.py`, `products.json`, `products.csv`

### Task 4: Extending Dynamic Data Display to Include SQLite
- Set up and interact with SQLite database
- Extend functionality to handle multiple data sources
- Implement error handling for database-related issues
- Files: `task_04_db.py`, `create_database.py`, `products.db`

## Usage Examples

### Running the Applications

```bash
# Task 0: Simple templating
python3 task_00_intro.py

# Task 1: Basic Flask app
python3 task_01_jinja.py

# Task 2: Dynamic templates
python3 task_02_logic.py

# Task 3: JSON/CSV data sources
python3 task_03_files.py

# Task 4: SQLite database support
python3 task_04_db.py
```

### Creating the Database

```bash
python3 create_database.py
```

### Testing URLs

#### Task 1 URLs:
- `http://localhost:5000/` - Home page
- `http://localhost:5000/about` - About page
- `http://localhost:5000/contact` - Contact page

#### Task 2 URLs:
- `http://localhost:5000/items` - Dynamic items list

#### Task 3 & 4 URLs:
- `http://localhost:5000/products?source=json` - JSON products
- `http://localhost:5000/products?source=csv` - CSV products
- `http://localhost:5000/products?source=sql` - SQLite products
- `http://localhost:5000/products?source=json&id=1` - Filtered by ID

## Key Concepts Learned

### Server-Side Rendering (SSR)
- HTML generation on the server before sending to client
- Better SEO and initial page load performance
- Reduced client-side JavaScript dependency

### Flask Framework
- Lightweight web framework for Python
- Route handling and request processing
- Template rendering with Jinja2

### Jinja2 Templating
- Template inheritance and includes
- Dynamic content rendering
- Loops, conditions, and filters
- Reusable components

### Data Sources
- **JSON**: Structured data format for APIs and configuration
- **CSV**: Tabular data format for spreadsheets and databases
- **SQLite**: Lightweight relational database
- **Query Parameters**: URL-based filtering and data source selection

### Error Handling
- Input validation and type checking
- File not found scenarios
- Invalid data format handling
- User-friendly error messages

## Technologies Used

- **Python 3.x**: Core programming language
- **Flask**: Web framework
- **Jinja2**: Template engine
- **SQLite**: Database
- **JSON/CSV**: Data formats
- **HTML/CSS**: Frontend markup and styling

## Best Practices Implemented

- Separation of concerns (MVC pattern)
- Reusable template components
- Comprehensive error handling
- Input validation and sanitization
- Modular code organization
- Consistent naming conventions

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
- [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)