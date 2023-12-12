export function narcissistic(positiveValue: number) {
    let stringValue = positiveValue.toString()
    let isNarcissistic = true
    let computation = 0

    if(stringValue.length !== 1) {
        for(let charValue of stringValue)
            computation += Math.pow(Number(charValue), stringValue.length)
        
        isNarcissistic = positiveValue === computation
    }

    return isNarcissistic
}