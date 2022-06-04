// NAV BAR Animation JS
const menuBtn = document.querySelector('.menu-btn');
const navBar = document.querySelector('.nav-container');
const cards = document.querySelectorAll('.card-body');
let menuOpen = false;

menuBtn.addEventListener('click', hideContentShowNav);

function hideContentShowNav() {
  if(!menuOpen) {
    menuBtn.classList.add('open');
    menuOpen = true;
    navBar.style.right = '0';

  } else {
    menuBtn.classList.remove('open');
    menuOpen = false;
    navBar.style.right = '-350px'
  }
}

cards.forEach(card => {card.addEventListener("click", 
  function () 
  {
    card.classList.toggle('flipped')
  })
})

