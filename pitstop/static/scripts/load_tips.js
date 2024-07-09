$(document).ready(function() {
    function loadTip() {
        $.getJSON("static/scripts/tips.json", function(data) { // Adjust the path to tips.json as per your directory structure
            var randomIndex = Math.floor(Math.random() * data.length);
            var randomTip = data[randomIndex];

            $(".title-tip").text(randomTip.title);
            $(".tip").text(randomTip.tip);
        });
    }

    loadTip(); // Initial load when the page loads

    // Optionally, load a new tip on button click or other event
    // Example:
    // $("#load-tip-button").click(function() {
    //     loadTip();
    // });
});
