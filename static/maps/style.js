function styleitem() {
  var cls = "CLASS";

  //Make symbol size 14 or 7
  var size = shape.attributes.NAME.length > 10 ? 14:7;

  var style1 = "STYLE SIZE " + size + " SYMBOL 'circle'";
  var style2 = "STYLE SIZE " + size + " SYMBOL 'cross'";

  var red = Math.random()*255;
  var green = Math.random()*255;
  var blue = Math.random()*255;
  style1 += "COLOR " + red + " " + green + " " + blue + " END";
  style2 += "COLOR " + red + " " + green + " " + blue + " END";

  cls += " " + style1 + " " + style2 + " END";

  //Return class to MapServer
  return cls;
}