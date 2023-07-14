import webbrowser as wb

def webauto():
    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    URLS = (
        "google.com",
        "youtube.com",
        "gmail.com"
        
    )
    for url in URLS :
        print("opening:" + url)
        wb.open(url)
webauto()
        
