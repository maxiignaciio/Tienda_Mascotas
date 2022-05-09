function myFunction() {
    var x = document.getElementById("formGroupExampleInput2");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }