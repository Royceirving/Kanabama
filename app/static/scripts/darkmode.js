dark_mode = false;


function change_mode() {

    var cssfirstlink = document.getElementsByTagName("link").item(0);
    if (dark_mode==false) {
      cssfirstlink.href = "static/styles/dark-storystyle.css";
      dark_mode = true;
    } else {
      cssfirstlink.href = "static/styles/storystyle.css";
      dark_mode = false;
    }
}

// function real_change_mode(to_change) {
//   var cssfirstlink = document.getElementsByTagName("link").item(0);
//   if (to_change==true) {
//     cssfirstlink.href = "static/styles/dark-storystyle.css";
//   } else {
//     cssfirstlink.href = "static/styles/storystyle.css";
//   }
// }
