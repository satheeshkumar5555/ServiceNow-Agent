# ServiceNow Incident Management Assistant

A Python-based command-line application that integrates with the ServiceNow REST API to perform common Incident Management operations.

This project was built as a hands-on learning exercise to understand:
- REST APIs
- HTTP methods (GET, POST, PATCH)
- Python
- ServiceNow Table API
- Building reusable API clients
- Preparing tools for future LLM integration

---

## Features

✅ Create Incident

✅ View Incident

✅ Update Incident
- Short Description
- Description
- Urgency

✅ Add Work Notes

✅ Add Customer Comments

✅ Resolve Incident
- Resolution Code Selection
- Resolution Notes

✅ Close Incident

✅ Input Validation

✅ Reusable PATCH implementation

---

## Project Structure

```
app.py
config.py
servicenow_client.py
requirements.txt
README.md
```

---

## Technologies

- Python
- requests
- ServiceNow Table API

---

## REST APIs Used

| Operation | Method |
|-----------|--------|
| Create Incident | POST |
| View Incident | GET |
| Update Incident | PATCH |

---

## Learning Outcomes

During this project I learned:

- Python fundamentals
- Object-Oriented Programming
- REST API integration
- JSON payload construction
- HTTP request handling
- Error handling
- ServiceNow Incident lifecycle
- Designing reusable API functions

---

## Future Enhancements

- Retrieve Resolution Codes dynamically
- Search incidents
- Delete incidents (optional)
- Attachment support
- Authentication improvements
- LLM / AI Agent integration