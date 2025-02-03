document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("convertForm").addEventListener("submit", function(event) {
        event.preventDefault();  // Prevent page reload

        let fromSystem = document.getElementById("number-system-1").value;
        let toSystem = document.getElementById("number-system-2").value;
        let value = document.getElementById("value").value;

        fetch('/numbers/', {  // Ensure this matches urls.py
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: `number-system-1=${fromSystem}&number-system-2=${toSystem}&value=${value}`
        })
        .then(response => response.text())
        .then(data => {
            document.getElementById("result").innerHTML =`<p>${data}</p>`;
            
        })
        .catch(error => console.error('Error:', error));
    });
});
