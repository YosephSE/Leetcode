/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let result = ''
    let longest = word1.length > word2.length ? word1.length: word2.length;
    for( i = 0; i < longest; i++){
        word1[i] != undefined ? result += word1[i]: null;
        word2[i] != undefined ? result += word2[i]: null;
    }
    return result
};