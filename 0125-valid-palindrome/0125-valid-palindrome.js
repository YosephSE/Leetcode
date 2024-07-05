/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s = s.toLowerCase()
    let alphaNumericValues = ""
    for(i = 0; i < s.length; i++){
        let letter = s.charAt(i)
        let cc = s.charCodeAt(i)

        if ((cc > 47 && cc < 58) || (cc > 64 && cc < 91) || (cc > 96 && cc < 123)) {
            alphaNumericValues += letter
        }

    }
    if (alphaNumericValues === alphaNumericValues.split("").reverse().join("")){
        return true
    }else{
        return false
    }
};