document.getElementById("searchBtn").addEventListener("click", async () => {
  const carNumber = document.getElementById("carNumber").value;
  const parkingTime = document.getElementById("parkingTime").value;

  try {
    const response = await fetch("http://localhost:5050/check-car", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        car_number: carNumber,
        parking_time: parseInt(parkingTime),
      }),
    });

    const data = await response.json();
    document.getElementById("result").textContent = JSON.stringify(data);
  } catch (error) {
    console.error("Error:", error);
    document.getElementById("result").textContent = "오류가 발생했습니다.";
  }
});

// 초기화 상태 확인
async function checkInitStatus() {
  const response = await fetch("http://localhost:5000/init-status");
  const data = await response.json();

  if (data.status === "not_initialized") {
    // 초기화 시작
    document.getElementById("status").textContent =
      "시스템을 초기화하는 중입니다...";
    document.getElementById("carNumberInput").disabled = true;

    await fetch("http://localhost:5000/initialize", { method: "POST" });
    await waitForInitialization();
  } else if (data.status === "initializing") {
    document.getElementById("status").textContent = "초기화 중입니다...";
    document.getElementById("carNumberInput").disabled = true;
    await waitForInitialization();
  } else {
    document.getElementById("status").textContent = "시스템이 준비되었습니다.";
    document.getElementById("carNumberInput").disabled = false;
  }
}

async function waitForInitialization() {
  const statusElement = document.getElementById("status");
  const inputElement = document.getElementById("carNumberInput");

  while (true) {
    try {
      const response = await fetch("http://localhost:5000/init-status");
      const data = await response.json();

      statusElement.textContent = data.message;

      if (data.status === "ready") {
        inputElement.disabled = false;
        break;
      } else {
        inputElement.disabled = true;
      }
    } catch (error) {
      statusElement.textContent = "서버 연결 중...";
      inputElement.disabled = true;
    }

    // 더 짧은 간격으로 상태 체크
    await new Promise((resolve) => setTimeout(resolve, 500));
  }
}

// 페이지 로드 시 즉시 로딩 상태 표시 및 초기화 시작
window.addEventListener("load", async () => {
  const statusElement = document.getElementById("status");
  const inputElement = document.getElementById("carNumberInput");

  statusElement.textContent = "시스템을 시작하는 중입니다...";
  inputElement.disabled = true;

  // 초기화 시작
  await fetch("http://localhost:5000/initialize", { method: "POST" });
  await waitForInitialization();
});
