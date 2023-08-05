from datetime import date, datetime, time, timedelta

from analytics import AnalyzerFacade

from google_calendar_analytics.authentication.auth import CalendarAuth
from google_calendar_analytics.visualization.image_saver import ImageSaver

# Get the user's calendar credentials. (You can get these by following the instructions in the README)
auth = CalendarAuth(token_path="token.json", credentials_path="credentials.json")
creds = auth.get_credentials()

# Create an instance of the ImageSaver class
image_saver = ImageSaver(route="visualization/charts")

# Create an instance of the AnalyzerFacade class
analyzer = AnalyzerFacade(creds=creds)
start_time = datetime(2023, 2, 1)
# Calculate tomorrow's date by adding one day to today's date
tomorrow = date.today() - timedelta(days=0)
end_time = datetime.combine(tomorrow, time.min)

# Analyze a single event and generate a chart
event_name = "Programming"
plot_type = "Line"
fig_1 = analyzer.analyze_one(
    start_time, end_time, event_name, plot_type, transparent=0, dark_theme=True
)

plot_type = "Bar"
fig_2 = analyzer.analyze_many(start_time, end_time, plot_type, dark_theme=False)

image_saver.save_plot(fig_1, "line")
image_saver.save_plot(fig_2, "bar")
