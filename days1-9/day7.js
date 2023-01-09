const fs = require('fs')
let content = fs.readFileSync('./day7input.txt', 'utf8', (err, data) => {
    if (err) throw err;
    return data;
})

let contentArray = content.split('\n');

for (let i = 0; i < contentArray.length - 1; i++) {
    contentArray[i] = contentArray[i].split(' ')
}

const lineReader = (contentArray) => {
    let whereWeAre = []
    let dirCount = 0
    let sizeArray = [['/', 0]]
    for (let i = 0; i < contentArray.length - 1; i++) {
        if (contentArray[i][1] == 'cd') {
            if (contentArray[i][2] == '..') {
                whereWeAre.pop()
            } else {
                whereWeAre.push(contentArray[i][2])
            }
        }
        if (contentArray[i][0] == 'dir') {
            let push = []
            dirCount++
            push.push(...whereWeAre)
            push.push(contentArray[i][1])
            push.push(0)
            sizeArray.push(push)
        }
        if (/\d/.test(contentArray[i][0])) {
            
            for (let j = 0; j < sizeArray.length; j++) {
                let check = sizeArray[j].slice(0, -1)
                if (JSON.stringify(check) === JSON.stringify(whereWeAre)) {
                    sizeArray[j][sizeArray[j].length - 1] += parseInt(contentArray[i][0])
                }
            }
        }
    }
    console.log(dirCount)
    return sizeArray
}
const arrayForSorting = lineReader(contentArray)

let total = 0

const reducer = (arrayForSorting) => {
    arrayForSorting.sort()
    // console.log(arrayForSorting)
    for (let i = 0; i < arrayForSorting.length; i++) {
        for (let j = i + 1; j < arrayForSorting.length; j++) {
            if (arrayForSorting[j].slice(0, arrayForSorting[i].length - 1).toString() == arrayForSorting[i].slice(0, arrayForSorting[i].length - 1).toString()) {
                arrayForSorting[i][arrayForSorting[i].length - 1] += arrayForSorting[j].at(-1)
            }
            
        }
    }
    // console.log(arrayForSorting)
    for (let i = 0; i < arrayForSorting.length; i++) {
        if (arrayForSorting[i].at(-1) <= 100000) {
            total += arrayForSorting[i].at(-1)
        }
    }
    return arrayForSorting
}
const sortedArray = reducer(arrayForSorting)

const dirFinder = (sortedArray) => {
    console.log(sortedArray[0].at(-1))
    let needToFree = sortedArray[0].at(-1) - (70000000 - 30000000) 
    console.log(needToFree)
    let currentDirSize = [sortedArray[0].at(-1)]
    let count = 0
    // sortedArray[0].at(-1)
    for (let i = 1; i < sortedArray.length; i++) {
        count++
        // console.log(currentDirSize, sortedArray[i].at(-1), 8381165 <= sortedArray[i].at(-1) && sortedArray[i].at(-1) < currentDirSize.at(-1))
        if (needToFree <= sortedArray[i].at(-1) && sortedArray[i].at(-1) < currentDirSize.at(-1) ) {
            currentDirSize.push(sortedArray[i].at(-1))
        }
    }
    console.log(count)
    return currentDirSize
}

console.log(dirFinder(sortedArray))