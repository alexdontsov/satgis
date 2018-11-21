function styleitem() {
  var cls = "CLASS";

  var red = Math.random()*255;
  var green = Math.random()*255;
  var blue = Math.random()*255;
  style1 += "COLOR " + red + " " + green + " " + blue + " END";
  style2 += "COLOR " + red + " " + green + " " + blue + " END";

  cls += " " + style1 + " " + style2 + " END";

  //Return class to MapServer
  return cls;
}