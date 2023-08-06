import os

from clearblade.cloud import iot_v1


def sample_get_device_states_list():
    client = iot_v1.DeviceManagerClient()
    device_path = client.device_path(
        "api-project-320446546234",
        "us-central1",
        "clarktest3",
        "deviceOne"
    )

    request = iot_v1.ListDeviceStatesRequest(name=device_path, numStates=3)
    response = client.list_device_states(request)

    for state in response.device_states:
        print(state)


os.environ["CLEARBLADE_CONFIGURATION"] = "/Users/rajas/Downloads/developers-credentials.json"
sample_get_device_states_list()
