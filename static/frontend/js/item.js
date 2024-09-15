document.addEventListener('DOMContentLoaded', function () {
  const swiper = new Swiper(".mySwiper", {
    spaceBetween: 10,
    slidesPerView: 4
  });
  
  const swiper2 = new Swiper(".mySwiper2", {
    thumbs: {
      swiper: swiper
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev"
    }
  });
});
