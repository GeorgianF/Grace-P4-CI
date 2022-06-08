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
  var today = new Date();
  var tomorrow = new Date();
  tomorrow.setDate(today.getDate() + 1);
  $("#datetimepicker").datetimepicker({
    format: 'd/m/Y H:i',
    allowTimes:[
      '17:00',
      '17:30',
      '18:00',
      '18:30',
      '19:00',
      '19:30',
      '20:00',
      '20:30',
      '21:00',
    ],
    theme:'dark',
    disabledDates: [
      new Date(),
      '12.06.2022','19.06.2022','26.06.2022',
      '03.07.2022','10.07.2022','17.07.2022',
      '24.07.2022','31.07.2022','07.08.2022',
      '14.08.2022','21.08.2022','28.08.2022',
      '04.09.2022','11.09.2022','18.09.2022',
      '25.09.2022','02.10.2022','09.10.2022',
      '16.10.2022','23.10.2022','30.10.2022',
      '06.11.2022','13.11.2022','20.11.2022',
      '27.11.2022','04.12.2022','11.12.2022',
      '18.12.2022','25.12.2022'],
	  formatDate:'d.m.Y',
    minDate: tomorrow,
  });
});

// MESSAGES

// https://github.com/studygyaan/Django-CRM-Project

setTimeout(function(){
  if ($('#msg').length > 0) {
    $('#msg').remove();
  }
}, 2000)