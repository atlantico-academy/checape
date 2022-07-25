"""
Authors: @pythonistabr / @PauloMarvin
project: Twitter Sentiment Analysis - Atlantico Bootcamp
"""

from datetime import timedelta
from pandas import to_datetime


class TimeConverter:
    
    def from_utc_to_local_time(london_time: str, london_reference: int):
        london_time = to_datetime(london_time) # str para datetime
        local_time = london_time + timedelta(hours = london_reference)
        return local_time
    
    def get_day_period(time: str) -> str:
        time = to_datetime(time)
        hour = time.hour

        if hour >= 0 and hour < 6:
            return "overnight"
        elif hour >= 6 and hour < 12:
            return "morning"
        elif hour >= 12 and hour < 18:
            return "afternoon"
        elif hour >= 18 and hour < 24:
            return "night"
        
        
def main():
    print("--" *20 + "TimeFormatter Test" + "--" *20)
    
    utc = "1988-10-02 06:42" # date for test
    brasilia = TimeConverter.from_utc_to_local_time("1988-10-02 06:42", -3)
    
    day_period = TimeConverter.get_day_period(
        TimeConverter.from_utc_to_local_time("1988-10-02 06:42", -3)
    )
    
    print(f"London: {utc}")
    print(f"Brasilia (utc-3): {brasilia}\n")
    print(f"Day Period(local): {day_period}") 
    
    
if __name__ == "__main__":
    main()
    
    