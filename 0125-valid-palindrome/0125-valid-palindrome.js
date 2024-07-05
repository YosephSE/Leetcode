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
    let left = 0, right = alphaNumericValues.length - 1
    while (left < right){
        if (alphaNumericValues[left] !== alphaNumericValues[right]){
            return false
        }
        left++
        right--
    }
    return true
};