




function liked(){
    var element = document.getElementById("like");
    element.classList.toggle("liked");
  }


BTN = document.getElementById('submit-at')
TEXT = document.getElementById('textinput')

function BLOCK() {
	if (TEXT.value == '') {
		BTN.disabled = true;
	}
	else if (TEXT.value != '') {
		BTN.disabled = false;
	}
}

TEXT.addEventListener('input', BLOCK);






document.addEventListener('DOMContentLoaded', function() {

    const end_date = new Date("2034-04-16");

    function countdownTimer() {
        const diff = end_date - new Date();
        const years = diff > 0 ? Math.floor(diff / 1000 / 60 / 60 / 24 / 365) : 0;
        const days = diff > 0 ? Math.floor(diff / 1000 / 60 / 60 / 24) % 365: 0;
        const hours = diff > 0 ? Math.floor(diff / 1000 / 60 / 60) % 24 : 0;
        const minutes = diff > 0 ? Math.floor(diff / 1000 / 60) % 60 : 0;
        const seconds = diff > 0 ? Math.floor(diff / 1000) % 60 : 0;
        $years.textContent = years < 10 ? '0' + years : years;
        $days.textContent = days < 10 ? '0' + days : days;
        $hours.textContent = hours < 10 ? '0' + hours : hours;
        $minutes.textContent = minutes < 10 ? '0' + minutes : minutes;
        $seconds.textContent = seconds < 10 ? '0' + seconds : seconds;
    }

    const $years = document.querySelector('.years');
    const $days = document.querySelector('.days');
    const $hours = document.querySelector('.hours');
    const $minutes = document.querySelector('.minutes');
    const $seconds = document.querySelector('.seconds');
    countdownTimer();
    timerId = setInterval(countdownTimer, 1000);

});



