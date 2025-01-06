document.addEventListener('DOMContentLoaded', () => 
    {
    // 현재 URL에 따라 활성화 상태 표시
    const currentPath = window.location.pathname;
    const menuItems = document.querySelectorAll('.navbar__menu li a');

    menuItems.forEach(item => {
        if (item.getAttribute('href') === currentPath) 
        {
            item.classList.add('active');
        }
    });
    });
