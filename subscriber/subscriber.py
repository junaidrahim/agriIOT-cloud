from google.cloud import pubsub_v1
from database import AgriIOTDatabase
import json, os


class AgriIOTSubscriber:
    def __init__(self):
        self.subscriber = pubsub_v1.SubscriberClient()
        self.db = AgriIOTDatabase()
        print("Starting AGRI IOT SUBSCRIBER")

    def getProjectID(self):
        try:
            cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
            project_id = json.loads(open(cred_path,"r").read())["project_id"]
            return project_id
        except Exception as e:
            raise RuntimeError(e)

    # use project id to send the topic path, if it already exists
    def getExistingTopicPath(self, topic):
        project_id = self.getProjectID()
        return f"projects/{project_id}/topics/{topic}"

    def getExistingSubscriptionPath(self, sub_name):
        project_id = self.getProjectID()
        subscription_path = f"projects/{project_id}/subscriptions/{sub_name}"
        return subscription_path


    def createSubscription(self, subscription_name, topic_name):
        project_id = self.getProjectID()

        subscription_path = f"projects/{project_id}/subscriptions/{subscription_name}"
        topic_path = self.getExistingTopicPath(topic_name)

        self.subscriber.create_subscription(name=subscription_path, topic=topic_path)
        return subscription_path

    def subscribe(self, subscription_path):
        def callback(message):
            self.db.write(message.data.decode())
            print("Data Received", json.loads(message.data.decode()))

        future = self.subscriber.subscribe(subscription_path, callback)

        try:
            future.result()
        except KeyboardInterrupt:
            future.cancel()
        except Exception as e:
            print(e)
            future.cancel()

