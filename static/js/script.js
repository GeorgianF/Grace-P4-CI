// NAV BAR Animation JS

const menuBtn = document.querySelector('.menu-btn');
const navBar = document.querySelector('.nav-container');
const siteWrapper = document.querySelector('site-wrapper');

let menuOpen = false;
menuBtn.addEventListener('click', () => {
  if(!menuOpen) {
    menuBtn.classList.add('open');
    menuOpen = true;
    navBar.style.display = 'block';
    
  } else {
    menuBtn.classList.remove('open');
    menuOpen = false;
    navBar.style.display = 'none';
  }
});


