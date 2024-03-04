# GitHub Starred Repositories

This application allows user's to login to their GitHub account and retrieve their starred repositories.

## Features

- User authentication via GitHub OAuth
- Fetches and displays a user's starred repositories
- Displays relevant data for each starred repository: name, description, URL, license (if exists), and topics
- Filters out private repositories

## Setup Instructions

### Prerequisites

- Python 3.x
- Clone this repository to your local machine: `git clone <repository-url>` then `cd <repository-directory>`.
- Install required packages using `pip install -r requirements.txt`.

### Configuration

1. Create a new OAuth application in your GitHub account settings.
2. Set the `ID`, `SECRET`, and `REDIRECT` variables in `main.py` to match your OAuth application credentials.
3. Ensure that the redirect URI matches the one specified in your OAuth application settings.

### Running the Application

1. Run the FastAPI application using `uvicorn main:app --reload`.
2. Access the application in your web browser at `http://127.0.0.1:8000/`.

### Testing

- Run tests using `pytest`.
- Ensure that all tests pass before deploying the application.

### Deployment

- Deploy the application to your desired hosting platform.
- Ensure that OAuth credentials are securely stored and not exposed in your codebase.

## API Endpoints

- `/`: Home page with a link to authenticate with GitHub.
- `/callback`: Endpoint to handle GitHub OAuth callback and display user's starred repositories.

## Technology Stack

- FastAPI: Python web framework for building APIs.
- Requests: HTTP library for making requests to the GitHub API.
- HTML/CSS: Frontend templates for rendering the UI.
- pytest: Testing framework for unit testing.

## Contributors

- [Matilda Stendahl](https://github.com/matildastendahl)
