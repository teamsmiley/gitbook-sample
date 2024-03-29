import time
from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
  wait_time = between(0.5, 1)
  def on_start(self):
    self.client.verify = False

  @task
  def launch(self):
      self.client.get(url="/values")



