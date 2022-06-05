// NAV BAR Animation JS
const menuBtn = document.querySelector('.menu-btn');
const navBar = document.querySelector('.nav-container');
const cards = document.querySelectorAll('.card');
let menuOpen = false;

// Function for the menu button animation

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
};

// Function for the card flip animation for the menu.html

cards.forEach(card => {card.addEventListener("click", 
  function () 
  {
    card.classList.add('flipped');
    setTimeout(() => {
      card.classList.remove('flipped');
    }, 10000);
  });
});


