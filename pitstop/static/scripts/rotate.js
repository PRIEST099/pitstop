// script.js
document.addEventListener('mousemove', (e) => {
    const container = document.querySelector('.container');
    const rect = container.getBoundingClientRect();
    const x = e.clientX - rect.left - container.offsetWidth / 2;
    const y = e.clientY - rect.top - container.offsetHeight / 2;

    document.querySelector('.circle1').style.transform = `translate(-50%, -50%) translate(${x * 0.2}px, ${y * 0.2}px) rotate(0deg)`;
    document.querySelector('.circle2').style.transform = `translate(-50%, -50%) translate(${x * 0.1}px, ${y * 0.1}px) rotate(0deg)`;
    document.querySelector('.circle3').style.transform = `translate(-50%, -50%) translate(${x * 0.05}px, ${y * 0.05}px) rotate(0deg)`;
});
