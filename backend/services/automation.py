from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class AutomationService:
    def __init__(self):
        self.driver = None
        self.logged_in = False
        self.base_url = "http://kmp0000673.iptime.org/cooperators/home"
        self.credentials = {
            "username": "바디앤솔",
            "password": "2728"
        }
        self.is_initialized = False
    
    def init_driver(self):
        if not self.driver:
            print("[DEBUG] 크롬 브라우저 초기화 시작")
            self.is_initialized = False  # 초기화 상태 리셋
            
            try:
                service = Service(ChromeDriverManager().install())
                options = webdriver.ChromeOptions()
                options.add_argument('--start-maximized')
                
                print("[DEBUG] 크롬 드라이버 생성 중...")
                self.driver = webdriver.Chrome(service=service, options=options)
                self.driver.implicitly_wait(5)
                
                print("[DEBUG] 로그인 시도 중...")
                login_success = self.login()
                if login_success:
                    self.is_initialized = True
                    print("[DEBUG] 크롬 브라우저 초기화 및 로그인 완료")
                else:
                    print("[ERROR] 초기 로그인 실패")
                    self.cleanup()
            except Exception as e:
                print(f"[ERROR] 브라우저 초기화 중 오류 발생: {str(e)}")
                self.cleanup()
                return False
                
        return self.is_initialized
    
    def get_initialization_status(self):
        """
        현재 초기화 상태를 반환
        """
        try:
            if not self.driver:
                return {
                    "status": "not_initialized",
                    "message": "크롬 브라우저를 시작하는 중입니다..."
                }
            
            if not self.is_initialized:
                return {
                    "status": "initializing",
                    "message": "로그인을 진행하는 중입니다..."
                }
            
            # 드라이버 상태 확인
            self.driver.current_url
            return {
                "status": "ready",
                "message": "시스템이 준비되었습니다."
            }
        except:
            self.driver = None
            self.logged_in = False
            self.is_initialized = False
            return {
                "status": "error",
                "message": "브라우저 연결이 끊어졌습니다. 재시작이 필요합니다."
            }
    
    def ensure_initialized(self):
        """
        시스템이 초기화되지 않았다면 초기화 수행
        """
        if not self.is_initialized:
            return self.init_driver()
        return True
    
    def login(self):
        try:
            self.driver.get(self.base_url)
            
            # 예기치 않은 알림창 처리
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
            except:
                pass
            
            # XPath를 사용하여 로그인 폼 요소 찾기
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="form-login-username"]'))
            )
            password_input = self.driver.find_element(By.XPATH, '//*[@id="form-login-password"]')
            
            username_input.send_keys(self.credentials["username"])
            password_input.send_keys(self.credentials["password"])
            
            # XPath를 사용하여 로그인 버튼 찾기
            login_button = self.driver.find_element(By.XPATH, '//*[@id="form-login"]/div[3]/button')
            login_button.click()
            
            # 로그인 후 발생할 수 있는 알림창 처리
            try:
                alert = WebDriverWait(self.driver, 3).until(EC.alert_is_present())
                alert.accept()
            except:
                pass
            
            # 로그인 성공 확인
            time.sleep(2)  # 로그인 처리 대기
            self.logged_in = True
            return True
            
        except Exception as e:
            print(f"Login failed: {str(e)}")
            return False
    
    def search_car(self, car_number):
        try:
            print(f"[DEBUG] 차량 검색 시작: {car_number}")
            
            # 드라이버 상태 확인 및 재초기화
            try:
                if self.driver:
                    # 드라이버 상태 확인
                    self.driver.current_url
            except:
                print("[DEBUG] 드라이버 세션 종료됨, 재초기화 시작")
                self.driver = None
                self.logged_in = False
            
            # 드라이버 초기화 확인
            if not self.driver:
                print("[DEBUG] 드라이버 초기화 시작")
                self.init_driver()
                print("[DEBUG] 드라이버 초기화 완료")
            
            # 로그인 상태 확인 및 로그인 수행
            if not self.logged_in:
                print("[DEBUG] 로그인 시도")
                login_success = self.login()
                if not login_success:
                    print("[ERROR] 로그인 실패")
                    return {
                        "status": "error",
                        "message": "로그인에 실패했습니다."
                    }
                print("[DEBUG] 로그인 성공")
            
            # 메인 페이지로 이동
            print(f"[DEBUG] 페이지 이동 시도: {self.base_url}")
            self.driver.get(self.base_url)
            
            # URL 이동 확인
            current_url = self.driver.current_url
            print(f"[DEBUG] 현재 URL: {current_url}")
            if not current_url.startswith(self.base_url):
                print(f"[ERROR] 잘못된 페이지로 이동: {current_url}")
                return {
                    "status": "error",
                    "message": f"페이지 이동 실패. 현재 URL: {current_url}"
                }
            print("[DEBUG] 페이지 이동 성공")
            
            # 페이지 로드 완료 대기
            try:
                print("[DEBUG] 페이지 로드 대기 시작")
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, "app"))
                )
                print("[DEBUG] 페이지 로드 완료")
            except Exception as e:
                print(f"[ERROR] 페이지 로드 실패: {str(e)}")
                return {
                    "status": "error",
                    "message": f"페이지 로드 실패: {str(e)}"
                }
            
            # 차량번호 입력 필드가 나타날 때까지 명시적 대기
            search_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="visit-lpn"]'))
            )
            
            # 기존 입력값 지우기
            search_input.clear()
            time.sleep(1)  # 입력 필드 초기화 대기
            
            # 차량번호 입력
            search_input.send_keys(car_number)
            time.sleep(1)  # 입력 완료 대기
            
            # 검색 버튼이 클릭 가능할 때까지 대기 후 클릭
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="btn-find"]'))
            )
            search_button.click()
            
            # 검색 결과 로딩 대기
            time.sleep(2)
            
            # 결과 테이블 확인
            try:
                table = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "gbox-table"))
                )
                
                # 차량 이미지 찾기
                image_elem = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "img[src*='car_images']"))
                )
                image_url = image_elem.get_attribute('src')
                
                return {
                    "status": "success",
                    "image_url": image_url,
                    "message": "차량 이미지를 찾았습니다."
                }
            except Exception as e:
                return {
                    "status": "error",
                    "message": "차량 이미지를 찾을 수 없습니다."
                }
                
        except Exception as e:
            print(f"[ERROR] 예외 발생: {str(e)}")
            # 심각한 오류 발생 시 드라이버 재초기화를 위해 상태 초기화
            self.driver = None
            self.logged_in = False
            return {
                "status": "error",
                "message": f"차량 검색 중 오류 발생: {str(e)}"
            }
    
    def apply_parking_time(self, parking_time):
        try:
            # 주차시간 버튼 찾기 및 클릭
            if parking_time == 30:
                time_button = self.driver.find_element(By.ID, "time_30min")
            elif parking_time == 60:
                time_button = self.driver.find_element(By.ID, "time_60min")
            elif parking_time == 90:
                # 1시간 30분은 1시간 + 30분 버튼 클릭
                time_button_1h = self.driver.find_element(By.ID, "time_60min")
                time_button_30m = self.driver.find_element(By.ID, "time_30min")
                time_button_1h.click()
                time.sleep(1)
                time_button_30m.click()
                return {"status": "success", "message": "주차시간 설정 완료"}
            
            time_button.click()
            return {"status": "success", "message": "주차시간 설정 완료"}
            
        except Exception as e:
            return {
                "status": "error",
                "message": f"주차시간 설정 중 오류 발생: {str(e)}"
            }
    
    def cleanup(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
            self.logged_in = False 