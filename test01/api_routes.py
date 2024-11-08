#API 라우트 정의
from analyzer.static_analysis import perform_static_analysis
from analyzer.dynamic_analysis import perform_dynamic_analysis
from analyzer.emulator_detection import check_emulator_detection
from utils.debug_utils import get_system_debug_info

def analyze_file(file):
    static_result = perform_static_analysis(file)
    dynamic_result = perform_dynamic_analysis(file)
    emulator_detection = check_emulator_detection(file)

    return {
        "static_analysis": static_result,
        "dynamic_analysis": dynamic_result,
        "emulator_detection": emulator_detection
    }

def automate_analysis(params):
    # 분석 자동화에 필요한 로직 추가
    return {"message": "Analysis automated with params", "params": params}

def debug_system():
    return get_system_debug_info()
