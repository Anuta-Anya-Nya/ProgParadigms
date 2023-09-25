// используются структурная и процедурная парадигмы 

const hours = document.querySelector('.hours');
const minutes = document.querySelector('.minutes');
const seconds = document.querySelector('.seconds');

const start = document.querySelector('#start');
const stop = document.querySelector('#stop');
const pause = document.querySelector('#pause');
const playAgain = document.querySelector('#play_again');

let countHours = 0;
let countMin = 0;
let countSec = 0;
let timerId;

const printStopwatch = () => {
    hours.innerHTML = String(countHours).padStart(2, '0');
    minutes.innerHTML = String(countMin).padStart(2, '0');
    seconds.innerHTML = String(countSec).padStart(2, '0');
}
const secStopWatch = () => {
    countSec++;
    if (countSec > 59) {
        countMin++;
        countSec = 0;
    }
    if (countMin > 59) {
        countHours++;
        countMin = 0;
    }
    printStopwatch();
}

start.addEventListener('click', () => {
    timerId = setInterval(() => {
        secStopWatch()
    }, 1000)
});

stop.addEventListener('click', () => {
    clearInterval(timerId);
    countSec = countMin = countHours = 0;
    printStopwatch();
    start.disabled = false;
    playAgain.disabled = true;
})

pause.addEventListener('click', () => {
    clearInterval(timerId);
    playAgain.disabled = false;
})

playAgain.addEventListener('click', () => {
    timerId = setInterval(() => {
        secStopWatch();
        playAgain.disabled = true;
        start.disabled = true;
    }, 1000)
})

start.addEventListener('click', () => {
    start.disabled = true;
})

