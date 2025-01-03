const startButton = document.querySelector("#startBtn");
const stopButton = document.querySelector("#stopBtn");
const resetButton = document.querySelector("#resetBtn");
const deleteButton = document.querySelector("#delete_button");

// 타이틀의 체크박스
const listTitleCheckbox = document.querySelector("#list-title input[type='checkbox']");

// 타이머 시간 표시 초기화
const timer_sec = document.querySelector("#timer-sec");
const timer_msec = document.querySelector("#timer-msec");

// 구간 기록 부분 초기화
const list = document.querySelector("#list");

let sec = 0;
let msec = 0;
let interval;
let isTimerRunning = false;

//============= 버튼 부분 구현 ===============

// 타이머 시작
function startTimer() {
    interval = setInterval(() => {
        msec++;
        if (msec >= 100) {
            msec = 0;
            sec++;
        }
        timer_sec.textContent = sec.toString().padStart(2, '0');
        timer_msec.textContent = msec.toString().padStart(2, '0');
    }, 10);
}

// 타이머 멈춤, 재시작
function stopTimer() {
    if (isTimerRunning) {
        clearInterval(interval);
        isTimerRunning = false;
        addListItem(sec, msec);  // STOP 버튼을 누를 때 자식 항목 추가
    } else {
        startTimer();
        isTimerRunning = true;
    }
}

// 타이머 재시작 
function resetTimer() {
    clearInterval(interval);
    sec = 0;
    msec = 0;
    timer_msec.textContent = "00";
    timer_sec.textContent = "00";
    isTimerRunning = false;
}

// 버튼마다 이벤트 설정
startButton.addEventListener("click", () => {
    startTimer();
    isTimerRunning = true;
});
stopButton.addEventListener("click", () => {
    stopTimer();
});
resetButton.addEventListener("click", () => {
    resetTimer();
});

// ===================== 체크박스 리스트 구현 ==================

// 리스트 항목 추가 함수
function addListItem(sec, msec) {
    const listItem = document.createElement("div");
    listItem.classList.add("list-item");

    const listText = document.createElement("span");
    listText.textContent = `${sec.toString().padStart(2, '0')}:${msec.toString().padStart(2, '0')}`;

    const listCheckbox = document.createElement("input");
    listCheckbox.type = "checkbox";
    listCheckbox.addEventListener("change", updateListTitleCheckbox);

    const emptyDiv = document.createElement("div");

    listItem.append(listCheckbox);
    listItem.append(listText);
    listItem.append(emptyDiv);
    list.appendChild(listItem);

    updateListTitleCheckbox();
}

listTitleCheckbox.addEventListener("change", () => {
    const checkboxes = document.querySelectorAll("#list .list-item input[type='checkbox']");
    checkboxes.forEach(checkbox => {
        checkbox.checked = listTitleCheckbox.checked;
    });
    updateDeleteButtonState();
});

function updateListTitleCheckbox() {
    const checkboxes = document.querySelectorAll("#list .list-item input[type='checkbox']");
    const allChecked = Array.from(checkboxes).every(checkbox => checkbox.checked);
    const anyChecked = Array.from(checkboxes).some(checkbox => checkbox.checked);
    listTitleCheckbox.checked = allChecked;
    listTitleCheckbox.indeterminate = !allChecked && anyChecked;
    updateDeleteButtonState();
}

deleteButton.addEventListener("click", () => {
    const checkedItems = document.querySelectorAll("#list .list-item input[type='checkbox']:checked");
    checkedItems.forEach(checkbox => {
        checkbox.parentElement.remove(); 
    });
    updateListTitleCheckbox(); 
    updateDeleteButtonState();
});

// 삭제 버튼 활성화 상태 업데이트
function updateDeleteButtonState() {
    const checkedItems = document.querySelectorAll("#list .list-item input[type='checkbox']:checked");
    deleteButton.disabled = checkedItems.length === 0;
}
