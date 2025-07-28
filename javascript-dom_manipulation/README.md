# JavaScript DOM Manipulation

This project demonstrates various JavaScript DOM manipulation techniques through 8 practical tasks. Each task focuses on different aspects of DOM manipulation, event handling, and API integration.

## Learning Objectives

At the end of this project, you will be able to explain to anyone, without the help of Google:

### General
- How to select HTML elements in JavaScript
- What are differences between ID, class and tag name selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a request with XmlHTTPRequest
- How to make a request with Fetch API
- How to listen/bind to DOM events
- How to listen/bind to user events

## Technologies Used

- **JavaScript (ES6+)**
- **HTML5**
- **CSS3**
- **Fetch API**
- **DOM Manipulation**
- **Event Handling**

## Project Structure

```
javascript-dom_manipulation/
├── 0-script.js          # Color Me - Basic DOM selection
├── 1-script.js          # Click and turn red - Event listeners
├── 2-script.js          # Add .red class - CSS class manipulation
├── 3-script.js          # Toggle classes - Class switching
├── 4-script.js          # List of elements - Dynamic element creation
├── 5-script.js          # Change the text - Content modification
├── 6-script.js          # Star Wars character - Fetch API (single item)
├── 7-script.js          # Star Wars movies - Fetch API (multiple items)
├── 8-script.js          # Say Hello! - Fetch API with DOMContentLoaded
└── README.md            # This file
```

## Tasks Overview

### Task 0: Color Me
- **File:** `0-script.js`
- **Objective:** Change header text color to red using `document.querySelector`
- **Key Concepts:** DOM selection, style manipulation
- **Technique:** Direct style modification

### Task 1: Click and turn red
- **File:** `1-script.js`
- **Objective:** Change header color to red only when clicking on `red_header` element
- **Key Concepts:** Event listeners, click events
- **Technique:** Event-driven DOM manipulation

### Task 2: Add `.red` class
- **File:** `2-script.js`
- **Objective:** Add CSS class `red` to header when clicking on `red_header`
- **Key Concepts:** CSS classes, classList manipulation
- **Technique:** Class-based styling

### Task 3: Toggle classes
- **File:** `3-script.js`
- **Objective:** Toggle between `red` and `green` classes on header
- **Key Concepts:** Class toggling, conditional logic
- **Technique:** Dynamic class switching

### Task 4: List of elements
- **File:** `4-script.js`
- **Objective:** Add new `<li>` elements to a list when clicking `add_item`
- **Key Concepts:** Dynamic element creation, appendChild
- **Technique:** DOM element generation

### Task 5: Change the text
- **File:** `5-script.js`
- **Objective:** Update header text to "New Header!!!" when clicking `update_header`
- **Key Concepts:** Content modification, textContent
- **Technique:** Text content manipulation

### Task 6: Star Wars character
- **File:** `6-script.js`
- **Objective:** Fetch and display Star Wars character name using Fetch API
- **Key Concepts:** Fetch API, JSON parsing, async operations
- **Technique:** API integration

### Task 7: Star Wars movies
- **File:** `7-script.js`
- **Objective:** Fetch and list all Star Wars movie titles
- **Key Concepts:** Array iteration, dynamic list creation
- **Technique:** Multiple element generation from API data

### Task 8: Say Hello!
- **File:** `8-script.js`
- **Objective:** Fetch translation and display "hello" in French
- **Key Concepts:** DOMContentLoaded, error handling, fallbacks
- **Technique:** Script loading from head tag

## How to Run

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd javascript-dom_manipulation
   ```

2. **Start a local server:**
   ```bash
   python3 -m http.server 8000
   ```

3. **Open in browser:**
   - Navigate to `http://localhost:8000`
   - Test each task using the provided HTML files

## Requirements

### General
- Allowed editors: All of them
- Files will be interpreted on Chrome browser (version 57.0 or later)
- All files should end with a new line
- Code should be semistandard compliant
- You are not allowed to use `var`
- HTML should not reload for each action: DOM manipulation, update values, fetch data

### Code Style
- Use `const` and `let` instead of `var`
- Follow semistandard JavaScript style
- Include meaningful comments
- Use proper error handling

## Technical Concepts Covered

### DOM Selection Methods
- `document.querySelector()` - Select first element matching CSS selector
- `document.getElementById()` - Select element by ID
- `document.querySelectorAll()` - Select all elements matching selector

### Event Handling
- `addEventListener()` - Attach event listeners
- Click events, DOM events
- Event delegation patterns

### DOM Manipulation
- `element.style.property` - Direct style modification
- `element.classList.add()` - Add CSS classes
- `element.classList.remove()` - Remove CSS classes
- `element.classList.toggle()` - Toggle CSS classes
- `element.textContent` - Modify text content
- `element.innerHTML` - Modify HTML content

### Element Creation
- `document.createElement()` - Create new elements
- `element.appendChild()` - Add child elements
- Dynamic DOM generation

### API Integration
- Fetch API for HTTP requests
- JSON parsing and handling
- Async/await patterns
- Error handling for network requests

### Advanced Concepts
- `DOMContentLoaded` event
- Promise chaining
- Error handling with try/catch
- Fallback mechanisms

## Learning Path

This project follows a progressive learning path:

1. **Basic DOM Selection** (Task 0-1)
2. **Event Handling** (Task 1-3)
3. **CSS Class Manipulation** (Task 2-3)
4. **Dynamic Element Creation** (Task 4)
5. **Content Modification** (Task 5)
6. **API Integration** (Task 6-8)
7. **Advanced Patterns** (Task 8)

## Debugging Tips

- Use browser developer tools (F12)
- Check console for JavaScript errors
- Verify network requests in Network tab
- Test API endpoints with curl or Postman
- Validate HTML structure

## Resources

- [MDN Web Docs - DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
- [MDN Web Docs - Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [JavaScript.info - DOM Manipulation](https://javascript.info/dom-navigation)
- [Star Wars API](https://swapi.dev/)
- [Hello API](https://hellosalut.stefanbohacek.dev/)

## Author

**Javier Valenzani** - Holberton School

## License

This project is part of the Holberton School curriculum.

---

**Happy coding!**