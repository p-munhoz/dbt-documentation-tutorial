# dbt Documentation Best Practices Example

This repository contains the example code and documentation referenced in the article [Level Up Your dbt Docs: Best Practices for Clearer Data Lineage & Team Clarity](https://p-munhoz.github.io/blog/dbt/dbt-documentation-best-practices).

## Overview

This repository demonstrates best practices for documenting dbt models, sources, and transformations. It serves as a practical example of how to create comprehensive, meaningful documentation that improves team collaboration and data understanding.

## Repository Structure

```
dbt_project/
├── models/
│   ├── staging/
│   │   ├── shopify/
│   │   │   ├── _shopify_models.yml
│   │   │   ├── _shopify_sources.yml
│   │   │   └── stg_orders.sql
│   │   └── google_ads/
│   │       ├── _google_ads_models.yml
│   │       ├── _google_ads_sources.yml
│   │       └── stg_clicks.sql
│   ├── intermediate/
│   │   ├── _intermediate_models.yml
│   │   └── int_orders_with_ads.sql
│   └── marts/
│       └── marketing/
│           ├── _mart_marketing_models.yml
│           └── fct_revenue_by_campaign.sql
├── docs/
│   └── [documentation markdown files]
└── dbt_project.yml
```

## Key Documentation Features Demonstrated

1. **Source Documentation**
   - Detailed source descriptions
   - Data loading information
   - Column-level documentation
   - Data type specifications
   - Data quality tests

2. **Model Documentation**
   - Clear transformation descriptions
   - Business purpose explanations
   - Comprehensive metadata
   - Data lineage information
   - Performance SLAs

3. **Column Documentation**
   - Reusable doc blocks
   - Data type specifications
   - Business rules
   - Data quality tests
   - Format validations

4. **Metadata and Tags**
   - Owner information
   - Refresh frequencies
   - PII indicators
   - Business impact levels
   - Related dashboards

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/p-munhoz/dbt-documentation.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add the dbt_project information in the profiles.yml

4. Generate the data in the `Duckdb` database by executing the `ingestion.py` Python script

5. Run dbt:
   ```bash
   dbt run
   ```

6. Generate and view documentation:
   ```bash
   dbt docs generate
   dbt docs serve
   ```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 