from flask import Flask, request, jsonify
from services.automation import AutomationService
from services.db_service import DatabaseService
from flask_cors import CORS  # CORS 지원 추가

app = Flask(__name__)
CORS(app)  # CORS 활성화
automation_service = AutomationService()
db_service = DatabaseService()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"})

@app.route('/init-status', methods=['GET'])
def get_init_status():
    """
    초기화 상태를 확인하는 엔드포인트
    """
    return jsonify(automation_service.get_initialization_status())

@app.route('/initialize', methods=['POST'])
def initialize_system():
    """
    시스템 초기화를 시작하는 엔드포인트
    """
    success = automation_service.init_driver()
    return jsonify({
        "status": "success" if success else "error",
        "message": "초기화가 완료되었습니다." if success else "초기화에 실패했습니다."
    })

@app.route('/check-car', methods=['POST'])
def check_car():
    """
    차량을 검색하는 엔드포인트
    """
    if not automation_service.ensure_initialized():
        return jsonify({
            "status": "error",
            "message": "시스템이 초기화되지 않았습니다. 잠시 후 다시 시도해주세요."
        })
    
    data = request.get_json()
    car_number = data.get('car_number')
    parking_time = data.get('parking_time')
    
    # Selenium 자동화 실행
    search_result = automation_service.search_car(car_number)
    
    if search_result["status"] == "success":
        # 주차시간 설정
        parking_result = automation_service.apply_parking_time(parking_time)
        search_result.update({"parking_result": parking_result})
    
    return jsonify(search_result)

if __name__ == '__main__':
    app.run(port=5050) 