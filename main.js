<script>
    function predictStats() {
        // Your JavaScript code for predicting stats goes here
        // You can use AJAX or fetch to send a request to your Flask server
        // and handle the response to update the HTML page
        // Example:
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                // Add the input fields and values
            }),
        })
        .then(response => response.json())
        .then(data => {
            // Update the HTML page with the prediction result
            document.getElementById('predictionResult').innerText = 'Predicted Value: ' + data[0].PTS;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
</script>
