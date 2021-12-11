from requests_html import HTMLSession

s= HTMLSession()


'''f string lets us put what ever is in query into variable'''


query = input("Where would you like weather data for? ")

url = f'https://www.google.com/search?q=weather+{query}'


''' User agent helps us bypass captcha type things'''

r = s.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'})


temp = (r.html.find('span#wob_tm', first=True).text)


unit = (r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text)


'''finds chained together to search with larger div'''


desc = (r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text)

print(query, temp, unit, desc)


'''element names'''

''' text description -
<div class="wob_dcp" id="wob_dcp"><span id="wob_dc">Partly cloudy</span></div>

'''

''' div id for element (with also time and location)
<div class="VQF4g"><span aria-level="3" role="heading"><div class="wob_loc q8U8x" id="wob_loc">Liverpool, UK</div><div class="wob_dts" id="wob_dts">Saturday 03:00</div><div class="wob_dcp" id="wob_dcp"><span id="wob_dc">Partly cloudy</span></div></span></div>'''






''' element of temp number:
<span class="wob_t q8U8x" id="wob_tm" style="display:inline">6</span>'''


'''element of measurement unit:

<div jscontroller="e0Sh5" class="vk_bk wob-unit"><span class="wob_t" style="display:inline" aria-label="°Celsius" aria-disabled="true" role="button">°C</span><a class="wob_t" href="#" style="display:none;text-decoration:none" data-lams="" data-metric="true" data-url="/setprefs?fheit=0&amp;sig=0_-eoLO6KYtCjqaV6TO3mM-eo1yQc=&amp;prev=https://www.google.com/search%3Fq%3Dweather%2Bliverpool%26source%3Dhp%26ei%3Djx20Ya3HDonWgQbl3q7gAQ%26iflsig%3DALs-wAMAAAAAYbQrnzUWTtCS76QJmxyE7aBF3rlq1LAV%26ved%3D0ahUKEwjtyqvA6dr0AhUJa8AKHWWvCxwQ4dUDCAk%26uact%3D5%26oq%3Dweather%2Bliverpool%26gs_lcp%3DCgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQgAIyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARCjAjoICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBEKMCOgsILhCABBDHARCjAjoLCC4QgAQQsQMQgwE6DgguEIAEELEDEMcBENEDOgsIABCABBCxAxDJAzoFCAAQkgM6CAgAELEDEIMBUABYhRdg3xdoAHAAeACAAcUBiAHyCZIBBDE2LjGYAQCgAQE%26sclient%3Dgws-wiz" role="button" jsaction="ytDzMd" data-ved="2ahUKEwiXnaHC6dr0AhUJZcAKHXWDBCUQ-lt6BAgSEAE"><span aria-label="°Celsius">°C</span></a><span class="Az4ne"></span><a class="wob_t" href="#" style="display:inline;text-decoration:none;margin-left:-1px" data-lams="" data-metric="false" data-url="/setprefs?fheit=1&amp;sig=0_-eoLO6KYtCjqaV6TO3mM-eo1yQc=&amp;prev=https://www.google.com/search%3Fq%3Dweather%2Bliverpool%26source%3Dhp%26ei%3Djx20Ya3HDonWgQbl3q7gAQ%26iflsig%3DALs-wAMAAAAAYbQrnzUWTtCS76QJmxyE7aBF3rlq1LAV%26ved%3D0ahUKEwjtyqvA6dr0AhUJa8AKHWWvCxwQ4dUDCAk%26uact%3D5%26oq%3Dweather%2Bliverpool%26gs_lcp%3DCgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQgAIyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARCjAjoICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBEKMCOgsILhCABBDHARCjAjoLCC4QgAQQsQMQgwE6DgguEIAEELEDEMcBENEDOgsIABCABBCxAxDJAzoFCAAQkgM6CAgAELEDEIMBUABYhRdg3xdoAHAAeACAAcUBiAHyCZIBBDE2LjGYAQCgAQE%26sclient%3Dgws-wiz" role="button" jsaction="ytDzMd" data-ved="2ahUKEwiXnaHC6dr0AhUJZcAKHXWDBCUQ-1t6BAgSEAI"><span aria-label="°Fahrenheit">°F</span></a>    <span class="wob_t" style="display:none;margin-left:-1px" aria-label="°Fahrenheit" aria-disabled="true" role="button">°F</span></div>

just C

<span class="wob_t" style="display:inline" aria-label="°Celsius" aria-disabled="true" role="button">°C</span>'''




