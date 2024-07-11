from datetime import datetime

def format_datetime(date_str):
    # Convert string to datetime object
    dt = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

    # Dictionary to add 'st', 'nd', 'rd', 'th' to the day
    suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
    if 11 <= dt.day <= 13:
        suffix = 'th'
    else:
        suffix = suffixes.get(dt.day % 10, 'th')
    
    # Formatting the date
    formatted_date = dt.strftime(f"%-d{suffix} %B %Y")
    return formatted_date



if __name__ == '__main__':
    # Example usage
    datetime_str = '2024-07-09 12:15:00'
    formatted_datetime = format_datetime(datetime_str)
    print(formatted_datetime)  # Output: "9th July 2024"
