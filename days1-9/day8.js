const fs = require('fs')
let content = fs.readFileSync('./day8input.txt', 'utf8', (err, data) => {
    if (err) throw err;
    return data;
})

let contentArray = content.split('\n');
if (!contentArray.at(-1)[0]) contentArray.pop()
const visFinder = (contentArray) => {
    let visibles = 0
    for (let i = 0; i < contentArray.length; i++) {
        for (let j = 0; j < contentArray[i].length; j++) {

            if (i == 0 || j == 0 || i == contentArray.length - 1 || j == contentArray[i].length - 1) {
                visibles++
            } else {
                let visibleSides = ["visible", "visible", "visible", "visible"]
                for (let k = 0; k < contentArray.length; k++) {
                    for (let l = 0; l < contentArray[k].length; l++) {
                        if (k < i && l == j && contentArray[k][l] >= contentArray[i][j]) {
                            visibleSides[0] = "not visible"
                        } else if (k > i && l == j && contentArray[k][l] >= contentArray[i][j]) {
                            visibleSides[1] = "not visible"
                        } else if (k == i && l < j && contentArray[k][l] >= contentArray[i][j]) {
                            visibleSides[2] = "not visible"
                        } else if (k == i && l > j && contentArray[k][l] >= contentArray[i][j]) {
                            visibleSides[3] = "not visible"
                        }
                    }
                }
                if (visibleSides.includes("visible")) visibles++
            }
        }
        
    }
    return visibles
}

const scenicScorer = (contentArray) => {
    let score = [0, 0, 0]
    for (let i = 0; i < contentArray.length; i++) {
        for (let j = 0; j < contentArray[i].length; j++) {
            let up = 0;
            let down = 0;
            let left = 0;
            let right = 0;
            if (i > 0) {
                for (let k = i - 1; k >= 0; k--) {
                    up++
                    if (contentArray[k][j] >= contentArray[i][j]) {
                        break
                    }
                }
            }
            if (j > 0) {
                for (let k = j - 1; k >= 0; k--) {
                    left++
                    if (contentArray[i][k] >= contentArray[i][j]) {
                        break
                    }
                }
            }
            if (i < contentArray.length - 1) {
                for (let k = i + 1; k < contentArray.length; k++) {
                    down++
                    if (contentArray[k][j] >= contentArray[i][j]) {
                        break
                    }
                }
            }
            if (j < contentArray[i].length - 1) {
                for (let k = j + 1; k < contentArray[i].length; k++) {
                    right++
                    if (contentArray[i][k] >= contentArray[i][j]) {
                        break
                    }
                }
            }
            if (up * down * left * right > score[0]) {
                score = [up * down * left * right, i, j]
            }
            console.log(i, j, up, down, left, right, score, contentArray[i][j])
        }
    }
        
    
    return score
}

// console.log("part 1 => ", visFinder(contentArray))
console.log("part 2 => ", scenicScorer(contentArray))