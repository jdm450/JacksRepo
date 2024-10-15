from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt

def plot_moving_averages(ticker, term):
    end_date = datetime.now()
    
    # Set start_date based on term
    if term == '1':
        start_date = '2024-01-01'
    elif term == '2':
        start_date = '2023-01-01'
    elif term == '3':
        start_date = '2021-01-01'
    elif term == '4':
        start_date = '2018-01-01'
    else:
        print("Invalid term. Please choose '1' for short, '2' for medium, '3' for long, or '4' for all da colors.")
        return
    data = yf.download(ticker, start=start_date, 
                             end=end_date.strftime('%Y-%m-%d'), 
                             interval='1d')
    
    # Calculate moving averages based on the selected term
    if term == '1':
        # Short Term: 20d MA, 50d MA, 100d MA
        data['20_MA'] = data['Close'].rolling(window=20).mean()
        data['50_MA'] = data['Close'].rolling(window=50).mean()
        data['100_MA'] = data['Close'].rolling(window=100).mean()
        title = f"{ticker} - Short Term (20, 50, 100-Day MA)"
        ma_columns = ['20_MA', '50_MA', '100_MA']
    elif term == '2':
        # Medium Term: 50d MA, 100d MA, 150d MA, 200d MA
        data['50_MA'] = data['Close'].rolling(window=50).mean()
        data['100_MA'] = data['Close'].rolling(window=100).mean()
        data['150_MA'] = data['Close'].rolling(window=150).mean()
        title = f"{ticker} - Medium Term (50, 100, 150-day MA)"
        ma_columns = ['50_MA', '100_MA', '150_MA']
    elif term == '3':
        # Long Term: 100d MA, 150d MA, 200d MA
        data['100_MA'] = data['Close'].rolling(window=100).mean()
        data['150_MA'] = data['Close'].rolling(window=150).mean()
        data['200_MA'] = data['Close'].rolling(window=200).mean()
        title = f"{ticker} - Long Term (100, 150, 200-Day MA)"
        ma_columns = ['100_MA', '150_MA', '200_MA']
    elif term == '4':
        # Long Term: 100d MA, 150d MA, 200d MA
        data['20_MA'] = data['Close'].rolling(window=20).mean()
        data['50_MA'] = data['Close'].rolling(window=50).mean()
        data['100_MA'] = data['Close'].rolling(window=100).mean()
        data['150_MA'] = data['Close'].rolling(window=150).mean()
        data['200_MA'] = data['Close'].rolling(window=200).mean()
        title = f"{ticker} - with Pretty Colors"
        ma_columns = ['20_MA', '50_MA', '100_MA', '150_MA', '200_MA']
    else:
        print("Invalid term. Please choose '1' for short, '2' for medium, or '3' for long.")
        return
    
    # Plot the closing prices and moving averages
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label='Closing Price', color='white') #Changed color from 'darkgray'
    color_map = {
        '20_MA': 'red',
        '50_MA': 'yellow',
        '100_MA': 'lime',
        '150_MA': 'cyan',
        '200_MA': 'fuchsia'
    }
    for ma_column in ma_columns:
        plt.plot(data[ma_column], label=f'{ma_column}', color=color_map.get(ma_column, 'cyan'))
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(color='dimgray')
    plt.show()

# User input for ticker and term
while True:
    choice = input("Enter 1 to enter Ticker or 2 to Quit: ")
    if choice == '1':
        ticker = input("Enter the ticker symbol: ")
        print("Select the term:")
        print("1. Short Term (20, 50, 100-Day MA)")
        print("2. Medium Term (50, 100, 150, 200-Day MA)")
        print("3. Long Term (100, 150, 200-Day MA)")
        print("4. All da colors...")
        term = input("Enter your choice (1, 2, 3, or 4): ")
        plot_moving_averages(ticker, term)
    elif choice == '2':
        print("is it pretty yet...")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")
