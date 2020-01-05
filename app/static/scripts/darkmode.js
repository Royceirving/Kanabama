dark_mode = false;

function change_mode(){
  console.log("Changed!");
  if (dark_mode==false) {
    var link = document.getElementById("lightdarkstoryboard"); //Fetch the link by its ID
    link.setAttribute("href", "{{ url_for('static', filename='styles/storystyle.css') }}"); //Change its href attribute
    dark_mode = true;
  } else {
    var link = document.getElementById("lightdarkstoryboard"); //Fetch the link by its ID
    link.setAttribute("href", "{{ url_for('static', filename='styles/dark-storystyle.css') }}"); //Change its href attribute
    dark_mode = false;
  }
}
