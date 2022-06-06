// NAV BAR Animation JS
const menuBtn = document.querySelector('.menu-btn');
const navBar = document.querySelector('.nav-container');
const cards = document.querySelectorAll('.card-menu');
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


// DATE PICKER EVENTS

// https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html

$(function () {
  $("#datetimepicker").datetimepicker({
    format: 'd/m/Y H:i',
  });
});

// MESSAGES

// https://github.com/studygyaan/Django-CRM-Project

setTimeout(function(){
  if ($('#msg').length > 0) {
    $('#msg').remove();
  }
}, 2000)