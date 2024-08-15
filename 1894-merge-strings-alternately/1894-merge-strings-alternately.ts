function mergeAlternately(word1: string, word2: string): string {
    let result: string = ''
    let longest: number = word1.length > word2.length ? word1.length: word2.length;
    for(let i = 0; i < longest; i++){
        word1[i] != undefined ? result += word1[i]: null;
        word2[i] != undefined ? result += word2[i]: null;
    }
    return result
};
