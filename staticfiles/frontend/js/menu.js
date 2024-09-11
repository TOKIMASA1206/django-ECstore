document.addEventListener('DOMContentLoaded', function () {
  const menuToggle = document.getElementById('menu-toggle');
  const navbarNav = document.getElementById('navbarNav');

  if (menuToggle && navbarNav) {

    menuToggle.addEventListener('click', function () {
      navbarNav.classList.toggle('show');
      menuToggle.classList.toggle('fa-bars');
      menuToggle.classList.toggle('fa-x');
    });

    window.addEventListener('resize', function () {
      const windowWidth = window.innerWidth;

      if (windowWidth > 769) {  // 920px以上の場合はメニューを非表示にし、スクロールを元に戻す
        navbarNav.classList.remove('show');
        menuToggle.classList.add('fa-bars');
        menuToggle.classList.remove('fa-x');
      }
    });
  };
});
