// NAV BAR Animation JS

const menuBtn = document.querySelector('.menu-btn');
const navBar = document.querySelector('.nav-container');
const siteWrapper = document.querySelector('site-wrapper');
const footer = document.querySelector('#footer')
let menuOpen = false;

menuBtn.addEventListener('click', hideContentShowNav);

function hideContentShowNav() {
  if(!menuOpen) {
    menuBtn.classList.add('open');
    menuOpen = true;
    navBar.style.display = 'block';
    footer.classList.add('d-none');
  } else {
    menuBtn.classList.remove('open');
    menuOpen = false;
    navBar.style.display = 'none';
    footer.classList.remove('d-none');
  }
}

