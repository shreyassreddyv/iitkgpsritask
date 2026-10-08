Basic TCP Chat Application (ChatNet)
A multithreaded TCP chat application built with Python using the built-in socket and threading modules. It supports real-time message broadcasting across multiple connected clients along with special commands for viewing active users and disconnecting.   
Features:
Multi-Client Support: Uses Python's threading module to handle concurrent client connections dynamically.   
Real-Time Broadcasting: Broadcasts messages to all active connected users.   
In-Chat Commands:
/list: Fetches and prints a list of currently connected usernames.   
/quit: Gracefully disconnects the client from the server session.   
Prerequisites & Installation:
1)Python 3.x
2)No external third-party libraries are required, as the project relies on standard built-in modules (socket,  threading). 
How to Run:
1. Start the Server
Run the server script first to listen for incoming connections:
The server will bind to 0.0.0.0 on port 5052 and start listening for connections.   
2. Connect Clients
In a separate terminal window (or multiple terminal windows), launch the client script:
Enter a unique username when prompted.   
Start chatting with other connected clients!   
How to Test:
Open three separate terminal windows.
Run server3.py in Terminal 1.   
Run client3.py in Terminal 2 .   
Run client3.py in Terminal 3 .   
Type a message in user 1's terminal and verify that user 2 receives it in real time.   
Type /list in any client terminal to see all connected users (user 1, user 2).   
Type /quit to test disconnecting a client safely.   
