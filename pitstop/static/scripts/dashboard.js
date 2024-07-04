function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content');

    if (sidebar.style.left === '-250px') {
        sidebar.style.left = '0';
        mainContent.style.marginLeft = '250px';
    } else {
        sidebar.style.left = '-250px';
        mainContent.style.marginLeft = '0';
    }
}
