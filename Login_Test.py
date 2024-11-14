from locust import HttpUser, TaskSet, between, task;
import json;
import urllib3;
import time;
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class TesteLoginPrincipal(TaskSet):
    wait_time = between(4, 5)

    def Post_login_return_token(self):
        token_pronto = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6WyJsdWNhcy5yYW1vc0BkYXJ0ZGlnaXRhbC5jb20uYnIiLCJMdWNhcyBSYW1vcyAoRGFydCkiXSwiZW1haWwiOiJsdWNhcy5yYW1vc0BkYXJ0ZGlnaXRhbC5jb20uYnIiLCJzdHVkZW50SWQiOiI0NzY1NiIsInN0dWRlbnRGcmVlbWl1bSI6IkZhbHNlIiwibmJmIjoxNzMxNTI4MTA0LCJleHAiOjE3MzE1Mjk5MDQsImlhdCI6MTczMTUyODEwNCwiaXNzIjoiQ29ydWphLldlYkFwaS5Jc3N1ZXIiLCJhdWQiOiJDb3J1amEuV2ViQXBpLkF1ZGllbmNlIn0.mGoP_Feu7xZURBHOArB8WzliZ52HEB7IIVEhZcXgzsJOLwRoKboa7GR0wDkHqrV1PlOmdNC3drHzHI-l64MEqIuYpbir1ump99ewiQfMYudfiS_qgX6BTxHq9fFxxbcNL7sSfLNh-_M-3Q3HA1JprKzBEpPPf185gR1YtepZsZcNZ5aVGAq3atL0Dnkh9SwgjmfXTsXwuiHJf3GxtvHTzaeH6Gbz9J_dQoTsNgo5FoO1c8BanOALBq_N4K9fEM_Gavfkp9O98l6AzoZnNgO-poaf-Ds6ybvuONpdCvyVZcK76VO5RTF_ssvrtvVAAZfxHYAoo2lHS-3TYDDFiWA0Gg"
        return token_pronto
    
    def on_start(self):
        self.token = self.Post_login_return_token();

    @task
    def Users_get_lessons_with_token (self):
        print("Test: Users_get_lessons_with_token. Status: Teste iniciado!");
        self.client.get("api/v1/student/lesson/search", 
                        headers = {'Authorization' : 'Bearer ' + self.token, 
                                   'X-Application-Key': 'webkey123', 
                                   'accept': 'application/json'}, 
                        verify=False);
        print("Test: Users_get_lessons_with_token. Status: Teste FINALIZADO!");
        

class WebsiteUser(HttpUser):
   tasks = [TesteLoginPrincipal]