// set up all the 'More Details' buttons (in the project headers)

var acc_buttons = document.getElementsByClassName('details');
var i;
for (i = 0;i < acc_buttons.length;i++){
  acc_buttons[i].addEventListener('click', function(){
    // change the text of the button
    if (this.innerHTML === "--- More Details ---"){
      this.innerHTML = "--- Less Details ---";
    }else{
      this.innerHTML = "--- More Details ---";
    }
    // chance the display state of the details panel
    var panel = this.nextElementSibling;
    if (panel.style.display === 'block'){
      panel.style.display = 'none';
    }else{
      panel.style.display = 'block';
    }
  });
}
