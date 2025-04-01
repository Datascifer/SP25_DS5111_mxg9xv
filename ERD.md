erDiagram
    INSTRUMENTS {
        string symbol PK
        string company_name
        string sector
    }

    RAW_DAILY_GAINERS {
        string symbol PK
        date   gainer_date PK
        float  price
        float  change_percent
        float  volume
    }

    RAW_CANDLESTICK {
        string symbol PK
        date   trading_date PK
        float  open
        float  high
        float  low
        float  close
        float  volume
    }

    INTERMEDIATE_GAINERS {
        string symbol PK
        date   gainer_date PK
        int    frequency_in_gainers
        float  avg_price
    }

    INTERMEDIATE_CANDLESTICK {
        string symbol PK
        date   trading_date PK
        float  average_close_price
        float  total_volume
    }

    FINAL_REPORT {
        string symbol PK
        date   week_ending PK
        int    total_appearances
        float  average_volume
        float  average_close_price
    }

    %% Relationships
    INSTRUMENTS ||--o{ RAW_DAILY_GAINERS : "symbol lookup"
    INSTRUMENTS ||--o{ RAW_CANDLESTICK    : "symbol lookup"

    RAW_DAILY_GAINERS }|--|| INTERMEDIATE_GAINERS : aggregates
    RAW_CANDLESTICK }|--|| INTERMEDIATE_CANDLESTICK : transforms

    INTERMEDIATE_GAINERS }|--|| FINAL_REPORT : merges
    INTERMEDIATE_CANDLESTICK }|--|| FINAL_REPORT : merges 


This ERD outlines the transformation of raw CSV data on daily stock gainers and candlestick information into aggregated intermediate tables and a final report. The schema separates raw data—stored in the `RAW_DAILY_GAINERS` and `RAW_CANDLESTICK` tables—from the derived datasets. Each raw table uses composite keys (combining `symbol` with a date attribute) to uniquely identify records, while the intermediate tables (`INTERMEDIATE_GAINERS` and `INTERMEDIATE_CANDLESTICK`) aggregate metrics such as frequency, average price, average closing price, and total volume. The final report merges these intermediate results to provide a weekly overview that includes total appearances, average trading volume, and average closing price, ensuring data traceability and facilitating clear joins.

The design supports several use cases: analyzing recurring symbols to identify trending stocks; assessing price and volume distributions through aggregated data for market trend evaluations; and summarizing weekly trends for non-technical stakeholders. Data is ingested from CSV files, transformed via SQL (using DBT), and stored in intermediate tables before being merged into the final report. This approach ensures modularity, ease of maintenance, and flexibility for future enhancements, while directly addressing key questions central to the project’s goals.
