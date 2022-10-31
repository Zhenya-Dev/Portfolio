const menuArrow = document.querySelector('.menu__arrow');
const headerBurger = document.querySelector('.header__burger');
const menu = document.querySelector('.header__menu');
const headerSocial = document.querySelectorAll('.header__social');
const menuSubLink = document.querySelectorAll('.menu__sub-link');
const body = document.querySelector('body');

headerBurger.onclick = () => {
    body.classList.toggle('active')
    menu.classList.toggle('active')
    headerBurger.classList.toggle('active')
    headerSocial.classList.toggle('active')
}
