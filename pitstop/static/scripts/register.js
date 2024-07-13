document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const firstName = document.getElementById("first_name");
    const lastName = document.getElementById("last_name");
    const username = document.getElementById("username");
    const email = document.getElementById("email");
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirm_password");

    // Function to check if user exists
    function checkUser(usernameValue, emailValue, phoneValue) {
        let url = `${BASE_URL}?username=${usernameValue}&email=${emailValue}`;

        return fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.exists) {
                    return Promise.resolve(false); // User exists
                } else {
                    return Promise.resolve(true); // User does not exist
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
                return Promise.reject(error);
            });
    }

    form.addEventListener("submit", async (e) => {
        e.preventDefault(); // Prevent form submission
        let valid = true;

        // Validate first name
        if (firstName.value.trim() === "") {
            valid = false;
            alert("First name is required.");
        }

        // Validate last name
        if (lastName.value.trim() === "") {
            valid = false;
            alert("Last name is required.");
        }

        // Validate username
        if (username.value.trim() === "") {
            valid = false;
            alert("Username is required.");
        }

        // Validate email
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailPattern.test(email.value)) {
            valid = false;
            alert("Please enter a valid email address.");
        }

        // Validate password
        if (password.value.trim() === "") {
            valid = false;
            alert("Password is required.");
        } else if (password.value !== confirmPassword.value) {
            valid = false;
            alert("Passwords do not match.");
        }

        // If all validations pass, check if user exists
        if (valid) {
            try {
                const userExists = await checkUser(username.value, email.value);
                if (!userExists) {
                    alert("User with that username or email already exists.");
                } else {
                    form.submit();
                }
            } catch (error) {
                console.error('Error checking user:', error);
                alert('An error occurred while checking user existence. Please try again.');
            }
        }
    });
});
