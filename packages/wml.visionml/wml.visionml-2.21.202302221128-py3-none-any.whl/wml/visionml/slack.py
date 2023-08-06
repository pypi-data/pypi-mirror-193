# pylint: disable=import-outside-toplevel

"""Modules dealing with posting messages to Slack.
"""

from mt import tp

channel_url_dict = {
    "model_training": "https://hooks.slack.com/services/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",
}


__all__ = ["send", "send_markdown", "send_asyn", "markdown_block"]


def send(text: tp.Optional[str] = None, channel: str = "model_training", **kwargs):
    """Sends a message to a Slack channel.

    Parameters
    ----------
    text : str, optional
        the message. Passed directly to :func:`slack_sdk.webhook.WebhookClient.send`
    channel : str, optional
        channel to send the message to
    **kwargs : dict
        any other keyword argument passed directly to :func:`slack_sdk.webhook.WebhookClient.send`

    Returns
    -------
    response : object
        the response from the Slack server
    """

    from slack_sdk.webhook import WebhookClient

    url = channel_url_dict[channel]
    webhook = WebhookClient(url)

    response = webhook.send(text=text, **kwargs)
    return response


#    assert response.status_code == 200
#    assert response.body == "ok"


def send_markdown(markdown_text: str, channel: str = "model_training"):
    """TBC"""
    return send(blocks=[markdown_block(markdown_text)], channel=channel)


async def send_asyn(
    text: tp.Optional[str] = None,
    channel: str = "model_training",
    context_vars: dict = {},
    **kwargs
):
    """An asyn function that sends a message to a Slack channel.

    Parameters
    ----------
    text : str, optional
        the message. Passed directly to :func:`slack_sdk.webhook.WebhookClient.send`
    channel : str, optional
        channel to send the message to
    context_vars : dict
        a dictionary of context variables within which the function runs. It must include
        `context_vars['async']` to tell whether to invoke the function asynchronously or not.
    **kwargs : dict
        any other keyword argument passed directly to :func:`slack_sdk.webhook.WebhookClient.send`

    Returns
    -------
    response : object
        the response from the Slack server
    """

    if not context_vars["async"]:
        return send(channel=channel, text=text, **kwargs)

    from slack_sdk.webhook.async_client import AsyncWebhookClient

    url = channel_url_dict[channel]
    webhook = AsyncWebhookClient(url)
    response = await webhook.send(text=text, **kwargs)
    # assert response.status_code == 200
    # assert response.body == "ok"
    return response


def markdown_block(markdown_msg: str) -> str:
    """Turns a Slack mark-down string into a block."""

    return {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": markdown_msg,
        },
    }
