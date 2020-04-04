# Code for the Publisher in GCP PubSub

import json, os
from google.cloud import pubsub_v1

class AgriIOTPublisher:
    def __init__(self):
        self.publisher = pubsub_v1.PublisherClient()


    def createTopic(self,topic_name):
        try:
            cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
            project_id = json.loads(open(cred_path,"r").read())["project_id"]

        except Exception as e:
            raise RuntimeError(e)
        
        try:
            topic_path = f"projects/{project_id}/topics/{topic_name}"
            self.publisher.create_topic(topic_path)
            return topic_path

        except Exception as e:
            raise RuntimeError(e)


    # use project id to send the topic path, if it already exists
    def getExistingTopicPath(self, topic):
        try:
            cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
            project_id = json.loads(open(cred_path,"r").read())["project_id"]
            return f"projects/{project_id}/topics/{topic}"

        except Exception as e:
            raise RuntimeError(e)


    def sendMessage(self, topic, data):
        self.publisher.publish(topic, str(data).encode(), spam='eggs')