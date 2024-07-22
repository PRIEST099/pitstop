document.addEventListener('DOMContentLoaded', (event) => {
    // Get the current date and time in the format required by the datetime-local input
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');

    // Combine into the format YYYY-MM-DDTHH:MM
    const minDateTime = `${year}-${month}-${day}T${hours}:${minutes}`;

    // Set the min attribute of the datetime input
    document.getElementById('appointment_time').setAttribute('min', minDateTime);
});