# Search Suggestion Engine for Archived Content

A project designed to provide **real-time search suggestions** for content archived by the [Wayback Machine](https://archive.org/web/). By utilizing Elasticsearch for fast querying and prefix matching, this engine delivers dynamic, relevant search results based on historical web data. The system can be extended and customized for various types of archival data.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: For the backend and Elasticsearch integration.
- **Docker**: To run Elasticsearch locally.
- **Git**: To clone the repository and manage contributions.

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/YOUR_USERNAME/search-suggest-archive.git
    cd search-suggest-archive
    ```

2. **Set up the virtual environment (optional but recommended)**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Elasticsearch using Docker**:

    You can launch Elasticsearch using Docker by running the following command:

    ```bash
    docker-compose up -d
    ```

    This will start Elasticsearch on `http://localhost:9200`.

5. **Create the Elasticsearch index**:

    Run the following command to create the index in Elasticsearch with the necessary mappings and analyzers:

    ```bash
    python elasticsearch/create_index.py
    ```

6. **Load data into Elasticsearch**:

    The data can either be **mocked search logs** or **archived web titles** (using the Wayback Machine). You can load these into Elasticsearch by running the following script:

    ```bash
    python scripts/index_data.py
    ```

7. **Start the backend (Flask)**:

    Start the Flask backend which serves the search suggestions:

    ```bash
    python backend/suggest.py
    ```

    This will run the backend locally on `http://localhost:5000`.

8. **Test the Suggestion Endpoint**:

    Open your browser or use `curl` to test the search suggestions:

    ```
    http://localhost:5000/suggest?q=clim
    ```

    The response should return a list of search suggestions based on the query.

---

## Project Structure

Here’s a breakdown of the project structure:

search-suggest-archive/ ├── backend/ # Backend code for API │ ├── suggest.py # Flask API for handling search suggestions │ ├── elastic_client.py # Helper to handle Elasticsearch connections │ └── utils.py # Optional utilities (e.g., logging, data formatting) ├── config/ # Configuration files │ ├── settings.py # Config settings for Elasticsearch and more │ └── logging.conf # Optional: logging configuration ├── data/ # Data files (CSV or JSON) │ ├── mock_search_logs.csv # Example of search query logs │ ├── archived_titles.csv # List of archived web page titles │ └── sample_output.json # Sample output to test the suggestions ├── elasticsearch/ # Elasticsearch index configuration │ ├── create_index.py # Python script to create Elasticsearch index │ ├── index_config.json # Elasticsearch index settings and mappings │ └── analyzer.json # Optional: custom analyzer configuration ├── scripts/ # Data preprocessing and loading scripts │ ├── load_data.py # Script to scrape or prepare data │ ├── index_data.py # Script to index data into Elasticsearch │ ├── test_query.py # Test query script to verify index functionality │ └── validate_data.py # Data cleaning/formatting script ├── ui/ # Optional: Frontend for search suggestions │ ├── index.html # Simple HTML page for testing suggestions │ ├── app.js # JS to interact with the backend API │ └── style.css # Optional: styling for the frontend ├── .env # Environment variables (e.g., port, ES URL) ├── .gitignore # Git ignore file ├── docker-compose.yml # Docker config to launch Elasticsearch ├── requirements.txt # Python dependencies └── README.md # Project documentation


---

## How It Works

1. **Data Indexing**: We use Elasticsearch for indexing and searching archived web data. The system uses **edge n-gram** tokenization for efficient autocomplete suggestions, which is optimal for prefix-based matching.
   
2. **Backend API**: The backend is built using **Flask**, which serves a simple API (`/suggest`) that accepts a query and returns search suggestions based on the indexed data.

3. **Frontend UI** (optional): A basic frontend interface is available where users can input a search query, and the engine provides suggestions in real-time. It uses plain HTML and JavaScript to fetch data from the backend.

---

## Contributing

We welcome contributions from the community! If you would like to contribute, please follow these steps:

1. **Fork the repository** and create your branch (`git checkout -b feature-name`).
2. **Make changes** to the codebase — feel free to work on bugs, features, or improvements!
3. **Write tests** for any new code to ensure the stability of the project.
4. **Submit a Pull Request** with a clear explanation of your changes.

### Good First Issues
Look out for issues labeled **good first issue** — they're a great starting point for new contributors.

### Code Style

- Follow **PEP 8** for Python code style.
- For Elasticsearch mappings, keep the structure clear and modular.
- Use **descriptive commit messages** to explain changes.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Additional Resources

- [Elasticsearch Documentation](https://www.elastic.co/guide/en/elasticsearch/reference/index.html)
- [Wayback Machine API](https://web.archive.org/help/)

