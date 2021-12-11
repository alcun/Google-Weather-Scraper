from requests_html import HTMLSession

s= HTMLSession()


'''f string lets us put what ever is in query into variable'''


query = 'liverpool'
url = f'https://www.google.com/search?q=weather+liverpool{query}'




r = s.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'})


temp = (r.html.find('span#wob_tm', first=True).text)

print(temp, "°C")



'''so far this should return Element 'title' '''


'''element names'''
''' element of temp number:
<span class="wob_t q8U8x" id="wob_tm" style="display:inline">6</span>'''







''' this is the div class where we will be getting element titles to scrape info from'''

'''
<div class="UQt4rd"><img class="wob_tci" alt="Partly cloudy" src="//ssl.gstatic.com/onebox/weather/64/partly_cloudy.png" id="wob_tci" data-atf="1" data-frt="0"><div jscontroller="e0Sh5" class="Ab33Nc" aria-level="3" role="heading"><div><div class="vk_bk TylWce"><span class="wob_t q8U8x" id="wob_tm" style="display:inline">6</span><span class="wob_t" id="wob_ttm" style="display:none">43</span></div><div jscontroller="e0Sh5" class="vk_bk wob-unit"><span class="wob_t" style="display:inline" aria-label="°Celsius" aria-disabled="true" role="button">°C</span><a class="wob_t" href="#" style="display:none;text-decoration:none" data-lams="" data-metric="true" data-url="/setprefs?fheit=0&amp;sig=0_-eoLO6KYtCjqaV6TO3mM-eo1yQc=&amp;prev=https://www.google.com/search%3Fq%3Dweather%2Bliverpool%26source%3Dhp%26ei%3Djx20Ya3HDonWgQbl3q7gAQ%26iflsig%3DALs-wAMAAAAAYbQrnzUWTtCS76QJmxyE7aBF3rlq1LAV%26ved%3D0ahUKEwjtyqvA6dr0AhUJa8AKHWWvCxwQ4dUDCAk%26uact%3D5%26oq%3Dweather%2Bliverpool%26gs_lcp%3DCgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQgAIyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARCjAjoICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBEKMCOgsILhCABBDHARCjAjoLCC4QgAQQsQMQgwE6DgguEIAEELEDEMcBENEDOgsIABCABBCxAxDJAzoFCAAQkgM6CAgAELEDEIMBUABYhRdg3xdoAHAAeACAAcUBiAHyCZIBBDE2LjGYAQCgAQE%26sclient%3Dgws-wiz" role="button" jsaction="ytDzMd" data-ved="2ahUKEwiXnaHC6dr0AhUJZcAKHXWDBCUQ-lt6BAgSEAE"><span aria-label="°Celsius">°C</span></a><span class="Az4ne"></span><a class="wob_t" href="#" style="display:inline;text-decoration:none;margin-left:-1px" data-lams="" data-metric="false" data-url="/setprefs?fheit=1&amp;sig=0_-eoLO6KYtCjqaV6TO3mM-eo1yQc=&amp;prev=https://www.google.com/search%3Fq%3Dweather%2Bliverpool%26source%3Dhp%26ei%3Djx20Ya3HDonWgQbl3q7gAQ%26iflsig%3DALs-wAMAAAAAYbQrnzUWTtCS76QJmxyE7aBF3rlq1LAV%26ved%3D0ahUKEwjtyqvA6dr0AhUJa8AKHWWvCxwQ4dUDCAk%26uact%3D5%26oq%3Dweather%2Bliverpool%26gs_lcp%3DCgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQgAIyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARCjAjoICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBEKMCOgsILhCABBDHARCjAjoLCC4QgAQQsQMQgwE6DgguEIAEELEDEMcBENEDOgsIABCABBCxAxDJAzoFCAAQkgM6CAgAELEDEIMBUABYhRdg3xdoAHAAeACAAcUBiAHyCZIBBDE2LjGYAQCgAQE%26sclient%3Dgws-wiz" role="button" jsaction="ytDzMd" data-ved="2ahUKEwiXnaHC6dr0AhUJZcAKHXWDBCUQ-1t6BAgSEAI"><span aria-label="°Fahrenheit">°F</span></a>    <span class="wob_t" style="display:none;margin-left:-1px" aria-label="°Fahrenheit" aria-disabled="true" role="button">°F</span></div></div></div><div class="wtsRwe"><div>Precipitation: <span id="wob_pp">2%</span></div><div>Humidity: <span id="wob_hm">86%</span></div><div>Wind: <span><span class="wob_t" id="wob_ws">8 mph</span><span class="wob_t" style="display:none" id="wob_tws">8 mph</span></span></div></div></div>
'''

