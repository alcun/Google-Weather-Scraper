Using python to scrape and display weather data for queried location from google weather api.

Change the 'query value' for different results.

Funny- gets back degC unit on uk ip, after installing html_requests it's bringing back Farenheit. I could add a user query to say what unit they want to see.  

CURRENT VERSION:
Works as intended in cmd terminal after pip install html_requests - 
 displays queried location, temp, unit and desc

TO DO:
I could add:
time
weather forecasts for a few days ahead
a way to export result as .csv file
a ui where the user is prompted for query and parameters like time
add a user query to state unit of measurement 