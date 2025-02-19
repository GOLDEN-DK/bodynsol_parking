const { app, BrowserWindow } = require("electron");
const path = require("path");
const { spawn } = require("child_process");

let pyProc = null;

function startPythonServer() {
  return new Promise((resolve, reject) => {
    console.log("Flask 서버 시작 중...");

    // 백엔드 디렉토리의 절대 경로 구성
    const scriptPath = path.join(__dirname, "..", "backend", "main.py");
    console.log("Python 스크립트 경로:", scriptPath);

    // 가상환경의 Python 실행 파일 경로 설정
    const pythonPath =
      process.platform === "win32"
        ? path.join(__dirname, "..", "venv", "Scripts", "python.exe")
        : path.join(__dirname, "..", "venv", "bin", "python");
    console.log("Python 실행 경로:", pythonPath);

    try {
      pyProc = spawn(pythonPath, [scriptPath], {
        // 작업 디렉토리를 backend로 설정
        cwd: path.join(__dirname, "..", "backend"),
        // 환경변수 설정
        env: {
          ...process.env,
          PYTHONPATH: path.join(__dirname, "..", "backend"),
        },
      });

      pyProc.stdout.on("data", (data) => {
        console.log(`Python 출력: ${data}`);
      });

      pyProc.stderr.on("data", (data) => {
        console.error(`Python 에러: ${data}`);
      });

      pyProc.on("error", (err) => {
        console.error("Python 프로세스 시작 실패:", err);
        reject(err);
      });

      // Flask 서버가 시작될 때까지 대기
      let serverStarted = false;
      const checkServer = async () => {
        try {
          const response = await fetch("http://localhost:5050/init-status");
          if (response.ok) {
            console.log("Flask 서버 시작 완료");
            serverStarted = true;
            resolve();
          }
        } catch (error) {
          console.log("서버 연결 대기 중...", error.message);
          if (!serverStarted) {
            setTimeout(checkServer, 1000);
          }
        }
      };

      // 첫 번째 체크 시작
      setTimeout(checkServer, 1000);

      // 30초 후에도 서버가 시작되지 않으면 타임아웃
      setTimeout(() => {
        if (!serverStarted) {
          reject(new Error("Flask 서버 시작 타임아웃"));
        }
      }, 30000);
    } catch (error) {
      console.error("Python 프로세스 생성 중 오류:", error);
      reject(error);
    }
  });
}

async function initializeAutomation() {
  try {
    console.log("자동화 시스템 초기화 시작...");
    const response = await fetch("http://localhost:5050/initialize", {
      method: "POST",
    });
    const data = await response.json();
    console.log("초기화 결과:", data);
    return data;
  } catch (error) {
    console.error("초기화 중 오류 발생:", error);
    throw error;
  }
}

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  win.loadFile("index.html");

  // 개발 도구 열기 (디버깅용)
  win.webContents.openDevTools();
}

// Node 18 이상에서는 fetch가 전역으로 사용 가능
if (!globalThis.fetch) {
  globalThis.fetch = require("node-fetch");
}

app.whenReady().then(async () => {
  try {
    console.log("Electron 앱 시작...");
    await startPythonServer();
    await initializeAutomation();
    createWindow();
  } catch (error) {
    console.error("앱 초기화 중 오류 발생:", error);
    app.quit();
  }
});

app.on("window-all-closed", () => {
  // Python 프로세스 종료
  if (pyProc) {
    console.log("Python 프로세스 종료 중...");
    pyProc.kill();
    pyProc = null;
  }

  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
