document.addEventListener('DOMContentLoaded', function () {
  const menuToggle = document.getElementById('menu-toggle');
  const navbarNav = document.getElementById('navbarNav');

  if (menuToggle && navbarNav) {
    
    function closeMenu() {
      navbarNav.classList.remove('show');
      menuToggle.classList.add('fa-bars');
      menuToggle.classList.remove('fa-x');
    }

    menuToggle.addEventListener('click', function () {
      navbarNav.classList.toggle('show');
      menuToggle.classList.toggle('fa-bars');
      menuToggle.classList.toggle('fa-x');
    });

    window.addEventListener('resize', function () {
      const windowWidth = window.innerWidth;

      if (windowWidth > 769) { 
        closeMenu();
      }
    });

    
    window.addEventListener('beforeunload', function () {
      closeMenu();
    });
  }
});







