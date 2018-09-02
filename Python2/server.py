# Runs a server at http://localhost:8000/ and displays the temperature in Celcius in Paris

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import requests

api_token = "6adb85e6c3b6bec49d7154a72e4bef65"
api_url_base = "http://api.openweathermap.org/data/2.5/weather"


def get_paris_weather_info():
    api_url = '{0}?id=2988507&APPID={1}'.format(api_url_base, api_token)
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


class TemperatureHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        json_response = get_paris_weather_info()
        if json_response == None:
            self.send(500, "Something is wrong with the openweathermap API")
            return
        temp_celcius = round(json_response["main"]["temp"] - 273.15, 2)
        self.send(200, str(temp_celcius) + "˚C currently in Paris, France")

    def send(self, response_code, response_body):
        self.send_response(response_code)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(response_body.encode("utf-8"))


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, TemperatureHTTPRequestHandler)
    httpd.serve_forever()
