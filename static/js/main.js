// NAV BAR Animation JS
const menuBtn = document.querySelector('.menu-btn');
const navBar = document.querySelector('.nav-container');
const cards = document.querySelectorAll('.card-body');
const card = document.querySelector('.flipped')
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
    card.classList.add('flipped');
    setTimeout(() => {
      card.classList.remove('flipped');
    }, 5000);
  })
})


