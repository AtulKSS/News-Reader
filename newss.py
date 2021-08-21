# 390ca346f5d5490d872d16e1ebf35eae
print("wrlcome to news app")
import requests
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__ == '__main__':
    speak("")
def modules():
    queries={
        "source":"Tesla news",
        "sortby":"top",
        "apikey":"390ca346f5d5490d872d16e1ebf35eae"
    }
    url ="https://newsapi.org/v2/everything?q=apple&from=2021-08-16&to=2021-08-16&sortBy=popularity&apiKey=390ca346f5d5490d872d16e1ebf35eae"
    rada=requests.get(url)
    open_page=rada.json()
    article=open_page["articles"]
    result=[]
    for ar in article:
        result.append(ar["title"])
    for i in range(len(result)):
        print(i+1,result[i])
    speak(result)

if __name__ == '__main__':
    modules()


