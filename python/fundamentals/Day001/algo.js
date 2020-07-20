function remove_blank(str) {

    var newstr = ""

    for (var i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            newstr += str[i]
    }
  }
  return newstr 
}

var fresh_new_string = remove_blank("Hello my name is Babul")
console.log(fresh_new_string)

function getDigits(str) {
  var digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  var str2 = '';
  for(var i = 0; i < str.length; i++) {
    if(str[i] in digits) {
      str2 = str[i];
    }
  }
  return str2;
}

console.log(getDigits('a1b2c3'))
console.log("1"== 1)
console.log("1"=== 1)