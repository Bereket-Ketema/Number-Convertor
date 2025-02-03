document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("convertForm").addEventListener("submit", function(event) {
        event.preventDefault();  // Prevent page reload

        let fromSystem = document.getElementById("number-system-1").value;
        let toSystem = document.getElementById("number-system-2").value;
        let value = document.getElementById("value").value;

        // Send the data via POST to the server
        fetch('/numbers/', {  // Ensure this matches urls.py
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: `number-system-1=${fromSystem}&number-system-2=${toSystem}&value=${value}`
        })
        .then(response => response.json())  // Expect JSON response from the server
        .then(data => {
            // Display the conversion result and include the from-system and to-system
            document.getElementById("result").innerHTML = `
                <h2>Conversion Result:</h2>
                <p><b>Converted Number:</b> ${data.number}</p>
                <p><b>From System:</b> ${data.from_system}</p>
                <p><b>To System:</b> ${data.to_system}</p>
            `;

            // Display the explanation of the conversion
            document.getElementById("explanation").innerHTML = `
                <h3>Explanation:</h3>
                <p>${data.explanation}</p>
            `;
        })
        .catch(error => console.error('Error:', error));
    });
});
