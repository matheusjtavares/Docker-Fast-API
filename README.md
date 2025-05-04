# 🚀 Dockerized ETL Pipeline with FastAPI & PostgreSQL

This project demonstrates a containerized ETL (Extract, Transform, Load) pipeline using FastAPI, PostgreSQL, and Docker. It simulates data acquisition, processing, and loading between source and target databases, providing a robust foundation for scalable data engineering workflows.

## 🧰 Tech Stack

- **FastAPI**: High-performance web framework for building APIs.
- **PostgreSQL**: Relational database for both source and target data storage.
- **Docker & Docker Compose**: Containerization and orchestration of services.
- **PgAdmin4**: Web-based PostgreSQL database management tool.
- **Python**: Scripting for ETL processes.

## 📁 Project Structure

```
├── app/                      # FastAPI application
├── etl/                      # ETL scripts
├── .env                      # Environment variables
├── Dockerfile                # Docker image for FastAPI
├── docker-compose.yml        # Docker Compose configuration
├── entrypoint.sh             # Entry point script
├── init.sql                  # SQL script to initialize source DB
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## ⚙️ Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/matheusjtavares/ETL-Postgres-FastAPI.git
   cd ETL-Postgres-FastAPI
   ```

2. **Build and Start Services**:

   ```bash
   docker-compose build
   docker-compose up -d
   ```

   This will set up the following services:
   - FastAPI application accessible at `http://localhost:80`
   - Source PostgreSQL database at `localhost:5432`
   - Target PostgreSQL database at `localhost:5433`
   - PgAdmin4 interface at `http://localhost:5000`

3. **Initialize Target Database**:

   ```bash
   docker-compose run python-app python etl/create_db.py
   ```

   This script sets up the target database schema.

4. **Run ETL Process**:

   ```bash
   docker-compose run python-app python etl/etl_process.py
   ```

   This script extracts data from the source database, transforms it as needed, and loads it into the target database.

## 📊 Data Simulation

- The source database is populated with randomized data ranging from 2024-05-01 to 2024-05-10, as defined in `init.sql`.
- The ETL process can be customized by modifying the parameters in `etl_process.py` to handle different variables or date ranges.

## 🧪 Testing the API

Once the services are up and running, you can access the FastAPI documentation at:

```
http://localhost:80/docs
```

This interactive interface allows you to test API endpoints and view the available operations.

## 📌 Key Features

- **Modular Design**: Separation of concerns between API, ETL processes, and database configurations.
- **Containerization**: Simplified deployment and scalability using Docker.
- **Data Management**: Efficient handling of data extraction, transformation, and loading between databases.
- **User Interface**: PgAdmin4 provides a user-friendly interface for database management.

## 👨‍💻 Author

- **Matheus Tavares**  
  - GitHub: [@matheusjtavares](https://github.com/matheusjtavares)  
  - LinkedIn: [Matheus Tavares](https://www.linkedin.com/in/matheusjtavares/)  

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
