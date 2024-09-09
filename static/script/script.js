document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("test-case-form");
    const outputDiv = document.getElementById("output");

    form.addEventListener("submit", async function(event) {
        event.preventDefault();

        // Create a FormData object to hold the form data
        const formData = new FormData(form);

        try {
            // Send the form data to the Flask back-end
            const response = await fetch('/generate-instructions', {
                method: 'POST',
                body: formData
            });

            // Check if the request was successful
            if (response.ok) {
                // Get the generated test case from the response
                const htmlResponse = await response.text();
                // Parse the HTML to extract the relevant part
                const parser = new DOMParser();
                const doc = parser.parseFromString(htmlResponse, 'text/html');
                const generatedText = doc.getElementById('output').innerHTML;

                // Display the generated test case in the output div
                outputDiv.innerHTML = generatedText;
            } else {
                outputDiv.innerHTML = "Error: Failed to generate test instructions. Please try again.";
            }
        } catch (error) {
            console.error("Error:", error);
            outputDiv.innerHTML = "Error: An unexpected error occurred. Please try again.";
        }
    });
});