''' this is the container div class where we will be getting element titles to scrape info from'''

'''
<div class="UQt4rd"><img class="wob_tci" alt="Partly cloudy" src="//ssl.gstatic.com/onebox/weather/64/partly_cloudy.png" id="wob_tci" data-atf="1" data-frt="0"><div jscontroller="e0Sh5" class="Ab33Nc" aria-level="3" role="heading"><div><div class="vk_bk TylWce"><span class="wob_t q8U8x" id="wob_tm" style="display:inline">6</span><span class="wob_t" id="wob_ttm" style="display:none">43</span></div><div jscontroller="e0Sh5" class="vk_bk wob-unit"><span class="wob_t" style="display:inline" aria-label="°Celsius" aria-disabled="true" role="button">°C</span><a class="wob_t" href="#" style="display:none;text-decoration:none" data-lams="" data-metric="true" data-url="/setprefs?fheit=0&amp;sig=0_-eoLO6KYtCjqaV6TO3mM-eo1yQc=&amp;prev=https://www.google.com/search%3Fq%3Dweather%2Bliverpool%26source%3Dhp%26ei%3Djx20Ya3HDonWgQbl3q7gAQ%26iflsig%3DALs-wAMAAAAAYbQrnzUWTtCS76QJmxyE7aBF3rlq1LAV%26ved%3D0ahUKEwjtyqvA6dr0AhUJa8AKHWWvCxwQ4dUDCAk%26uact%3D5%26oq%3Dweather%2Bliverpool%26gs_lcp%3DCgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQgAIyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARCjAjoICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBEKMCOgsILhCABBDHARCjAjoLCC4QgAQQsQMQgwE6DgguEIAEELEDEMcBENEDOgsIABCABBCxAxDJAzoFCAAQkgM6CAgAELEDEIMBUABYhRdg3xdoAHAAeACAAcUBiAHyCZIBBDE2LjGYAQCgAQE%26sclient%3Dgws-wiz" role="button" jsaction="ytDzMd" data-ved="2ahUKEwiXnaHC6dr0AhUJZcAKHXWDBCUQ-lt6BAgSEAE"><span aria-label="°Celsius">°C</span></a><span class="Az4ne"></span><a class="wob_t" href="#" style="display:inline;text-decoration:none;margin-left:-1px" data-lams="" data-metric="false" data-url="/setprefs?fheit=1&amp;sig=0_-eoLO6KYtCjqaV6TO3mM-eo1yQc=&amp;prev=https://www.google.com/search%3Fq%3Dweather%2Bliverpool%26source%3Dhp%26ei%3Djx20Ya3HDonWgQbl3q7gAQ%26iflsig%3DALs-wAMAAAAAYbQrnzUWTtCS76QJmxyE7aBF3rlq1LAV%26ved%3D0ahUKEwjtyqvA6dr0AhUJa8AKHWWvCxwQ4dUDCAk%26uact%3D5%26oq%3Dweather%2Bliverpool%26gs_lcp%3DCgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQgAIyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARCjAjoICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBEKMCOgsILhCABBDHARCjAjoLCC4QgAQQsQMQgwE6DgguEIAEELEDEMcBENEDOgsIABCABBCxAxDJAzoFCAAQkgM6CAgAELEDEIMBUABYhRdg3xdoAHAAeACAAcUBiAHyCZIBBDE2LjGYAQCgAQE%26sclient%3Dgws-wiz" role="button" jsaction="ytDzMd" data-ved="2ahUKEwiXnaHC6dr0AhUJZcAKHXWDBCUQ-1t6BAgSEAI"><span aria-label="°Fahrenheit">°F</span></a>    <span class="wob_t" style="display:none;margin-left:-1px" aria-label="°Fahrenheit" aria-disabled="true" role="button">°F</span></div></div></div><div class="wtsRwe"><div>Precipitation: <span id="wob_pp">2%</span></div><div>Humidity: <span id="wob_hm">86%</span></div><div>Wind: <span><span class="wob_t" id="wob_ws">8 mph</span><span class="wob_t" style="display:none" id="wob_tws">8 mph</span></span></div></div></div>
'''

