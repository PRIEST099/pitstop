// document.addEventListener('DOMContentLoaded', function() {
//     var flashMessages = document.getElementsByClassName('flash-message');
//     for (var i = 0; i < flashMessages.length; i++) {
//         (function(flashMessage) {
//             setTimeout(function() {
//                 flashMessage.style.opacity = '0';
//                 flashMessage.style.transform = 'translateY(-20px)';
//             }, 3000);  // 3000 milliseconds = 3 seconds
//             setTimeout(function() {
//                 flashMessage.style.display = 'none';
//             }, 3500);  // 3500 milliseconds = 3.5 seconds to allow for transition
//         })(flashMessages[i]);
//     }
// });