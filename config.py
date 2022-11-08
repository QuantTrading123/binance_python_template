from decimal import Decimal

class Two_symbol_Config:
    # Target symbol is where the LIMIT orders are placed based on calculated spreads.
    TARGET_SYMBOL = "ATOMUSDT"

    # Reference symbol is where the MARKET orders are intiated AFTER target symbol's limit orders are filled.
    REFERENCE_SYMBOL = "ETHUSDT"

    # Reference symbol is where the MARKET orders are intiated AFTER target symbol's limit orders are filled.

    OPEN_THRESHOLD = 100

    STOP_LOSS_THRESHOLD =100
    # Window size for calculating spread mean.
    MA_WINDOW_SIZE = 100
    
    RETRY_TIME = 1
    
    PRECISION_AMOUNT_REF = Decimal('0.000')
    
    PRECISION_PRICE_REF = Decimal('0.00')
    
    
    PRECISION_AMOUNT_TARGET = Decimal('0.00')
    
    PRECISION_PRICE_TARGET = Decimal('0.000')
    
    SLIPPAGE = 0.001
    TEST_SECOND = 600
    