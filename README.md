# 🚀 End-to-End Data Engineering Project

A complete modern data stack implementation featuring **PostgreSQL → Airbyte → BigQuery → dbt → Dagster** pipeline for e-commerce analytics.

## 📋 Project Overview

This project demonstrates a production-ready data engineering pipeline that:
- **Extracts** data from PostgreSQL using Airbyte
- **Loads** raw data into BigQuery 
- **Transforms** data using dbt with staging and mart layers
- **Orchestrates** the entire pipeline with Dagster
- **Schedules** automated hourly runs

### 🏗️ Architecture

```
PostgreSQL → Airbyte → BigQuery → dbt → Dagster
    ↓           ↓         ↓        ↓       ↓
  Source    Extract   Raw Data  Transform Orchestrate
```

## 📁 Project Structure

```
├── 📂 airbyte/                    # Airbyte connector configurations
│   ├── airbyte-cdk/              # Airbyte Connector Development Kit
│   ├── airbyte-ci/               # CI/CD configurations
│   └── airbyte-integrations/     # Integration templates
├── 📂 dagster_orchestration/     # Dagster orchestration layer
│   ├── dagster_orchestration/
│   │   ├── __init__.py           # Main Dagster definitions
│   │   └── assets/
│   │       └── __init__.py       # Asset definitions (Airbyte + dbt)
│   └── dagster_orchestration_tests/
├── 📂 dbt_transformation/        # dbt transformation layer
│   ├── models/
│   │   ├── staging/              # Staging models
│   │   │   ├── stg_customers.sql
│   │   │   ├── stg_orders.sql
│   │   │   ├── src_big_star_db.yml
│   │   │   └── stg_big_star_db.yml
│   │   └── marts/                # Mart models
│   │       ├── dim_customers.sql
│   │       └── marts_big_star_db.yml
│   ├── config/
│   │   └── profiles.yml          # dbt BigQuery profile
│   └── dbt_project.yml          # dbt project configuration
├── 📄 setup.py                   # Python package dependencies
├── 📄 env.example                # Environment variables template
└── 📄 README.md                  # This file
```

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Source** | PostgreSQL | E-commerce database |
| **EL** | Airbyte | Extract & Load data |
| **Warehouse** | BigQuery | Data warehouse |
| **Transform** | dbt | Data transformations |
| **Orchestrate** | Dagster | Pipeline orchestration |
| **Language** | Python | Backend development |

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL database with e-commerce data
- Google Cloud Platform account with BigQuery
- Airbyte instance running locally

### 1. Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd end-to-end-data-engineering-project-4413618

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -e ".[dev]"
```

### 2. Environment Configuration

```bash
# Copy environment template
cp env.example .env

# Edit .env with your actual values
```

**Required Environment Variables:**
```bash
# dbt Configuration
DBT_PROJECT_DIR=dbt_transformation
DBT_PROFILES_DIR=dbt_transformation/config

# BigQuery Configuration
DBT_BIGQUERY_PROJECT=your-gcp-project-id
DBT_BIGQUERY_DATASET=your_dataset_name
DBT_BIGQUERY_LOCATION=US
DBT_BIGQUERY_KEYFILE_PATH=path/to/your/service-account-key.json

# Airbyte Configuration
AIRBYTE_PASSWORD=your_airbyte_password
```

### 3. Setup Airbyte

1. **Start Airbyte:**
   ```bash
   # Run Airbyte locally (port 8000)
   docker-compose up
   ```

2. **Configure Connections:**
   - Create PostgreSQL source connector
   - Create BigQuery destination connector
   - Set up connection between source and destination

### 4. Setup BigQuery

1. **Create Service Account:**
   - Go to GCP Console → IAM & Admin → Service Accounts
   - Create service account with BigQuery permissions
   - Download JSON key file

2. **Create Dataset:**
   ```sql
   CREATE SCHEMA `your-project.your_dataset` 
   OPTIONS(description="Raw data from Airbyte");
   ```

### 5. Run the Pipeline

```bash
# Start Dagster UI
cd dagster_orchestration
dagster dev
```

Visit `http://localhost:3000` to see your pipeline!

## 📊 Data Models

### Raw Data (BigQuery)
- `customers` - Customer information
- `orders` - Order details
- `products` - Product catalog
- `order_items` - Order line items

### Staging Layer (dbt Views)
- `stg_customers` - Cleaned customer data
- `stg_orders` - Cleaned order data

### Mart Layer (dbt Tables)
- `dim_customers` - Customer dimension with order aggregations

## 🔄 Pipeline Flow

1. **Extract**: Airbyte pulls data from PostgreSQL
2. **Load**: Raw data lands in BigQuery `raw_data` schema
3. **Transform**: dbt creates staging views and mart tables
4. **Orchestrate**: Dagster manages the entire pipeline
5. **Schedule**: Runs automatically every hour

## 🧪 Testing

```bash
# Test dbt models
cd dbt_transformation
dbt test

# Test Dagster assets
cd dagster_orchestration
pytest dagster_orchestration_tests
```

## 📈 Monitoring

- **Dagster UI**: `http://localhost:3000` - Pipeline monitoring
- **BigQuery Console**: Data warehouse inspection
- **Airbyte UI**: `http://localhost:8000` - EL monitoring

## 🔧 Development

### Adding New Models

1. **Staging Model:**
   ```sql
   -- dbt_transformation/models/staging/stg_new_table.sql
   select column1, column2
   from {{ source("raw_data", "new_table") }}
   ```

2. **Mart Model:**
   ```sql
   -- dbt_transformation/models/marts/fact_new_table.sql
   select *
   from {{ ref("stg_new_table") }}
   ```

3. **Update Documentation:**
   ```yaml
   # Add to appropriate .yml file
   models:
     - name: stg_new_table
       columns:
         - name: column1
           tests:
             - not_null
   ```

### Modifying Schedule

Edit `dagster_orchestration/dagster_orchestration/__init__.py`:
```python
big_star_schedule = ScheduleDefinition(
    job=big_star_job,
    cron_schedule="0 9 * * *",  # Daily at 9 AM
)
```

## 🚨 Troubleshooting

### Common Issues

1. **Environment Variables Not Found**
   - Ensure `.env` file exists and is properly configured
   - Check file paths are absolute or relative to project root

2. **BigQuery Authentication Failed**
   - Verify service account JSON key path
   - Check BigQuery permissions for service account

3. **Airbyte Connection Failed**
   - Ensure Airbyte is running on localhost:8000
   - Verify PostgreSQL connection details

4. **dbt Profile Not Found**
   - Check `profiles.yml` configuration
   - Verify environment variables are set

## 📚 Resources

- [Dagster Documentation](https://docs.dagster.io/)
- [dbt Documentation](https://docs.getdbt.com/)
- [Airbyte Documentation](https://docs.airbyte.com/)
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Acknowledgments

- Based on LinkedIn Learning course by Thalia Barrera
- Modern Data Stack community
- Open source contributors

---

**Happy Data Engineering! 🎉**