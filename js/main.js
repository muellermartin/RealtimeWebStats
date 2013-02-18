function log(s)
{
	var time = new Date();
	// append zeros: (m<=9?'0'+m:m)
	var timestamp = time.getFullYear() + "-" + time.getMonth() + 1 + "-" + time.getDate() + " " + time.getHours() + ":" + time.getMinutes() + ":" + time.getSeconds();

	$("#log").append("<p><time>" + timestamp + "</time>" + s + "</p>");
}

function connect()
{
	return new WebSocket("ws://127.0.0.1:9000/ws");
}

function send(ws)
{
	// send some data to the server
	ws.send("some data from the client")
}

function close(ws)
{
	// close the socket
	ws.close();
}

$(document).ready(function() {
	if("WebSocket" in window)
	{
		try
		{
			var ws = connect();

			// WebSocket.readyState values taken from http://dev.w3.org/html5/websockets/
			// CONNECTING (numeric value 0): The connection has not yet been established.
			// OPEN (numeric value 1): The WebSocket connection is established and communication is possible.
			// CLOSING (numeric value 2): The connection is going through the closing handshake, or the close() method has been invoked.
			// CLOSED (numeric value 3)
			//
			log("WebSocket status: " + ws.readyState);

			ws.onopen = function() {
				// called when connection is opened
				log("WebSocket status: " + ws.readyState + " (open)");
			};

			ws.onerror = function() {
				// called in case of error, when connection is broken in example
				log("Error");
			};

			ws.onclose = function() {
				// called when connection is closed
				log("WebSocket status: " + ws.readyState + " (closed)");
			};

			ws.onmessage = function(msg) {
				// called when the server sends a message to the client
				// msg.data contains the message
				log("Received message: " + msg.data);
			};

			$("#submit").click(function() {
				send(ws);
			});

			$("#disconnect").click(function() {
				close(ws);
			});
		}

		catch(exception)
		{
			alert("Error: " + exception);
		}
	}

	else
	{
		alert("Your browser does not support WebSockets!");
	}
});
