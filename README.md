# eventcapture
Service used to receive and store events that can be analyzed directly or exported to other analytics and/or BI systems

## Sending events

The event server accepts both events and requests.

`Events` are composed by the following attributes:


| Field        | Required | Default | Type     |
| -------------| ---------|---------|----------|
| name         | Yes      | -       | str      |
| segmentation | Yes      | -       | JSON     |
| timestamp    | No       | Now     | datetime |
| device_id    | No       | -       | str      |
| session_id   | No       | -       | str      |
| user_id      | No       | -       | int      |
| business_id  | No       | -       | int      |

To send a new event we need to send a `POST` to the `/event` end-point.
