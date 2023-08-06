import os
from dotenv import load_dotenv
from slack import WebClient


class SlackMessenger:

    def __init__(self, message, error):
        load_dotenv()
        self.channel = os.getenv('SLACK_CHANEL')
        self.message = message
        self.error = error

        self.message_block = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": (
                        self.message + '\n\n'
                ),
            },
        }

    def _prepare_message(self):
        error = {"type": "section", "text": {"type": "mrkdwn", "text": f"{self.error}"}}
        return error

    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        error = self._prepare_message()
        return {
            "channel": self.channel,
            "blocks": [
                self.message_block,
                error,
            ],
        }


def send_to_slack(message, error):
    load_dotenv()

    # Create a slack client
    slack_web_client = WebClient(token=os.getenv("SLACK_TOKEN"))

    send_message = SlackMessenger(
        message=message,
        error=error
    )

    # Get the onboarding message payload
    message = send_message.get_message_payload()

    # Post the onboarding message in Slack
    slack_web_client.chat_postMessage(**message)


class DiscordServer:
    """This is a discord bot,
    he will be able to take message
    and send data for server.
    Communicate with the customer.
    Has a behavioral role roles.
    Need """


    def __init__(self):
        pass
