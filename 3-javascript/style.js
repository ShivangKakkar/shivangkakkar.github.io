const id = "shape";
const bestId = "best";
const timeId = "time";

document.getElementById("best").style.display = "none";

function random(limit) {
    return Math.floor(Math.random() * limit)
}

function getRandomColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function useRandomStyle() {
    document.getElementById(id).style.width = random(100) + 100 + "px"
    document.getElementById(id).style.height = random(100) + 100 + "px"
    document.getElementById(id).style.top = random(300) + "px"
    document.getElementById(id).style.left = random(800) + "px"
    document.getElementById(id).style.backgroundColor = getRandomColor();
    let items = ["50", "0"];
    let item = items[Math.floor(Math.random() * items.length)];
    document.getElementById(id).style.borderRadius = item + "%"
    document.getElementById(id).style.display = "";
}

function gayab() {
    document.getElementById(id).style.display = "none";
}

let startTime = new Date().getTime();

function appearAfterDelay() {
    const randomTime = Math.floor(Math.random() * 2000);
    startTime = new Date().getTime() + randomTime;
    setTimeout(useRandomStyle, randomTime);
}

var bestScore;

function setBestScore(diff) {
    if (!bestScore || diff < bestScore) {
        bestScore = diff
    }
    let ans = "Best Score: " + bestScore + "s";
    if (bestScore == diff) {
        ans = "New " + ans
    }
    document.getElementById(bestId).innerHTML = ans;
    document.getElementById(bestId).style.display = "";
}

let timeText = document.getElementById(timeId).innerHTML + " "

function setTime(diff) {
    document.getElementById(timeId).innerHTML = timeText + diff + "s"
}

useRandomStyle();

let shape = document.getElementById(id);

shape.onclick = () => {
    const endTime = new Date().getTime();
    let diff = (endTime - startTime) / 1000;
    console.log(diff);
    setTime(diff);
    setBestScore(diff);
    
    gayab();
    appearAfterDelay();
}
