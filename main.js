function getStats() {
    const playerName = document.getElementById('playerName').value;
    const statType = document.getElementById('statType').value;
    const comparison = document.getElementById('comparison').value;

    // You can make an API request here to get stats based on the entered parameters.
    // For simplicity, let's display a message for now.
    const playerStats = `Stats for ${playerName}: ${statType} is ${comparison} than expected.`;

    document.getElementById('playerStats').innerText = playerStats;
}
