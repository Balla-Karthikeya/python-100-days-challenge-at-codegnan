let input = document.getElementById("display");

// console.log(input.value="")
let btn = document.getElementsByTagName("button");

console.log(btn);


let btn1 = ()=>{
    input.value += 1
}


let btn2 = ()=>{
    input.value += 2
}
let btn3 = ()=>{
    input.value += 3
}
let btn4 = ()=>{
    input.value += 4
}
let btn5 = ()=>{
    input.value += 5
}
let btn6 = ()=>{
    input.value += 6
}
let btn7 = ()=>{
    input.value += 7
}
let btn8 = ()=>{
    input.value += 8
}
let btn9 = ()=>{
    input.value += 9
}

// cler all values
let DELETE = ()=>{
    input.value = 0
}


// clear last value
let CLEAR = ()=>{
    input.value = input.value.slice(0,-1)
}

// equal
let EQUAL = ()=>{
    input.value = eval(input.value)
}

// dot
let DOT = ()=>{
    input.value += "."
}

// percent
let PERCENT = ()=>{
    input.value = input.value/100
}

// add
let ADD = ()=>{
    input.value += "+"
}

// minus
let MINUS = ()=>{
    input.value += "-"
}

// multiply
let MULTIPLY = ()=>{
    input.value += "*"
}

// divide
let DIVIDE = ()=>{
    input.value += "/"
}


let img = document.getElementById("box1");

let array =[ "👦","😊","🛻" ]


let emoji = ()=>{
    let random = Math.floor(Math.random()*array.length)
     img.innerHTML = array[random]
}