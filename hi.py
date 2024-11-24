<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Travel Chatbot</title>
</head>
<body>
    <h1>Welcome to Travel Chatbot</h1>
    <form id="chat-form">
        <input type="text" name="message" id="message" placeholder="Ask something..." required>
        <button type="submit">Send</button>
    </form>
    <div id="chat-log"></div>
    <iframe id="map" src="" style="width: 100%; height: 500px; display: none;"></iframe>
    <script>
        document.getElementById('chat-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const message = document.getElementById('message').value;
            const res = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message })
            });
            const data = await res.json();
            document.getElementById('chat-log').innerText += `\nYou: ${message}`;
            document.getElementById('chat-log').innerText += `\nBot: ${data.response}`;
            if (data.map) {
                document.getElementById('map').src = data.map;
                document.getElementById('map').style.display = "block";
            }
        });
    </script>
</body>
</html>
