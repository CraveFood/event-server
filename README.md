# event-server
Service used to receive and store events that can be analyzed directly or exported to other analytics and/or BI systems

## Sending events

The event server accepts both events and requests.

`Events` are composed by the following attributes:

* name (mandatory)
* segmentation - an arbitrary JSON object
* timestamp - defaults to now
* device_id
* request_id
* session_id
* user_id
* business_id

To send a new event we need to send a `POST` to the `/event` end-point.

And the `Requests` are composed by (all mandatory):

* agent
* user_id
* bytes
* client_ip
* host
* referrer
* path
* request_time
* request_id
* timestamp
* verb
* request_body
* request_headers
* response_status
* response_headers
* response_body
* api_version

To send new requests call the `POST` `/request` end-point.
