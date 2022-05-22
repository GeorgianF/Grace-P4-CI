// NAV BAR Animation JS

const menuBtn = document.querySelector('.menu-btn');
const navBar = document.querySelector('.nav-container');

let menuOpen = false;
menuBtn.addEventListener('click', () => {
  if(!menuOpen) {
    menuBtn.classList.add('open');
    menuOpen = true;
    navBar.style.opacity = "0.7"
  } else {
    menuBtn.classList.remove('open');
    menuOpen = false;
    navBar.style.opacity = "0"
  }
});



