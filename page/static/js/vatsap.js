var close_button = document.querySelector(".close-button");
var social_buttons = document.querySelectorAll(".social");

close_button.addEventListener('click',()=>{
   social_buttons.forEach(function(buttons){
       buttons.classList.toggle('hide');
   });
});