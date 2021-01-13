# How to proceed

-   Create an api that retrieves the request sent by openedx

-   Specify the url of your api in the openedx config file.

-   Send the information received in the commands of your machine or import the
    functions for another use.
   
### example response from openedx : 
`{
“EdX-ID”: “ad216c07--3a25b56b3787",
“ExpectedName”: "ad216c07--3a25b56b3787”,
“PhotoID”: “https:///photo_id/ad216c07-3a25b56b3787?Signature=4%3D&Expires=199&AWSAccessKeyId=openedx”,
“PhotoIDKey”: “SHA1dmWUiwH4U0q/H+rIejx5Ez6ZPvMporQRj8U9y4wItHz1rVcF2a88XyOWuINmzVNix0xHgyZaGU0VjfviyKVEKCvJP1cQgdA0Ec7XR4zk2ULNRf5+FVKhOeL1MLFGtRsYzJf/lFsfRsOCS+vxrTvBKQCwGVN6GU/wbFaZgi5WrO30erRMY1MTgDLdw9pdwl3k0EV+YZ5XF7GXIP5P+Wo2EVLqUB7F3ZlI/fkrG7rqZiOZQ==↵",
“UserPhoto”: "https:///openedx/face/ad216c07-503a-460c-8b75-3a25b56b3787?Signature=DqF2uQy8hKkTwptbLEJw%3D&Expires=19229&AWSAccessKeyId=openedx”,
“UserPhotoKey”: “lcGPipE0DzYmLcnSPn+Est0SQJlvrlaijfpkJKiV+0oDLKY0WBIrcKzyKeR+FUkjCjOPOXmtX9kNbVIzazZFeI4RszD0vwX7WPQrL4iegmMW7CeHrjnvyU5/czScA2f9A9UCTwPALmxFCowUH4dbNCaZQKm5Saj37FSM5UNSC3D1b+5+5ps75171IBEB3aQgMaG6LdxXy1XCinbbTyWaiabyMQojP4FduoYOscbE45ghKrLsYP4TkMXQ7LqAl4E1HrfzFjHfx5hNYqFNoRfeRlKwshZicGZeMkqTzjKw2j2v4NzPKQ==↵",
“SendResponseTo”: "https://*****/verify_student/results_callback”
}`

then you have to retrieve the information and transmit it to the order.

Then you can send back a request if it’s ok or refused on ironwood on the other hand the verification of the message by contribution to the encrypted message was not activated it is just necessary to send back to him on the new version I have not looked at yet.
the api key is the one you specified in the config file for identity

#### POST https://*/verify_student/results_callback
`Content-Type: application/json
Authorization: _ API_KEY:_
{“Result”: “PASS”,
“EdX-ID”:“550fa42f--8bbb-702ee7407c94"
}`

or

`{“Result”: “FAIL”,
“EdX-ID”:"550fa42f-36--8bbb-702ee7407c94”,
“Reason”: “not the same person”.
}`

