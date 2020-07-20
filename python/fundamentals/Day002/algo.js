function reverseString(str_input) {
  var temp = ""
  for(var i = 0; i < str_input.length; i++) {
    temp = str_input[i]+ temp;
  }
  return temp;
}
console.log(reverseString("spaghetti"))

// var reverseStringResult = reverseString("spaghetti")
// -> "ittehgaps"

function isPalindrome(str_input) {
  var x = str_input.length - 1
  var equal_or_naw = false
  var left = []
  var right = []

  for(var i= 0; i < str_input.length-1 / 2; i++) {
    left.push(str_input[i])
    right.push(str_input[x])
    if(left[0] == right[0]) {
      equal_or_naw = true
      left.pop()
      right.pop()

    }else if (left !== right) {
      equal_or_naw = false
      return equal_or_naw
    }
  }
  return equal_or_naw
}

var isPalindromeResultOne = isPalindrome("tacocat");
console.log(isPalindromeResultOne);