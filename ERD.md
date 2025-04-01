erDiagram
    RAW_DAILY_GAINERS ||--o{ INTERMEDIATE_GAINERS : aggregates
    RAW_CANDLESTICK ||--o{ INTERMEDIATE_CANDLESTICK : transforms
    INTERMEDIATE_GAINERS }|--|| FINAL_REPORT : merges
    INTERMEDIATE_CANDLESTICK }|--|| FINAL_REPORT : merges
    INSTRUMENTS ||--o{ RAW_DAILY_GAINERS : "symbol lookup"
    INSTRUMENTS ||--o{ RAW_CANDLESTICK : "symbol lookup"

    INSTRUMENTS {
        string symbol PK
        string company_name
        string sector
        ...
    }

    RAW_DAILY_GAINERS {
        string symbol FK
        date   gainer_date
        float  price
        float  change_percent
        float  volume
        PK (symbol, gainer_date)
    }

    RAW_CANDLESTICK {
        string symbol FK
        date   trading_date
        float  open
        float  high
        float  low
        float  close
        float  volume
        PK (symbol, trading_date)
    }

    INTERMEDIATE_GAINERS {
        string symbol
        date   gainer_date
        int    frequency
        float  avg_price
        PK (symbol, gainer_date)
    }

    INTERMEDIATE_CANDLESTICK {
        string symbol
        date   trading_date
        float  avg_close_price
        float  total_volume
        PK (symbol, trading_date)
    }

    FINAL_REPORT {
        string symbol
        date   week_ending
        int    total_appearances
        float  average_volume
        float  average_close_price
        PK (symbol, week_ending)
    } 
