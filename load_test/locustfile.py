from locust import HttpUser, between, task

# locust -f load_test/locustfile.py --host=https://harmonyharbor.azurewebsites.net


class MyLocustUser(HttpUser):
    wait_time = between(1, 5)  # Random wait time between 1 and 5 seconds

    @task(1)
    def execute_query(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "queryInput": "SELECT * FROM prepared_song_data WHERE time_signature = 4 AND tempo between 100 and 140"
        }
        self.client.post("/execute_query", data=data, headers=headers)

    @task(10)
    def get_bot_response(self):
        user_text = "give me some music that is happy"
        self.client.get(f"/get?msg={user_text}")

    @task(500)
    def chatbot(self):
        self.client.get("/chatbot")

    @task(500)
    def stats(self):
        self.client.get("/stats")

    @task(100)
    def index(self):
        self.client.get("/")
