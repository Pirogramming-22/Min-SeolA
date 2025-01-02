let answerNum = []; // 정답 배열
let attempts = 9; // 남은 시도 횟수

// 남은 시도 횟수 초기화
document.getElementById("attempts").innerText = attempts;

// 중복되지 않는 랜덤 숫자 3개 생성
while (answerNum.length < 3) {
    let randomNum = Math.floor(Math.random() * 10);
    if (!answerNum.includes(randomNum)) answerNum.push(randomNum);
}

function check_numbers() {
    const number1 = document.getElementById("number1").value;
    const number2 = document.getElementById("number2").value;
    const number3 = document.getElementById("number3").value;

    if (number1 === '' || number2 === '' || number3 === '') {
        document.getElementById("number1").value = '';
        document.getElementById("number2").value = '';
        document.getElementById("number3").value = '';
        return;
    }

    const userInputNum = [parseInt(number1), parseInt(number2), parseInt(number3)];
    const { strike } = inputResult(userInputNum);

    // 입력 필드 초기화
    document.getElementById("number1").value = '';
    document.getElementById("number2").value = '';
    document.getElementById("number3").value = '';

    // 시도 횟수 감소
    attempts--;
    document.getElementById("attempts").innerText = attempts;

    // 게임 종료 조건 확인
    if (strike === 3) {
        finalResult(true);
    } else if (attempts === 0) {
        finalResult(false);
    }
}

function inputResult(inputNum) {
    let strike = 0;
    let ball = 0;

    // 스트라이크와 볼 계산
    for (let i = 0; i < 3; i++) {
        if (inputNum[i] === answerNum[i]) {
            strike++;
        } else if (answerNum.includes(inputNum[i])) {
            ball++;
        }
    }

    // 결과를 화면에 표시
    const resultDisplay = document.querySelector(".result-display");

    const resultContainer = document.createElement("div");
    resultContainer.classList.add("check-result");

    // 입력값 표시
    const inputSpan = document.createElement("span");
    inputSpan.classList.add("num-result");
    inputSpan.innerText = inputNum.join(" ");

    // 구분자 `:` 표시
    const dividerSpan = document.createElement("span");
    dividerSpan.innerText = " : ";

    // 결과 표시
    const resultSpan = document.createElement("span");
    if (strike === 0 && ball === 0) {
        resultSpan.innerHTML = `<span class="num-result out">O</span>`;
    } else {
        resultSpan.innerHTML = `
            <span class="num-result strike">S</span><span>${  strike}</span>
            <span class="num-result ball">B</span><span>${  ball}</span>
        `;
    }

    // 결과 컨테이너에 추가
    resultContainer.appendChild(inputSpan);
    resultContainer.appendChild(dividerSpan);
    resultContainer.appendChild(resultSpan);

    resultDisplay.appendChild(resultContainer);

    return { strike, ball };
}

function finalResult(success) {
    const finalResultImg = document.getElementById("game-result-img");
    const button = document.querySelector(".submit-button");
    button.disabled = true;

    if (success) {
        finalResultImg.src = "success.png";
    } else {
        finalResultImg.src = "fail.png";
    }
}
