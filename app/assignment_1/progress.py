from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def progress_bar(taskid, percentage_complete):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        taskid,  # Use the task ID as the channel group name
        {"type": "task_progress", "percentage_complete": percentage_complete},
    )