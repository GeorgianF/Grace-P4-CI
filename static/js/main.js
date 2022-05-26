// NAV BAR Animation JS
const menuBtn = document.querySelector('.menu-btn');
const navBar = document.querySelector('.nav-container');
const footer = document.querySelector('#footer')
const landing = document.querySelector('#landing-page')
let menuOpen = false;

menuBtn.addEventListener('click', hideContentShowNav);

function hideContentShowNav() {
  if(!menuOpen) {
    menuBtn.classList.add('open');
    menuOpen = true;
    navBar.style.display = 'block';
    footer.classList.add('d-none');
    landing.classList.add('d-none');

  } else {
    menuBtn.classList.remove('open');
    menuOpen = false;
    navBar.style.display = 'none';
    footer.classList.remove('d-none');
    landing.classList.remove('d-none');
  }
}