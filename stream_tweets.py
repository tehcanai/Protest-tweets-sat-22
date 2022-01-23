from datetime import datetime
import http.client
import json
from time import sleep

def write_data(df, file):
    line_count = 0
    file_obj = open(file, "a", encoding="utf-8")
    line_count+= 1
    file_obj.write(df['data']['text'] + "\n")
    file_obj.close()
    return line_count


conn = http.client.HTTPSConnection("api.twitter.com")
payload = ''
headers = {'Authorization Goes Here'}

def get_stream() :
    while (True) :
        try :
            conn.request("GET", "/2/tweets/search/stream", payload, headers)
            sleep(10)
            res = conn.getresponse()
            data = res.readline().decode("utf-8")
            conn.close()
            if (len(data) > 20) :
                df = json.loads(data)
                print(str(datetime.now()) + " : \n" + df['data']['text'] + "\n")
                write_data(df, "sat22-1-22")
        except Exception:
            get_stream()

get_stream()
