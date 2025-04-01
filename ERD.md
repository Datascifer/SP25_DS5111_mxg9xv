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
